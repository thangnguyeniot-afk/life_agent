#!/usr/bin/env python3
"""tools/test_ticktick_task_fields.py

Phase 2B-5: TickTick API field capability test.

Creates ONE disposable test task with full field payload (startDate, dueDate,
reminders, tags, priority), reads it back, verifies each field, updates it,
and optionally deletes it.

This script is NOT a batch exporter. It does NOT read PEC files, create mapping
files, or export Life Agent plans. It creates exactly ONE test task.

Usage:
    python tools/test_ticktick_task_fields.py --project-id PROJECT_ID
    python tools/test_ticktick_task_fields.py --project-id PROJECT_ID --delete
    python tools/test_ticktick_task_fields.py --project-id PROJECT_ID --no-tags
    python tools/test_ticktick_task_fields.py --project-id PROJECT_ID --no-reminder
    python tools/test_ticktick_task_fields.py  # uses TICKTICK_DEFAULT_PROJECT_ID
    python tools/test_ticktick_task_fields.py --project-id PID --task-id TID --delete-only

Preconditions:
    1. python tools/auth_ticktick.py login    (run once)
    2. python tools/auth_ticktick.py status   (must show valid token)
    3. A test project/list must exist in TickTick:
         python tools/lookup_ticktick_project.py ensure "Life Agent - API Test" --create

API scope (task endpoints only):
    POST   /task                            — create task
    GET    /project/{projectId}/task/{id}  — read task back
    POST   /task/{taskId}                  — update task
    DELETE /project/{projectId}/task/{id}  — only with --delete or --delete-only

Does NOT call project endpoints.
Does NOT create multiple tasks.
Does NOT read PEC files or write mapping files.

Requires: Python 3.10+, requests library.
"""

from __future__ import annotations

import argparse
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


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

API_BASE  = "https://api.ticktick.com/open/v1"
REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE  = REPO_ROOT / ".env"

FIELD_TAG_PREFIX = "[FIELD TEST]"
FIELD_TAG_LABEL  = "la-field-test"
SOURCE_ID        = "LA-CW2026-W18-D20260427-FIELD-GENERAL-001"

# Priority values: TickTick Open API — 0=None, 1=Low, 3=Medium, 5=High
PRIORITY_HIGH = 5
PRIORITY_LOW  = 1

_RULE = "  ══════════════════════════════════════════════════════"
_THIN = "  ──────────────────────────────────────────────────────"


# ---------------------------------------------------------------------------
# .env loader — stdlib only, matches auth_ticktick.py pattern
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
# API helpers
# ---------------------------------------------------------------------------

def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _handle_api_error(resp: requests.Response, context: str) -> None:
    """Emit a specific, actionable error message and exit."""
    if resp.status_code == 401:
        sys.exit(
            f"Error: {context} — HTTP 401 Unauthorized\n"
            "  Access token is invalid or expired.\n"
            "  Run: python tools/auth_ticktick.py refresh\n"
            "  If refresh also fails, re-run: python tools/auth_ticktick.py login"
        )
    if resp.status_code == 403:
        sys.exit(
            f"Error: {context} — HTTP 403 Forbidden\n"
            "  Token may lack 'tasks:write' scope or insufficient app permissions.\n"
            "  Re-run: python tools/auth_ticktick.py login"
        )
    if resp.status_code == 404:
        sys.exit(
            f"Error: {context} — HTTP 404 Not Found\n"
            "  Task or project ID not found.\n"
            "  Verify the project ID is correct:\n"
            "    python tools/lookup_ticktick_project.py list"
        )
    if resp.status_code == 429:
        sys.exit(
            f"Error: {context} — HTTP 429 Rate Limited\n"
            "  Wait 60 seconds and try again."
        )
    sys.exit(
        f"Error: {context} — HTTP {resp.status_code}\n"
        f"  Response: {resp.text[:400]}"
    )


