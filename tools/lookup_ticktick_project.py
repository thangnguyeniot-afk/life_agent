#!/usr/bin/env python3
"""tools/lookup_ticktick_project.py

Phase 2B-3: TickTick project/list resolver and API smoke test.

Usage:
    python tools/lookup_ticktick_project.py list
    python tools/lookup_ticktick_project.py find "Life Agent - 2026-W18"
    python tools/lookup_ticktick_project.py ensure "Life Agent - 2026-W18"
    python tools/lookup_ticktick_project.py ensure "Life Agent - 2026-W18" --create

Commands:
    list    Print all TickTick projects/lists with IDs. Smoke-tests auth.
    find    Find a project by exact name. Exit 0 if found, 1 if not.
    ensure  Like find. With --create, creates the project if it does not exist.

API scope: GET /project and POST /project only.
Does NOT call task endpoints. Does NOT create or read tasks.
Reads token from .ticktick/ticktick_token.json via tools/auth_ticktick.py.

Requires: Python 3.10+, requests library.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

try:
    import requests
except ImportError:
    sys.exit("Error: 'requests' not installed. Run: pip install requests")

# Import auth helper from sibling module
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

_RULE = "  ══════════════════════════════════════════════════════"
_THIN = "  ──────────────────────────────────────────────────────"


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def _auth_headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def _handle_api_error(resp: requests.Response, context: str) -> None:
    """Provide specific guidance for each error code and exit."""
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
            "  Token may lack 'tasks:write' scope or the app has insufficient permissions.\n"
            "  Re-run: python tools/auth_ticktick.py login"
        )
    if resp.status_code == 404:
        sys.exit(
            f"Error: {context} — HTTP 404 Not Found\n"
            "  API endpoint not found. The base URL or path may have changed.\n"
            f"  URL attempted: {API_BASE}/project"
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
# Project API calls
# ---------------------------------------------------------------------------

def api_list_projects(token: str) -> list[dict[str, Any]]:
    """GET /project — return list of all project objects."""
    try:
        resp = requests.get(
            f"{API_BASE}/project",
            headers=_auth_headers(token),
            timeout=15,
        )
    except requests.RequestException as exc:
        sys.exit(f"Error: GET /project network failure: {exc}")

    if resp.status_code != 200:
        _handle_api_error(resp, "GET /project")

    try:
        data = resp.json()
    except Exception:
        sys.exit(
            "Error: GET /project returned non-JSON.\n"
            f"  Status: {resp.status_code}  Body: {resp.text[:200]}"
        )

    if not isinstance(data, list):
        sys.exit(
            f"Error: GET /project expected a JSON array, got {type(data).__name__}.\n"
            "  The TickTick API response format may have changed."
        )

    return data


def api_create_project(token: str, name: str) -> dict[str, Any]:
    """POST /project — create a new project with the given name."""
    payload = {"name": name, "viewMode": "list"}

    try:
        resp = requests.post(
            f"{API_BASE}/project",
            headers=_auth_headers(token),
            json=payload,
            timeout=15,
        )
    except requests.RequestException as exc:
        sys.exit(f"Error: POST /project network failure: {exc}")

    if resp.status_code not in (200, 201):
        _handle_api_error(resp, "POST /project")

    try:
        data = resp.json()
    except Exception:
        sys.exit(
            "Error: POST /project returned non-JSON.\n"
            f"  Status: {resp.status_code}  Body: {resp.text[:200]}"
        )

    if not isinstance(data, dict):
        sys.exit(
            f"Error: POST /project expected a JSON object, got {type(data).__name__}."
        )

    return data


# ---------------------------------------------------------------------------
# Project matching
# ---------------------------------------------------------------------------

def find_by_name(
    projects: list[dict[str, Any]],
    name: str,
) -> dict[str, Any] | None:
    """Return the first project whose name exactly matches, or None."""
    for p in projects:
        if p.get("name", "") == name:
            return p
    return None


def find_by_name_icase(
    projects: list[dict[str, Any]],
    name: str,
) -> list[dict[str, Any]]:
    """Return all projects whose name matches case-insensitively (for suggestions)."""
    lower = name.lower()
    return [p for p in projects if p.get("name", "").lower() == lower]


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def _print_project_detail(project: dict[str, Any]) -> None:
    pid  = project.get("id", "?")
    name = project.get("name", "?")
    kind = project.get("kind", project.get("projectType", "?"))
    color = project.get("color", "?")
    print(f"  Name   : {name}")
    print(f"  ID     : {pid}")
    print(f"  Kind   : {kind}")
    print(f"  Color  : {color}")


def _print_env_hint(project_id: str) -> None:
    """Print the .env line the user should add for this project."""
    print()
    print("  To use this project in the exporter, add to .env:")
    print(f"  TICKTICK_DEFAULT_PROJECT_ID={project_id}")


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_list() -> None:
    token    = get_access_token()
    projects = api_list_projects(token)

    print()
    print(_RULE)
    print(f"  TickTick Projects  ({len(projects)} total)")
    print(_RULE)

    if not projects:
        print("  (no projects found — inbox only)")
    else:
        sorted_projects = sorted(projects, key=lambda p: p.get("name", "").lower())
        max_id_len = max((len(str(p.get("id", ""))) for p in sorted_projects), default=8)
        col_id   = max(max_id_len, 8)
        print(f"  {'ID':<{col_id}}  Name")
        print(f"  {'─' * col_id}  {'─' * 40}")
        for p in sorted_projects:
            pid  = str(p.get("id",   "?"))
            name = str(p.get("name", "?"))
            print(f"  {pid:<{col_id}}  {name}")

    print(_RULE)
    print()
    print("  ✓  GET /project smoke test passed — authentication is working.")
    print()


def cmd_find(name: str) -> None:
    token    = get_access_token()
    projects = api_list_projects(token)
    found    = find_by_name(projects, name)

    print()
    print(_RULE)
    print(f"  Find: \"{name}\"")
    print(_RULE)

    if found is None:
        print("  NOT FOUND")

        # Check for case-insensitive near-matches as suggestions
        near = find_by_name_icase(projects, name)
        if near:
            print()
            print("  Near matches (case differs):")
            for p in near:
                print(f"    \"{p.get('name')}\"  (ID: {p.get('id')})")

        print()
        print("  To create it, run:")
        print(f'  python tools/lookup_ticktick_project.py ensure "{name}" --create')
        print()
        sys.exit(1)

    _print_project_detail(found)
    _print_env_hint(str(found.get("id", "")))
    print()
    sys.exit(0)


def cmd_ensure(name: str, create: bool) -> None:
    token    = get_access_token()
    projects = api_list_projects(token)
    found    = find_by_name(projects, name)

    print()
    print(_RULE)
    print(f"  Ensure: \"{name}\"")
    print(_RULE)

    if found is not None:
        print("  Status : Already exists")
        print()
        _print_project_detail(found)
        _print_env_hint(str(found.get("id", "")))
        print()
        sys.exit(0)

    if not create:
        print("  Status : NOT FOUND")
        near = find_by_name_icase(projects, name)
        if near:
            print()
            print("  Near matches (case differs):")
            for p in near:
                print(f"    \"{p.get('name')}\"  (ID: {p.get('id')})")
        print()
        print("  Add --create to create it:")
        print(f'  python tools/lookup_ticktick_project.py ensure "{name}" --create')
        print()
        sys.exit(1)

    print("  Status : Not found — creating...")
    created = api_create_project(token, name)

    pid = created.get("id", "?")
    print()
    print(_RULE)
    print("  ✓  Project created successfully")
    print(_RULE)
    _print_project_detail(created)
    _print_env_hint(str(pid))
    print()
    sys.exit(0)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        prog="lookup_ticktick_project",
        description="Phase 2B-3: TickTick project/list resolver and API smoke test.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python tools/lookup_ticktick_project.py list\n"
            '  python tools/lookup_ticktick_project.py find "Life Agent - 2026-W18"\n'
            '  python tools/lookup_ticktick_project.py ensure "Life Agent - 2026-W18"\n'
            '  python tools/lookup_ticktick_project.py ensure "Life Agent - 2026-W18" --create\n'
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser(
        "list",
        help="List all TickTick projects/lists. Smoke-tests authentication.",
    )

    find_p = sub.add_parser(
        "find",
        help="Find a project by exact name. Exit 0 if found, 1 if not.",
    )
    find_p.add_argument("name", help="Exact project name to find")

    ensure_p = sub.add_parser(
        "ensure",
        help="Find project by exact name. With --create, creates it if absent.",
    )
    ensure_p.add_argument("name", help="Exact project name")
    ensure_p.add_argument(
        "--create",
        action="store_true",
        default=False,
        help="Create the project if it does not already exist",
    )

    args = parser.parse_args()

    if args.command == "list":
        cmd_list()
    elif args.command == "find":
        cmd_find(args.name)
    elif args.command == "ensure":
        cmd_ensure(args.name, args.create)


if __name__ == "__main__":
    main()
