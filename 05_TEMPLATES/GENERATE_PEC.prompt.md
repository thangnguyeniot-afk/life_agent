# GENERATE_PEC.prompt.md

> **Purpose:** Canonical copyable prompt for generating a Plan Execution Contract (PEC) JSON from an approved Life Agent week plan.
>
> **Use case:** Phase 2C manual agent-normalized PEC generation. Send this prompt (filled with actual paths) to GPT, Claude, or Copilot.
>
> **Scope:** Generation only. This prompt does NOT trigger TickTick writes. The agent produces JSON output; the user validates and commits it before any export runs.
>
> **Spec reference:** `TICKTICK_BRIDGE_SPEC.md` §12 — Plan-to-PEC Generation Contract.

---

## How to use this prompt

1. Copy the prompt block below.
2. Fill in the bracketed placeholders with actual values.
3. Paste into your agent session (GPT / Claude / Copilot).
4. Agent returns PEC JSON only.
5. Save output to `03_PLANNING/03_WEEK/W{n}/YYYY-W{n}_pec.json`.
6. Validate: `python tools/validate_pec.py <pec_path>`
7. Review and commit before running the exporter.

---

## Prompt

```
You are generating a Plan Execution Contract (PEC) JSON file for Life Agent.

ROLE AND BOUNDARY:
- You are a generation agent only. You produce the PEC JSON file.
- You do NOT apply it to TickTick.
- You do NOT modify any Life Agent planning files.
- You do NOT make any API calls.
- Output is the PEC JSON text only. No markdown commentary. No explanation prose inside or around the JSON.

INPUTS:
- Week plan: [PATH — e.g., 03_PLANNING/03_WEEK/W15/2026-W15_WeekPlan.md]
- Daily plan folder: [PATH or "not available" — e.g., 03_PLANNING/04_DAY/W15/]
- Existing PEC (if replan): [PATH or "none" — e.g., 03_PLANNING/03_WEEK/W15/2026-W15_pec.json]
- Target TickTick project/list name: [e.g., "Life Agent - 2026-W15"]
- Target TickTick projectId: [e.g., "69ef06ed8f08711a62591f0c" or "to be filled by user"]

SOURCE PRIORITY (read in this order):
1. Existing PEC (if provided): read ALL source_ids before generating anything. Preserve source_ids for tasks that remain on the same day.
2. Daily plan files (if available): use for precise start_time and end_time from block labels.
3. Week plan §7 Weekly Anchor Map: primary source for anchor identity, project scope, and artifact direction.
4. Week plan §6.1 Goals section: use for priority inference (PRIORITY 1 / blocker → high).

SOURCE ID RULES — READ CAREFULLY:
- Format: LA-CW{year}-W{week}-D{YYYYMMDD}-{TYPE}-{PROJECT}-{sequence}
- Example: LA-CW2026-W15-D20260407-BLOCK-ROBOTOS-001
- {year}: 4-digit calendar year (e.g., 2026)
- {week}: ISO week number, zero-padded to 2 digits (e.g., 15 → "15")
- {YYYYMMDD}: exact execution date (e.g., 20260407)
- {TYPE}: uppercase task type abbreviation:
    deep_work_block → BLOCK
    shallow_task → TASK
    routine_checklist → ROUTINE
    recovery_block → RECOVERY
    blocker_item → BLOCKER
    review_task → REVIEW
    reminder → REMIND
- {PROJECT}: uppercase project slug (e.g., ROBOTOS, SIGNEE, ZEPHYR, ACCOUNTANT, GENERAL)
- {sequence}: zero-padded 3-digit counter per TYPE+PROJECT+DATE (001, 002, ...)
- REPLAN RULE: If an existing PEC was provided, you MUST use the same source_id for any task that remains on the same day, regardless of title or time changes.
- NEW TASK RULE: Assign the next available sequence number for that TYPE+PROJECT+DATE combination.
- DAY-MOVE RULE: If a task moves to a different day, it gets a new source_id (new YYYYMMDD). The old source_id should become export_status: "cancelled" in the PEC.

FIELD DERIVATION RULES:

title:
- From anchor name in WeekPlan §7 or Daily Canonical Anchors section.
- Max 60 characters. Truncate if needed; keep project prefix + core action.
- No vague language ("work on", "continue", "improve").

date:
- YYYY-MM-DD format. Exact execution date from day row in WeekPlan §7 or daily file header.

start_time / end_time:
- Derive from "Execution Window" or Block label (e.g., "Block 1 (09:00–12:00)").
- If daily files are available, prefer daily file precision.
- If not available from any source, use these defaults:
    Pool A (office hours): start_time = "09:00"
    Pool B (evening): start_time = "19:30"
  End time defaults by task_type (from default start):
    deep_work_block: start + 90 minutes
    shallow_task: start + 30 minutes
    recovery_block: start + 30 minutes
    review_task: start + 60 minutes
    blocker_item: start + 60 minutes
- IMPORTANT: If start_time or end_time was defaulted (not derived), set a note in the "notes" field or add a generation_note at the task level. The user must be able to identify which times were defaults vs. derived.

all_day:
- false when start_time is present.
- true only for tasks with no time window (explicitly all-day items).

project_scope:
- Derive from project prefix of the anchor name.
- Mapping:
    Zephyr → "zephyr"
    RobotOS → "robotos"
    Signee → "signee"
    Project Accountant / Accountant → "accountant"
    General / KTLO / routine / review → "general"

task_type:
- Apply this priority order:
    1. If anchor name or goal contains "blocker" or "unblock" AND high urgency → "blocker_item"
    2. If work type is Heavy Engineering / Ambiguity Discovery / Integration AND size M or L → "deep_work_block"
    3. If anchor is a weekly or monthly review action → "review_task"
    4. If anchor is a buffer, recovery, or rest block → "recovery_block"
    5. If anchor is short, no artifact expected, size S → "shallow_task"
    6. Default: "shallow_task"

priority:
- "high": blocker_item tasks; tasks explicitly marked PRIORITY 1 in Goals section; any anchor described as "unblocking" a downstream team.
- "low": recovery_block tasks.
- "normal": all others.

tags:
- ALWAYS []. Tags cause HTTP 500 in TickTick API. Never populate this field.

reminder_policy:
- deep_work_block → "15min_before"
- blocker_item → "at_start"
- all others → "none"
- NOTE: The exporter does NOT send reminders to TickTick (causes HTTP 500). This field is retained as logical metadata only.

recurrence:
- Always null for week/day export.

notes:
- Format: "[short artifact description — 1 sentence max] <!-- la:source_id={source_id} -->"
- Artifact description: what concrete deliverable or state exists after this block completes.
- If no artifact: "<!-- la:source_id={source_id} -->" only.
- Do NOT include: customer names, internal architecture details, credential hints, full decision context.
- For Zephyr-internal tasks: use sanitized description only (e.g., "Zephyr: CI health check completed").

export_status:
- Always "pending" at generation. Never set to "exported" or "updated" manually.

ticktick_project_id:
- Use the projectId provided in inputs if known. Set null if unknown; the exporter accepts --project-id at CLI.

ticktick_task_id:
- Always null at generation.

EXPORT META:
- week_id: "YYYY-W{n}" (e.g., "2026-W15")
- week_start: Monday of the ISO week, YYYY-MM-DD
- week_end: Friday of the ISO week (or Saturday if week runs Mon–Sat), YYYY-MM-DD
- exported_at: current datetime ISO 8601 (use actual generation time)
- mode: "B"
- dry_run: true
- mapping_file: ".ticktick/YYYY-W{n}_map.json"

WHAT TO EXPORT:
- Export: deep work blocks, blocker items, review tasks, recovery buffers, KTLO routines if useful.
- Do NOT export: exercise, cooking, rest, sleep, lifestyle blocks.
- Do NOT export: project context notes, decision context, internal planning rationale.
- Do NOT export: Zephyr-internal architecture details in notes.

GENERATION CONSTRAINTS:
- Produce the JSON file content only. No commentary, no markdown, no explanation text outside the JSON.
- The JSON must be valid. Use proper escaping.
- Every task must have a valid source_id matching the format above.
- Every task source_id must appear in the notes <!-- la:source_id=... --> comment.
- Title must not exceed 60 characters.
- All dates must be YYYY-MM-DD. All times must be HH:MM.
- tags must be [].
- recurrence must be null.
- export_status must be "pending".
- ticktick_task_id must be null.

REPLAN CHECKLIST (required if existing PEC was provided):
Before outputting, verify:
[ ] Every source_id from the existing PEC that remains on the same day is preserved unchanged.
[ ] Tasks not in the new plan have export_status set to "cancelled".
[ ] New tasks have new source_ids with the correct next sequence number.
[ ] No source_id was regenerated for an unchanged task.

REVIEW CHECKLIST (agent self-check before outputting):
[ ] Task count is reasonable for the week (typically 5–20 tasks for a Mon–Fri week).
[ ] Every deep_work_block has a concrete artifact in notes.
[ ] All titles are ≤ 60 characters.
[ ] No sensitive project details in notes.
[ ] No tags populated (must be []).
[ ] All times are HH:MM format.
[ ] All source_ids match format LA-CW{year}-W{week}-D{YYYYMMDD}-{TYPE}-{PROJECT}-{sequence}.
[ ] source_id preservation rule followed for replan (if applicable).
[ ] ticktick_project_id set to provided projectId (or null if not provided).

NEXT STEPS AFTER OUTPUT:
User will:
1. Save JSON to 03_PLANNING/03_WEEK/W{n}/YYYY-W{n}_pec.json
2. Run: python tools/validate_pec.py 03_PLANNING/03_WEEK/W{n}/YYYY-W{n}_pec.json
3. Review output, fix any validation errors.
4. Commit: git add ... && git commit -m "feat: add PEC for YYYY-W{n}"
5. Dry-run: python tools/export_ticktick_batch.py <pec_path> --project-id <PROJECT_ID>
6. Apply: python tools/export_ticktick_batch.py <pec_path> --project-id <PROJECT_ID> --apply
Do NOT proceed to step 6 without explicit user approval after step 5.

Now generate the PEC JSON for the inputs provided above.
```