def _is_recoverable_error(resp: requests.Response) -> bool:
    """Return True if the HTTP error suggests a field was rejected (not an auth/system failure).

    TickTick returns HTTP 500 "Unknown exception" when an unsupported or malformed
    field is included in the payload (observed in live testing). Treat 500 as
    recoverable in the fallback context so we can retry with a reduced payload.
    Do NOT treat 401/403/404/429 as recoverable — those indicate auth or system failures.
    """
    return resp.status_code in (400, 422, 500)


# ---------------------------------------------------------------------------
# Task API calls — scoped to exactly 4 endpoints (create/get/update/delete)
# ---------------------------------------------------------------------------

def _try_create_task(
    token: str,
    payload: dict[str, Any],
    attempt_label: str,
) -> tuple[dict[str, Any] | None, str | None]:
    """Attempt to create a task. Returns (task_dict, None) on success.
    Returns (None, error_description) on recoverable field rejection (HTTP 400/422).
    Calls sys.exit() on non-recoverable auth/system errors.
    """
    try:
        resp = requests.post(
            f"{API_BASE}/task",
            headers=_auth_headers(token),
            json=payload,
            timeout=15,
        )
    except requests.RequestException as exc:
        sys.exit(f"Error: POST /task network failure: {exc}")

    if resp.status_code in (200, 201):
        try:
            data = resp.json()
        except Exception:
            sys.exit(
                "Error: POST /task returned non-JSON.\n"
                f"  Status: {resp.status_code}  Body: {resp.text[:200]}"
            )
        if not isinstance(data, dict):
            sys.exit(
                f"Error: POST /task expected JSON object, got {type(data).__name__}."
            )
        return data, None

    if _is_recoverable_error(resp):
        return None, f"HTTP {resp.status_code} — {resp.text[:200]}"

    _handle_api_error(resp, f"POST /task ({attempt_label})")
    return None, None  # unreachable — _handle_api_error exits


def api_get_task(token: str, project_id: str, task_id: str) -> dict[str, Any]:
    """GET /project/{projectId}/task/{taskId} — read a task back by ID."""
    url = f"{API_BASE}/project/{project_id}/task/{task_id}"
    try:
        resp = requests.get(url, headers=_auth_headers(token), timeout=15)
    except requests.RequestException as exc:
        sys.exit(f"Error: GET task network failure: {exc}")

    if resp.status_code != 200:
        _handle_api_error(resp, f"GET /project/{project_id}/task/{task_id}")

    try:
        data = resp.json()
    except Exception:
        sys.exit(
            "Error: GET task returned non-JSON.\n"
            f"  Status: {resp.status_code}  Body: {resp.text[:200]}"
        )
    if not isinstance(data, dict):
        sys.exit(f"Error: GET task expected JSON object, got {type(data).__name__}.")
    return data


def api_update_task(
    token: str,
    task_id: str,
    update_fields: dict[str, Any],
) -> dict[str, Any]:
    """POST /task/{taskId} — update an existing task. Returns updated task object."""
    try:
        resp = requests.post(
            f"{API_BASE}/task/{task_id}",
            headers=_auth_headers(token),
            json=update_fields,
            timeout=15,
        )
    except requests.RequestException as exc:
        sys.exit(f"Error: POST /task/{task_id} (update) network failure: {exc}")

    if resp.status_code not in (200, 201):
        _handle_api_error(resp, f"POST /task/{task_id} (update)")

    try:
        data = resp.json()
    except Exception:
        sys.exit(
            "Error: POST /task update returned non-JSON.\n"
            f"  Status: {resp.status_code}  Body: {resp.text[:200]}"
        )
    if not isinstance(data, dict):
        sys.exit(
            f"Error: POST /task update expected JSON object, got {type(data).__name__}."
        )
    return data


