# TickTick Bridge Security

> **Purpose:** Define credential handling, token storage, sensitive content, and security pre-conditions for the Life Agent → TickTick execution bridge.
> This document governs security decisions for all phases of TickTick bridge implementation.

---

## Table of Contents

- [1. Credential Handling Rules](#1-credential-handling-rules)
- [2. Token Storage Policy](#2-token-storage-policy)
- [3. Local Mapping File Policy](#3-local-mapping-file-policy)
- [4. Sensitive Task Content Rules](#4-sensitive-task-content-rules)
- [5. Phone Display Rules](#5-phone-display-rules)
- [6. Pre-Implementation Security Checklist](#6-pre-implementation-security-checklist)

---

## 1. Credential Handling Rules

These rules apply before any code is written and must not be violated at any phase.

| Rule | Rationale |
|---|---|
| No credentials, tokens, or client secrets in git — ever | TickTick OAuth credentials grant full access to the user's TickTick account. A leaked secret cannot be easily rotated without invalidating all exported tasks. |
| No tokens or secrets in any markdown file | Markdown files are version-controlled and may be shared, audited, or opened in tooling that logs content. |
| No client secret hardcoded in script source | Scripts are committed to git. Hardcoded secrets become permanent repo history even after deletion. |
| `.env` must be added to `.gitignore` before any real credential is written | The gitignore entry must exist before the first `TICKTICK_CLIENT_SECRET` value is ever set locally. |
| `.env.example` may contain placeholder values only — no real credentials | `.env.example` is the instructional scaffold. It shows field names without values. |
| TickTick Developer App registration is done manually by the user | The exporter script cannot and must not create the app registration on behalf of the user. Instructions must guide the user to do this via the TickTick developer portal. |

---

## 2. Token Storage Policy

OAuth access tokens and refresh tokens are runtime state. They are not planning state and do not belong in the repo.

| Storage location | Policy |
|---|---|
| Local `.env` file (gitignored) | Acceptable for prototype and local CLI use. Sufficient for Phase 2. |
| OS keychain / credential manager | Preferred for personal machine setups with long-lived use. Recommended over `.env` once the exporter stabilizes. |
| Token cache file (e.g., `.ticktick/token_cache.json`) | Must be gitignored. Must never be committed. |
| Any markdown planning file | Never. |
| Hardcoded in script | Never. |
| Committed to git in any form | Never. |

**Token refresh:** The exporter script is responsible for handling token expiry and refresh. Token refresh logic is a runtime concern, not a planning concern. Do not store refresh timestamps or token metadata in planning docs.

**Revocation:** If credentials are suspected to have leaked into git (accidental commit), the TickTick Developer App credentials must be rotated immediately via the TickTick developer portal. Git history must be scrubbed using `git filter-branch` or `git filter-repo`. Do not assume `git rm` is sufficient.

---

## 3. Local Mapping File Policy

The per-week mapping file (`.ticktick/{year}-W{week}_map.json`) is not a secret. However, it contains TickTick task IDs and exported task metadata that are specific to the user's TickTick account.

| Rule | Rationale |
|---|---|
| `.ticktick/` directory must be gitignored by default | Mapping files reveal task IDs, export timestamps, and task metadata. These are not planning truth and do not belong in version-controlled repo state. |
| Do not commit mapping files unless a future explicit team policy decision says otherwise | The default is local-only. Any change to this policy requires a team decision. |
| Mapping files may be deleted without data loss | If the mapping file is lost, the embedded `source_id` comment in each TickTick task notes field allows recovery. See TICKTICK_BRIDGE_SPEC.md §7 for recovery procedure. |

---

## 4. Sensitive Task Content Rules

TickTick is a third-party cloud service. Treat it as a semi-public execution surface.

**Do not export to TickTick:**
- Full internal architecture details or design decisions
- Customer names, project codenames, or client-identifiable information if this creates a data sensitivity risk
- Credential hints, internal repo URLs, or access paths
- Full context from decision logs or spike documents
- Detailed operating rules or capacity constraints

**Do export to TickTick:**
- Short action-oriented task titles
- Project scope tags
- Time windows (start/end time)
- Priority
- One-line artifact expectation in notes (if not sensitive)
- Embedded source_id comment in notes

**For sensitive tasks (e.g., Zephyr KTLO with client context):**
Export a sanitized title and project tag only. Leave notes field empty. Example:
- Full title in Life Agent plan: "Zephyr: investigate auth regression in client X's staging environment"
- Exported TickTick title: "Zephyr: auth regression investigation"
- Exported notes: `<!-- la:source_id=LA-CW2026-W14-D20260409-BLOCK-ZEPHYR-001 -->`

**Notes length rule:** Notes should never exceed 2–3 lines. If you find yourself writing a paragraph in the notes field, stop. That content belongs in the Life Agent plan doc, not in TickTick.

---

## 5. Phone Display Rules

Tasks exported to TickTick will be read on a phone screen. Format accordingly.

| Rule | Guidance |
|---|---|
| Task titles should be short and action-oriented | Target: under 60 characters. On a phone, long titles are truncated or require scrolling. |
| Do not embed project name in the title if it's already a tag | Bad: `[RobotOS] Motor driver interrupt test`. Good: `Motor driver interrupt test` + tag `#robotos`. |
| Do not use markdown formatting in titles | No backticks, asterisks, or brackets in task titles. TickTick displays these as literal characters. |
| Use tags for context, not title prefixes | Tags are visible in TickTick's filter/group views. Prefixes clutter the title. |
| Reserve notes for one-line artifact hints | If the user needs to know what artifact to produce, one line in notes is acceptable. Do not write instructions. |
| Avoid abbreviations that are only meaningful in the repo | `KTLO`, `ADR`, `W14` may not be self-explanatory on the phone. Expand if needed. |

---

## 6. Pre-Implementation Security Checklist

Complete this checklist before writing any Phase 2 code.

- [ ] `.gitignore` updated to include: `.env`, `.ticktick/`, `*_map.json`, `token_cache.json`
- [ ] `.env.example` file added with placeholder values only (no real credentials)
- [ ] TickTick Developer App registered manually by user via TickTick developer portal
- [ ] OAuth client_id and client_secret stored only in local `.env`, never committed
- [ ] Token cache file location confirmed as gitignored before first OAuth flow
- [ ] Exporter script reviewed: no `print(token)`, no `log(secret)`, no credential in stdout
- [ ] Sample export run verified against a test TickTick list before touching production list
- [ ] Exported sample content reviewed: no sensitive project context, no customer data in task titles or notes
- [ ] Mapping file location confirmed as gitignored
- [ ] Team informed that `.env` must be created locally per machine; it is not shared via git

---

**Last updated:** 2026-04-27 | **Version:** 1.0 | **Phase:** Architecture/Spec only — Phase 1
