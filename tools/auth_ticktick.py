#!/usr/bin/env python3
"""tools/auth_ticktick.py

Phase 2B-2: TickTick OAuth / token helper for the Life Agent bridge.

Usage:
    python tools/auth_ticktick.py login    # Full Authorization Code Grant flow
    python tools/auth_ticktick.py status   # Show token status (no network call)
    python tools/auth_ticktick.py refresh  # Exchange refresh_token for new access_token

Reads OAuth app config from:  .env          (repo root — gitignored)
Stores runtime tokens in:     .ticktick/ticktick_token.json  (gitignored)

Scope: authentication only.
Does NOT call task or project API endpoints.
Does NOT read PEC files or mapping files.
Does NOT modify Life Agent planning documents.

Requires: Python 3.10+, requests library.
Install:  pip install requests
"""

from __future__ import annotations

import argparse
import http.server
import json
import sys
import time
import urllib.parse
import webbrowser
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    import requests
    import requests.auth
except ImportError:
    sys.exit(
        "Error: 'requests' is not installed.\n"
        "  Run: pip install requests"
    )


# ---------------------------------------------------------------------------
# Paths and constants
# ---------------------------------------------------------------------------

REPO_ROOT      = Path(__file__).resolve().parent.parent
ENV_FILE       = REPO_ROOT / ".env"
TOKEN_DIR      = REPO_ROOT / ".ticktick"
TOKEN_FILE     = TOKEN_DIR / "ticktick_token.json"
GITIGNORE_FILE = REPO_ROOT / ".gitignore"

AUTH_URL  = "https://ticktick.com/oauth/authorize"
TOKEN_URL = "https://ticktick.com/oauth/token"
SCOPES    = "tasks:read tasks:write"

CALLBACK_TIMEOUT = 120  # seconds to wait for browser redirect


# ---------------------------------------------------------------------------
# .env loader — stdlib only, no python-dotenv dependency
# ---------------------------------------------------------------------------

def load_env(path: Path) -> dict[str, str]:
    """Parse a .env file. Returns empty dict if file does not exist."""
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


def require_env(env: dict[str, str], key: str) -> str:
    """Return a required .env value or exit with a clear instructional message."""
    val = env.get(key, "").strip()
    if not val or val.startswith("your_"):
        sys.exit(
            f"Error: {key} is missing or still set to a placeholder in .env\n"
            f"  Copy .env.example to .env and fill in your TickTick Developer App credentials.\n"
            f"  Register the app at https://developer.ticktick.com/\n"
            f"  See tools/README.md for setup instructions."
        )
    return val


# ---------------------------------------------------------------------------
# Token file operations
# ---------------------------------------------------------------------------

def _save_token(data: dict[str, Any]) -> None:
    TOKEN_DIR.mkdir(parents=True, exist_ok=True)
    TOKEN_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _load_token() -> dict[str, Any] | None:
    if not TOKEN_FILE.exists():
        return None
    try:
        return json.loads(TOKEN_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _mask(token: str) -> str:
    """Return a safely masked token representation for display."""
    if len(token) <= 8:
        return "***"
    return token[:4] + "···" + token[-4:]


def _annotate_expiry(data: dict[str, Any]) -> dict[str, Any]:
    """Add obtained_at and expires_at timestamps to a token response dict."""
    now = datetime.now(timezone.utc)
    data["obtained_at"] = now.isoformat()
    expires_in = int(data.get("expires_in", 0))
    data["expires_at"] = (now + timedelta(seconds=expires_in)).isoformat() if expires_in else None
    return data


# ---------------------------------------------------------------------------
# Expiry helpers
# ---------------------------------------------------------------------------

def _parse_expiry(token: dict[str, Any]) -> datetime | None:
    exp_at = token.get("expires_at")
    if not exp_at:
        return None
    try:
        dt = datetime.fromisoformat(exp_at)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except (ValueError, TypeError):
        return None


def _expiry_summary(token: dict[str, Any]) -> str:
    expires = _parse_expiry(token)
    if expires is None:
        return "unknown"
    remaining = expires - datetime.now(timezone.utc)
    if remaining.total_seconds() <= 0:
        return "EXPIRED"
    days  = remaining.days
    hours = remaining.seconds // 3600
    return f"valid  ({days}d {hours}h remaining)"


# ---------------------------------------------------------------------------
# Pre-flight gitignore safety check
# ---------------------------------------------------------------------------

def _check_gitignore() -> None:
    if not GITIGNORE_FILE.exists():
        print("[WARN] .gitignore not found — ensure .ticktick/ and .env are not committed.", file=sys.stderr)
        return
    content = GITIGNORE_FILE.read_text(encoding="utf-8")
    for entry in (".env", ".ticktick/"):
        if entry not in content:
            print(f"[WARN] .gitignore is missing '{entry}'. Token storage may not be protected.", file=sys.stderr)


# ---------------------------------------------------------------------------
# OAuth callback server
# ---------------------------------------------------------------------------

class _CallbackHandler(http.server.BaseHTTPRequestHandler):
    """One-shot local HTTP server that captures the OAuth redirect code."""

    captured_code:  str | None = None
    captured_error: str | None = None

    def do_GET(self) -> None:  # noqa: N802
        params = dict(urllib.parse.parse_qsl(urllib.parse.urlparse(self.path).query))
        if "error" in params:
            _CallbackHandler.captured_error = params["error"]
            body = f"<h2>Authorization Error</h2><p>{params['error']}</p><p>Return to terminal.</p>"
        elif "code" in params:
            _CallbackHandler.captured_code = params["code"]
            body = "<h2>Authorization Successful</h2><p>Return to terminal. You may close this tab.</p>"
        else:
            body = "<h2>Unexpected callback</h2><p>Return to terminal.</p>"

        html = f"<html><body>{body}</body></html>".encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(html)))
        self.end_headers()
        self.wfile.write(html)

    def log_message(self, fmt: str, *args: Any) -> None:
        pass  # suppress server access log