def api_delete_task(token: str, project_id: str, task_id: str) -> None:
    """DELETE /project/{projectId}/task/{taskId} — permanently delete a task."""
    url = f"{API_BASE}/project/{project_id}/task/{task_id}"
    try:
        resp = requests.delete(url, headers=_auth_headers(token), timeout=15)
    except requests.RequestException as exc:
        sys.exit(f"Error: DELETE task network failure: {exc}")

    if resp.status_code not in (200, 204):
        _handle_api_error(resp, f"DELETE /project/{project_id}/task/{task_id}")


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def _print_task_fields(task: dict[str, Any], label: str) -> None:
    print(f"  {label}")
    print(_THIN)
    print(f"  Title      : {task.get('title', '?')}")
    print(f"  ID         : {task.get('id', '?')}")
    print(f"  Project    : {task.get('projectId', '?')}")
    print(f"  Priority   : {task.get('priority', '?')}")
    print(f"  Status     : {task.get('status', '?')}")
    print(f"  StartDate  : {task.get('startDate', '(not returned)')}")
    print(f"  DueDate    : {task.get('dueDate', '(not returned)')}")
    print(f"  IsAllDay   : {task.get('isAllDay', '(not returned)')}")
    tags = task.get("tags")
    print(f"  Tags       : {tags if tags is not None else '(not returned)'}")
    reminders = task.get("reminders")
    print(f"  Reminders  : {reminders if reminders is not None else '(not returned)'}")
    content = task.get("content") or task.get("desc") or ""
    if content:
        display = content[:120] + ("…" if len(content) > 120 else "")
        print(f"  Content    : {display}")


def _step(n: int, label: str) -> None:
    print()
    print(f"  Step {n}: {label}")
    print(_THIN)


def _check(label: str, passed: bool, detail: str = "") -> None:
    icon = "✓" if passed else "✗"
    suffix = f" — {detail}" if detail else ""
    print(f"  {icon}  {label}{suffix}")


def _cap(value: bool | str | None) -> str:
    if value is True:
        return "YES"
    if value is False:
        return "NO"
    if value is None:
        return "NOT_TESTED"
    return str(value)


def _print_capability_matrix(caps: dict[str, Any]) -> None:
    print()
    print(_RULE)
    print("  Capability Matrix")
    print(_RULE)
    max_key = max(len(k) for k in caps)
    for k, v in caps.items():
        print(f"  {k:<{max_key}} : {_cap(v)}")
    print(_RULE)


# ---------------------------------------------------------------------------
# Date/time helpers
# ---------------------------------------------------------------------------

def _build_start_due(ts_utc: str) -> tuple[str, str, str, str]:
    """Return (start_iso, due_iso, start_local_display, due_local_display).

    Start = next whole UTC hour (safe default for any timezone).
    Due   = Start + 90 minutes.
    Returns ISO 8601 strings with timezone offset for TickTick.
    """
    local_now = datetime.now().astimezone()
    # Round up to next whole hour in local time
    start = local_now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    due   = start + timedelta(minutes=90)
    return (
        start.isoformat(),
        due.isoformat(),
        start.strftime("%Y-%m-%d %H:%M %Z"),
        due.strftime("%Y-%m-%d %H:%M %Z"),
    )


# ---------------------------------------------------------------------------
# Create with progressive fallback
# ---------------------------------------------------------------------------