---

## Timing default reference

If daily plan files are not available, use these defaults and note them explicitly in task `notes`:

| Pool | Default start_time | Notes on origin |
|---|---|---|
| Pool A (office hours) | `09:00` | Zephyr primary block start; after KTLO baseline |
| Pool B (evening) | `19:30` | Evening primary block start; standard personal project window |

| task_type | Duration from start |
|---|---|
| `deep_work_block` | 90 min |
| `shallow_task` | 30 min |
| `recovery_block` | 30 min |
| `review_task` | 60 min |
| `blocker_item` | 60 min |
| `reminder` | 0 min (point in time) |

---

## Example output skeleton

```json
{
  "export_meta": {
    "week_id": "2026-W15",
    "week_start": "2026-04-07",
    "week_end": "2026-04-11",
    "exported_at": "2026-04-07T08:00:00",
    "mode": "B",
    "dry_run": true,
    "mapping_file": ".ticktick/2026-W15_map.json"
  },
  "days": {
    "2026-04-07": {
      "tasks": [
        {
          "source_id": "LA-CW2026-W15-D20260407-BLOCK-ZEPHYR-001",
          "title": "Zephyr: smoke test and CI health check",
          "date": "2026-04-07",
          "start_time": "09:00",
          "end_time": "10:30",
          "all_day": false,
          "project_scope": "zephyr",
          "task_type": "deep_work_block",
          "priority": "normal",
          "tags": [],
          "reminder_policy": "15min_before",
          "recurrence": null,
          "notes": "Artifact: CI status logged; smoke test pass/fail recorded. <!-- la:source_id=LA-CW2026-W15-D20260407-BLOCK-ZEPHYR-001 -->",
          "export_status": "pending",
          "ticktick_project_id": null,
          "ticktick_task_id": null
        }
      ]
    }
  }
}
```

---

## Field constraints summary (from Phase 2B-5 live test)

| Field | Status | Behavior |
|---|---|---|
| `title` | ✅ Works | Required. Max 60 chars recommended. |
| `content` / `notes` | ✅ Works | `<!-- la:source_id=... -->` comment survives round-trip. |
| `priority` | ✅ Works | 0=normal, 1=low, 5=high. |
| `startDate` | ✅ Works | ISO 8601 datetime. Renders correctly in local TickTick UI. |
| `dueDate` | ✅ Works | ISO 8601 datetime. Used as end_time anchor. |
| `isAllDay` | ✅ Works | Boolean. |
| `tags` | ❌ HTTP 500 | **Must never be sent.** PEC `tags` is always `[]`; exporter omits it. |
| `reminders` | ❌ HTTP 500 | **Must never be sent.** PEC `reminder_policy` is logical metadata only; exporter omits reminders. |
| `recurrence` | ⏳ Deferred | Not sent in MVP. Always `null` in PEC. |

---

**Last updated:** 2026-04-27 | **Spec version:** TICKTICK_BRIDGE_SPEC.md §12