def _port_from_uri(redirect_uri: str) -> int:
    return urllib.parse.urlparse(redirect_uri).port or 8080


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

_RULE = "  ══════════════════════════════════════════════════════"


def cmd_login(env: dict[str, str]) -> None:
    client_id     = require_env(env, "TICKTICK_CLIENT_ID")
    client_secret = require_env(env, "TICKTICK_CLIENT_SECRET")
    redirect_uri  = require_env(env, "TICKTICK_REDIRECT_URI")

    _check_gitignore()

    # Warn if already authenticated
    existing = _load_token()
    if existing and existing.get("access_token"):
        expiry = _expiry_summary(existing)
        print(f"  [INFO] Existing token found (status: {expiry}).")
        print("  Proceeding with new login will replace it.")
        print()

    port = _port_from_uri(redirect_uri)
    auth_url = (
        AUTH_URL
        + "?"
        + urllib.parse.urlencode({
            "client_id":     client_id,
            "redirect_uri":  redirect_uri,
            "response_type": "code",
            "scope":         SCOPES,
        })
    )

    _CallbackHandler.captured_code  = None
    _CallbackHandler.captured_error = None

    try:
        server = http.server.HTTPServer(("localhost", port), _CallbackHandler)
    except OSError as exc:
        sys.exit(
            f"Error: Could not bind to localhost:{port} — {exc}\n"
            f"  Check that nothing else is using port {port}, "
            f"or change TICKTICK_REDIRECT_URI in .env."
        )

    server.timeout = 2  # poll interval in seconds

    print()
    print("  Opening browser for TickTick authorization...")
    print(f"  Waiting for callback on localhost:{port}  (timeout: {CALLBACK_TIMEOUT}s)")
    print()

    try:
        webbrowser.open(auth_url)
    except Exception:
        print(f"  Could not open browser. Open this URL manually:")
        print(f"  {auth_url}")
        print()

    code:  str | None = None
    error: str | None = None

    try:
        deadline = time.monotonic() + CALLBACK_TIMEOUT
        while time.monotonic() < deadline:
            server.handle_request()
            code  = _CallbackHandler.captured_code
            error = _CallbackHandler.captured_error
            if code or error:
                break
    finally:
        server.server_close()

    if error:
        sys.exit(f"Error: Authorization rejected — {error}")
    if not code:
        sys.exit("Error: Timed out waiting for authorization code. Try again.")

    print("  Authorization code received. Exchanging for tokens...")

    try:
        resp = requests.post(
            TOKEN_URL,
            auth=requests.auth.HTTPBasicAuth(client_id, client_secret),
            data={
                "grant_type":   "authorization_code",
                "code":         code,
                "redirect_uri": redirect_uri,
            },
            timeout=30,
        )
    except requests.RequestException as exc:
        sys.exit(f"Error: Token exchange network failure: {exc}")

    if resp.status_code != 200:
        sys.exit(
            f"Error: Token exchange failed (HTTP {resp.status_code})\n"
            f"  Response: {resp.text[:300]}"
        )

    try:
        token_data: dict[str, Any] = resp.json()
    except Exception:
        sys.exit("Error: Token endpoint returned non-JSON. Response may not be the TickTick API.")

    if "access_token" not in token_data:
        sys.exit(f"Error: No access_token in response. Keys received: {list(token_data.keys())}")

    _annotate_expiry(token_data)
    _save_token(token_data)

    print()
    print(_RULE)
    print("  ✓  Login successful")
    print(f"  Tokens saved  : .ticktick/ticktick_token.json")
    print(f"  Access token  : {_mask(token_data['access_token'])}")
    rt = token_data.get("refresh_token", "")
    print(f"  Refresh token : {_mask(rt) if rt else 'NOT PROVIDED'}")
    print(f"  Scope         : {token_data.get('scope', '?')}")
    print(f"  Expiry        : {_expiry_summary(token_data)}")
    print(_RULE)
    print()
    print("  Next: python tools/auth_ticktick.py status")
    print()