def _create_with_fallback(
    token: str,
    project_id: str,
    title: str,
    content: str,
    start_iso: str,
    due_iso: str,
    use_tags: bool,
    use_reminder: bool,
    caps: dict[str, Any],
) -> dict[str, Any]:
    """Try creating the task with full payload, falling back gracefully.

    Fallback order:
      1. Full payload (tags + reminders + dates + priority)
      2. No tags
      3. No reminders
      4. Minimal payload (title + content + dates + priority)

    Updates caps dict in place for tags_create_supported and reminder_create_supported.
    """

    def _base_payload() -> dict[str, Any]:
        return {
            "title": title,
            "projectId": project_id,
            "content": content,
            "priority": PRIORITY_HIGH,
            "startDate": start_iso,
            "dueDate": due_iso,
            "isAllDay": False,
        }

    # Attempt 1: Full payload
    payload = _base_payload()
    if use_tags:
        payload["tags"] = [FIELD_TAG_LABEL]
    if use_reminder:
        payload["reminders"] = [{"trigger": "TRIGGER:PT15M"}]

    task, err = _try_create_task(token, payload, "full payload")
    if task:
        if use_tags:
            caps["tags_create_supported"] = True
        if use_reminder:
            caps["reminder_create_supported"] = True
        return task

    print(f"  ⚠  Full payload rejected: {err}")

    # Attempt 2: Drop tags
    if use_tags:
        print("  ↳  Retrying without tags ...")
        payload2 = _base_payload()
        if use_reminder:
            payload2["reminders"] = [{"trigger": "TRIGGER:PT15M"}]
        task2, err2 = _try_create_task(token, payload2, "no tags")
        if task2:
            caps["tags_create_supported"] = False
            if use_reminder:
                caps["reminder_create_supported"] = True
            print("  ↳  Create without tags: OK")
            return task2
        print(f"  ⚠  No-tags payload rejected: {err2}")
        caps["tags_create_supported"] = False

    # Attempt 3: Drop reminders
    if use_reminder:
        print("  ↳  Retrying without reminders ...")
        payload3 = _base_payload()
        task3, err3 = _try_create_task(token, payload3, "no reminder")
        if task3:
            caps["reminder_create_supported"] = False
            print("  ↳  Create without reminders: OK")
            return task3
        print(f"  ⚠  No-reminder payload rejected: {err3}")
        caps["reminder_create_supported"] = False

    # Attempt 4: Minimal payload
    print("  ↳  Retrying with minimal payload ...")
    minimal: dict[str, Any] = {
        "title": title,
        "projectId": project_id,
        "content": content,
        "priority": PRIORITY_HIGH,
    }
    task4, err4 = _try_create_task(token, minimal, "minimal")
    if task4:
        caps["startDate_create_supported"] = "UNCLEAR"
        caps["dueDate_create_supported"] = "UNCLEAR"
        print("  ↳  Minimal create: OK (dates/tags/reminders not submitted)")
        return task4

    sys.exit(
        "Error: All create attempts failed.\n"
        f"  Last error: {err4}\n"
        "  Check your token and project ID:\n"
        "    python tools/auth_ticktick.py status\n"
        "    python tools/lookup_ticktick_project.py list"
    )


# ---------------------------------------------------------------------------
# source_id check
# ---------------------------------------------------------------------------

def _check_source_id(content: str) -> bool:
    return f"<!-- la:source_id={SOURCE_ID} -->" in content


# ---------------------------------------------------------------------------
# Field test — main orchestrator
# ---------------------------------------------------------------------------

