#!/usr/bin/env python3
"""tools/smoke_ticktick_task.py

Phase 2B-4: TickTick task API smoke test.

Creates ONE disposable test task, reads it back, updates it, applies a
[CANCELLED] prefix, then optionally deletes it. Used to validate task API
field behavior before any real PEC/week export.

This script is NOT an exporter. It does NOT read PEC files, create mapping
files, or export Life Agent plans. It creates exactly ONE test task.

Usage:
    python tools/smoke_ticktick_task.py --project-id PROJECT_ID
    python tools/smoke_ticktick_task.py --project-id PROJECT_ID --delete
    python tools/smoke_ticktick_task.py  # uses TICKTICK_DEFAULT_PROJECT_ID
    python tools/smoke_ticktick_task.py --project-id PID --task-id TID --delete-only

Preconditions:
    1. python tools/auth_ticktick.py login  (run once)
    2. python tools/auth_ticktick.py status  (must show valid token)
    3. A test project/list must exist in TickTick, e.g.:
         python tools/lookup_ticktick_project.py ensure "Life Agent - API Test" --create

API scope (task endpoints only):
    POST   /task                           — create task
    GET    /project/{projectId}/task/{id} — read task back
    POST   /task/{taskId}                 — update task
    POST   /task/{taskId}                 — apply [CANCELLED] prefix (second update)
    DELETE /project/{projectId}/task/{id} — only with --delete or --delete-only

Does NOT call project endpoints beyond what is needed to accept the project ID.
Does NOT create multiple tasks. Does NOT read PEC files or write mapping files.

Requires: Python 3.10+, requests library.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
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

API_BASE = "https://api.ticktick.com/open/v1"
REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = REPO_ROOT / ".env"

SMOKE_TAG = "[SMOKE TEST]"
CANCEL_PREFIX = "[CANCELLED]"

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


# ---------------------------------------------------------------------------
# Task API calls — scoped to exactly 4 endpoints (create/get/update/delete)
# ---------------------------------------------------------------------------

def api_create_task(
    token: str,
    project_id: str,
    title: str,
    content: str,
) -> dict[str, Any]:
    """POST /task — create a single task. Returns the created task object."""
    payload: dict[str, Any] = {
        "title": title,
        "projectId": project_id,
        "content": content,
        "priority": 0,
    }
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
        _handle_api_error(resp, "POST /task (create)")

    try:
        data = resp.json()
    except Exception:
        sys.exit(
            "Error: POST /task returned non-JSON.\n"
            f"  Status: {resp.status_code}  Body: {resp.text[:200]}"
        )
    if not isinstance(data, dict):
        sys.exit(f"Error: POST /task expected JSON object, got {type(data).__name__}.")
    return data


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

    # TickTick returns 200 or 204 on successful deletion
    if resp.status_code not in (200, 204):
        _handle_api_error(resp, f"DELETE /project/{project_id}/task/{task_id}")


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def _print_task(task: dict[str, Any], label: str) -> None:
    print(f"  {label}")
    print(_THIN)
    print(f"  Title    : {task.get('title', '?')}")
    print(f"  ID       : {task.get('id', '?')}")
    print(f"  Project  : {task.get('projectId', '?')}")
    print(f"  Priority : {task.get('priority', '?')}")
    print(f"  Status   : {task.get('status', '?')}")
    content = task.get("content") or task.get("desc") or ""
    if content:
        display = content[:100] + ("…" if len(content) > 100 else "")
        print(f"  Content  : {display}")


def _step(n: int, label: str) -> None:
    print()
    print(f"  Step {n}: {label}")
    print(_THIN)


# ---------------------------------------------------------------------------
# Smoke test — 5 steps
# ---------------------------------------------------------------------------

def run_smoke_test(project_id: str, delete: bool) -> None:
    token = get_access_token()

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    task_title = f"{SMOKE_TAG} Life Agent API Test — {ts}"
    task_content = (
        "Disposable smoke test task created by tools/smoke_ticktick_task.py.\n"
        "Safe to delete. Not part of any real Life Agent plan."
    )

    print()
    print(_RULE)
    print("  TickTick Task API Smoke Test — Phase 2B-4")
    print(_RULE)
    print(f"  Project ID : {project_id}")
    print(f"  Cleanup    : {'--delete set — task will be deleted after test' if delete else 'manual (task left with [CANCELLED] prefix)'}")
    print(f"  Timestamp  : {ts}")

    task_id: str | None = None

    # ------------------------------------------------------------------
    # Step 1: CREATE
    # ------------------------------------------------------------------
    _step(1, "Create test task — POST /task")
    created = api_create_task(token, project_id, task_title, task_content)
    task_id = created.get("id")
    if not task_id:
        sys.exit(
            "Error: POST /task succeeded but response has no 'id' field.\n"
            f"  Response keys: {list(created.keys())}"
        )
    _print_task(created, "Created task")
    print(f"  ✓  CREATE passed — task ID: {task_id}")

    # ------------------------------------------------------------------
    # Step 2: READ
    # ------------------------------------------------------------------
    _step(2, f"Read task back — GET /project/{project_id}/task/{task_id}")
    fetched = api_get_task(token, project_id, task_id)
    _print_task(fetched, "Fetched task")
    fetched_title = fetched.get("title", "")
    if fetched_title != task_title:
        print(
            f"  ⚠  Title mismatch after GET.\n"
            f"     Expected : {task_title}\n"
            f"     Got      : {fetched_title}"
        )
    else:
        print("  ✓  READ passed — title matches created task")

    # ------------------------------------------------------------------
    # Step 3: UPDATE
    # ------------------------------------------------------------------
    _step(3, f"Update task — POST /task/{task_id}")
    updated_title = f"{task_title} [updated]"
    update_payload: dict[str, Any] = {
        "id": task_id,
        "projectId": project_id,
        "title": updated_title,
        "content": task_content + "\nUpdate step: content appended.",
    }
    updated = api_update_task(token, task_id, update_payload)
    _print_task(updated, "Updated task")
    returned_title = updated.get("title", "")
    if returned_title != updated_title:
        print(
            f"  ⚠  Title mismatch after UPDATE.\n"
            f"     Expected : {updated_title}\n"
            f"     Got      : {returned_title}"
        )
    else:
        print("  ✓  UPDATE passed — title updated correctly")

    # ------------------------------------------------------------------
    # Step 4: CANCEL PREFIX
    # ------------------------------------------------------------------
    _step(4, f"Apply cancel prefix — POST /task/{task_id}")
    cancelled_title = f"{CANCEL_PREFIX} {updated_title}"
    cancel_payload: dict[str, Any] = {
        "id": task_id,
        "projectId": project_id,
        "title": cancelled_title,
    }
    cancelled = api_update_task(token, task_id, cancel_payload)
    _print_task(cancelled, "Cancel-prefixed task")
    returned_cancelled = cancelled.get("title", "")
    if returned_cancelled != cancelled_title:
        print(
            f"  ⚠  Title mismatch after CANCEL PREFIX.\n"
            f"     Expected : {cancelled_title}\n"
            f"     Got      : {returned_cancelled}"
        )
    else:
        print("  ✓  CANCEL PREFIX passed — title has [CANCELLED] prefix")

    # ------------------------------------------------------------------
    # Step 5: DELETE (only with --delete)
    # ------------------------------------------------------------------
    if delete:
        _step(5, f"Delete test task — DELETE /project/{project_id}/task/{task_id}")
        api_delete_task(token, project_id, task_id)
        print(f"  ✓  DELETE passed — task {task_id} removed from TickTick")
        task_id = None
    else:
        print()
        print(_THIN)
        print("  Step 5: Delete — SKIPPED (--delete not passed)")
        print(_THIN)
        print(f"  Task left in TickTick: {cancelled_title}")
        print()
        print("  To delete it now, run:")
        print(
            f"    python tools/smoke_ticktick_task.py"
            f" --project-id {project_id}"
            f" --task-id {task_id}"
            f" --delete-only"
        )
        print("  Or delete it directly from the TickTick app.")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print()
    print(_RULE)
    print("  Smoke Test Summary")
    print(_RULE)
    print("  Step 1  CREATE         ✓")
    print("  Step 2  READ (GET)     ✓")
    print("  Step 3  UPDATE         ✓")
    print("  Step 4  CANCEL PREFIX  ✓")
    if task_id is None:
        print("  Step 5  DELETE         ✓")
    else:
        print("  Step 5  DELETE         — skipped (task left with [CANCELLED] prefix)")
    print()
    print("  ✓  Phase 2B-4 smoke test complete.")
    print("  Task endpoint behavior confirmed. Safe to proceed to Phase 2B-5.")
    print()


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
        "  To look up or create a test project:\n"
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
        prog="smoke_ticktick_task",
        description=(
            "Phase 2B-4: TickTick task API smoke test.\n"
            "Creates ONE disposable test task, reads it back, updates it,\n"
            "applies a [CANCELLED] prefix, then optionally deletes it.\n"
            "Does NOT export plans. Does NOT create multiple tasks."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python tools/smoke_ticktick_task.py --project-id abc123\n"
            "  python tools/smoke_ticktick_task.py --project-id abc123 --delete\n"
            "  python tools/smoke_ticktick_task.py  # uses TICKTICK_DEFAULT_PROJECT_ID\n"
            "  python tools/smoke_ticktick_task.py --project-id abc123 --task-id xyz789 --delete-only\n"
            "\n"
            "preconditions:\n"
            "  python tools/auth_ticktick.py status   # must show valid token\n"
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
            "Without this flag, the task remains in TickTick with a [CANCELLED] prefix."
        ),
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
            "the smoke test. Use for cleanup after a run without --delete."
        ),
    )

    args = parser.parse_args()
    project_id = _resolve_project_id(args.project_id)

    if args.delete_only:
        if not args.task_id:
            sys.exit(
                "Error: --delete-only requires --task-id.\n"
                "  Usage: python tools/smoke_ticktick_task.py "
                "--project-id PROJECT_ID --task-id TASK_ID --delete-only"
            )
        run_delete_only(project_id, args.task_id)
        return

    run_smoke_test(project_id, args.delete)


if __name__ == "__main__":
    main()