def cmd_status() -> None:
    token = _load_token()
    print()
    print(_RULE)
    print("  TickTick Token Status")
    print(_RULE)

    if token is None:
        print("  Token file    : NOT FOUND")
        print("  Status        : Not authenticated")
        print(_RULE)
        print()
        print("  Run: python tools/auth_ticktick.py login")
        print()
        return

    access  = token.get("access_token", "")
    refresh = token.get("refresh_token", "")

    print(f"  Token file    : {TOKEN_FILE}")
    print(f"  Access token  : {_mask(access) if access else 'MISSING'}")
    print(f"  Refresh token : {_mask(refresh) if refresh else 'MISSING'}")
    print(f"  Scope         : {token.get('scope', 'unknown')}")
    print(f"  Obtained at   : {token.get('obtained_at', 'unknown')}")
    print(f"  Expires at    : {token.get('expires_at', 'unknown')}")
    print(f"  Expiry status : {_expiry_summary(token)}")

    print(_RULE)

    if not access:
        print("  → Run: python tools/auth_ticktick.py login")
    elif _expiry_summary(token) == "EXPIRED":
        print("  → Run: python tools/auth_ticktick.py refresh  (or login if refresh_token is also expired)")
    else:
        print("  → Token is valid. Ready for Phase 2B-3.")

    print()


def cmd_refresh(env: dict[str, str]) -> None:
    client_id     = require_env(env, "TICKTICK_CLIENT_ID")
    client_secret = require_env(env, "TICKTICK_CLIENT_SECRET")

    token = _load_token()
    if token is None:
        sys.exit(
            "Error: No token file found.\n"
            "  Run: python tools/auth_ticktick.py login"
        )

    refresh_token = token.get("refresh_token", "").strip()
    if not refresh_token:
        sys.exit(
            "Error: refresh_token is missing from .ticktick/ticktick_token.json\n"
            "  Run: python tools/auth_ticktick.py login"
        )

    print()
    print("  Refreshing access token...")

    try:
        resp = requests.post(
            TOKEN_URL,
            auth=requests.auth.HTTPBasicAuth(client_id, client_secret),
            data={
                "grant_type":    "refresh_token",
                "refresh_token": refresh_token,
            },
            timeout=30,
        )
    except requests.RequestException as exc:
        sys.exit(f"Error: Refresh network failure: {exc}")

    if resp.status_code == 401:
        sys.exit(
            "Error: Refresh token rejected (HTTP 401). "
            "Token may be expired or revoked.\n"
            "  Run: python tools/auth_ticktick.py login"
        )
    if resp.status_code != 200:
        sys.exit(
            f"Error: Refresh failed (HTTP {resp.status_code})\n"
            f"  Response: {resp.text[:300]}"
        )

    try:
        new_data: dict[str, Any] = resp.json()
    except Exception:
        sys.exit("Error: Refresh endpoint returned non-JSON response.")

    if "access_token" not in new_data:
        sys.exit(f"Error: No access_token in refresh response. Keys: {list(new_data.keys())}")

    # Some OAuth servers omit refresh_token on refresh — preserve existing one.
    if not new_data.get("refresh_token"):
        new_data["refresh_token"] = refresh_token

    _annotate_expiry(new_data)
    _save_token(new_data)

    print()
    print(_RULE)
    print("  ✓  Token refreshed")
    print(f"  Access token  : {_mask(new_data['access_token'])}")
    print(f"  Expiry        : {_expiry_summary(new_data)}")
    print(_RULE)
    print()


# ---------------------------------------------------------------------------
# Public API for downstream tools (Phase 2B-4 exporter)
# ---------------------------------------------------------------------------

def load_valid_token() -> dict[str, Any]:
    """
    Load the stored token for use by downstream tools such as the exporter.

    Returns the full token dict if valid.
    Exits with a clear message if token is missing or expired.
    Does not auto-refresh — caller must run `auth_ticktick.py refresh` explicitly.
    """
    token = _load_token()
    if token is None:
        sys.exit(
            "Error: Not authenticated. Run:\n"
            "  python tools/auth_ticktick.py login"
        )
    if not token.get("access_token"):
        sys.exit(
            "Error: access_token missing from token file. Run:\n"
            "  python tools/auth_ticktick.py login"
        )
    expires = _parse_expiry(token)
    if expires and datetime.now(timezone.utc) > expires:
        sys.exit(
            "Error: Access token is expired. Run:\n"
            "  python tools/auth_ticktick.py refresh"
        )
    return token


def get_access_token() -> str:
    """Return the current access_token string for use in API calls."""
    return str(load_valid_token()["access_token"])


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        prog="auth_ticktick",
        description="Phase 2B-2: TickTick OAuth / token helper for Life Agent bridge.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Token storage policy:\n"
            "  .env                           — OAuth app config only (client_id, secret, redirect_uri)\n"
            "  .ticktick/ticktick_token.json  — runtime tokens (gitignored, never committed)\n"
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("login",   help="Run full OAuth Authorization Code Grant flow")
    sub.add_parser("status",  help="Show current token status (no network calls)")
    sub.add_parser("refresh", help="Exchange refresh_token for a new access_token")

    args = parser.parse_args()
    env  = load_env(ENV_FILE)

    if args.command == "login":
        cmd_login(env)
    elif args.command == "status":
        cmd_status()
    elif args.command == "refresh":
        cmd_refresh(env)


if __name__ == "__main__":
    main()