def run_field_test(
    project_id: str,
    delete: bool,
    use_tags: bool,
    use_reminder: bool,
) -> None:
    token = get_access_token()

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    start_iso, due_iso, start_display, due_display = _build_start_due(ts)

    task_title = f"{FIELD_TAG_PREFIX} Life Agent API Field Test — {ts}"
    task_content = (
        "Field capability test only. Safe to delete.\n"
        f"<!-- la:source_id={SOURCE_ID} -->"
    )

    caps: dict[str, Any] = {
        "create_task":                None,
        "read_task":                  None,
        "content_source_id_survives": None,
        "priority_create_supported":  None,
        "priority_update_supported":  None,
        "startDate_create_supported": None,
        "startDate_readback":         None,
        "dueDate_create_supported":   None,
        "dueDate_readback":           None,
        "reminder_create_supported":  None,
        "reminder_readback":          None,
        "tags_create_supported":      None,
        "tags_readback":              None,
        "update_task":                None,
        "delete_cleanup":             None,
    }

    if not use_tags:
        caps["tags_create_supported"] = "SKIPPED (--no-tags)"
        caps["tags_readback"]         = "SKIPPED (--no-tags)"
    if not use_reminder:
        caps["reminder_create_supported"] = "SKIPPED (--no-reminder)"
        caps["reminder_readback"]         = "SKIPPED (--no-reminder)"

    print()
    print(_RULE)
    print("  TickTick Field Capability Test — Phase 2B-5")
    print(_RULE)
    print(f"  Project ID : {project_id}")
    print(f"  Timestamp  : {ts}")
    print(f"  Source ID  : {SOURCE_ID}")
    print(f"  Start      : {start_display}  [{start_iso}]")
    print(f"  Due        : {due_display}  [{due_iso}]")
    print(f"  Tags       : {'la-field-test' if use_tags else 'skipped (--no-tags)'}")
    print(f"  Reminder   : {'TRIGGER:PT15M' if use_reminder else 'skipped (--no-reminder)'}")
    print(f"  Cleanup    : {'--delete set — task will be deleted after test' if delete else 'manual (task left visible)'}")

    task_id: str | None = None

    # ------------------------------------------------------------------
    # Step 1: CREATE with fallback
    # ------------------------------------------------------------------
    _step(1, "Create field test task — POST /task (with fallback)")
    created = _create_with_fallback(
        token, project_id, task_title, task_content,
        start_iso, due_iso, use_tags, use_reminder, caps,
    )
    task_id = created.get("id")
    if not task_id:
        sys.exit(
            "Error: POST /task succeeded but response has no 'id' field.\n"
            f"  Response keys: {list(created.keys())}"
        )
    _print_task_fields(created, "Created task (raw response)")

    # Assess create capabilities from response
    caps["create_task"] = True

    created_priority = created.get("priority")
    caps["priority_create_supported"] = (
        True if created_priority == PRIORITY_HIGH
        else f"UNCLEAR (sent {PRIORITY_HIGH}, got {created_priority})"
    )

    created_start = created.get("startDate")
    caps["startDate_create_supported"] = bool(created_start)

    created_due = created.get("dueDate")
    caps["dueDate_create_supported"] = bool(created_due)

    print(f"  ✓  CREATE passed — task ID: {task_id}")

    # ------------------------------------------------------------------
    # Step 2: READ BACK
    # ------------------------------------------------------------------
    _step(2, f"Read task back — GET /project/{project_id}/task/{task_id}")
    fetched = api_get_task(token, project_id, task_id)
    _print_task_fields(fetched, "Fetched task (read-back)")

    caps["read_task"] = True

    # source_id
    fetched_content = fetched.get("content") or fetched.get("desc") or ""
    source_id_ok = _check_source_id(fetched_content)
    caps["content_source_id_survives"] = source_id_ok
    _check("source_id survives read-back", source_id_ok,
           "" if source_id_ok else "<!-- la:source_id=... --> not found in content")

    # startDate
    fetched_start = fetched.get("startDate")
    caps["startDate_readback"] = bool(fetched_start)
    _check("startDate returned", bool(fetched_start),
           str(fetched_start) if fetched_start else "field absent or null")

    # dueDate
    fetched_due = fetched.get("dueDate")
    caps["dueDate_readback"] = bool(fetched_due)
    _check("dueDate returned", bool(fetched_due),
           str(fetched_due) if fetched_due else "field absent or null")

    # tags
    if use_tags and caps.get("tags_create_supported") is True:
        fetched_tags = fetched.get("tags")
        tags_ok = isinstance(fetched_tags, list) and FIELD_TAG_LABEL in fetched_tags
        caps["tags_readback"] = tags_ok
        _check("tags returned", tags_ok,
               str(fetched_tags) if fetched_tags else "field absent or empty")
    elif use_tags:
        caps["tags_readback"] = False
        _check("tags returned", False, "create did not include tags (fallback was used)")

    # reminders
    if use_reminder and caps.get("reminder_create_supported") is True:
        fetched_rem = fetched.get("reminders")
        rem_ok = isinstance(fetched_rem, list) and len(fetched_rem) > 0
        caps["reminder_readback"] = rem_ok
        _check("reminders returned", rem_ok,
               str(fetched_rem) if fetched_rem else "field absent or empty")
    elif use_reminder:
        caps["reminder_readback"] = False
        _check("reminders returned", False, "create did not include reminders (fallback was used)")

    # title match
    fetched_title = fetched.get("title", "")
    if fetched_title != task_title:
        print(
            f"  ⚠  Title mismatch after GET.\n"
            f"     Expected : {task_title}\n"
            f"     Got      : {fetched_title}"
        )
    else:
        print("  ✓  READ passed — title matches")

    # ------------------------------------------------------------------
    # Step 3: UPDATE
    # ------------------------------------------------------------------
    _step(3, f"Update task — POST /task/{task_id}")
    updated_title   = f"[FIELD TEST UPDATED] Life Agent API Field Test — {ts}"
    updated_content = (
        "Field capability test only. Safe to delete.\n"
        f"<!-- la:source_id={SOURCE_ID} -->\n"
        "Read-back update verified."
    )

    update_payload: dict[str, Any] = {
        "id":        task_id,
        "projectId": project_id,
        "title":     updated_title,
        "content":   updated_content,
        "priority":  PRIORITY_LOW,
    }
    # Preserve dates in update to avoid accidental clear
    if fetched_start:
        update_payload["startDate"] = fetched_start
    if fetched_due:
        update_payload["dueDate"] = fetched_due

    updated = api_update_task(token, task_id, update_payload)
    _print_task_fields(updated, "Updated task")

    # Verify update
    upd_title = updated.get("title", "")
    upd_priority = updated.get("priority")
    update_title_ok    = (upd_title == updated_title)
    update_priority_ok = (upd_priority == PRIORITY_LOW)

    caps["update_task"] = update_title_ok

    _check("UPDATE title applied", update_title_ok,
           "" if update_title_ok else f"got '{upd_title}'")
    _check("priority update applied", update_priority_ok,
           f"sent {PRIORITY_LOW}, got {upd_priority}")
    caps["priority_update_supported"] = update_priority_ok

    upd_content = updated.get("content") or updated.get("desc") or ""
    source_id_after_update = _check_source_id(upd_content)
    _check("source_id survives update", source_id_after_update)

    # ------------------------------------------------------------------
    # Step 4: DELETE or leave visible
    # ------------------------------------------------------------------
    _step(4, "Delete / leave visible")
    if delete:
        api_delete_task(token, project_id, task_id)
        caps["delete_cleanup"] = True
        print(f"  ✓  Task {task_id} deleted.")
    else:
        caps["delete_cleanup"] = "SKIPPED (--delete not passed)"
        print("  Task left visible in TickTick for UI inspection.")
        print(f"  Task title   : {updated_title}")
        print()
        print("  To delete later, run:")
        print(
            f"    python tools/test_ticktick_task_fields.py"
            f" --project-id {project_id}"
            f" --task-id {task_id} --delete-only"
        )
        print("  Or delete it directly from the TickTick app.")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    _print_capability_matrix(caps)

    # ------------------------------------------------------------------
    # User inspection checklist (only when task is left visible)
    # ------------------------------------------------------------------
    if not delete:
        print()
        print(_RULE)
        print("  User UI Inspection Checklist")
        print(_RULE)
        print(f"  Open TickTick and look in: Life Agent - API Test")
        print()
        print(f"  Task title to find:")
        print(f"    {updated_title}")
        print()
        print("  Check each item in TickTick app (phone or web):")
        print("  [ ] Task is visible in 'Life Agent - API Test'")
        print("  [ ] Title shows '[FIELD TEST UPDATED]' prefix")
        start_label = str(fetched_start) if fetched_start else "(not set)"
        due_label   = str(fetched_due) if fetched_due else "(not set)"
        print(f"  [ ] StartDate displays correctly   — intended: {start_display}  (API returned: {start_label})")
        print(f"  [ ] DueDate displays correctly     — intended: {due_display}  (API returned: {due_label})")
        print("  [ ] Task is NOT marked all-day (if isAllDay=False was accepted)")
        fetched_tags_display = fetched.get("tags") if use_tags else "(--no-tags skipped)"
        print(f"  [ ] Tags display correctly         — {fetched_tags_display}")
        fetched_rem_display = fetched.get("reminders") if use_reminder else "(--no-reminder skipped)"
        print(f"  [ ] Reminder display               — {fetched_rem_display}")
        print("  [ ] Notes/content visible including source_id comment")
        print("  [ ] Priority indicator visible (was set to Low=1 after update)")
        print()
        print("  Confirm what you see in TickTick before Phase 2B-6 exporter design.")
        print(_RULE)

    all_core_pass = all(
        caps.get(k) is True
        for k in ["create_task", "read_task", "update_task", "content_source_id_survives"]
    )
    if all_core_pass:
        print()
        print("  ✓  Phase 2B-5 field test complete. Core CRUD + source_id confirmed.")
        print("     Review capability matrix for date/tag/reminder caveats before Phase 2B-6.")
    else:
        print()
        print("  ✗  Phase 2B-5 field test: one or more core checks failed.")
        print("     Review the capability matrix above before proceeding.")


