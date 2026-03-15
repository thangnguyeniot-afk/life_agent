# INTEGRATE_DAILY — Daily Reverse-Integration Procedure

> **Type:** Operating Procedure  
> **Layer:** OS / Operations  
> **Scope:** Single completed Daily execution file → all upstream system layers  
> **Reuse:** Run once per closed daily. Safe to re-run if interrupted.  
> **Maintained by:** Agent 2 (file reads/writes) + Agent 1 (decisions only when escalation required)  
> **Sequence:** After this completes, run [`PREPARE_NEXT_DAILY.md`](PREPARE_NEXT_DAILY.md)  
> **Weekly framing:** Generated/updated by [`GENERATE_WEEKLY_EXECUTION.md`](../WEEKLY_CONTROL/GENERATE_WEEKLY_EXECUTION.md); corrected mid-week by [`WEEKLY_REBALANCE.md`](../WEEKLY_CONTROL/WEEKLY_REBALANCE.md) if drift detected; closed by [`WEEK_CLOSEOUT.md`](../WEEKLY_CONTROL/WEEK_CLOSEOUT.md) at week end

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. When to Run](#2-when-to-run)
- [3. Inputs](#3-inputs)
- [4. Outputs](#4-outputs)
- [5. Source of Truth Rule](#5-source-of-truth-rule)
- [6. Update Order](#6-update-order)
- [7. Data to Extract from Daily](#7-data-to-extract-from-daily)
- [8. Integration Procedure](#8-integration-procedure)
- [9. Guardrails](#9-guardrails)
- [10. Definition of Good Integration](#10-definition-of-good-integration)
- [11. Standard Integration Checklist](#11-standard-integration-checklist)
- [12. Reusable Execution Template](#12-reusable-execution-template)

---

## 1. Purpose

This procedure reverse-integrates a completed Daily execution file back into the LIFE_AGENT operating system so that **system state matches real execution**.

The Daily file is the authoritative record of what actually happened on a given day. Weekly, Monthly, Project, and Anchor tracking layers are downstream consumers of that reality. They must be updated from Daily — not the other way around.

Running this procedure ensures:
- No execution reality is lost between days
- Carry-over work is concretely expressed, not vague
- Weekly and Monthly layers reflect actual progress, not planned progress
- Project state is accurate for scope freeze and review decisions
- The next daily file starts with a clean, pre-loaded context

This procedure does **not** judge execution quality, assign blame, or refactor strategy. It syncs the record.

---

## 2. When to Run

**Trigger:** After a Daily file is sufficiently completed at end-of-day closure.

Sufficient completion means:
- Shutdown section completed (main artifact, re-entry pack if applicable)
- DoD checkboxes filled
- At minimum: completed work captured + unfinished work with next step

**Run before:**
- Planning or prefilling the next daily file

**Also run when:**
- Significant execution reality differs from weekly/monthly assumptions mid-week
- A project state changed (merge, block, dependency resolved) that upstream layers do not yet reflect
- A carry-over from a previous day was not yet propagated

---

## 3. Inputs

| Input | Description | Required? |
|---|---|---|
| `<DAILY_FILE>` | Completed daily execution file (Daily Plan + Shutdown) | Required |
| `<WEEK_FILE>` | Active weekly execution file (WeekPlan for current week) | Required |
| `<MONTH_FILE>` | Active monthly execution file (MonthPlan for current month) | Required |
| `<PROJECT_FILE_1>` | Project context/state file (if project state changed today) | If changed |
| `<PROJECT_FILE_2>` | Second project context/state file if secondary anchor project changed | If changed |
| `<ANCHOR_TRACKING_FILE>` | Weekly anchor load tracking (Execution Tracker in WeekPlan §TRACKER) | Required |
| `<NEXT_DAILY_FILE>` | Target next-day file (may not exist yet; create if absent) | Required |
| `<DAILY_TEMPLATE_FILE>` | Canonical daily template for next-day prefill | Required |

> If a project file does not exist for the project, skip Step 4 for that project. Don't create project files as a side effect of integration.

---

## 4. Outputs

| Output | Description |
|---|---|
| Weekly execution updated | Day row status, carry-over registered, progress notes accurate |
| Monthly execution updated | Execution/progress fields updated; dependency changes reflected |
| Project state updated | Only if meaningful state change occurred (see §8 Step 4) |
| Anchor Load Tracking updated | Actual anchor vs. planned anchor recorded |
| Next daily file created or prefilled | Primary/Secondary anchors, re-entry block, first step populated |
| Integration report produced | Files modified, carry-over items, project state changes, inconsistencies |

---

## 5. Source of Truth Rule

- **Daily execution file is the source of truth** for what actually happened on a given day.
- Weekly, Monthly, Project, and tracking layers are **derived layers**. They are not allowed to contradict the Daily record.
- **Historical Daily files must not be rewritten** except to fix minor factual consistency errors (typos, wrong date references, broken formatting). Execution facts cannot be retroactively changed.
- **Never update strategy because of a single day** unless the day surfaced an explicit escalation, a hard dependency resolution, or a scope change decision. Day-level noise is not month-level signal.

---

## 6. Update Order

Execute in this exact order. Do not skip steps or reorder them.

1. **Parse Daily** — extract facts before modifying anything
2. **Update Weekly** — closest layer; update first
3. **Update Monthly** — second-closest layer; reflect only meaningful changes
4. **Update Project State** — only if state changed in Daily today
5. **Update Anchor Load Tracking** — register actual vs. planned anchor load
6. **Prepare Next Daily Carry-over** — carry forward only unresolved, concrete items
7. **Consistency Check** — verify no contradiction across layers
8. **Produce Report** — record what changed

**Why order matters:**
Execution layer (Daily) must be fully parsed before any writing begins. Weekly must be updated before Monthly, because Monthly imports from Weekly — not from Daily directly. Project state is updated after both planning layers so there is no misalignment. Next Daily is prepared last, after all upstream layers are consistent, so the carry-forward reflects the current true state.

---

## 7. Data to Extract from Daily

Read the Daily file and extract all of the following before beginning any writes.

**Identity fields:**
- [ ] Date
- [ ] Week reference
- [ ] Primary Anchor (executed identity, not just planned)
- [ ] Secondary Anchor (executed identity, not just planned)

**Execution results:**
- [ ] Major work blocks executed (name, size, outcome)
- [ ] Completed artifacts (what was produced and its state)
- [ ] Unfinished work (what stopped and exactly where)
- [ ] Blocked work (what was blocked and by what — internal vs. external)
- [ ] Deferred work (moved to another day with clear next action)
- [ ] External dependencies changed (resolved, new, or still open)

**Forward signals:**
- [ ] Carry-over items (concrete next actions, not vague tasks)
- [ ] Next exact action per unfinished thread
- [ ] Re-entry mode specified (Quick / Analytical / Fragile)
- [ ] Receiving day constraint (load, energy fit, work type)

**System signals:**
- [ ] Decision changes (anything that alters project/anchor state)
- [ ] Scope changes (expansion or reduction vs. weekly plan)
- [ ] Drift Early Warning readings (trajectory indicators)
- [ ] Escalation signals (from Signals section and DoD)

**Capacity data (for anchor tracking):**
- [ ] Blocks actually executed vs. planned
- [ ] Energy level recorded
- [ ] Evening capacity mode vs. actual

---

## 8. Integration Procedure

### Step 1 — Parse the Daily

1. Read the full Daily file from top to bottom.
2. Identify each work item's outcome status:
   - **Done** — artifact produced and captured
   - **Partial** — meaningful progress made; continuation needed
   - **Blocked** — work stopped due to external dependency; resolution path exists
   - **Deferred** — work explicitly moved to a later day; re-entry note captured
   - **Not started** — block was in plan but not attempted
3. For each unfinished or blocked item, capture:
   - Exact stopping point
   - Artifact state
   - Next exact step (< 15 min to restart)
4. Distinguish internal delays (ran out of time, energy) from external dependencies (review pending, customer response, branch conflict).
5. Note any signals raised, decisions made, or scope changes.

Do not write to any file until extraction is complete.

---

### Step 2 — Update Weekly Execution

File: `<WEEK_FILE>`

1. Locate the Execution Tracker section (or the day's row in the anchor map).
2. Mark today's completed anchors as done. Mark spillover/carry-over items clearly.
3. Register carry-over tasks under the correct target day row.
4. Update project progress notes with the actual outcome (factual, not narrative).
5. Preserve all existing weekly template structure. Do not restructure.
6. Keep notes concise and operational. Avoid vague summaries like "made progress" — write "tests coded, merge pending review" instead.
7. Do not convert execution history into generic labels. Keep the facts.

---

### Step 3 — Update Monthly Execution

File: `<MONTH_FILE>`

1. Open the monthly file and locate execution/progress sections for the relevant projects.
2. Update only the execution fields. Reflect:
   - Meaningful progress toward monthly goals
   - Dependency or blocker changes that affect monthly delivery
   - Scope changes if any were captured in today's Daily
3. Preserve all monthly strategy and planning sections unchanged. Month strategy is not re-evaluated from a single day.
4. Escalate day-level facts to month-level only if they are milestone-relevant:
   - An anchor completed its key artifact
   - A project entered a new phase (e.g., writing → review → merge)
   - A hard dependency was resolved or newly established
   - A scope decision was made

---

### Step 4 — Update Project State

Files: `<PROJECT_FILE_1>`, `<PROJECT_FILE_2>`

1. Open the relevant project context file.
2. Update the project state section only if a meaningful state change occurred today. Examples of meaningful state changes:
   - Review pending (was not previously in review state)
   - Merged to target branch
   - Blocked by a new dependency
   - Dependency resolved
   - Artifact completed (test, doc, implementation)
   - Phase transition (writing → verification → closure)
3. Write factual, minimal updates. One to three lines per project. Do not create narrative logs.
4. If no meaningful state change occurred, skip this file. A day of continued work on an in-progress task does not require a project file update.

---

### Step 5 — Update Anchor Load Tracking

File: `<ANCHOR_TRACKING_FILE>` (weekly Execution Tracker, or dedicated section)

1. Record which anchor actually dominated office hours.
2. Record which anchor was attempted or held for evening.
3. Note any mismatch between planned vs. actual anchor load if it is meaningful. Examples:
   - Primary anchor took more time than planned (overflow into Block 3 or evening)
   - Secondary anchor was demoted to checkpoint vs. active execution
   - Third project appeared unexpectedly
4. Keep each entry short (one line per anchor per day). The tracking value comes from comparability across days, not narrative length.

---

### Step 6 — Prepare Next Day Carry-over

File: `<NEXT_DAILY_FILE>` (create from `<DAILY_TEMPLATE_FILE>` if not present)

> **Full procedure:** For complete next-day preparation including anchor selection, block design, dependency-aware encoding, and overload check, run [`PREPARE_NEXT_DAILY.md`](PREPARE_NEXT_DAILY.md) after this step.
> The instructions below cover the minimum carry-over required during integration. PREPARE_NEXT_DAILY handles full drafting.

1. If the next daily file does not exist, create it from the canonical daily template.
2. Prefill the following sections from today's carry-over:
   - **Morning Setup / Re-entry Block:** Inherit spillover anchor, re-entry mode, first action
   - **Canonical Daily Anchors:** Primary and Secondary anchors from real carry-over state
   - **Source / Inherited from Weekly:** Pull from WeekPlan §7 for the target day row
   - **First Execution Step:** Exact next action (e.g., "8:00–8:15: check merge review status → merge if approved")
3. Write the next-day anchor as an **exact continuation**, not a vague restating. Wrong: "Continue Zephyr work." Correct: "Zephyr — check merge review → merge Dbugs write test to develop if approved."
4. Do not mix two project threads into one anchor line.
5. Only carry forward items that still matter. If a task was blocked and the block has a clear expected resolution, set it as conditional and specify the resolution condition.

---

### Step 7 — Consistency Check

Verify that these facts are consistent across all updated files:

| Check | Files to compare |
|---|---|
| Completed work is marked done everywhere | Daily ↔ Weekly ↔ Monthly |
| Blocked work is not marked done elsewhere | Daily ↔ Project ↔ Monthly |
| External dependency status matches across files | Daily ↔ Monthly ↔ Project |
| Carry-over in next Daily matches unfinished in today's Daily | Daily ↔ Next Daily |
| Anchor identity matches (no silent renames) | Daily ↔ Weekly ↔ Next Daily |
| No text says "merged" when review is still pending | All files |
| Re-entry mode in next Daily matches today's Shutdown recommendation | Daily Shutdown ↔ Next Daily Morning Setup |

If any inconsistency is found, fix the downstream layer (Weekly / Monthly / Project / Next Daily) to match the Daily. Never fix the Daily to match downstream layers.

---

### Step 8 — Produce Integration Report

Write a brief integration report. This can be inline in the session or logged in the weekly Execution Tracker.

Required fields:

```
## Daily Integration Report – YYYY-MM-DD

**Files modified:**
- [list each file touched]

**Files created:**
- [list each new file created, or "None"]

**Carry-over tasks registered:**
- [project] – [exact action] → target: [day or condition]

**Project state changes:**
- [project] – [old state] → [new state]

**Dependency changes:**
- [project] – [dependency] – [status: new / resolved / still open]

**Inconsistencies fixed:**
- [describe any contradiction corrected, or "None"]

**Unresolved uncertainties:**
- [anything that remains unclear and needs human decision, or "None"]
```

---

## 9. Guardrails

These rules override any perceived efficiency gain. Do not break them.

- **Do not alter system architecture** during daily integration. If integration reveals a system design issue, log it in `04_LOGS/Decision_Log.md` and continue.
- **Do not rewrite templates** while integrating a day. Templates are maintained separately.
- **Do not rewrite historical Daily content** except minor consistency fixes (spelling, wrong date reference, formatting). Execution facts are immutable.
- **Do not inflate progress.** "Tests coded, merge pending review" is correct. "Tests merged" when review is still open is a false state.
- **Do not erase blocked or deferred reality.** If work was blocked, the system must show it as blocked — not as a completed block stripped of context.
- **Do not carry over vague tasks.** If a task is unfinished, its carry-over entry must specify the exact next step. "Continue Zephyr" does not qualify.
- **Do not merge multiple anchors into one unclear line.** Each anchor owns its own carry-over entry.
- **Do not promote day-level noise to month level.** Fatigue on a single day is not a monthly capacity signal. Two consecutive days of the same signal might be.

---

## 10. Definition of Good Integration

Integration is complete and correct when:

- **System reflects reality.** Any reader looking at the weekly or monthly layer sees the same execution state as the Daily file.
- **Next day has clean re-entry.** The next Daily file contains a concrete first step, the correct anchor identity, and the correct re-entry mode — all derived from today's Shutdown.
- **Carry-over is concrete.** Every unfinished thread has an exact next action. No vague intentions.
- **No contradiction across layers.** Blocked work is shown as blocked everywhere. Done work is shown as done everywhere.
- **Project state can be read quickly.** A five-second scan of the project file reveals current phase, major open item, and next gate.
- **Anchor load is analyzable.** The tracking record shows actual vs. planned load for each day, enabling weekly review to detect patterns.

---

## 11. Standard Integration Checklist

Copy this checklist into each session when running integration.

```
### Integration Checklist – YYYY-MM-DD

**Parse:**
- [ ] Full Daily file read
- [ ] Done / Partial / Blocked / Deferred status assigned to all work items
- [ ] Exact next step extracted for each unfinished thread
- [ ] Re-entry mode identified for each carry-over anchor

**Weekly:**
- [ ] Completed anchors marked in Execution Tracker
- [ ] Carry-over tasks registered to target day
- [ ] Project progress notes updated

**Monthly:**
- [ ] Execution/progress fields updated
- [ ] Dependency changes reflected
- [ ] Monthly strategy sections untouched

**Project:**
- [ ] Project file updated if state changed today (else skipped)
- [ ] Update is factual, minimal (1–3 lines max)

**Anchor Load Tracking:**
- [ ] Actual anchor load recorded (office + evening)
- [ ] Planned vs. actual mismatch noted if meaningful

**Next Daily:**
- [ ] File created from template (if not exist)
- [ ] Primary Anchor and Secondary Anchor prefilled from carry-over
- [ ] Re-entry block configured (mode + first action + timing)
- [ ] First Execution Step is exact (not vague)

**Consistency:**
- [ ] Completed work matches across Daily / Weekly / Monthly
- [ ] Blocked work not shown as done anywhere
- [ ] Dependency status consistent across files
- [ ] Carry-over in next Daily matches unfinished in today's Daily
- [ ] Re-entry mode in next Daily matches today's Shutdown recommendation

**Report:**
- [ ] Integration report produced
- [ ] Unresolved uncertainties flagged for human decision (or confirmed: none)
```

---

## 12. Reusable Execution Template

Use this command block to run daily integration. Replace all placeholders before submitting.

```
TASK: Run daily reverse-integration procedure for YYYY-MM-DD

Procedure reference: 01_OS/04_OPERATIONS/DAILY_INTEGRATION/INTEGRATE_DAILY.md

Inputs:
- DAILY_FILE: <path to today's completed daily, e.g. 03_PLANNING/03_WEEK/YYYY-MM-DD_Daily.md>
- WEEK_FILE: <path to active weekly plan, e.g. 03_PLANNING/03_WEEK/YYYY-Www_WeekPlan.md>
- MONTH_FILE: <path to active monthly plan, e.g. 03_PLANNING/02_MONTH/YYYY-MM_March_Planning.md>
- PROJECT_FILE_1: <path to project 1 context file, e.g. 08_PROJECT_CONTEXT/Zephyr_Project_Context.md — or SKIP if no state change>
- PROJECT_FILE_2: <path to project 2 context file, e.g. 08_PROJECT_CONTEXT/Signee_CONTEXT.md — or SKIP if no state change>
- ANCHOR_TRACKING_FILE: <path or section reference for anchor load tracking, e.g. WEEK_FILE §EXECUTION TRACKER>
- NEXT_DAILY_FILE: <path for tomorrow's daily, e.g. 03_PLANNING/03_WEEK/YYYY-MM-DD_Daily.md>
- DAILY_TEMPLATE_FILE: 05_TEMPLATES/TEMPLATE_Daily.md

Instructions:
1. Follow the integration procedure exactly as defined in INTEGRATE_DAILY.md §8 (Steps 1–8).
2. Apply guardrails from §9 without exception.
3. Produce an integration report as defined in §8 Step 8 at the end.
4. If any inconsistency requires human decision (scope change, architecture change, dependency escalation),
   flag it in the report under "Unresolved uncertainties" — do not resolve it autonomously.
5. Commit all modified files with message:
   "integrate: daily reverse-integration YYYY-MM-DD → weekly/monthly/project sync"
```

---

> **Procedure version:** 1.0  
> **Created:** 2026-03-15  
> **Location:** `01_OS/04_OPERATIONS/DAILY_INTEGRATION/INTEGRATE_DAILY.md`  
> **Next review trigger:** When system architecture changes (new layers, new file conventions, renamed templates)
