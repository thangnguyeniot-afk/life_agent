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
| Phase 2B-4 | Task API smoke test (single disposable task) | ✅ Complete — `tools/smoke_ticktick_task.py` |
| Phase 2B-5 | Field capability test (startDate/dueDate/tags/reminders/priority) | ✅ Complete — `tools/test_ticktick_task_fields.py` |
| Phase 2B-6 | PEC-to-TickTick batch exporter skeleton (dry-run default) | ✅ Complete — `tools/export_ticktick_batch.py` |
| Phase 2B-7 | First live export with non-sensitive test tasks | ✅ Complete — W18 sample PEC, 7 tasks created in `Life Agent - API Test` |
| Phase 2C | Plan-to-PEC generation contract + prompt template | ✅ Complete — `05_TEMPLATES/GENERATE_PEC.prompt.md`, `TICKTICK_BRIDGE_SPEC.md §12` |

Automation commands `export week` and `export day` are declared in [LIFE_AGENT_AUTOMATION_INTERFACE.md](../LIFE_AGENT_AUTOMATION_INTERFACE.md) and remain **NOT IMPLEMENTED** as automation commands. `tools/export_ticktick_batch.py` (Phase 2B-6) is a manual batch exporter script — it is not the automation command.

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

### Phase 2B-4 — Task API smoke test

Before building any batch exporter, validate that task create/read/update/delete
behaves as expected against the real TickTick API using ONE disposable test task.

**Steps run by `smoke_ticktick_task.py`:**
1. `POST /task` — create a labeled smoke test task
2. `GET /project/{id}/task/{id}` — read it back and verify title
3. `POST /task/{id}` — update the task (title + content)
4. `POST /task/{id}` — apply `[CANCELLED]` prefix (cancel-policy pre-test)
5. `DELETE /project/{id}/task/{id}` — only with `--delete` flag

**Preconditions:**
- `python tools/auth_ticktick.py status` shows valid token
- A test project/list exists: `python tools/lookup_ticktick_project.py ensure "Life Agent - API Test" --create`

**API calls:** task endpoints only — `POST /task`, `GET /project/*/task/*`, `DELETE /project/*/task/*`

---

### Phase 2B-5 — Field capability test

Before building any batch exporter, validate that TickTick API accepts and returns
all required task fields using ONE disposable test task.

**NOT a batch exporter. Does NOT read PEC files. Creates exactly ONE test task.**

**Steps run by `test_ticktick_task_fields.py`:**
1. `POST /task` — create task with full field payload: title, content, priority, startDate, dueDate, isAllDay, reminders, tags
2. `GET /project/{id}/task/{id}` — read back and verify each field was accepted and returned
3. `POST /task/{id}` — update title, content, priority; verify update applies
4. `DELETE /project/{id}/task/{id}` — only with `--delete` flag

**Flags:**
- `--delete` — delete after test (default: leave visible for UI inspection)
- `--no-tags` — skip tags field (use if tags cause API errors)
- `--no-reminder` — skip reminders field (use if reminders cause API errors)
- `--delete-only --task-id TASK_ID` — cleanup a task left from a prior run

**Capability matrix output:** `create_task`, `read_task`, `content_source_id_survives`,
`priority_create_supported`, `priority_update_supported`, `startDate_create_supported`,
`startDate_readback`, `dueDate_create_supported`, `dueDate_readback`,
`reminder_create_supported`, `reminder_readback`, `tags_create_supported`,
`tags_readback`, `update_task`, `delete_cleanup`

**Fallback behavior:** If full payload is rejected (HTTP 400/422), retries without tags,
then without reminders, then with a minimal payload. Records which fields failed.

**API calls:** task endpoints only — `POST /task`, `GET /project/*/task/*`,
`POST /task/*`, `DELETE /project/*/task/*`

---

### Phase 2B-6 — Batch export skeleton (dry-run default)

Reads a PEC JSON file, validates it, computes create/update/skip/cancel actions
against a local mapping file, and prints the export plan. Live writes only with `--apply`.

**Default mode: dry-run. No API writes without `--apply`.**

**NOT a `export week` / `export day` automation command.** Those remain NOT IMPLEMENTED.

**Usage:**
```
python tools/export_ticktick_batch.py <pec_file> --project-id PROJECT_ID
python tools/export_ticktick_batch.py <pec_file> --project-id PROJECT_ID --apply
python tools/export_ticktick_batch.py <pec_file> --project-id PROJECT_ID --apply --limit 2
```

**Flags:**
- `--apply` — required to write to TickTick (default: dry-run)
- `--limit N` — max number of create/update/cancel ops applied per run
- `--yes` — skip interactive confirmation
- `--mapping-file PATH` — override default mapping file path
- `--cancel-policy prefix` — prepend `[CANCELLED]` to removed tasks (default)
- `--no-cancel` — do not cancel tasks absent from PEC

