# tools/

This directory contains local tooling for Life Agent automation.

---

## Purpose

Life Agent plans live as structured markdown in git. The tools here bridge those plans to execution surfaces — starting with TickTick for phone-level task management.

All tools are local CLI scripts. They do not modify Life Agent planning docs. They read approved plans, produce normalized output, and export to external services when explicitly triggered.

Life Agent markdown and git remain the source of truth for all planning decisions. Tools here are output adapters only.

---

## TickTick Bridge Status

| Phase | Description | Status |
| --- | --- | --- |
| Phase 1 | Architecture spec + security rules | ✅ Complete |
| Phase 2A | API capability audit | ✅ Complete |
| Phase 2B-0 | Safety scaffold (this directory) | ✅ Complete |
| Phase 2B-1 | PEC validator + dry-run renderer | ✅ Complete — `tools/validate_pec.py` |
| Phase 2B-2 | OAuth / token flow | ✅ Complete — `tools/auth_ticktick.py` |
| Phase 2B-3 | TickTick project lookup and create | ✅ Complete — `tools/lookup_ticktick_project.py` |
| Phase 2B-4 | Batch export with `dry_run: true` default | Not started |
| Phase 2B-5 | First live export with non-sensitive test tasks | Not started |

Automation commands `export week` and `export day` are declared in [LIFE_AGENT_AUTOMATION_INTERFACE.md](../LIFE_AGENT_AUTOMATION_INTERFACE.md) but remain **NOT IMPLEMENTED** until Phase 2B-4 is complete and tested.

---

## Security Rules

These rules apply to all tooling in this directory. They are not optional.

1. **No secrets in git.** Credentials, tokens, and client secrets must never appear in any committed file — including source code, comments, or markdown.
2. **`.env` is local only.** Copy `.env.example` to `.env` locally and fill in your values. `.env` is gitignored and must never be committed.
3. **`.ticktick/` is gitignored.** This directory holds per-week mapping files and the token cache. It must not be committed.
4. **Token files are gitignored.** Any file matching `ticktick_token*.json` or `ticktick_map*.json` is gitignored. Do not override this.
5. **Exporter must never log tokens.** No `print(access_token)`, no `console.log(secret)`, no token in stdout or stack traces.
6. **Test against a test list first.** Before any live export, run against a throwaway TickTick list to verify field mapping without affecting real data.

See [TICKTICK_BRIDGE_SECURITY.md](../TICKTICK_BRIDGE_SECURITY.md) for the full security policy.

---

## Planned Phase Details

### Phase 2B-1 — PEC validator / dry-run renderer

Load a PEC JSON file (see `samples/pec_week_sample.json`), validate all fields against the spec, and print a human-readable summary of what would be created/updated/skipped in TickTick. No API calls. No credentials required.

**Input:** `tools/samples/pec_week_sample.json` or a generated PEC
**Output:** Terminal summary — task count, field warnings, source_id list
**API calls:** None

---

### Phase 2B-2 — OAuth / token flow

Implements the Authorization Code Grant flow:

1. Open browser to `https://ticktick.com/oauth/authorize`
2. Capture redirect to `localhost:8080/callback`
3. Exchange authorization code for access + refresh tokens
4. Store tokens in `.ticktick/ticktick_token.json` (gitignored — never in `.env`)

**Scopes required:** `tasks:read tasks:write`
**Precondition:** TickTick Developer App registered; `TICKTICK_CLIENT_ID` and `TICKTICK_CLIENT_SECRET` in `.env`

---

### Phase 2B-3 — TickTick project lookup and create

Before exporting tasks, ensure the target TickTick project/list exists.
For each week, look up or create a list named `Life Agent - {YYYY}-W{week}`.
Store the resolved `projectId` for use in the exporter.

**API calls:** `GET /project`, `POST /project` (only with `--create`)

---

### Phase 2B-4 — Batch export with `dry_run: true` default

Implements the full idempotency loop:

- Load PEC
- Check mapping file for existing source_ids
- Compute content_hash for each task
- Determine: create / update / skip / cancel
- `dry_run: true` (default): print the plan, no API write
- `dry_run: false`: execute via `POST /batch/task` or `PUT /batch/task`

**Cancel policy default:** Prepend `[CANCELLED]` to title (non-destructive).
See [TICKTICK_BRIDGE_SPEC.md §7](../TICKTICK_BRIDGE_SPEC.md) for full idempotency design.

---

### Phase 2B-5 — First live export

After Phase 2B-4 is validated on dry-run:

1. Create a throwaway test list in TickTick.
2. Run `export day` on a non-sensitive sample PEC with `dry_run: false`.
3. Verify tasks appear correctly in TickTick (title, date, priority, reminder).
4. Verify re-export is idempotent (no duplicates).
5. Verify cancel policy applies correctly.

Only promote to production use after this test passes.

---

## Sample PEC Files

`tools/samples/pec_week_sample.json` — a non-sensitive example PEC for a single week, used for:

- PEC validator development (Phase 2B-1)
- Dry-run output formatting
- Field mapping verification
- Idempotency logic testing

Sample files must never contain:

- real client names or project codenames
- internal architecture details
- actual TickTick project IDs or task IDs
- credentials or tokens

---

## Source-of-Truth Reminder

Tools in this directory are export adapters. They read Life Agent plans and push to TickTick.

**They do not:**

- modify Life Agent planning docs
- rewrite weekly or daily plans
- alter capacity rules, anchor assignments, or project priorities
- treat TickTick completion status as authoritative planning truth

If TickTick data and Life Agent plans conflict, Life Agent plans take precedence.

---

**Last updated:** 2026-04-27 | **Phase:** 2B-3 Complete
