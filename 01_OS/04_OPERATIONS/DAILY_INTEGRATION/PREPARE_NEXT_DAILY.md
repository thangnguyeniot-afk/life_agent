# PREPARE_NEXT_DAILY — Next-Day Preparation Procedure

> **Type:** Operating Procedure  
> **Layer:** OS / Operations  
> **Scope:** Current system state → next Daily execution file  
> **Prerequisite:** `INTEGRATE_DAILY.md` must have completed first  
> **Reuse:** Run once per day after daily integration. Safe to re-run before next day starts.  
> **Maintained by:** Agent 2 (file reads/writes) + Agent 1 (decisions only when escalation required)  
> **Sequence:** Run after [`INTEGRATE_DAILY.md`](INTEGRATE_DAILY.md) completes  
> **Weekly framing:** Weekly file generated/updated by [`GENERATE_WEEKLY_EXECUTION.md`](../WEEKLY_CONTROL/GENERATE_WEEKLY_EXECUTION.md)

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. When to Run](#2-when-to-run)
- [3. Prerequisites](#3-prerequisites)
- [4. Inputs](#4-inputs)
- [5. Outputs](#5-outputs)
- [6. Planning Boundaries](#6-planning-boundaries)
- [7. Source-of-Truth Hierarchy](#7-source-of-truth-hierarchy)
- [8. Data to Extract Before Drafting](#8-data-to-extract-before-drafting)
- [9. Preparation Procedure](#9-preparation-procedure)
- [10. Carry-over Rules](#10-carry-over-rules)
- [11. Anchor Selection Rules](#11-anchor-selection-rules)
- [12. Definition of a Good Next Daily](#12-definition-of-a-good-next-daily)
- [13. Standard Checklist](#13-standard-checklist)
- [14. Reusable Execution Template](#14-reusable-execution-template)

---

## 1. Purpose

This procedure creates or pre-fills the next Daily execution file from the current operating state, after daily reverse integration is complete.

The next Daily must reflect four things simultaneously:
- **Real carry-over from today** — where execution actually stopped, not where it was supposed to stop
- **Active Weekly commitments** — the week plan is still the primary planning frame
- **Current dependency reality** — held or blocked work must be expressed with conditions, not as live execution
- **Actual next action** — concrete, restartable, 10–15 min to enter, not vague intention

The goal is **clean re-entry**, not overplanning. Tomorrow starts in execution mode, not planning mode. A good next Daily answers one question instantly: *What do I do first?*

---

## 2. When to Run

**Primary trigger:** After `INTEGRATE_DAILY.md` procedure is completed.

**Also run when:**
- Tomorrow's start is likely affected by unfinished meaningful work
- A dependency resolution is expected tomorrow that changes the execution shape
- Day closure happens late and morning prep time is constrained

**Do not run when:**
- Integration is not yet complete (next Daily would be based on incomplete state)
- The next day already has a fully drafted Daily and requires only minor updates (amend directly instead)

---

## 3. Prerequisites

All of these must be true before running this procedure:

- [ ] Current Daily file has a completed Shutdown section (main artifact + re-entry pack)
- [ ] Current Daily DoD is filled
- [ ] `INTEGRATE_DAILY` has updated: Weekly execution tracker, Monthly (if applicable), Project state (if applicable), Anchor load tracking
- [ ] Weekly anchor map / execution state is available and reflects today's outcomes
- [ ] Next day date and filename are known
- [ ] Canonical Daily template is accessible

If any prerequisite is not met, complete it first. Do not start next-day prep on an unclosed Daily.

---

## 4. Inputs

| Input | Description | Required? |
|---|---|---|
| `<CURRENT_DAILY_FILE>` | Closed Daily file with completed Shutdown | Required |
| `<WEEK_FILE>` | Active weekly plan (WeekPlan for current week) | Required |
| `<MONTH_FILE>` | Active monthly plan — for context only, not re-planning | Context only |
| `<ANCHOR_TRACKING_FILE>` | Execution tracker or anchor load section (in WeekPlan) | Required |
| `<PROJECT_FILE_1>` | Project context file if project state affects tomorrow's execution readiness | If relevant |
| `<PROJECT_FILE_2>` | Second project context file if applicable | If relevant |
| `<NEXT_DAILY_FILE>` | Target path for tomorrow's Daily (may not exist yet) | Required |
| `<DAILY_TEMPLATE_FILE>` | Canonical Daily template: `05_TEMPLATES/TEMPLATE_Daily.md` | Required |
| `<NEXT_DATE>` | Tomorrow's date in YYYY-MM-DD format | Required |
| `<NEXT_WEEKDAY>` | Tomorrow's weekday (Monday / Tuesday / …) | Required |

---

## 5. Outputs

| Output | Description |
|---|---|
| Next Daily file created or updated | Based on canonical template; prefilled from carry-over + Weekly state |
| Clean Primary Anchor | Singular, clearly named, grounded in Weekly commitments + real carry-over |
| Clean Secondary Anchor | Present only if day scope and domain rules allow; conditional if dependency-held |
| Re-entry block prepared | Only if unfinished meaningful work requires context reload |
| First exact execution step | Concrete, restartable in 10–15 min from cold start |
| Realistic capacity mode selected | Derived from Weekly energy pattern hypothesis + today's actual energy read |
| Dependency-sensitive handling encoded | Conditional blocks, hold/checkpoint patterns where needed |
| Preparation report produced | Files created/updated, anchors chosen, re-entry mode, escalations |

---

## 6. Planning Boundaries

### Allowed

- Translate Weekly commitments into tomorrow's execution plan
- Carry forward unfinished meaningful work as concrete next actions
- Refine tomorrow's first steps based on actual stopped state
- Downgrade or defer work when dependency or capacity changed
- Adjust block design to reflect real execution risk from today
- Set blocks as conditional when dependency is unresolved

### Not Allowed

- Create new strategic commitments without escalation to Weekly Review
- Exceed 2 active projects in a normal day without explicit written escalation
- Change Monthly strategy based on a single day's outcome
- Rewrite the Weekly plan silently as a side effect of next-day prep
- Overload tomorrow with today's slippage without first checking tomorrow's available capacity

**When tomorrow requires more than local adjustment:**  
Log the escalation path in the next Daily's Source section and flag it for Weekly Review or mid-week rebalance. Do not silently absorb systemic overload into the next Daily.

---

## 7. Source-of-Truth Hierarchy

When information sources conflict, resolve in this order:

1. **Weekly commitments and anchor map** — what tomorrow is supposed to serve
2. **Current Daily shutdown and re-entry pack** — where execution actually stopped
3. **Dependency reality** — what is actually executable vs. held
4. **Capacity / energy reality** — what is realistically absorbable given today's load
5. **Monthly context** — for awareness only; does not override daily/weekly execution
6. **Project state** — only if a state change materially affects tomorrow's execution readiness

Tomorrow's Daily must reconcile Weekly intent and Daily reality **without contradiction**:
- Weekly defines the commitment frame
- Daily shutdown defines the execution entry point
- If they conflict, carry-over state wins for *how* to execute, but Weekly wins for *what* to execute

---

## 8. Data to Extract Before Drafting

Read source files and collect all of the following before writing anything into the next Daily.

**Time and scope:**
- [ ] Tomorrow's date and weekday
- [ ] Active week reference
- [ ] Weekly commitments for tomorrow's day row (primary anchor + secondary anchor + artifact direction)

**Carry-over from today:**
- [ ] Unfinished work with re-entry pack (exact stopping point, artifact state, next step)
- [ ] Whether carry-over is meaningful (worth continuing) or trivial (drop/defer)
- [ ] Re-entry mode recommended in today's Shutdown: Quick / Analytical / Fragile

**Anchor readiness:**
- [ ] Whether today's primary anchor continues tomorrow or closes
- [ ] Whether today's secondary anchor is still valid for tomorrow
- [ ] Whether the secondary project has new execution conditions (dependency resolved, new info, deferred)

**Dependency status:**
- [ ] Open external dependencies (review pending, customer email, branch state)
- [ ] Dependencies expected to resolve tomorrow (if so, when and how to confirm)
- [ ] Dependencies that remain blocked — must be marked conditional, not active

**Capacity and energy:**
- [ ] Today's energy level recorded
- [ ] Tomorrow's energy mode from Weekly §6.8 energy pattern (planning hypothesis)
- [ ] Whether today's fatigue/overload affects tomorrow's starting capacity

**Required artifacts for tomorrow:**
- [ ] Main expected artifact per anchor
- [ ] Whether artifact is new production or continuation/verification

**Re-entry requirements:**
- [ ] Is a re-entry block needed? (Yes if unfinished meaningful work exists)
- [ ] Re-entry mode: Quick / Analytical / Fragile
- [ ] First exact re-entry action (≤10 min, concrete)
- [ ] Receiving day capacity constraint (can tomorrow absorb the re-entry overhead?)

---

## 9. Preparation Procedure

### Step 1 — Read Source State

1. Read today's Daily Shutdown section in full.
2. Read the Weekly plan's row for tomorrow (anchor map, work type, artifact direction, energy mode).
3. Read the Execution Tracker / anchor load tracking for carry-over notes added during INTEGRATE_DAILY.
4. Classify tomorrow's execution shape:
   - **Continuation** — same primary anchor continues (re-entry block likely required)
   - **Fresh execution** — weekly-defined new anchor; today's anchor closes cleanly
   - **Mixed** — primary closes, secondary continues (or vice versa)
   - **Conditional** — one or both anchors depend on unresolved dependency

Do not write to any file until source reading is complete.

---

### Step 2 — Decide Tomorrow's Anchor Structure

1. Select one **Primary Anchor**:
   - If meaningful carry-over exists from today's primary → continue it (same anchor identity)
   - If today's primary closed cleanly → use Weekly's defined anchor for tomorrow
   - Do not split two threads into one anchor sentence
2. Select **Secondary Anchor** only if:
   - It fits tomorrow's available time domain (office vs. evening)
   - It is genuinely secondary (not competing with primary for cognitive load)
   - It has no unresolved dependency that would make it non-executable; if it does, mark it conditional
3. If dependency invalidates the secondary anchor entirely, remove it or hold as a checkpoint. Do not include it as an active block.
4. Enforce max-2-project rule. If a third project needs attention tomorrow, escalate explicitly in the Source section — do not silently add it.

---

### Step 3 — Decide Whether Re-entry Block Is Required

**Re-entry block required if:** Unfinished meaningful work is continuing from today and requires context reload before execution resumes.

Select mode:
| Mode | When to use | Typical duration |
|---|---|---|
| **Quick** | Work was almost complete; artifact state is clear; restart cost is low | 5–10 min |
| **Analytical** | Must restore a reasoning chain; notes review + mental model reload needed | 10–15 min |
| **Fragile** | State or environment must be inspected before continuation; Integration or debug work | 10–20 min |

Write the exact first re-entry action. Must be:
- Scoped to ≤10–15 min
- Concrete enough to start without re-analysis
- Named as pre-step attached to the inherited anchor (not as a separate anchor)

Confirm receiving day can absorb the overhead: check tomorrow's anchor load and energy mode before scheduling.

---

### Step 4 — Draft Tomorrow's Execution Blocks

1. Derive blocks from Weekly commitments + real carry-over state. Do not invent scope.
2. Convert vague carry-over into operational blocks. Each block must state:
   - Anchor name
   - Goal (what is being produced)
   - Size (S / M / L)
   - Ambiguity (0–5)
   - Expected artifact
   - First step
3. Apply time domain rules:
   - Office hours → Primary anchor (Zephyr or equivalent primary project)
   - Evening slots → Secondary anchor (personal, research, secondary project)
4. Keep weekday evening scope conservative. No L-sized tasks on weekday evenings.
5. Encode dependency conditions explicitly. A block that can only execute if a dependency resolves must state the condition and a fallback/checkpoint.

---

### Step 5 — Write Artifacts and First Outcome

1. For each anchor, specify the main expected artifact:
   - Format: `[project]: [artifact name] ([state at end of day])`
   - Example: `Zephyr: merge verification log (confirming both tests pass on develop)`
2. Write **1 Most Important Outcome** for the day. One sentence. The single result that makes tomorrow a success.
3. Write **First Execution Step** for the primary anchor:
   - Include time reference (e.g., `(8:00–8:15 after re-entry)`)
   - Must be the literal first executable action
   - Concrete enough to launch without decision-making at day start

---

### Step 6 — Encode Dependency-Aware Behavior

**If dependency is unresolved:**
- Write the block as conditional: `CONDITIONAL BLOCK — proceed only if [dependency] arrives by [time]`
- Write explicit fallback: what to do if the condition is not met by the stated time
- Do not include the block as an active execution block without the conditional wrapper

**If dependency is expected to resolve tomorrow:**
- Note the resolution condition and the window: `If [item] arrives by [time] → execute; if not → defer to [date/context]`
- Do not assume resolution without stating it explicitly

**If dependency resolved today:**
- Convert the previously-held block to a normal execution block
- Remove the conditional pattern; it is no longer needed

**If dependency creates risk of weekly distortion:**
- Note the escalation path in the Source section
- Do not absorb the distortion silently into tomorrow's plan

---

### Step 7 — Run Overload and Coherence Check

Before writing the final file, verify:

- [ ] Tomorrow is not overloaded because today slipped (check anchor load vs. typical daily capacity)
- [ ] Primary and Secondary anchors still match Weekly commitment intent
- [ ] First execution step is concrete and specific (not "continue work on Zephyr")
- [ ] Block sizes are realistic given today's energy read and tomorrow's energy hypothesis
- [ ] No third project has silently appeared
- [ ] All carry-over items are meaningful — drop anything trivial
- [ ] Evening domain rules are respected (no L-task on weekday evening)
- [ ] Tomorrow does not function as a replanning session disguised as a daily

If any check fails, fix the draft before writing the file.

---

### Step 8 — Create or Update Next Daily File

1. If the next Daily file does not exist, create it from `<DAILY_TEMPLATE_FILE>`.
2. Prefill these sections minimum:
   - **Header:** Date, Week reference
   - **Source:** Weekly commitments for tomorrow + inherited spillover
   - **Morning Setup:** Work time domain check + Re-entry Block Check (mode + first action + time)
   - **Canonical Daily Anchors:** Primary and Secondary anchor identity (exact, not vague)
   - **First Execution Step:** Concrete step with time reference
   - **Office Hours blocks:** At least Block 1 derived from primary anchor
   - **Evening block:** Prefilled or marked optional/conditional
   - **Dependency notes:** Conditional blocks, hold/checkpoint entries
3. Keep historical references factual and brief. Do not write narrative.
4. Do not fill the Signals, Shutdown, Metrics Capture, Drift Early Warning, DoD, or Human Reflection sections. These are execution-time outputs, not planning-time inputs.

---

### Step 9 — Produce Report

Write a brief preparation report at end of session or in the weekly Execution Tracker.

Required fields:

```
## Next-Day Preparation Report – YYYY-MM-DD (prepared for YYYY-MM-DD)

**File created or updated:**
- [path to next Daily file]

**Primary Anchor selected:**
- [anchor name and exact identity]

**Secondary Anchor:**
- [anchor name] / [conditional — reason] / [removed — reason]

**Re-entry block:**
- Mode: Quick / Analytical / Fragile / None
- First action: [exact action, time reference]

**Carry-over inserted:**
- [project] – [exact next action] – [re-entry mode]

**Dependency conditions encoded:**
- [project] – [condition] – [fallback]

**Escalation notes (if any):**
- [note, or "None"]
```

---

## 10. Carry-over Rules

These rules apply every time work is carried forward from one day to the next.

- Carry forward only **meaningful unfinished work** — work that has real impact if not continued soon.
- Always **rewrite carry-over as an exact next action**. The carry-over entry is not a task name; it is a restart instruction.
- **Do not carry vague intentions.** "Think more about the design" is not carry-over. "Review draft API schema in Zephyr/docs → verify against Mon test results (15 min)" is carry-over.
- **Do not carry completed work.** Work that reached its DoD does not need a carry-over entry.
- **Do not carry blocked work as if it were executable.** Blocked work must be encoded as conditional or checkpoint.
- If carry-over **no longer matters** (superseded, irrelevant, or low signal), drop it explicitly and note the drop in the preparation report.
- If carry-over **conflicts with Weekly priorities**, escalate instead of silently displacing the week's intended work.

---

## 11. Anchor Selection Rules

**Primary Anchor:**
- Must be singular. One project, one clear phase.
- Must correspond to a Weekly commitment for tomorrow's day row.
- If today's primary continues, carry the same anchor identity — do not rename it.
- Must be executable without unresolved dependency. If blocked, replace with the next Weekly-ready anchor and hold the blocked anchor as conditional.

**Secondary Anchor:**
- Must remain truly secondary — smaller scope, lower cognitive load, different time domain.
- Must respect office-hours vs. evening domain separation.
- Must have realistic capacity in the evening given today's energy read.
- If development is conditional on a dependency, mark it conditional — do not activate it.
- If no Secondary Anchor fits cleanly, leave the Evening slot as optional or rest.

**Anchor identity stability:**
- Weekly defines the anchor identity.
- Daily confirms, refines, or downgrades execution — not identity.
- Do not rename an anchor mid-week unless an explicit escalation or incident justifies it (and document the reason).

---

## 12. Definition of a Good Next Daily

A next Daily is ready when:

- **Tomorrow starts without confusion.** Open the file and know exactly what to do in the first 10 minutes.
- **First 10–15 min action is obvious.** Re-entry block or first execution step is listed with a time reference and a concrete action.
- **Carry-over is operational.** Every unfinished thread has an exact restart instruction.
- **Anchors are clean.** Primary and Secondary anchor identities are unambiguous; no project conflation.
- **Day scope is believable.** The total planned load fits a normal working day without relying on exceptional energy.
- **Dependency handling is explicit.** Conditional blocks state their condition and fallback. Nothing pretends to be executable if it isn't.
- **Daily file supports execution, not just documentation.** Reading it should shorten the cognitive startup cost, not add to it.

---

## 13. Standard Checklist

Copy this checklist into each session when running next-day preparation.

```
### Next-Day Preparation Checklist – preparing for YYYY-MM-DD (WEEKDAY)

**Source reading:**
- [ ] Current Daily Shutdown read in full
- [ ] Tomorrow's Weekly row read (anchor + artifact + energy mode)
- [ ] Execution Tracker / anchor load notes reviewed

**Anchor structure:**
- [ ] Primary Anchor selected (singular, concrete, Weekly-grounded)
- [ ] Secondary Anchor selected OR removed/made conditional (documented reason)
- [ ] Max-2-project rule confirmed

**Re-entry block:**
- [ ] Re-entry block needed? → Yes (mode: ___) / No
- [ ] If Yes: mode selected, first action written, timing placed, receiving day capacity checked

**Carry-over:**
- [ ] All unfinished meaningful items carried forward as exact next actions
- [ ] Vague intentions dropped or rewritten
- [ ] Completed work not repeated
- [ ] Blocked work marked conditional, not active

**Dependency handling:**
- [ ] Open dependencies identified
- [ ] Conditional blocks or hold/checkpoint patterns applied
- [ ] Dependency resolution conditions stated explicitly

**Block design:**
- [ ] Blocks derived from Weekly + carry-over (no new scope invented)
- [ ] Sizes realistic (S / M / L correctly assigned)
- [ ] Domain rules respected (office = primary project; evening = secondary)
- [ ] Weekday evening is not L-sized

**Artifacts and first outcome:**
- [ ] Main artifact per anchor specified
- [ ] 1 Most Important Outcome written
- [ ] First Execution Step written with time reference

**Overload check:**
- [ ] Tomorrow's load is not inflated by today's slippage
- [ ] No hidden third project
- [ ] Day scope is believable

**File:**
- [ ] Next Daily file created from template (if absent)
- [ ] Minimum sections prefilled (Source, Morning Setup, Anchors, First Step, Blocks, Dependencies)
- [ ] Execution-time sections left blank (Signals, Shutdown, Metrics, Drift, DoD, Reflection)

**Report:**
- [ ] Preparation report produced
- [ ] Escalation notes flagged if any (or confirmed: none)
```

---

## 14. Reusable Execution Template

Use this command block to run next-day preparation. Replace all placeholders before submitting.

```
TASK: Run next-day preparation procedure for <NEXT_DATE> (<NEXT_WEEKDAY>)

Procedure reference: 01_OS/04_OPERATIONS/DAILY_INTEGRATION/PREPARE_NEXT_DAILY.md
Prerequisite: INTEGRATE_DAILY.md must already be completed for <CURRENT_DATE>.

Inputs:
- CURRENT_DAILY_FILE: <path to today's closed Daily, e.g. 03_PLANNING/03_WEEK/YYYY-MM-DD_Daily.md>
- WEEK_FILE: <path to active weekly plan, e.g. 03_PLANNING/03_WEEK/YYYY-Www_WeekPlan.md>
- MONTH_FILE: <path to active monthly plan, e.g. 03_PLANNING/02_MONTH/YYYY-MM_March_Planning.md — context only>
- ANCHOR_TRACKING_FILE: <path or section reference for anchor load tracking, e.g. WEEK_FILE §EXECUTION TRACKER>
- PROJECT_FILE_1: <path to project 1 context file — or SKIP if not materially affecting tomorrow>
- PROJECT_FILE_2: <path to project 2 context file — or SKIP if not materially affecting tomorrow>
- NEXT_DAILY_FILE: <target path for tomorrow's Daily, e.g. 03_PLANNING/03_WEEK/YYYY-MM-DD_Daily.md>
- DAILY_TEMPLATE_FILE: 05_TEMPLATES/TEMPLATE_Daily.md
- NEXT_DATE: <YYYY-MM-DD>
- NEXT_WEEKDAY: <Monday / Tuesday / Wednesday / Thursday / Friday>

Instructions:
1. Follow the preparation procedure exactly as defined in PREPARE_NEXT_DAILY.md §9 (Steps 1–9).
2. Apply carry-over rules from §10 without exception.
3. Apply anchor selection rules from §11.
4. Run the overload and coherence check (Step 7) before writing any file.
5. Only prefill planning-time sections in the next Daily. Leave execution-time sections blank.
6. Produce a preparation report as defined in §9 Step 9.
7. If any adjustment requires escalation (new scope, overloaded day, strategic conflict),
   flag it in the report under "Escalation notes" — do not resolve it autonomously.
8. Commit all created or modified files with message:
   "prepare: next daily YYYY-MM-DD ready from YYYY-MM-DD carry-over + weekly state"
```

---

> **Procedure version:** 1.0  
> **Created:** 2026-03-15  
> **Location:** `01_OS/04_OPERATIONS/DAILY_INTEGRATION/PREPARE_NEXT_DAILY.md`  
> **Sequence:** Run after `INTEGRATE_DAILY.md` completes  
> **Next review trigger:** When system architecture changes (new layers, new file conventions, renamed templates)