**Field constraints (from Phase 2B-5 live test):**
- Tags: NOT sent (causes HTTP 500)
- Reminders: NOT sent (causes HTTP 500)
- Recurrence: NOT sent (out of scope for MVP)
- Supported: `title`, `content` (with embedded source_id comment), `priority`, `startDate`, `dueDate`, `isAllDay`

**Priority mapping:**
- `low` → 1, `normal` → 0, `high` → 5

**Idempotency:**
- Mapping file: `.ticktick/{week_id}_map.json` (gitignored)
- Hash includes: title, content, priority, startDate, dueDate, isAllDay, projectId
- create: source_id absent from mapping
- update: source_id present + hash changed
- skip: source_id present + hash same
- cancel: source_id in mapping but absent from PEC

**Mapping file saved only after each successful API operation** (partial-failure safe).

**API calls (only when `--apply`):** `POST /task`, `POST /task/{id}` (update/cancel prefix)

---

## Phase 2C — Plan-to-PEC Generation Contract

### What Phase 2C defines

Phase 2C formalizes the bridge between approved Life Agent planning documents (week plans, daily plans) and the PEC JSON that the exporter consumes.

The full pipeline is:

```
Approved WeekPlan + Daily files
        ↓
[Agent generates PEC JSON using 05_TEMPLATES/GENERATE_PEC.prompt.md]
        ↓
[python tools/validate_pec.py <pec_path>]  ← MUST PASS before commit
        ↓
[git commit PEC file]                      ← Locks source_ids
        ↓
[export_ticktick_batch.py dry-run]          ← Human reviews planned actions
        ↓
[export_ticktick_batch.py --apply]          ← Only after explicit user approval
```

### PEC files vs. mapping files

| Artifact | Type | Location | Committed? |
|---|---|---|---|
| PEC JSON | Planning artifact | `03_PLANNING/03_WEEK/W{n}/YYYY-W{n}_pec.json` | **Yes — commit before apply** |
| Mapping file | Runtime artifact | `.ticktick/YYYY-W{n}_map.json` | **No — gitignored** |

### export week / export day status

`export week` and `export day` remain **NOT IMPLEMENTED** as automation commands.
`tools/export_ticktick_batch.py` is a manual batch exporter script. It is not the automation command. The automation commands will be implemented in a future phase.

### API field constraints (permanent)

| Field | Status |
|---|---|
| `title`, `content`, `priority`, `startDate`, `dueDate`, `isAllDay` | ✅ Works |
| `tags` | ❌ HTTP 500 — never send |
| `reminders` | ❌ HTTP 500 — never send |
| `recurrence` | ⏳ Deferred — null in MVP |

### Example commands for a real week export

**Step 1 — Create the TickTick list for the week (if it does not exist):**
```
python tools/lookup_ticktick_project.py ensure "Life Agent - 2026-W15" --create
```

**Step 2 — Validate the PEC:**
```
python tools/validate_pec.py 03_PLANNING/03_WEEK/W15/2026-W15_pec.json
```

**Step 3 — Dry-run (review planned actions, no writes):**
```
python tools/export_ticktick_batch.py 03_PLANNING/03_WEEK/W15/2026-W15_pec.json --project-id <PROJECT_ID>
```

**Step 4 — Live apply (after dry-run review):**
```
python tools/export_ticktick_batch.py 03_PLANNING/03_WEEK/W15/2026-W15_pec.json --project-id <PROJECT_ID> --apply
```

**Step 5 — Incremental apply (first 2 tasks only):**
```
python tools/export_ticktick_batch.py 03_PLANNING/03_WEEK/W15/2026-W15_pec.json --project-id <PROJECT_ID> --apply --limit 2
```

### Prompt template

To generate a PEC from an approved week plan, use the canonical prompt at:

```
05_TEMPLATES/GENERATE_PEC.prompt.md
```

Fill in the bracketed placeholders (week plan path, daily plan folder, existing PEC if replan, TickTick project ID), then send to your agent of choice. The agent returns PEC JSON only.

Full spec: `TICKTICK_BRIDGE_SPEC.md §12`.

---

### Phase 2B-7 — First live export (complete)

The first live export used `tools/samples/pec_week_sample.json` (W18, 7 tasks) against the `Life Agent - API Test` list. All 7 tasks created successfully. Re-run confirmed idempotency (7 SKIP, 0 CREATE).

**Confirmed working fields:** title, content (source_id comment survives), priority, startDate, dueDate, isAllDay
**Confirmed broken fields:** tags (HTTP 500), reminders (HTTP 500) — permanently excluded from `_build_payload()`

---

After Phase 2B-6 batch export is validated on dry-run:

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

**Last updated:** 2026-04-27 | **Phase:** 2C Complete