# ---------------------------------------------------------------------------
# Cleanup mode — delete a specific task by ID
# ---------------------------------------------------------------------------

def run_delete_only(project_id: str, task_id: str) -> None:
    token = get_access_token()
    print()
    print(f"  Deleting task {task_id} from project {project_id} ...")
    api_delete_task(token, project_id, task_id)
    print(f"  ✓  Task {task_id} deleted.\n")


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
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        prog="test_ticktick_task_fields",
        description=(
            "Phase 2B-5: TickTick API field capability test.\n"
            "Creates ONE disposable test task with full field payload,\n"
            "reads it back, updates it, and prints a capability matrix.\n"
            "Does NOT export plans. Does NOT create multiple tasks."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python tools/test_ticktick_task_fields.py --project-id abc123\n"
            "  python tools/test_ticktick_task_fields.py --project-id abc123 --delete\n"
            "  python tools/test_ticktick_task_fields.py --project-id abc123 --no-tags\n"
            "  python tools/test_ticktick_task_fields.py --project-id abc123 --no-reminder\n"
            "  python tools/test_ticktick_task_fields.py  # uses TICKTICK_DEFAULT_PROJECT_ID\n"
            "  python tools/test_ticktick_task_fields.py "
            "--project-id abc123 --task-id xyz789 --delete-only\n"
            "\n"
            "preconditions:\n"
            "  python tools/auth_ticktick.py status    # must show valid token\n"
            '  python tools/lookup_ticktick_project.py ensure "Life Agent - API Test" --create\n'
        ),
    )

    parser.add_argument(
        "--project-id",
        dest="project_id",
        metavar="PROJECT_ID",
        default=None,
        help=(
            "TickTick project/list ID to create the test task in. "
            "Falls back to TICKTICK_DEFAULT_PROJECT_ID in .env if not passed."
        ),
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        default=False,
        help=(
            "Delete the test task after all steps pass. "
            "Without this flag, the task remains visible in TickTick for UI inspection."
        ),
    )
    parser.add_argument(
        "--no-tags",
        dest="no_tags",
        action="store_true",
        default=False,
        help="Skip adding tags to the test task (use if tags cause API errors).",
    )
    parser.add_argument(
        "--no-reminder",
        dest="no_reminder",
        action="store_true",
        default=False,
        help="Skip adding a reminder to the test task (use if reminders cause API errors).",
    )
    parser.add_argument(
        "--task-id",
        dest="task_id",
        metavar="TASK_ID",
        default=None,
        help="Task ID to delete. Required with --delete-only for post-run cleanup.",
    )
    parser.add_argument(
        "--delete-only",
        dest="delete_only",
        action="store_true",
        default=False,
        help=(
            "Delete a specific task by --project-id and --task-id without running "
            "the field test. Use for cleanup after a run without --delete."
        ),
    )

    args = parser.parse_args()
    project_id = _resolve_project_id(args.project_id)

    if args.delete_only:
        if not args.task_id:
            sys.exit(
                "Error: --delete-only requires --task-id.\n"
                "  Usage: python tools/test_ticktick_task_fields.py "
                "--project-id PROJECT_ID --task-id TASK_ID --delete-only"
            )
        run_delete_only(project_id, args.task_id)
        return

    run_field_test(
        project_id  = project_id,
        delete      = args.delete,
        use_tags    = not args.no_tags,
        use_reminder= not args.no_reminder,
    )


if __name__ == "__main__":
    main()
