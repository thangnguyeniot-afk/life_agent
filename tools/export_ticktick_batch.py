#!/usr/bin/env python3
"""tools/export_ticktick_batch.py

Phase 2B-6: PEC-to-TickTick batch exporter skeleton with dry-run default.

Reads a PEC JSON file, validates it, computes create/update/skip/cancel actions
against a local mapping file, and prints the export plan. Writes to TickTick only
when --apply is explicitly passed.

This is NOT the `export week` / `export day` automation command.
Those commands remain NOT IMPLEMENTED in LIFE_AGENT_AUTOMATION_INTERFACE.md.

Field constraints (from Phase 2B-5 live test):
  - tags:      NOT sent — causes HTTP 500 in current TickTick API behavior
  - reminders: NOT sent — causes HTTP 500 in current TickTick API behavior
  - recurrence: NOT sent — out of scope for MVP

Supported fields:
  - title, projectId, content (with embedded source_id comment)
  - priority  (0=none/normal, 1=low, 5=high)
  - startDate, dueDate  (ISO 8601 with local timezone offset for timed tasks)
  - isAllDay  (bool)

Usage:
    # Dry-run (default, no API writes):
    python tools/export_ticktick_batch.py <pec_file.json> --project-id PROJECT_ID

    # Live apply — writes to TickTick:
    python tools/export_ticktick_batch.py <pec_file.json> --project-id PROJECT_ID --apply

    # Live apply with limit (recommended for first test):
    python tools/export_ticktick_batch.py <pec_file.json> --project-id PROJECT_ID --apply --limit 2

    # Skip interactive confirmation:
    python tools/export_ticktick_batch.py ... --apply --yes

    # Explicit mapping file:
    python tools/export_ticktick_batch.py ... --mapping-file .ticktick/2026-W18_map.json

    # Cancel-policy options:
    python tools/export_ticktick_batch.py ... --cancel-policy prefix   (default)
    python tools/export_ticktick_batch.py ... --no-cancel

Preconditions:
    python tools/auth_ticktick.py status   # must show valid token
    A test project/list must exist in TickTick.

Mapping file location:
    .ticktick/{week_id}_map.json   (gitignored — never committed)

Requires: Python 3.10+, requests library.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    import requests
except ImportError:
    sys.exit("Error: 'requests' not installed. Run: pip install requests")

_TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_TOOLS_DIR))

try:
    from auth_ticktick import get_access_token
except ImportError as exc:
    sys.exit(
        "Error: Could not import tools/auth_ticktick.py\n"
        f"  Detail: {exc}\n"
        "  Ensure Phase 2B-2 is complete and the file exists."
    )

try:
    from validate_pec import validate_pec, PECReport
except ImportError as exc:
    sys.exit(
        "Error: Could not import tools/validate_pec.py\n"
        f"  Detail: {exc}\n"
        "  Ensure Phase 2B-1 is complete and the file exists."
    )


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

API_BASE   = "https://api.ticktick.com/open/v1"
REPO_ROOT  = Path(__file__).resolve().parent.parent
ENV_FILE   = REPO_ROOT / ".env"
TICKTICK_DIR = REPO_ROOT / ".ticktick"

CANCEL_PREFIX = "[CANCELLED]"

# Priority mapping: PEC priority string → TickTick priority integer
PRIORITY_MAP: dict[str, int] = {
    "low":    1,
    "normal": 0,
    "high":   5,
}

_RULE = "  ══════════════════════════════════════════════════════"
_THIN = "  ──────────────────────────────────────────────────────"


# ---------------------------------------------------------------------------
# .env loader — stdlib only
# ---------------------------------------------------------------------------

def _load_env(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    if not path.exists():
        return result
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        result[key.strip()] = val.strip().strip('"').strip("'")
    return result


# ---------------------------------------------------------------------------
# Project ID resolver
# ---------------------------------------------------------------------------

def _resolve_project_id(args_project_id: str | None) -> str:
    if args_project_id:
        return args_project_id.strip()
    env = _load_env(ENV_FILE)
    pid = env.get("TICKTICK_DEFAULT_PROJECT_ID", "").strip()
    if pid:
        return pid
    sys.exit(
        "Error: No project ID provided.\n"
        "  Pass --project-id PROJECT_ID, or set TICKTICK_DEFAULT_PROJECT_ID in .env.\n"
        "\n"
        "  To look up the test project:\n"
        "    python tools/lookup_ticktick_project.py list\n"
        '    python tools/lookup_ticktick_project.py ensure "Life Agent - API Test" --create\n'
        "  Then pass the returned project ID with --project-id."
    )


# ---------------------------------------------------------------------------
# Mapping file
# ---------------------------------------------------------------------------

MappingEntry = dict[str, Any]
MappingFile  = dict[str, MappingEntry]  # keyed by source_id


def _resolve_mapping_path(args_mapping: str | None, week_id: str) -> Path:
    if args_mapping:
        return Path(args_mapping)
    safe_week = week_id.replace("/", "-")
    return TICKTICK_DIR / f"{safe_week}_map.json"


def _load_mapping(path: Path) -> MappingFile:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(
            f"Error: mapping file {path} contains invalid JSON.\n"
            f"  Detail: {exc}\n"
            "  Fix or delete the file and re-run."
        )
    if not isinstance(data, dict):
        sys.exit(f"Error: mapping file {path} must be a JSON object, got {type(data).__name__}.")
    return data


def _save_mapping(path: Path, mapping: MappingFile) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(mapping, indent=2, ensure_ascii=False), encoding="utf-8")


def _mapping_entry(
    source_id: str,
    task_id: str,
    project_id: str,
    content_hash: str,
    status: str,
) -> MappingEntry:
    return {
        "source_id":          source_id,
        "ticktick_task_id":   task_id,
        "ticktick_project_id": project_id,
        "content_hash":       content_hash,
        "last_exported":      datetime.now(timezone.utc).isoformat(),
        "status":             status,
    }


# ---------------------------------------------------------------------------
# Content hash
# ---------------------------------------------------------------------------

def _compute_hash(payload: dict[str, Any]) -> str:
    """Hash the normalized export payload for idempotency comparison.

    Includes only the fields that affect TickTick task appearance:
    title, content, priority, startDate, dueDate, isAllDay, projectId.
    Excludes runtime fields, tags, reminders, recurrence.
    """
    canonical = {
        k: payload.get(k)
        for k in ("title", "content", "priority", "startDate", "dueDate", "isAllDay", "projectId")
    }
    normalized = json.dumps(canonical, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------
# PEC task → TickTick payload
# ---------------------------------------------------------------------------

def _build_datetime(date_str: str, time_str: str) -> str:
    """Combine date (YYYY-MM-DD) + time (HH:MM) into ISO 8601 with local offset."""
    local_now = datetime.now().astimezone()
    offset    = local_now.utcoffset() or timedelta(0)
    # Build naive datetime then attach offset
    naive = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    aware = naive.replace(tzinfo=timezone(offset))
    return aware.isoformat()


def _build_payload(task_raw: dict[str, Any], project_id: str) -> dict[str, Any]:
    """Convert a single PEC task dict to a TickTick API payload.

    Does NOT include tags, reminders, or recurrence (Phase 2B-5 findings).
    """
    source_id = str(task_raw.get("source_id") or "")
    title     = str(task_raw.get("title") or "")
    notes     = str(task_raw.get("notes") or "")
    priority  = str(task_raw.get("priority") or "normal")
    all_day   = bool(task_raw.get("all_day", False))
    date_str  = str(task_raw.get("date") or "")
    start_str = task_raw.get("start_time")
    end_str   = task_raw.get("end_time")

    # Ensure source_id comment is in content
    sid_comment = f"<!-- la:source_id={source_id} -->"
    if sid_comment not in notes:
        content = f"{notes}\n{sid_comment}".strip()
    else:
        content = notes

    payload: dict[str, Any] = {
        "title":     title,
        "projectId": project_id,
        "content":   content,
        "priority":  PRIORITY_MAP.get(priority, 0),
        "isAllDay":  all_day,
    }

    if all_day:
        # All-day: set dueDate as date-only; omit startDate to be safe
        if date_str:
            payload["dueDate"] = f"{date_str}T00:00:00.000+0000"
    else:
        # Timed: startDate + dueDate with local timezone offset
        if date_str and start_str:
            payload["startDate"] = _build_datetime(date_str, str(start_str))
        if date_str and end_str:
            payload["dueDate"] = _build_datetime(date_str, str(end_str))
        elif date_str and start_str:
            # No end_time: dueDate = startDate (point-in-time)
            payload["dueDate"] = payload["startDate"]

    return payload


# ---------------------------------------------------------------------------
# Action plan
# ---------------------------------------------------------------------------

# Action constants
ACTION_CREATE = "CREATE"
ACTION_UPDATE = "UPDATE"
ACTION_SKIP   = "SKIP"
ACTION_CANCEL = "CANCEL"


class PlannedAction:
    __slots__ = (
        "action", "source_id", "task_raw", "payload",
        "content_hash", "existing_task_id",
    )

    def __init__(
        self,
        action: str,
        source_id: str,
        task_raw: dict[str, Any],
        payload: dict[str, Any],
        content_hash: str,
        existing_task_id: str | None = None,
    ) -> None:
        self.action           = action
        self.source_id        = source_id
        self.task_raw         = task_raw
        self.payload          = payload
        self.content_hash     = content_hash
        self.existing_task_id = existing_task_id


def _collect_pec_tasks(report: PECReport, pec_data: dict[str, Any]) -> list[dict[str, Any]]:
    """Return flat list of all raw task dicts from PEC, in day order."""
    tasks: list[dict[str, Any]] = []
    for day_data in pec_data.get("days", {}).values():
        for raw in (day_data.get("tasks") or []):
            if isinstance(raw, dict):
                tasks.append(raw)
    return tasks


def _plan_actions(
    tasks: list[dict[str, Any]],
    mapping: MappingFile,
    project_id: str,
    no_cancel: bool,
) -> tuple[list[PlannedAction], list[PlannedAction]]:
    """Compute actions for PEC tasks and mapping-only stale tasks.

    Returns (task_actions, cancel_actions).
    """
    task_actions: list[PlannedAction] = []
    seen_source_ids: set[str] = set()

    for raw in tasks:
        sid   = str(raw.get("source_id") or "")
        if not sid:
            continue

        export_status = str(raw.get("export_status") or "pending")
        if export_status == "cancelled":
            # Explicitly cancelled in PEC — treat as cancel even if in mapping
            payload = _build_payload(raw, project_id)
            content_hash = _compute_hash(payload)
            existing_id  = mapping.get(sid, {}).get("ticktick_task_id")
            task_actions.append(PlannedAction(
                ACTION_CANCEL, sid, raw, payload, content_hash, existing_id
            ))
            seen_source_ids.add(sid)
            continue

        payload      = _build_payload(raw, project_id)
        content_hash = _compute_hash(payload)
        seen_source_ids.add(sid)

        if sid not in mapping:
            task_actions.append(PlannedAction(ACTION_CREATE, sid, raw, payload, content_hash))
        else:
            entry = mapping[sid]
            mapped_hash      = entry.get("content_hash", "")
            mapped_status    = entry.get("status", "")
            existing_task_id = entry.get("ticktick_task_id")

            if mapped_status == "cancelled":
                # Previously cancelled; skip unless export_status is reset
                task_actions.append(PlannedAction(
                    ACTION_SKIP, sid, raw, payload, content_hash, existing_task_id
                ))
            elif mapped_hash == content_hash:
                task_actions.append(PlannedAction(
                    ACTION_SKIP, sid, raw, payload, content_hash, existing_task_id
                ))
            else:
                task_actions.append(PlannedAction(
                    ACTION_UPDATE, sid, raw, payload, content_hash, existing_task_id
                ))

    # Stale mapping entries (source_id in mapping but not in PEC) → cancel
    cancel_actions: list[PlannedAction] = []
    if not no_cancel:
        for sid, entry in mapping.items():
            if sid not in seen_source_ids and entry.get("status") not in ("cancelled",):
                cancel_actions.append(PlannedAction(
                    ACTION_CANCEL, sid, {}, {}, "",
                    entry.get("ticktick_task_id"),
                ))

    return task_actions, cancel_actions


# ---------------------------------------------------------------------------
# Dry-run renderer
# ---------------------------------------------------------------------------

def _action_line(act: PlannedAction) -> str:
    raw  = act.task_raw
    date = str(raw.get("date") or "?")
    start = raw.get("start_time") or "?"
    end   = raw.get("end_time") or ""
    time_range = f"{start}-{end}" if end else start
    scope = str(raw.get("project_scope") or "?")
    prio  = str(raw.get("priority") or "?")
    title = str(raw.get("title") or act.source_id)

    if act.action == ACTION_CANCEL and not raw:
        # Stale mapping entry — minimal info
        return f"  [{act.action:<6}] (stale) source_id={act.source_id}"

    return (
        f"  [{act.action:<6}] {date} {time_range:<12} {prio:<8}"
        f" {scope:<12} :: {title}"
    )


def _render_plan(
    pec_path: str,
    project_id: str,
    mapping_path: Path,
    report: PECReport,
    task_actions: list[PlannedAction],
    cancel_actions: list[PlannedAction],
    apply: bool,
    limit: int | None,
) -> None:
    all_actions = task_actions + cancel_actions

    n_create = sum(1 for a in task_actions if a.action == ACTION_CREATE)
    n_update = sum(1 for a in task_actions if a.action == ACTION_UPDATE)
    n_skip   = sum(1 for a in task_actions if a.action == ACTION_SKIP)
    n_cancel = (
        sum(1 for a in task_actions if a.action == ACTION_CANCEL)
        + len(cancel_actions)
    )

    print()
    print(_RULE)
    print("  Life Agent  ·  TickTick Batch Export  ·  Phase 2B-6")
    print(_RULE)
    print(f"  PEC file     : {pec_path}")
    print(f"  Project ID   : {project_id}")
    print(f"  Mapping file : {mapping_path}")
    print(f"  Mode         : {'APPLY' if apply else 'DRY-RUN (no API writes)'}")
    if limit is not None:
        print(f"  Limit        : {limit} operations")
    print(_THIN)
    print(f"  Tasks in PEC : {len(report.tasks)}")
    print(f"  Errors       : {len(report.errors)}")
    print(f"  Warnings     : {len(report.warnings)}")
    print(_THIN)
    print(f"  CREATE       : {n_create}")
    print(f"  UPDATE       : {n_update}")
    print(f"  SKIP         : {n_skip}")
    print(f"  CANCEL       : {n_cancel}")
    print(_THIN)

    if report.errors:
        print("  VALIDATION ERRORS (must fix before apply):")
        for issue in report.errors:
            print(f"    [ERROR] {issue.location}")
            print(f"            {issue.message}")
        print(_THIN)

    if report.warnings:
        print("  Warnings:")
        for issue in report.warnings:
            print(f"    [WARN]  {issue.location}")
            print(f"            {issue.message}")
        print(_THIN)

    print("  Export Plan:")
    for act in all_actions:
        print(_action_line(act))

    if limit is not None and apply:
        write_ops = [a for a in all_actions if a.action != ACTION_SKIP]
        effective = write_ops[:limit]
        skipped   = write_ops[limit:]
        print()
        print(f"  --limit {limit}: {len(effective)} write operation(s) will be applied.")
        if skipped:
            print(f"  {len(skipped)} operation(s) beyond limit will be skipped this run.")

    print(_RULE)


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _handle_api_error(resp: requests.Response, context: str, payload_keys: list[str]) -> None:
    """Emit a specific, actionable error and exit. For HTTP 500, shows payload keys only."""
    sanitized_keys = [k for k in payload_keys if k not in ("title", "content")]

    if resp.status_code == 401:
        sys.exit(
            f"Error: {context} — HTTP 401 Unauthorized\n"
            "  Access token expired. Run: python tools/auth_ticktick.py login"
        )
    if resp.status_code == 403:
        sys.exit(
            f"Error: {context} — HTTP 403 Forbidden\n"
            "  Token may lack 'tasks:write' scope.\n"
            "  Re-run: python tools/auth_ticktick.py login"
        )
    if resp.status_code == 404:
        sys.exit(
            f"Error: {context} — HTTP 404 Not Found\n"
            "  Task or project ID not found. Verify project ID:\n"
            "    python tools/lookup_ticktick_project.py list"
        )
    if resp.status_code == 429:
        sys.exit(
            f"Error: {context} — HTTP 429 Rate Limited\n"
            "  Wait 60 seconds and try again."
        )
    if resp.status_code == 500:
        sys.exit(
            f"Error: {context} — HTTP 500\n"
            "  TickTick returned Unknown exception.\n"
            f"  Payload keys sent (excluding title/content): {sanitized_keys}\n"
            "  Ensure tags/reminders are NOT in payload (Phase 2B-5 finding).\n"
            f"  Response: {resp.text[:300]}"
        )
    sys.exit(
        f"Error: {context} — HTTP {resp.status_code}\n"
        f"  Response: {resp.text[:300]}"
    )


def _api_create_task(token: str, payload: dict[str, Any]) -> dict[str, Any]:
    try:
        resp = requests.post(
            f"{API_BASE}/task",
            headers=_auth_headers(token),
            json=payload,
            timeout=15,
        )
    except requests.RequestException as exc:
        sys.exit(f"Error: POST /task network failure: {exc}")

    if resp.status_code not in (200, 201):
        _handle_api_error(resp, "POST /task (create)", list(payload.keys()))

    try:
        return resp.json()
    except Exception:
        sys.exit(
            f"Error: POST /task returned non-JSON.\n"
            f"  Status: {resp.status_code}  Body: {resp.text[:200]}"
        )


def _api_update_task(token: str, task_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    try:
        resp = requests.post(
            f"{API_BASE}/task/{task_id}",
            headers=_auth_headers(token),
            json=payload,
            timeout=15,
        )
    except requests.RequestException as exc:
        sys.exit(f"Error: POST /task/{task_id} (update) network failure: {exc}")

    if resp.status_code not in (200, 201):
        _handle_api_error(resp, f"POST /task/{task_id} (update)", list(payload.keys()))

    try:
        return resp.json()
    except Exception:
        sys.exit(
            f"Error: POST /task/{task_id} update returned non-JSON.\n"
            f"  Status: {resp.status_code}  Body: {resp.text[:200]}"
        )


# ---------------------------------------------------------------------------
# Apply executor
# ---------------------------------------------------------------------------

class ApplyResult:
    __slots__ = ("source_id", "action", "task_id", "success", "error")

    def __init__(
        self,
        source_id: str,
        action: str,
        task_id: str | None = None,
        success: bool = False,
        error: str | None = None,
    ) -> None:
        self.source_id = source_id
        self.action    = action
        self.task_id   = task_id
        self.success   = success
        self.error     = error


def _apply_actions(
    token: str,
    project_id: str,
    all_actions: list[PlannedAction],
    cancel_actions: list[PlannedAction],
    cancel_policy: str,
    mapping: MappingFile,
    mapping_path: Path,
    limit: int | None,
) -> list[ApplyResult]:
    """Execute write operations against TickTick API sequentially.

    Updates mapping in-place after each successful operation.
    Only saves mapping after each successful operation (partial-failure safe).
    """
    write_ops = [a for a in (all_actions + cancel_actions) if a.action != ACTION_SKIP]

    if limit is not None:
        write_ops = write_ops[:limit]

    results: list[ApplyResult] = []

    for act in write_ops:
        print()
        print(f"  Applying [{act.action}] source_id={act.source_id} ...")

        try:
            if act.action == ACTION_CREATE:
                result = _apply_create(token, act, project_id, mapping, mapping_path)

            elif act.action == ACTION_UPDATE:
                result = _apply_update(token, act, project_id, mapping, mapping_path)

            elif act.action == ACTION_CANCEL:
                result = _apply_cancel(token, act, cancel_policy, mapping, mapping_path)

            else:
                result = ApplyResult(act.source_id, act.action, success=False,
                                     error=f"Unknown action: {act.action}")

        except SystemExit as exc:
            # sys.exit() inside API helpers surfaces here; record and stop
            results.append(ApplyResult(act.source_id, act.action, success=False,
                                       error=str(exc)))
            print(f"  ✗  [{act.action}] FAILED — {exc}")
            print("  Stopping apply due to API error. Mapping saved up to last success.")
            results_summary(results)
            raise

        if result.success:
            print(f"  ✓  [{act.action}] OK — task_id={result.task_id}")
        else:
            print(f"  ✗  [{act.action}] FAILED — {result.error}")

        results.append(result)

    return results


def _apply_create(
    token: str,
    act: PlannedAction,
    project_id: str,
    mapping: MappingFile,
    mapping_path: Path,
) -> ApplyResult:
    created = _api_create_task(token, act.payload)
    task_id = created.get("id")
    if not task_id:
        return ApplyResult(act.source_id, ACTION_CREATE, success=False,
                           error=f"Response missing 'id'. Keys: {list(created.keys())}")

    mapping[act.source_id] = _mapping_entry(
        act.source_id, task_id, project_id, act.content_hash, "exported"
    )
    _save_mapping(mapping_path, mapping)
    return ApplyResult(act.source_id, ACTION_CREATE, task_id=task_id, success=True)


def _apply_update(
    token: str,
    act: PlannedAction,
    project_id: str,
    mapping: MappingFile,
    mapping_path: Path,
) -> ApplyResult:
    task_id = act.existing_task_id
    if not task_id:
        return ApplyResult(act.source_id, ACTION_UPDATE, success=False,
                           error="No ticktick_task_id in mapping — cannot update")

    update_payload = dict(act.payload)
    update_payload["id"] = task_id

    _api_update_task(token, task_id, update_payload)

    mapping[act.source_id] = _mapping_entry(
        act.source_id, task_id, project_id, act.content_hash, "exported"
    )
    _save_mapping(mapping_path, mapping)
    return ApplyResult(act.source_id, ACTION_UPDATE, task_id=task_id, success=True)


def _apply_cancel(
    token: str,
    act: PlannedAction,
    cancel_policy: str,
    mapping: MappingFile,
    mapping_path: Path,
) -> ApplyResult:
    task_id = act.existing_task_id
    if not task_id:
        # No existing task ID — nothing to cancel in TickTick
        if act.source_id in mapping:
            mapping[act.source_id]["status"] = "cancelled"
            _save_mapping(mapping_path, mapping)
        return ApplyResult(act.source_id, ACTION_CANCEL, success=True,
                           error="No ticktick_task_id — mapping status set to cancelled only")

    if cancel_policy == "prefix":
        # Read current title to prepend [CANCELLED]
        # We cannot GET by task_id alone without project_id in this context.
        # Use the title from act.task_raw if present; fall back to a generic prefix.
        old_title = str(act.task_raw.get("title") or act.source_id)
        if not old_title.startswith(CANCEL_PREFIX):
            new_title = f"{CANCEL_PREFIX} {old_title}"
        else:
            new_title = old_title

        cancel_payload: dict[str, Any] = {"id": task_id, "title": new_title}
        _api_update_task(token, task_id, cancel_payload)

    # Update mapping status
    if act.source_id in mapping:
        mapping[act.source_id]["status"] = "cancelled"
    else:
        mapping[act.source_id] = _mapping_entry(
            act.source_id, task_id, "", "", "cancelled"
        )
    _save_mapping(mapping_path, mapping)
    return ApplyResult(act.source_id, ACTION_CANCEL, task_id=task_id, success=True)


# ---------------------------------------------------------------------------
# Results summary
# ---------------------------------------------------------------------------

def results_summary(results: list[ApplyResult]) -> None:
    n_ok   = sum(1 for r in results if r.success)
    n_fail = sum(1 for r in results if not r.success)
    print()
    print(_RULE)
    print(f"  Apply Results: {n_ok} succeeded, {n_fail} failed")
    print(_THIN)
    for r in results:
        icon = "✓" if r.success else "✗"
        tid  = f"  task_id={r.task_id}" if r.task_id else ""
        err  = f"  — {r.error}" if r.error and not r.success else ""
        print(f"  {icon}  [{r.action:<6}] {r.source_id}{tid}{err}")
    print(_RULE)


# ---------------------------------------------------------------------------
# Confirm prompt
# ---------------------------------------------------------------------------

def _confirm_apply(
    n_create: int, n_update: int, n_cancel: int, limit: int | None
) -> bool:
    total = n_create + n_update + n_cancel
    if limit is not None:
        total = min(total, limit)
    print()
    print(f"  About to apply {total} write operation(s) to TickTick.")
    if limit is not None:
        print(f"  (--limit {limit} active)")
    try:
        answer = input("  Type 'yes' to proceed, anything else to cancel: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        answer = ""
    return answer == "yes"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        prog="export_ticktick_batch",
        description=(
            "Phase 2B-6: PEC-to-TickTick batch exporter.\n"
            "Default mode: dry-run (no API writes).\n"
            "Live apply requires --apply flag.\n"
            "Does NOT implement 'export week' or 'export day' automation commands."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python tools/export_ticktick_batch.py tools/samples/pec_week_sample.json "
            "--project-id abc123\n"
            "  python tools/export_ticktick_batch.py ... --apply --limit 2\n"
            "  python tools/export_ticktick_batch.py ... --apply --yes\n"
            "\n"
            "preconditions:\n"
            "  python tools/auth_ticktick.py status    # must show valid token\n"
            "  python tools/lookup_ticktick_project.py list\n"
        ),
    )

    parser.add_argument(
        "pec_file",
        metavar="PEC_FILE",
        help="Path to the PEC JSON file to export.",
    )
    parser.add_argument(
        "--project-id",
        dest="project_id",
        metavar="PROJECT_ID",
        default=None,
        help=(
            "TickTick project/list ID. "
            "Falls back to TICKTICK_DEFAULT_PROJECT_ID in .env if not passed."
        ),
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        default=False,
        help="Write to TickTick. Without this flag, only a dry-run plan is printed.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        metavar="N",
        default=None,
        help="Maximum number of create/update/cancel operations to apply (dry-run shows full plan).",
    )
    parser.add_argument(
        "--mapping-file",
        dest="mapping_file",
        metavar="PATH",
        default=None,
        help=(
            "Path to mapping file. "
            "Defaults to .ticktick/{week_id}_map.json (gitignored)."
        ),
    )
    parser.add_argument(
        "--cancel-policy",
        dest="cancel_policy",
        choices=["prefix"],
        default="prefix",
        help=(
            "How to mark removed tasks. 'prefix' prepends [CANCELLED] to title (default)."
        ),
    )
    parser.add_argument(
        "--no-cancel",
        dest="no_cancel",
        action="store_true",
        default=False,
        help="Do not cancel tasks that are in the mapping but absent from the PEC.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        default=False,
        help="Skip interactive confirmation when --apply is used.",
    )

    args = parser.parse_args()
    project_id = _resolve_project_id(args.project_id)

    # ------------------------------------------------------------------
    # 1. Validate PEC
    # ------------------------------------------------------------------
    print(f"\n  Validating PEC: {args.pec_file} ...")
    report = validate_pec(args.pec_file)

    if report.errors:
        print(f"\n  ✗  PEC validation FAILED — {len(report.errors)} error(s).")
        for issue in report.errors:
            print(f"    [ERROR] {issue.location}: {issue.message}")
        if args.apply:
            sys.exit("  Apply blocked by validation errors. Fix PEC and re-run.")
        print("  (Dry-run plan shown below despite errors.)\n")
    else:
        print(f"  ✓  PEC valid — {len(report.tasks)} tasks, {len(report.warnings)} warning(s).")

    # ------------------------------------------------------------------
    # 2. Load raw PEC for task data
    # ------------------------------------------------------------------
    try:
        pec_data: dict[str, Any] = json.loads(
            Path(args.pec_file).read_text(encoding="utf-8")
        )
    except (OSError, json.JSONDecodeError) as exc:
        sys.exit(f"Error: Could not re-read PEC file: {exc}")

    meta     = pec_data.get("export_meta", {})
    week_id  = str(meta.get("week_id") or "unknown")

    # ------------------------------------------------------------------
    # 3. Load mapping file
    # ------------------------------------------------------------------
    mapping_path = _resolve_mapping_path(args.mapping_file, week_id)
    mapping      = _load_mapping(mapping_path)

    # ------------------------------------------------------------------
    # 4. Plan actions
    # ------------------------------------------------------------------
    raw_tasks = _collect_pec_tasks(report, pec_data)
    task_actions, cancel_actions = _plan_actions(
        raw_tasks, mapping, project_id, args.no_cancel
    )

    # ------------------------------------------------------------------
    # 5. Render plan
    # ------------------------------------------------------------------
    _render_plan(
        pec_path      = args.pec_file,
        project_id    = project_id,
        mapping_path  = mapping_path,
        report        = report,
        task_actions  = task_actions,
        cancel_actions= cancel_actions,
        apply         = args.apply,
        limit         = args.limit,
    )

    # ------------------------------------------------------------------
    # 6. Apply (only when --apply)
    # ------------------------------------------------------------------
    if not args.apply:
        print()
        print("  Dry-run complete. No API writes.")
        print("  To apply, re-run with: --apply  (add --limit N for a partial first apply)")
        print()
        return

    # Confirm
    n_create = sum(1 for a in task_actions if a.action == ACTION_CREATE)
    n_update = sum(1 for a in task_actions if a.action == ACTION_UPDATE)
    n_cancel = (
        sum(1 for a in task_actions if a.action == ACTION_CANCEL)
        + len(cancel_actions)
    )

    if not args.yes:
        if not _confirm_apply(n_create, n_update, n_cancel, args.limit):
            print("\n  Apply cancelled by user.")
            return

    token = get_access_token()

    print()
    print(_RULE)
    print("  Applying to TickTick ...")
    print(_THIN)

    results = _apply_actions(
        token         = token,
        project_id    = project_id,
        all_actions   = task_actions,
        cancel_actions= cancel_actions,
        cancel_policy = args.cancel_policy,
        mapping       = mapping,
        mapping_path  = mapping_path,
        limit         = args.limit,
    )

    results_summary(results)

    n_ok = sum(1 for r in results if r.success)
    if n_ok > 0:
        print()
        print(f"  Mapping file updated: {mapping_path}")
        print("  (Mapping file is gitignored — not committed.)")


if __name__ == "__main__":
    main()
