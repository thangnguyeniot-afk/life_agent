#!/usr/bin/env python3
"""tools/validate_pec.py

Phase 2B-1: Plan Execution Contract (PEC) validator and dry-run renderer.

Usage:
    python tools/validate_pec.py <pec_file.json>
    python tools/validate_pec.py tools/samples/pec_week_sample.json

Validates a PEC JSON file against TICKTICK_BRIDGE_SPEC.md and prints a
human-readable dry-run export summary.

Scope: validation and rendering only.
No network calls. No credentials. No TickTick API. No external dependencies.

Requires: Python 3.10+. stdlib only.
Exit code: 0 = PASS, 1 = FAIL (validation errors present).
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Constants — derived from TICKTICK_BRIDGE_SPEC.md §4–§5
# ---------------------------------------------------------------------------

VALID_TASK_TYPES: frozenset[str] = frozenset({
    "deep_work_block",
    "shallow_task",
    "routine_checklist",
    "recovery_block",
    "blocker_item",
    "review_task",
    "reminder",
})

VALID_PRIORITIES: frozenset[str] = frozenset({"low", "normal", "high"})

VALID_REMINDER_POLICIES: frozenset[str] = frozenset({
    "at_start",
    "15min_before",
    "none",
})

VALID_EXPORT_STATUSES: frozenset[str] = frozenset({
    "pending",
    "exported",
    "updated",
    "cancelled",
})

VALID_MODES: frozenset[str] = frozenset({"A", "B", "C", "D"})

# Maps each task_type to its expected uppercase abbreviation in source_id.
# Defined in TICKTICK_BRIDGE_SPEC.md §5.
TASK_TYPE_ABBREV: dict[str, str] = {
    "deep_work_block":   "BLOCK",
    "shallow_task":      "TASK",
    "routine_checklist": "ROUTINE",
    "recovery_block":    "RECOVERY",
    "blocker_item":      "BLOCKER",
    "review_task":       "REVIEW",
    "reminder":          "REMIND",
}

# source_id: LA-CW{year}-W{week}-D{YYYYMMDD}-{TYPE}-{SLUG}-{seq}
_SID_RE = re.compile(
    r"^LA-CW(\d{4})-W(\d{2})-D(\d{8})-([A-Z]+)-([A-Z0-9]+)-(\d{3})$"
)

_DATE_RE    = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_TIME_RE    = re.compile(r"^\d{2}:\d{2}$")
_WEEK_ID_RE = re.compile(r"^\d{4}-W\d{2}$")

TITLE_MAX_CHARS = 60


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Issue:
    level: str      # "error" | "warning"
    location: str   # e.g. "meta.week_id" or "task[LA-...].notes"
    message: str


@dataclass
class TaskSummary:
    source_id: str
    day: str
    task_type: str
    project_scope: str
    priority: str
    action: str     # WOULD_CREATE | WOULD_UPDATE | WOULD_SKIP | WOULD_CANCEL
    issues: list[Issue] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return not any(i.level == "error" for i in self.issues)


@dataclass
class PECReport:
    filepath: str
    meta: dict[str, Any]
    tasks: list[TaskSummary] = field(default_factory=list)
    meta_issues: list[Issue] = field(default_factory=list)

    @property
    def all_issues(self) -> list[Issue]:
        return self.meta_issues + [i for t in self.tasks for i in t.issues]

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.all_issues if i.level == "error"]

    @property
    def warnings(self) -> list[Issue]:
        return [i for i in self.all_issues if i.level == "warning"]

    @property
    def is_valid(self) -> bool:
        return not self.errors


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------

def _validate_meta(meta: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []

    for key in ("week_id", "week_start", "week_end", "exported_at", "mode", "dry_run"):
        if key not in meta:
            issues.append(Issue("error", f"meta.{key}", "Required field missing"))

    mode = meta.get("mode")
    if mode and mode not in VALID_MODES:
        issues.append(Issue(
            "error", "meta.mode",
            f"'{mode}' is not a valid mode. Expected one of {sorted(VALID_MODES)}",
        ))

    week_id = meta.get("week_id", "")
    if week_id and not _WEEK_ID_RE.match(str(week_id)):
        issues.append(Issue(
            "warning", "meta.week_id",
            f"'{week_id}' does not match YYYY-Www pattern",
        ))

    if meta.get("dry_run") is not True:
        issues.append(Issue(
            "warning", "meta.dry_run",
            "dry_run should be true for sample and validator use",
        ))

    return issues


def _check_source_id(sid: str, task_type: str, date_val: str) -> list[Issue]:
    issues: list[Issue] = []

    m = _SID_RE.match(sid)
    if not m:
        issues.append(Issue(
            "error", f"task[{sid}].source_id",
            "Does not match LA-CW{year}-W{week}-D{YYYYMMDD}-{TYPE}-{SLUG}-{seq}",
        ))
        return issues

    _year, _week, sid_date, type_abbrev, _slug, _seq = m.groups()

    # Date component must match the task's date field.
    if date_val and _DATE_RE.match(date_val):
        expected_date = date_val.replace("-", "")
        if sid_date != expected_date:
            issues.append(Issue(
                "error", f"task[{sid}].source_id",
                f"Date component '{sid_date}' does not match task date '{date_val}'",
            ))

    # Type abbreviation must correspond to task_type.
    expected_abbrev = TASK_TYPE_ABBREV.get(task_type)
    if expected_abbrev and type_abbrev != expected_abbrev:
        issues.append(Issue(
            "warning", f"task[{sid}].source_id",
            f"Type abbreviation '{type_abbrev}' does not match "
            f"expected '{expected_abbrev}' for task_type '{task_type}'",
        ))

    return issues


def _validate_task(raw: dict[str, Any], day: str) -> TaskSummary:
    sid = str(raw.get("source_id") or "") or "<missing>"
    loc = f"task[{sid}]"
    issues: list[Issue] = []

    # Required fields — presence and type
    required: list[tuple[str, type]] = [
        ("source_id",     str),
        ("title",         str),
        ("date",          str),
        ("all_day",       bool),
        ("project_scope", str),
        ("task_type",     str),
        ("priority",      str),
        ("export_status", str),
    ]
    for fname, ftype in required:
        val = raw.get(fname)
        if val is None:
            issues.append(Issue("error", f"{loc}.{fname}", "Required field missing or null"))
        elif not isinstance(val, ftype):
            issues.append(Issue(
                "error", f"{loc}.{fname}",
                f"Expected {ftype.__name__}, got {type(val).__name__}",
            ))

    # Extract values with safe fallbacks for further checks
    title         = str(raw.get("title") or "")
    date_val      = str(raw.get("date") or "")
    task_type     = str(raw.get("task_type") or "")
    priority      = str(raw.get("priority") or "")
    export_status = str(raw.get("export_status") or "pending")
    reminder      = raw.get("reminder_policy")
    start_time    = raw.get("start_time")
    end_time      = raw.get("end_time")
    notes         = raw.get("notes")
    tt_task_id    = raw.get("ticktick_task_id")

    # Enum validations
    if task_type and task_type not in VALID_TASK_TYPES:
        issues.append(Issue(
            "error", f"{loc}.task_type",
            f"'{task_type}' invalid. Valid: {sorted(VALID_TASK_TYPES)}",
        ))

    if priority and priority not in VALID_PRIORITIES:
        issues.append(Issue(
            "error", f"{loc}.priority",
            f"'{priority}' invalid. Valid: {sorted(VALID_PRIORITIES)}",
        ))

    if export_status and export_status not in VALID_EXPORT_STATUSES:
        issues.append(Issue(
            "error", f"{loc}.export_status",
            f"'{export_status}' invalid. Valid: {sorted(VALID_EXPORT_STATUSES)}",
        ))

    if reminder is not None and reminder not in VALID_REMINDER_POLICIES:
        issues.append(Issue(
            "error", f"{loc}.reminder_policy",
            f"'{reminder}' invalid. Valid: {sorted(VALID_REMINDER_POLICIES)}",
        ))

    # Format validations
    if date_val and not _DATE_RE.match(date_val):
        issues.append(Issue("error", f"{loc}.date", f"'{date_val}' does not match YYYY-MM-DD"))

    if date_val and day and date_val != day:
        issues.append(Issue(
            "error", f"{loc}.date",
            f"Task date '{date_val}' does not match parent day key '{day}'",
        ))

    if start_time is not None and not _TIME_RE.match(str(start_time)):
        issues.append(Issue(
            "error", f"{loc}.start_time",
            f"'{start_time}' does not match HH:MM",
        ))

    if end_time is not None and not _TIME_RE.match(str(end_time)):
        issues.append(Issue(
            "error", f"{loc}.end_time",
            f"'{end_time}' does not match HH:MM",
        ))

    if len(title) > TITLE_MAX_CHARS:
        issues.append(Issue(
            "warning", f"{loc}.title",
            f"Length {len(title)} exceeds recommended {TITLE_MAX_CHARS} chars",
        ))

    # source_id format and consistency
    if sid != "<missing>":
        issues.extend(_check_source_id(sid, task_type, date_val))

    # Embedded source_id comment in notes
    if notes is None:
        issues.append(Issue(
            "warning", f"{loc}.notes",
            "notes is absent; embedded source_id comment cannot be verified",
        ))
    elif sid != "<missing>" and f"<!-- la:source_id={sid} -->" not in str(notes):
        issues.append(Issue(
            "error", f"{loc}.notes",
            f"Missing embedded comment: <!-- la:source_id={sid} -->",
        ))

    # Dry-run action
    if export_status == "cancelled":
        action = "WOULD_CANCEL"
    elif tt_task_id is not None:
        action = "WOULD_UPDATE"
    else:
        action = "WOULD_CREATE"

    return TaskSummary(
        source_id=sid,
        day=day,
        task_type=task_type or "unknown",
        project_scope=str(raw.get("project_scope") or "unknown"),
        priority=priority or "unknown",
        action=action,
        issues=issues,
    )


def validate_pec(filepath: str) -> PECReport:
    path = Path(filepath)
    if not path.exists():
        sys.exit(f"Error: file not found: {filepath}")

    try:
        data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(f"Error: invalid JSON in {filepath}: {exc}")

    meta_issues: list[Issue] = []

    if "export_meta" not in data:
        meta_issues.append(Issue("error", "root", "Missing 'export_meta' key"))
    if "days" not in data:
        meta_issues.append(Issue("error", "root", "Missing 'days' key"))
        return PECReport(filepath=str(path), meta={}, meta_issues=meta_issues)

    meta: dict[str, Any] = data.get("export_meta", {})
    meta_issues.extend(_validate_meta(meta))

    tasks: list[TaskSummary] = []
    seen: dict[str, str] = {}  # source_id -> first day it appeared

    for day, day_data in data.get("days", {}).items():
        if not _DATE_RE.match(day):
            meta_issues.append(Issue(
                "warning", f"days.{day}",
                f"Day key '{day}' does not match YYYY-MM-DD",
            ))
            continue

        day_tasks = day_data.get("tasks", []) if isinstance(day_data, dict) else []
        if not isinstance(day_tasks, list):
            meta_issues.append(Issue("error", f"days.{day}", "'tasks' must be an array"))
            continue

        for raw in day_tasks:
            if not isinstance(raw, dict):
                meta_issues.append(Issue(
                    "error", f"days.{day}", "Non-object entry found in tasks array",
                ))
                continue

            result = _validate_task(raw, day)

            # Uniqueness check across the whole PEC
            sid = result.source_id
            if sid not in ("<missing>", ""):
                if sid in seen:
                    result.issues.append(Issue(
                        "error", f"task[{sid}].source_id",
                        f"Duplicate — same source_id also found on {seen[sid]}",
                    ))
                else:
                    seen[sid] = day

            tasks.append(result)

    return PECReport(filepath=str(path), meta=meta, tasks=tasks, meta_issues=meta_issues)


# ---------------------------------------------------------------------------
# Renderer
# ---------------------------------------------------------------------------

_LINE_WIDE = "══════════════════════════════════════════════════════"
_LINE_THIN = "──────────────────────────────────────────────────────"


def _render_kv(label: str, value: Any) -> None:
    print(f"  {label:<10}: {value}")


def render_report(report: PECReport) -> None:
    meta  = report.meta
    total = len(report.tasks)
    errs  = report.errors
    warns = report.warnings

    # Header
    print()
    print(_LINE_WIDE)
    print("  Life Agent  ·  PEC Dry-Run Validator  ·  Phase 2B-1")
    print(_LINE_WIDE)
    _render_kv("File",   report.filepath)
    if meta:
        week_range = f"{meta.get('week_start', '?')} → {meta.get('week_end', '?')}"
        _render_kv("Week",   f"{meta.get('week_id', '?')}  ({week_range})")
        _render_kv("Mode",   f"{meta.get('mode', '?')}  |  dry_run: {meta.get('dry_run', '?')}")
    _render_kv("Tasks",  total)
    _render_kv("Issues", f"{len(errs)} error(s)   {len(warns)} warning(s)")
    print(_LINE_THIN)

    if total == 0:
        print("  (no tasks found in PEC)")
        _render_footer(report)
        return

    type_counts     = Counter(t.task_type     for t in report.tasks)
    scope_counts    = Counter(t.project_scope for t in report.tasks)
    priority_counts = Counter(t.priority      for t in report.tasks)
    action_counts   = Counter(t.action        for t in report.tasks)

    # Task type breakdown
    print("  Task Types")
    for name, n in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"    {name:<24} {n:>2}")

    # Project scope breakdown
    print(_LINE_THIN)
    print("  Project Scopes")
    for name, n in sorted(scope_counts.items(), key=lambda x: -x[1]):
        print(f"    {name:<24} {n:>2}")

    # Priority breakdown
    print(_LINE_THIN)
    print("  Priorities")
    for name, n in sorted(priority_counts.items()):
        print(f"    {name:<24} {n:>2}")

    # Idempotency readiness
    valid_sid_count = sum(1 for t in report.tasks if _SID_RE.match(t.source_id))
    dup_count       = sum(
        1 for t in report.tasks
        if any("Duplicate" in i.message for i in t.issues)
    )
    embedded_count  = sum(
        1 for t in report.tasks
        if not any(
            "embedded comment" in i.message or "notes is absent" in i.message
            for i in t.issues
        )
    )
    unique_count = total - dup_count

    print(_LINE_THIN)
    print("  Idempotency Readiness")
    print(f"    source_id format  {'✓' if valid_sid_count == total else '✗'}  {valid_sid_count}/{total} valid")
    print(f"    source_id unique  {'✓' if unique_count    == total else '✗'}  {unique_count}/{total} unique")
    print(f"    notes embedded    {'✓' if embedded_count  == total else '✗'}  {embedded_count}/{total} have <!-- la:source_id=... -->")

    # Dry-run export plan
    print(_LINE_THIN)
    print("  Dry-Run Export Plan")
    for action in ("WOULD_CREATE", "WOULD_UPDATE", "WOULD_SKIP", "WOULD_CANCEL"):
        n      = action_counts.get(action, 0)
        marker = "→" if n > 0 else " "
        label  = action.replace("_", " ")
        print(f"  {marker} {label:<18} {n:>2}")

    # Issues
    print(_LINE_THIN)
    print("  Issues")
    if not errs and not warns:
        print("    (none)")
    else:
        for issue in errs:
            print(f"    [ERROR]  {issue.location}")
            print(f"             {issue.message}")
        for issue in warns:
            print(f"    [WARN]   {issue.location}")
            print(f"             {issue.message}")

    # Per-task list
    print(_LINE_THIN)
    print("  Tasks")
    for t in report.tasks:
        icon   = "✓" if t.is_valid else "✗"
        e_cnt  = sum(1 for i in t.issues if i.level == "error")
        w_cnt  = sum(1 for i in t.issues if i.level == "warning")
        suffix = f"  [{e_cnt}E {w_cnt}W]" if t.issues else ""
        print(
            f"  {icon} {t.day}  {t.task_type:<22} {t.priority:<8}"
            f" {t.project_scope:<12}  {t.action}{suffix}"
        )

    _render_footer(report)


def _render_footer(report: PECReport) -> None:
    print(_LINE_WIDE)
    if report.is_valid:
        print("  ✓  PASS — PEC is ready for Phase 2B-2 (OAuth / token flow)")
    else:
        n = len(report.errors)
        print(f"  ✗  FAIL — {n} error(s) must be resolved before proceeding")
    print(_LINE_WIDE)
    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    # Ensure UTF-8 output on Windows terminals that default to cp1252.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    if len(sys.argv) < 2:
        print("Usage:   python tools/validate_pec.py <pec_file.json>", file=sys.stderr)
        print("Example: python tools/validate_pec.py tools/samples/pec_week_sample.json",
              file=sys.stderr)
        sys.exit(1)

    report = validate_pec(sys.argv[1])
    render_report(report)
    sys.exit(0 if report.is_valid else 1)


if __name__ == "__main__":
    main()
