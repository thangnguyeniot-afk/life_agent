# TickTick Bridge Spec

> **Purpose:** Define the architecture, data contract, mapping rules, and idempotency strategy for the Life Agent → TickTick execution bridge.
> This is a specification document. It governs implementation decisions. Do not derive operating rules from TickTick state.

---

## Table of Contents

- [1. Purpose and Scope](#1-purpose-and-scope)
- [2. Source-of-Truth Boundary](#2-source-of-truth-boundary)
- [3. Operating Modes](#3-operating-modes)
- [4. Plan Execution Contract](#4-plan-execution-contract)
- [5. Source ID Convention](#5-source-id-convention)
- [6. Life Agent → TickTick Mapping](#6-life-agent--ticktick-mapping)
- [7. Idempotency Design](#7-idempotency-design)
- [8. TickTick List and Project Strategy](#8-ticktick-list-and-project-strategy)
- [9. Export Trigger Points](#9-export-trigger-points)
- [10. Read-back Audit Policy](#10-read-back-audit-policy)
- [11. Open Questions](#11-open-questions)
- [12. Plan-to-PEC Generation Contract](#12-plan-to-pec-generation-contract)

---

## 1. Purpose and Scope

Life Agent generates weekly and daily plans as structured markdown. Currently, those plans live only in the repo. The user must re-read markdown and manually enter tasks into TickTick to have an actionable phone-level view.

This bridge eliminates that friction by defining a formal path from Life Agent planning output to TickTick task execution.

**What this bridge does:**
- Exports approved Life Agent plan items to TickTick as tasks with dates, times, project tags, and priorities.
- Enables idempotent re-export when plans change mid-week.
- Optionally reads back completion status for weekly review evidence.

**What this bridge does NOT do:**
- Replace Life Agent as the source of truth for planning decisions.
- Allow TickTick edits to rewrite Life Agent plans automatically.
- Export lifestyle blocks (cooking, rest, sleep) or detailed decision context.
- Implement two-way sync in the first version.

**Scope:** This spec covers Phase 1 (architecture definition) and Phase 2 (local exporter) design. Phase 3 (agent-triggered export, MCP integration) is future state and not specified here.

---

## 2. Source-of-Truth Boundary

This boundary is hard. It does not change between phases.

**Life Agent owns:**
- All planning decisions: priorities, capacity allocation, project batching, energy rules
- Definition of Done for each day, week, and month
- Project scope rules and operating constraints
- Anchor assignments (which project gets which day)
- Risk and blocker identification
- Weekly and monthly review conclusions

**TickTick owns:**
- Task presentation on the phone execution surface
- Reminder delivery
- Completion checkboxes for individual tasks
- Phone-level reordering and display

**Completion read-back (future Mode D):**
TickTick completion status may later be read back as audit evidence for weekly review. It is informational input only. It does not automatically update markdown plans, metrics files, or operating rules. Any mismatch between TickTick completion data and Life Agent DoD is surfaced for human judgment.

If TickTick data contradicts Life Agent planning truth, Life Agent planning truth takes precedence.

---

## 3. Operating Modes

Four modes are defined. Only Mode B is the current implementation target.

### Mode A — One-way export only
Life Agent exports tasks to TickTick once. No subsequent update of existing tasks.

| | |
|---|---|
| **Benefit** | Simplest implementation. Low risk of accidental mutation. |
| **Risk** | Re-export creates duplicates. No mid-week replan support. |
| **Complexity** | Low |
| **Status** | Rejected as first target due to idempotency gap. Acceptable only as a dry-run test mode. |

---

### Mode B — One-way export with idempotent update ← Current target
Life Agent exports tasks to TickTick. Re-export detects existing tasks via source_id and updates only changed fields. Removed plan items are semantically cancelled.

| | |
|---|---|
| **Benefit** | Supports mid-week replan. Safe to re-run. Preserves audit trail. |
| **Risk** | Requires stable source_id convention and local mapping file. Parser or PEC generator must be reliable. |
| **Complexity** | Medium |
| **Status** | Target for first usable implementation. |

---

### Mode C — Two-way sync
TickTick task edits (title, date, priority) propagate back into Life Agent planning docs.

| | |
|---|---|
| **Benefit** | Phone edits immediately reflected in planning truth. |
| **Risk** | Phone edits may conflict with Life Agent capacity rules, anchor assignments, or energy guards. High risk of silent planning truth mutation. |
| **Complexity** | High |
| **Status** | Out of scope until Mode B is stable and battle-tested. Do not implement. |

---

### Mode D — Completion read-back audit
After a week closes, Life Agent reads TickTick completion status for the exported task set. Completion data is appended as evidence in the weekly review file. Planning docs are not automatically modified.

| | |
|---|---|
| **Benefit** | Reduces manual weekly review data entry. Adds phone execution evidence to planning review. |
| **Risk** | Completion data may be incomplete (tasks not opened on phone, or phone edits diverged from exported set). |
| **Complexity** | Low-Medium |
| **Status** | Future phase. Not in scope for Phase 2. |

---

## 4. Plan Execution Contract

The Plan Execution Contract (PEC) is the normalized intermediate representation between Life Agent planning artifacts and TickTick export.

### Why PEC exists

Current Life Agent plans are structured markdown prose — bilingual, narrative-heavy, and templated for human readability. Direct markdown parsing is fragile. The PEC decouples planning representation from export representation.

### Two valid generation routes

**Route 1 — Agent-normalized PEC (active path):**
A planning agent reads the approved week plan and available daily plan files and produces a PEC JSON directly. No markdown parser required. The agent interprets anchor assignments, block schedules, and project context to fill PEC fields.

This is the active generation route for Phase 2C. Real Life Agent weekly and daily plan files diverge from the canonical templates in structure and language — they contain bilingual content, evolving table schemas, and natural-language block labels. A script-based parser cannot reliably handle this variability. Agent-normalized PEC is therefore the only viable route for the current plan corpus.

**Route 2 — Markdown parser → PEC (deferred):**
A local script parses daily plan markdown files and extracts structured data into PEC format. Viable only when daily plan files have consistent, machine-readable block structure.

Route 2 is deferred until the plan corpus has accumulated at least 2–3 months of strict template adherence. It is not implemented in Phase 2C and must not be added speculatively. The spec retains the option for future phases.

For the Phase 2C prompt template used to drive Route 1, see `05_TEMPLATES/GENERATE_PEC.prompt.md`.

### PEC field definitions

| Field | Type | Required | Description |
|---|---|---|---|
| `source_id` | string | Yes | Stable identifier for idempotency. See §5. |
| `title` | string | Yes | Short, phone-friendly task title. Max 60 chars. |
| `date` | string (YYYY-MM-DD) | Yes | Assigned execution date. |
| `start_time` | string (HH:MM) | No | Block start time. Null for all-day tasks. |
| `end_time` | string (HH:MM) | No | Block end time in HH:MM format. Null for all-day tasks. For TickTick export, maps to `dueDate` as an ISO 8601 datetime. The public TickTick Open API does not document a dedicated `endTime` or `duration` field; `dueDate` is therefore used as the functional end/deadline anchor. This may render as a deadline rather than a true time range in the phone UI. True time-range rendering depends on TickTick API/Premium behavior and must be live-tested before being treated as guaranteed. |
| `all_day` | boolean | Yes | True if no time window. |
| `project_scope` | string | Yes | Life Agent project slug: `zephyr`, `robotos`, `signee`, `accountant`, or `general`. |
| `task_type` | enum | Yes | See task_type enum below. |
| `priority` | enum | Yes | Life Agent PEC values: `low`, `normal`, `high`. TickTick integer mapping: `low`→`1`, `normal`→`0` (None), `high`→`5`. TickTick value `3` (Medium) is not used by Life Agent PEC MVP unless a future policy explicitly introduces it. |
| `tags` | string[] | No | TickTick tag names. Derived from project_scope and pool. |
| `reminder_policy` | string | No | Life Agent values: `at_start`, `15min_before`, `none`. Maps to TickTick `reminders` array using ISO 8601 trigger notation: `at_start`→`["TRIGGER:PT0S"]`, `15min_before`→`["TRIGGER:PT15M"]`, `none`→`[]`. |
| `recurrence` | string | No | `daily_weekday`, `weekly`, or null. |
| `notes` | string | No | Short context note. Sanitized. Must not contain sensitive architecture details or customer data. |
| `export_status` | enum | Yes | `pending`, `exported`, `updated`, `cancelled`. Managed by exporter, not by planning. |
| `ticktick_project_id` | string | No | TickTick list/project ID. Populated after first export. |
| `ticktick_task_id` | string | No | TickTick task ID. Populated after first export. |

### Task type enum

| Value | Meaning |
|---|---|
| `deep_work_block` | Named ~90 min deep work session. Artifact expected. |
| `shallow_task` | Short action, no artifact required. |
| `routine_checklist` | Morning setup or shutdown checklist (parent task). |
| `recovery_block` | Buffer or rest block. Low priority, no artifact. |
| `blocker_item` | P0 or unblocking item. High priority. |
| `review_task` | Weekly or monthly review trigger. |
| `reminder` | Time-aware reminder without artifact. |

### Example PEC task object

```json
{
  "source_id": "LA-CW2026-W14-D20260409-BLOCK-ROBOTOS-001",
  "title": "RobotOS: motor driver interrupt test",
  "date": "2026-04-09",
  "start_time": "19:00",
  "end_time": "20:30",
  "all_day": false,
  "project_scope": "robotos",
  "task_type": "deep_work_block",
  "priority": "normal",
  "tags": ["robotos", "pool-b"],
  "reminder_policy": "15min_before",
  "recurrence": null,
  "notes": "Artifact: interrupt handler stub. <!-- la:source_id=LA-CW2026-W14-D20260409-BLOCK-ROBOTOS-001 -->",
  "export_status": "pending",
  "ticktick_project_id": null,
  "ticktick_task_id": null
}
```

### Example weekly export envelope

```json
{
  "export_meta": {
    "week_id": "2026-W14",
    "week_start": "2026-04-07",
    "week_end": "2026-04-11",
    "exported_at": "2026-04-07T06:00:00",
    "mode": "B",
    "mapping_file": ".ticktick/2026-W14_map.json"
  },
  "days": {
    "2026-04-07": { "tasks": [] },
    "2026-04-08": { "tasks": [] },
    "2026-04-09": { "tasks": [] },
    "2026-04-10": { "tasks": [] },
    "2026-04-11": { "tasks": [] }
  }
}
```

---

## 5. Source ID Convention

Source IDs must be collision-resistant across years, weeks, and repeated blocks.

### Preferred form

```
LA-CW{year}-W{week}-D{YYYYMMDD}-{task_type}-{project_slug}-{sequence}
```

### Example

```
LA-CW2026-W14-D20260409-BLOCK-ROBOTOS-001
LA-CW2026-W14-D20260409-BLOCK-ZEPHYR-002
LA-CW2026-W14-D20260410-ROUTINE-MORNING-001
LA-CW2026-W14-D20260410-BLOCKER-SIGNEE-001
LA-CW2026-W14-D20260411-REVIEW-GENERAL-001
```

### Construction rules

| Rule | Reason |
|---|---|
| Always prefix with `LA-` | Namespace safety. Prevents collision with any other tool's ID. |
| Always include `CW{year}` | Avoids ambiguity between W14 of 2026 and W14 of 2027. |
| Always include `W{week}` (zero-padded to 2 digits) | Explicit week for week-level grouping. |
| Always include `D{YYYYMMDD}` for day-level tasks | Unique per day. Required for idempotency within a week. |
| Always include task_type in uppercase | Distinguishes two blocks on the same project on the same day. |
| Always include project_slug or `GENERAL` | Required. Use `GENERAL` for non-project tasks (routines, reminders). |
| Always include zero-padded sequence (3 digits) | Supports up to 999 tasks of the same type+project per day. In practice, 001–005 is typical. |
| Never use only `W14` alone | Week alone is ambiguous across years and calendar-week interpretation conventions. |

### Task type abbreviations for source_id

| task_type | source_id abbreviation |
|---|---|
| `deep_work_block` | `BLOCK` |
| `shallow_task` | `TASK` |
| `routine_checklist` | `ROUTINE` |
| `recovery_block` | `RECOVERY` |
| `blocker_item` | `BLOCKER` |
| `review_task` | `REVIEW` |
| `reminder` | `REMIND` |

---

## 6. Life Agent → TickTick Mapping

### Mapping table

| Life Agent concept | TickTick representation | Export default | Notes / Risks |
|---|---|---|---|
| Weekly plan (e.g., W14) | TickTick list: `Life Agent - 2026-W14` | Yes — creates the list | One list per week. Provides clean export isolation per week. |
| Daily plan (per day) | Tasks grouped by due date within week list | Yes — tasks carry date | No separate TickTick object for a "daily plan". Date on each task is sufficient. |
| Primary Anchor (project) | Task tag `#{project_slug}` + pool tag | Yes | e.g., `#robotos #pool-b`. Tag makes project visible on phone. |
| Secondary Anchor (project) | Task tag `#{project_slug}` | Yes | Same mechanism as Primary. Priority may differ. |
| Deep Work Block (named) | Task with title, start_time, end_time, priority Normal | Yes | Title should be short. Artifact expectation goes in notes. |
| Blocker / P0 item | Task with priority High + tag `#blocker` | Yes | Export all active blockers. These are highest-value items for phone visibility. |
| Review task (weekly/monthly) | Single task on review day with reminder | Yes | e.g., "Weekly Review — close W14" on Sunday. |
| Routine (Morning Setup, Shutdown) | Optional: single parent task with subtask checklist | Not exported by default | If exported, use `routine_checklist` type. Evaluate whether phone checklist adds value or clutter per user preference. |
| Recovery block | Task with priority Low, no artifact | Not exported by default | Optional. Export only if user finds recovery scheduling useful on phone. |
| Exercise | Not exported | No | Calendar-layer item, not a task. Adds phone clutter. |
| Cooking / rest / sleep | Not exported | No | Lifestyle blocks belong on calendar, not task list. |
| Energy leak check | Single weekly review task, not daily | Deferred to review task | Do not create a daily energy-check task. Too much noise. |
| Weekly metrics capture | Single reminder task on review day | Yes — as `reminder` type | e.g., "Capture weekly metrics" on Sunday. |
| Project context notes | Not exported | No | Internal planning context. Do not push to TickTick. |
| Monthly/quarterly plan items | Not exported in weekly bridge | No | Weekly bridge covers day-scoped and week-scoped tasks only. |

### Notes policy

- Notes field should contain: expected artifact (one line) + embedded source_id comment.
- Notes must not contain: customer names, internal architecture details, credential hints, full decision context.
- For sensitive project tasks: export sanitized title + project tag only. Leave notes empty.
- Default: short notes are acceptable. Long notes are not.

---

## 7. Idempotency Design

### Recommended strategy: embedded source_id + local mapping file

**Step 1 — Embed source_id in TickTick task notes:**

Every exported task includes a machine-readable source_id comment in its notes field:

```
Artifact: interrupt handler stub.
<!-- la:source_id=LA-CW2026-W14-D20260409-BLOCK-ROBOTOS-001 -->
```

This makes the mapping recoverable even if the local mapping file is lost or out of sync.

**Step 2 — Maintain a local per-week mapping file:**

Location: `.ticktick/{year}-W{week}_map.json`
Example: `.ticktick/2026-W14_map.json`

Structure:

```json
{
  "LA-CW2026-W14-D20260409-BLOCK-ROBOTOS-001": {
    "ticktick_task_id": "tt_abc123",
    "ticktick_project_id": "tt_proj_w14",
    "content_hash": "sha256:abcdef...",
    "last_exported": "2026-04-09T07:00:00",
    "status": "exported"
  }
}
```

### Export decision logic

```
For each task in PEC:

  1. Look up source_id in mapping file.

  2a. Not found → CREATE in TickTick → write new entry to mapping file.

  2b. Found, content_hash unchanged → SKIP. No API call needed.

  2c. Found, content_hash changed → UPDATE in TickTick → update mapping file entry.

For each source_id in mapping file absent from new PEC:

  3. Apply cancel policy → update status to "cancelled" in mapping file.
```

### Cancel policy

"Cancel" is a Life Agent semantic state, not a native TickTick status. TickTick may not support a native cancelled state.

**Default policy: archive/cancel, not destructive delete.**

Implementation may realize the cancel semantic as:
- Prepending `[CANCELLED]` to the task title in TickTick.
- Moving the task to a designated cancelled list.
- Marking the task complete with a cancellation note.
- Deleting only if the user explicitly selects a delete policy.

The choice among these is an implementation decision for Phase 2. The spec mandates that the default must be non-destructive.

**Cancel policy field in export command:** The `export week` and `export day` commands accept a `cancel_policy` parameter. Default value: `archive`.

### Failure and recovery cases

| Failure | Effect | Recovery |
|---|---|---|
| Mapping file deleted | source_ids lost; next export would create duplicates | Re-run with `--recover` flag: scan TickTick tasks for embedded source_id comments, rebuild mapping file |
| TickTick task manually deleted | Mapping holds stale ticktick_task_id; update call returns 404 | Adapter catches 404, removes stale entry, re-creates task, updates mapping |
| source_id collision | Two tasks share one ID | Prevented by construction rules in §5. If detected, stop export and report error. |
| Network failure mid-export | Partial export | Mapping file updated only on confirmed API success. Retry is safe because existing tasks are skipped (hash match). |
| TickTick API field not supported | tags/reminders cause HTTP 500 | Permanent fix: `_build_payload()` never sends tags or reminders. See §11 Q2/Q3 for resolution. |

---

## 8. TickTick List and Project Strategy

### Default recommendation

Use **one TickTick list per Life Agent week**, named: `Life Agent - 2026-W14`.

Use **tags** to encode Life Agent project scope: `#zephyr`, `#robotos`, `#signee`, `#accountant`, `#pool-a`, `#pool-b`.

**Rationale:**

- One list per week provides clean export isolation. Re-export updates only tasks within the week's list.
- Tags provide project filtering without requiring a separate TickTick project per Life Agent project.
- A separate TickTick project per Life Agent project (e.g., a "RobotOS" project in TickTick) would scatter the weekly view and make week-level idempotency harder.

**Alternative** (evaluate in Phase 2): one persistent `Life Agent` list with week tags. Simpler setup, but less week-level isolation. Does not invalidate idempotency strategy since source_id includes the week.

The list strategy is configurable. This recommendation applies to the first implementation.

---

## 9. Export Trigger Points

### `export week {week_id}`

Exports or re-exports the full approved task set for a given week.

- Reads the approved week plan and/or daily plan files for the specified week.
- Generates or receives a PEC for all exportable tasks in the week.
- Runs idempotency check against the week's mapping file.
- Creates, updates, skips, or cancels tasks in TickTick as needed.
- Updates `.ticktick/{year}-W{week}_map.json`.
- Returns PEC summary: counts of created / updated / skipped / cancelled + any warnings.

**When to trigger:**
- After `plan week` is approved and the week plan is finalized.
- After a mid-week replan that changes anchor assignments or block structure.
- On demand when the user wants to push the latest plan state to TickTick.

**Re-export is always safe.** Unchanged tasks are skipped. Only diffs cause API calls.

---

### `export day {date}`

Exports or re-exports the approved task set for a single day.

- Reads the approved daily plan file for the specified date.
- Generates or receives a PEC for that day's exportable tasks.
- Runs idempotency check scoped to tasks for that date.
- Creates, updates, skips, or cancels tasks as needed.
- Updates the week's mapping file.
- Returns PEC summary for that day.

**When to trigger:**
- After daily plan is finalized with `open day` and user wants phone execution view immediately.
- After a mid-day replan changes block structure.
- For spot export without re-exporting the full week.

---

### Export readiness gate

Export should only run on **user-approved plans**. An approved plan means:
- The week plan has been reviewed and confirmed (not a draft).
- Or the user explicitly triggers export, which is itself a confirmation signal.

The export adapter must not auto-export drafts or plans in progress.

---

## 10. Read-back Audit Policy

This section defines the future Mode D behavior. It is not implemented in Phase 2.

**Read-back purpose:** After a week closes, query TickTick for the completion status of the exported task set and use that data as evidence in the weekly review.

**Read-back rules:**

1. Read-back is triggered manually, as part of `close week`, not automatically.
2. Completion data is appended to the weekly review file as a structured input section, not as a replacement for the human-authored review.
3. Life Agent's DoD and week review conclusions are written by the human. Read-back data is informational.
4. If a task was marked complete in TickTick but the Life Agent DoD for that day was not met, the discrepancy is surfaced for human judgment. TickTick completion does not auto-resolve Life Agent DoD.
5. If a task was exported but never opened on the phone, that absence is noted but does not alter the plan retroactively.

**What read-back does NOT do:**
- Rewrite week plans, daily plans, or anchor assignments.
- Auto-compute block completion rate from TickTick data.
- Replace the metrics capture step in the daily shutdown.

---

## 11. Open Questions

Status updated after Phase 2B-5 field capability test and Phase 2B-6 live export (commit `1d34df6`, 2026-04-27).

| # | Question | Status | Resolution |
|---|---|---|---|
| Q1 | Does TickTick Open API support task creation with `start_time` and `end_time` fields? | ✅ Resolved | `startDate` and `dueDate` (ISO 8601 datetime) are accepted and render correctly in the local TickTick UI. Used for block start and end respectively. True time-range rendering depends on TickTick client/premium — confirmed sufficient for MVP. |
| Q2 | Does TickTick Open API support tags on task creation/update? | ✅ Resolved — **DO NOT USE** | Tags cause HTTP 500. Must never be sent. `_build_payload()` in `export_ticktick_batch.py` permanently omits tags. PEC `tags` field is vestigial for schema compatibility; `export_ticktick_batch.py` never reads it. |
| Q3 | Does TickTick Open API support per-task reminders? | ✅ Resolved — **DO NOT USE** | Reminders cause HTTP 500. Must never be sent. PEC `reminder_policy` field is retained as logical metadata only; `export_ticktick_batch.py` permanently omits reminders from API payloads. |
| Q4 | What is the TickTick rate limit for task create/update calls? | ⏳ Not yet measured | Sequential apply with no artificial delay worked for 7 tasks. Assumed safe for typical week sizes (≤20 tasks). Measure if batch size grows. |
| Q5 | Python or Node.js for the Phase 2 local exporter? | ✅ Resolved | Python 3.10+, stdlib + `requests`. Direct REST route. No Node.js. |
| Q6 | Should routines be exported as a recurring parent task or omitted entirely? | ⏳ Deferred | Routine checklist export adds phone clutter for minimal value. Not exported in MVP. Revisit if user finds phone checklist useful. |
| Q7 | Batch endpoint available? | ✅ Resolved — **Not used** | No documented batch endpoint. Sequential per-task apply chosen for MVP safety and partial-failure handling. |
| Q8 | Should notes be omitted entirely for sensitive project tasks (e.g., Zephyr KTLO)? | ⏳ Deferred | Sanitize notes at generation time: omit or use placeholder for Zephyr-internal detail. Export sanitized title + project tag for sensitive tasks. Revisit if leakage observed. |
| Q9 | Should the mapping file be committed to git? | ✅ Resolved | Mapping files remain gitignored under `.ticktick/` (runtime artifacts). PEC files under `03_PLANNING/` are committed (planning artifacts). See §12.2. |
| Q10 | One TickTick list per week, or one persistent list with week tags? | ✅ Resolved | One list per week: `Life Agent - YYYY-W{n}`. Tags not viable (HTTP 500). See §12.5. |

---

**Last updated:** 2026-04-27 | **Version:** 1.1 | **Phase:** 2C — Plan-to-PEC Generation Contract

---

## 12. Plan-to-PEC Generation Contract

This section defines the Phase 2C contract for generating a PEC JSON from an approved Life Agent week plan. It formalizes the manual agent-normalized workflow that bridges planning documents and the `export_ticktick_batch.py` exporter.

---

### 12.1 Scope

This contract covers **manual agent-driven PEC generation only**. It does not implement the `export week` or `export day` automation commands — those remain NOT IMPLEMENTED in `LIFE_AGENT_AUTOMATION_INTERFACE.md`.

The Phase 2C pipeline is:

```
Approved WeekPlan + Daily files (if available)
        ↓
[Agent generates PEC JSON]
— reads existing PEC if replan (for source_id preservation)
— reads §7 Anchor Map + Goals from WeekPlan
— reads Canonical Daily Anchors if daily files exist
— applies derivation rules in §12.4
— produces YYYY-W{n}_pec.json
        ↓
[validate_pec.py] — human reviews PASS/FAIL
        ↓
[git commit PEC file]
        ↓
[export_ticktick_batch.py dry-run] — human reviews plan
        ↓
[export_ticktick_batch.py --apply] — user-approved only
        ↓
TickTick tasks created/updated
```

---

### 12.2 PEC Storage Convention

| Aspect | Rule |
|---|---|
| **Location** | `03_PLANNING/03_WEEK/W{n}/YYYY-W{n}_pec.json` |
| **Example** | `03_PLANNING/03_WEEK/W15/2026-W15_pec.json` |
| **Commit policy** | PEC is a planning artifact. Commit to git **before** live apply. This locks source_ids into version control. |
| **Gitignore** | PEC files under `03_PLANNING/` are **not** gitignored. Mapping files under `.ticktick/` are gitignored (runtime artifacts). |
| **Replan** | Re-generate PEC → preserve source_ids for unchanged tasks → re-commit → dry-run → apply. |

---

### 12.3 Source ID Stability Rules

Source IDs are the idempotency key for Mode B. Stability rules:

| Scenario | source_id policy | TickTick effect |
|---|---|---|
| Same logical anchor, same day, content unchanged | Preserve source_id | SKIP (no API call) |
| Same logical anchor, same day, title/time/priority changed | Preserve source_id; content hash changes | UPDATE |
| Anchor moved to a different day | New source_id (D{date} segment changes); old source_id → `export_status: cancelled` | CANCEL old, CREATE new |
| Anchor removed from plan | Set `export_status: cancelled` in PEC | CANCEL (apply cancel_policy) |
| New anchor added to plan | New source_id with next sequence number | CREATE |
| Title changed, logical anchor identity unchanged | Preserve source_id | UPDATE |

**Agent replan discipline:** When regenerating a PEC for a replanned week, the agent **must** read the existing committed PEC file first and preserve all source_ids for anchors that remain on the same day. Never regenerate source_ids for unchanged tasks.

---

### 12.4 PEC Field Derivation Rules

| Field | Source | Default if absent |
|---|---|---|
| `source_id` | Agent generates using §5 convention. Preserved from existing PEC for unchanged tasks. | None — required |
| `title` | Anchor name from WeekPlan §7 or Daily Canonical Anchors. Max 60 chars. | None — required |
| `date` | Day row in WeekPlan §7 or daily file header. | None — required |
| `start_time` | Execution Window / Block label in daily file. | Pool A (office): `09:00`; Pool B (evening): `19:30` |
| `end_time` | Execution Window / Block label in daily file. | `deep_work_block`: start + 90 min; `shallow_task` / `recovery_block`: start + 30 min |
| `all_day` | `false` when start_time present; `true` for all-day flags. | `false` |
| `project_scope` | Project prefix of anchor name. Map: Zephyr→`zephyr`, RobotOS→`robotos`, Signee→`signee`, Project Accountant/Accountant→`accountant`, General→`general`. | `general` |
| `task_type` | Work type + block size + criticality. Heavy Engineering/Ambiguity Discovery + M/L → `deep_work_block`; blocker → `blocker_item`; review → `review_task`; recovery → `recovery_block`; short non-artifact → `shallow_task`. | `shallow_task` |
| `priority` | Blocker / Goal PRIORITY 1 → `high`; `recovery_block` → `low`; others → `normal`. | `normal` |
| `tags` | **Always `[]`** — tags cause HTTP 500 and must not be sent. | `[]` |
| `reminder_policy` | Not present in markdown. Defaults: `deep_work_block` → `15min_before`; `blocker_item` → `at_start`; others → `none`. | `none` |
| `recurrence` | Always `null` for week/day export. | `null` |
| `notes` | Short artifact description (≤1 sentence) + `<!-- la:source_id=... -->` comment. No sensitive content. | `<!-- la:source_id=... -->` only |
| `export_status` | Always `pending` at generation. Exporter manages subsequent states. | `pending` |
| `ticktick_project_id` | Always `null` at generation. Exporter populates after CREATE. | `null` |
| `ticktick_task_id` | Always `null` at generation. Exporter populates after CREATE. | `null` |

**Timing defaults must be visible in the generated PEC for human review.** If start_time was defaulted rather than derived from a daily file, the agent should note this in a generation summary or commit message.

---

### 12.5 TickTick List Naming Convention

One TickTick list per Life Agent week:

```
Life Agent - 2026-W{n}
```

Example: `Life Agent - 2026-W15`

Use `tools/lookup_ticktick_project.py ensure "Life Agent - 2026-W15" --create` to create the list if it does not exist. Resolve the `projectId` before running the exporter.

**Do not rely on TickTick tags** for project scope encoding — tags cause HTTP 500. The `project_scope` field in PEC is Life Agent metadata only; it does not reach TickTick.

---

### 12.6 Prompt Template

The canonical prompt for agent-driven PEC generation is:

```
05_TEMPLATES/GENERATE_PEC.prompt.md
```

Use this prompt when generating a PEC from an approved week plan. Do not improvise the generation prompt — the template encodes source_id stability rules, field derivation defaults, and the human review checklist.

---

### 12.7 First Real Export Protocol

1. **Select week.** Choose an approved upcoming week plan (not a draft).
2. **Create TickTick list.** `python tools/lookup_ticktick_project.py ensure "Life Agent - YYYY-W{n}" --create`
3. **Generate PEC.** Use `05_TEMPLATES/GENERATE_PEC.prompt.md` prompt with the agent.
4. **Save PEC.** Write to `03_PLANNING/03_WEEK/W{n}/YYYY-W{n}_pec.json`.
5. **Validate.** `python tools/validate_pec.py 03_PLANNING/03_WEEK/W{n}/YYYY-W{n}_pec.json`
6. **Human review.** Check task count, titles, times, priorities, notes for sensitive content.
7. **Commit PEC.** `git add 03_PLANNING/03_WEEK/W{n}/YYYY-W{n}_pec.json && git commit -m "feat: add PEC for YYYY-W{n}"`
8. **Dry-run.** `python tools/export_ticktick_batch.py 03_PLANNING/03_WEEK/W{n}/YYYY-W{n}_pec.json --project-id <PROJECT_ID>`
9. **Live apply.** `python tools/export_ticktick_batch.py ... --apply` (after dry-run review passes)
10. **Verify in TickTick.** Confirm tasks appear with correct dates, priorities, and titles.
