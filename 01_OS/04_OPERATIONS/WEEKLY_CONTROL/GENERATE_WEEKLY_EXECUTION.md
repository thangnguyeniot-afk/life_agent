# GENERATE_WEEKLY_EXECUTION — Weekly Execution File Generation Procedure

> **Type:** Operating Procedure  
> **Layer:** OS / Operations  
> **Scope:** Monthly direction + execution reality → Weekly Execution file  
> **Prerequisite:** Month file must exist and be accessible  
> **Reuse:** Run once per week, typically at end of week or Sunday, OR on-demand for reconstruction/rebalance  
> **Maintained by:** Agent 2 (file reads/writes + data collection) + Agent 1 (escalation decisions only)  
> **Related:** [`WEEKLY_REBALANCE.md`](WEEKLY_REBALANCE.md) (mid-week correction) | [`WEEK_CLOSEOUT.md`](WEEK_CLOSEOUT.md) (week-end closure) | [`INTEGRATE_DAILY.md`](../DAILY_INTEGRATION/INTEGRATE_DAILY.md) | [`PREPARE_NEXT_DAILY.md`](../DAILY_INTEGRATION/PREPARE_NEXT_DAILY.md)

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. When to Run](#2-when-to-run)
- [3. Supported Modes](#3-supported-modes)
- [4. Prerequisites](#4-prerequisites)
- [5. Inputs](#5-inputs)
- [6. Outputs](#6-outputs)
- [7. Source-of-Truth Hierarchy](#7-source-of-truth-hierarchy)
- [8. Planning Boundaries](#8-planning-boundaries)
- [9. Data to Collect Before Writing](#9-data-to-collect-before-writing)
- [10. Generation Procedure](#10-generation-procedure)
- [11. Anchor Rules](#11-anchor-rules)
- [12. Carry-over Rules](#12-carry-over-rules)
- [13. Reconstruction Rules](#13-reconstruction-rules)
- [14. Definition of a Good Weekly Execution File](#14-definition-of-a-good-weekly-execution-file)
- [15. Standard Checklist](#15-standard-checklist)
- [16. Reusable Execution Template](#16-reusable-execution-template)

---

## 1. Purpose

The Weekly Execution file is the operational bridge between Monthly strategy and Daily execution reality.

**Why it exists:**

The Monthly file provides direction: commitments, projects, rough capacity allocation, and key risks.

The Daily files provide ground truth: what actually happened, where work stopped, what unfinished items remain, what dependencies blocked us.

The Weekly Execution file **reconciles both without contradiction**:
- Translates monthly direction into a realistic weekly frame
- Encodes carry-over from recent execution reality
- Defines daily anchor structure so daily planning inherits cleanly
- Tracks dependency-aware sequencing and weekly re-entry patterns
- Maintains realistic workload assumptions
- Produces weekly artifacts explicitly

This procedure ensures Weekly Execution files are not planning documents pretending to be operational frames. They are concrete execution files: small enough to fit in a human week, coherent enough to guide daily planning, detailed enough to reconcile month and day without distortion.

---

## 2. When to Run

**Primary trigger:** End of week planning window, typically Sunday, when preparing the upcoming week.

**Also run when:**
- A new weekly file must be created for an upcoming week (preparation mode)
- A weekly file is missing and must be reconstructed from Daily files + month context
- An active week requires controlled adjustment (weekly rebalance) due to material change in reality
- Carrying forward from a previous week that ended with significant unfinished work

**Do not run when:**
- The active weekly file is sufficient and no material change requires rebalance
- Escalation is still unresolved (wait for escalation decision before rewriting the week)
- Daily execution is ongoing and the week is actively tracking (wait until shutdown window)

---

## 3. Supported Modes

### Mode A — New Week Generation

**Use when:** Preparing an upcoming week from Month + recent execution reality.

**Input:** Month file + previous week (if previous week completed) + carry-over summary + empty or template weekly structure.

**Output:** Complete Weekly Execution file ready for daily planning.

**Timing:** Usually Sunday planning window or Friday afternoon (advance prep).

**Key constraint:** Must incorporate realistic carry-forward from previous week without overloading the new week.

### Mode B — Week Reconstruction

**Use when:** A weekly file is missing and must be reconstructed from Daily files + available tracking.

**Input:** Complete set of Daily files from that week + month guidance + project state files (optional).

**Output:** Weekly Execution file with actual day-by-day execution summary + reconstructed weekly anchor summary.

**Timing:** Usually after week ends; may happen days or weeks later.

**Key constraint:** Reconstruction must state uncertainty explicitly. Do not invent clean history. Reconstruction is forensic, not prescriptive.

### Mode C — Weekly Rebalance Update

**Use when:** The week is active, but reality changed enough to require controlled adjustment of the weekly frame.

**Input:** Existing weekly file + mid-week execution data + new dependency/blocker info + capacity reassessment.

**Output:** Updated weekly file that reframes anchor structure, adjusts expectations, or rescopes secondary anchors in response to new data.

**Timing:** Typically mid-week (Wed/Thu) if a major blocker or capacity change occurs.

**Key constraint:** Rebalance updates are controlled rewrites, not panic revisions. Escalation decision should be made before running rebalance. Preserve weekly coherence.

---

All three modes preserve the same **Weekly Execution file structure**. Mode determines which sections are filled from what sources.

---

## 4. Prerequisites

All of these must be true before running this procedure:

- [ ] Target month file exists and is accessible
- [ ] Previous week file exists (if completing a hand-off from prior week) OR carry-over notes are available
- [ ] Recent Daily files are available and readable (at minimum: last 2–3 days of previous week)
- [ ] Weekly template or canonical weekly structure is accessible (e.g., `05_TEMPLATES/TEMPLATE_Week_Final.md`)
- [ ] Target week date range is known (YYYY-Www format)
- [ ] If rebalance mode: escalation decision or blocker is clearly documented before proceeding

If any prerequisite is not met, complete it first. Do not generate a weekly file on incomplete information.

---

## 5. Inputs

| Input | Description | Required? | Source |
|---|---|---|---|
| `<MONTH_FILE>` | Active month execution file with priority/commitment direction | Required | `03_PLANNING/02_MONTH/` |
| `<PREVIOUS_WEEK_FILE>` | Completed previous week file (if Mode A hand-off) | Conditional | `03_PLANNING/03_WEEK/` |
| `<CARRY_OVER_SUMMARY>` | Unfinished meaningful work from previous week | Conditional | Previous week Shutdown notes or raw Daily summary |
| `<DAILY_FILES>` | Recent Daily files relevant to prior/current week | Conditional | `03_PLANNING/03_WEEK/YYYY-MM-DD_Daily.md` |
| `<PROJECT_STATE_FILES>` | Project context files if project state affects weekly priorities (optional) | Optional | `08_PROJECT_CONTEXT/` |
| `<ANCHOR_TRACKING_FILE>` | Anchor load tracking or execution history (optional) | Optional | Section in monthly or legacy tracking file |
| `<WEEKLY_TEMPLATE_FILE>` | Canonical weekly structure template | Required | `05_TEMPLATES/TEMPLATE_Week_Final.md` |
| `<TARGET_WEEK_NAME>` | Week identifier (e.g., 2026-W11) | Required | User input |
| `<DATE_RANGE>` | Week date range (e.g., March 16–22, 2026) | Required | User input |
| `<MODE>` | Generation mode: A (New), B (Reconstruction), or C (Rebalance) | Required | User input |

---

## 6. Outputs

| Output | Description |
|---|---|
| Target Weekly Execution file created or updated | At `03_PLANNING/03_WEEK/<WEEK_NAME>_Execution.md` (e.g., `2026-W11_Execution.md` or `2026-W11_WeekPlan.md`) |
| Weekly focus defined | Singular coherent center of gravity for the week |
| Primary and optional secondary anchors defined | Weekly-level anchors that daily anchors inherit from |
| Weekly outcomes defined | 1–2 primary outcomes; optional supporting outcomes |
| Dependency/risk notes embedded | Explicit dependency awareness + weekly re-entry patterns |
| Daily anchor map | One row per weekday with Primary/Secondary anchor + artifact direction |
| Carry-over encoded | Meaningful unfinished work from prior week converted to weekly entry points |
| If Mode B: actual day summaries | Quick factual execution summary for each day from Daily files |
| Weekly execution report | Concise summary of what was generated and what assumptions were made |

---

## 7. Source-of-Truth Hierarchy

When information sources conflict, resolve in this rank order:

### For New Week Generation (Mode A)

1. **Monthly commitments and direction** — what the month intends this week to serve
2. **Carry-over from previous week (recent Daily shutdowns)** — where execution actually stopped
3. **Dependency reality** — what is actually executable vs. held/blocked
4. **Capacity / energy reality** — realistic workload given recent execution patterns
5. **Project state files** — for awareness; does not override weekly/monthly frame
6. **Anchor tracking history** — context for anchor load patterns; informational

**Reconciliation rule:** Month defines the commitment frame. Carry-over execution reality defines the entry point. Daily planning will inherit from this week, so the weekly file must be concrete enough to guide daily work without re-planning.

### For Week Reconstruction (Mode B)

1. **Daily files from that week** — factual ground truth of what happened
2. **Month file (from that time period)** — what the month intended
3. **Project state files** — project context during that week
4. **Anchor tracking if available** — helpful but not required
5. **Inferred weekly structure only where sufficient evidence** — never invent history

**Reconstruction rule:** Let daily evidence speak. If Daily files are missing, state explicitly. Do not create fake weekly structure to fill gaps.

### For Weekly Rebalance (Mode C)

1. **Existing weekly file** — preserve structure
2. **New execution data / mid-week actual results** — reality that triggered rebalance
3. **New dependency/blocker information** — changed conditions
4. **Capacity reassessment** — new energy/load data
5. **Month direction** — does not change; rebalance adjusts weekly frame to serve month, not replace it

**Rebalance rule:** Update expectations, rescope secondary work, adjust carry-over, but preserve the week's coherence and monthly alignment.

---

## 8. Planning Boundaries

### Allowed

- Translate monthly goals into one realistic weekly frame
- Choose one dominant anchor; optional second anchor only if truly secondary
- Carry forward meaningful unfinished work as concrete weekly entry points
- Encode dependency-aware sequencing and re-entry patterns
- Reduce scope to fit real capacity if previous week revealed overestimate
- Downgrade work type if capacity or energy assumptions were wrong
- Update the weekly file during controlled rebalance (C mode)
- Defer secondary work to future week with explicit reason
- Escalate incompatibilities between month and reality instead of silently absorbing them

### Not Allowed

- Silently rewrite monthly strategy without escalation
- Overload the week with > 2 active projects (weekday execution boundary)
- Pretend blocked work is executable without encoding conditions
- Create fake certainty during reconstruction when evidence is missing
- Turn the weekly file into a narrative journal or prose document
- Insert new strategic commitments that bypass month-level planning review
- Distribute unfinished work across all 5 days as if every evening comes free
- Absorb systemic overload into the week without flagging rebalance risk

**When weekly frame conflicts with monthly strategy:** Escalate instead of silently hiding it. Record the incompatibility in the weekly file and recommend monthly rebalance or weekly rescope.

---

## 9. Data to Collect Before Writing

**Do not write anything until you have collected all of the following:**

### Week identity and scope

- [ ] Week name (format: YYYY-Www, e.g., 2026-W11)
- [ ] Date range (e.g., March 16–22, 2026)
- [ ] Mode: A (New) / B (Reconstruction) / C (Rebalance)

### Month context

- [ ] Month file read in full (section on this week's priorities)
- [ ] Month commitment state (are we ahead/behind month plan?)
- [ ] Month energy pattern hypothesis for this week (if provided)
- [ ] Month carry-forward notes (if any carry into this week)

### Previous week state

- [ ] Previous week file read (if exists)
- [ ] Actual vs. planned completion: what delivered, what didn't?
- [ ] Major blockers or unexpected issues from previous week
- [ ] Clean carry-forward items (meaningful unfinished work)
- [ ] Drop list: items no longer relevant carried forward

### Unfinished meaningful work

- [ ] Identify all unfinished work from previous week with re-entry mode needed
- [ ] Classify each as: critical (must do this week), important (should do), nice-to-have (defer if load)
- [ ] Determine if carry-over threatens the new week's capacity or viability

### Active projects

- [ ] List all active projects entering the week
- [ ] For each: primary anchor territory, likely daily window (office hours / evening), estimated load
- [ ] Which projects are blocked or dependency-held?
- [ ] Which projects are execution-ready?

### Dominant dependency chain

- [ ] Identify the critical path: what must happen for the month to advance?
- [ ] Note external dependencies (reviews, customer responses, environment readiness)
- [ ] Note internal dependencies (project A must finish before B can start)
- [ ] Unblock timing: when are blocked items likely to unblock?

### Anchor structure

- [ ] Likely primary anchor (single; 1–2 projects only)
- [ ] Valid secondary anchor (only if it fits; must be truly secondary)
- [ ] Why is this anchor coherent for the week? (one-sentence justification)
- [ ] Office hours vs. evening domain usage (if system uses this boundary)

### Capacity and energy

- [ ] Recent energy level readings (from last 3–5 daily files)
- [ ] Expected energy pattern for this week (if month file provides hypothesis)
- [ ] Realistic load: how many daily deep-work blocks are actually sustainable?
- [ ] Evening capacity: how much meaningful work fits each weekday evening?
- [ ] Any known energy dips (recurring patterns like Thu dip)?

### Artifacts and outcomes

- [ ] What is the expected primary outcome this week?
- [ ] What artifact should exist by Friday EOD that proves the week worked?
- [ ] Is there a secondary outcome worth tracking?
- [ ] Do any artifacts depend on external delivery (reviews, customer response)?

### Risk and uncertainty

- [ ] What is the single biggest risk to weekly delivery?
- [ ] If that risk happens, what is the fallback plan?
- [ ] What is unknown or uncertain entering the week?
- [ ] Should the week be flagged for mid-week rebalance if certain conditions occur?

---

## 10. Generation Procedure

### Step 1 — Read Source State (Mode-Dependent)

**For Mode A (New Week):**
1. Read the month file thoroughly. Locate the section for this week (if exists) or this week's priority description.
2. Read the entire previous week file (if it completed on time) to understand execution shape and any hand-off.
3. Extract carry-over notes from previous week's Shutdown sections (especially unfinished work + recommended re-entry mode).
4. Scan recent Daily files (last 3–4 days of previous week) to calibrate energy patterns, blockers, and execution style.
5. Read project state files only if they materially affect weekly priorities (e.g., "deployment happens this week").

**For Mode B (Reconstruction):**
1. Read all Daily files from the target week (every day available).
2. Read the month file from that time period to understand what the month intended.
3. Scan project state files from that week if available.
4. Do NOT read Daily files from other weeks unless they provide missing context.
5. Accept incomplete data. Mark uncertainty explicitly if daily files are missing.

**For Mode C (Rebalance):**
1. Read the existing weekly file in full.
2. Read the mid-week (Tue/Wed) Daily file(s) that triggered the rebalance.
3. Identify what changed: blocker, new dependency, capacity shift, energy change.
4. Read month file only to confirm weekly frame is still aligned with monthly intent.
5. Do not rewrite unchallenged sections.

---

### Step 2 — Determine Weekly Focus

1. Identify the **single dominant activity** for the week:
   - One project taking 60–70% of weekly effort
   - One coherent phase (e.g., "merge testing," "customer presentation," "architecture consolidation")
   - One clear outcome that Friday could verify
2. Ask: "If I had to answer 'what is this week about?' in one sentence, what would it be?"
3. Identify optional **secondary anchor** only if:
   - It genuinely fits available time domain (evening or flexible time)
   - It does not compete cognitively with primary anchor
   - It is not blocked by the same dependency as primary
   - You can imagine one daily block (60–90 min) sufficing for its weekly scope
4. If a third project wants attention, explicitly defer it to following week or flag as blocker.
5. State the full weekly focus as a one-sentence frame:
   - Example: "W10: Scope Freeze Prep — merge 3 tests to develop; deliver team plan + pptx findings"
   - Not: "Zephyr work, Signee work, RobotOS work" (that's project listing, not focus)

---

### Step 3 — Define Weekly Outcomes

1. Define **1 Primary Outcome**:
   - Artifact-oriented (not task-oriented)
   - Example: "3 tests merged to develop + verification log" NOT "write tests"
   - One-sentence statement
   - Deliverable by Friday EOD
2. Define optional **Secondary Outcome** only if:
   - It flows naturally from secondary anchor
   - It does not dilute primary outcome focus
   - It is realistic given capacity
   - Example: "team plan V1 drafted + environment setup checklist"
3. Support outcomes may exist (nice-to-have), but keep them lightweight:
   - Example: "project merge log updated"
   - Mark as "support" or "optional" in the weekly file
4. State: "Week succeeds if [Primary Outcome] is delivered by Fri EOD."

---

### Step 4 — Build Dependency-Aware Weekly Strategy

1. For each active project, map **blocking dependencies**:
   - External: waiting for customer email, review approval, branch change
   - Internal: project A must finish before B can start
   - Environmental: tool/environment readiness
2. Encode **unblock conditions and timing**:
   - Example: "Signee team plan can start Wed evening once customer email arrives"
   - Mark as conditional block (not active execution) until condition clears
3. Encode **weekly re-entry pattern**:
   - If carrying over Mon, determine re-entry mode: Quick / Analytical / Fragile
   - If carrying over Tue, determine Wed re-entry cost
4. State **when weekly rebalance should trigger**:
   - Example: "If Zephyr merge blocked by more than 24h, rebalance"
   - Example: "If test environment unavailable Wed, defer secondary anchor to following week"

---

### Step 5 — Build Daily Anchor Map

1. For each weekday (Mon–Fri):
   - Define **Primary Anchor** (inherited from weekly primary)
   - Define optional **Secondary Anchor** only if it fits that day
   - Avoid: same anchor twice (no Mon/Tue duplication); hidden third project spread
2. Use columns:
   - Day
   - Office Hours Anchor (what is work 8:00–17:30)
   - Evening Anchor (if any; must be secondary or personal)
   - Work Type (Structured Execution, Synthesis, Integration, Closure)
   - Artifact direction (what artifact should exist EOD)
   - Risk / Flex note (if conditions change, plan B)
3. Respect domain rules (if system uses Work Time Domain rule):
   - Office hours = primary project only
   - Evening = secondary project or personal work only
   - Do not allow primary project to sprawl into evening unless escalation documented
4. Keep **weekday evening conservative**:
   - No L-sized tasks on weekday evenings
   - Default: `1×M` or `2×S` capacity
   - Adjust down based on energy pattern

---

### Step 6 — Encode Carry-over into the Week

1. **List all unfinished meaningful work** from previous week:
   - Item name
   - Current artifact state (e.g., "test code written, waiting for review")
   - Next exact step (not vague intention; concrete action)
   - Re-entry mode needed (Quick / Analytical / Fragile)
   - Receiving day (which day will absorb this carry-over)
2. **Check carrying-over saturation**: Does the receiving day have room?
   - Example: "Wed has 2 L-blocks already. Adding Mon carry-over (Fragile, 20 min) is safe."
   - Example: "Tue good-depth day. Can absorb Mon carry-over (Quick 10 min) + execute primary anchor same day."
3. **Convert carry-over to weekly entry point**:
   - NOT: "finish the test" ← vague intention
   - YES: "(8:00–8:10 Quick re-entry) Open test file → review Mon notes → confirm test ready for merge → begin merge procedure"
4. **Mark as carry-over in daily anchor map**:
   - Example: Mon spillover → (Wed 8:00–8:10 Quick re-entry to absorb test merge)

---

### Step 7 — If Reconstruction Mode, Summarize Actual Execution

1. For each day where Daily files exist, write a short factual summary:
   - What anchor(s) executed
   - What artifact was produced
   - Major blockers or spillover to next day
   - Example: "Mon: Zephyr test write (aim: 2 tests). Completed Dbugs write ✓; Dbus break ← spillover to Tue."
2. **Only infer where evidence is clear:**
   - If Mon Daily says tests wrote, state "test write executed."
   - Do NOT say "probably worked hard" or worse: "clearly struggled" without evidence.
3. **Mark missing days explicitly:**
   - If Wed Daily is missing: "(Wed Daily missing — reconstructed from Thu notes)"
   - Do NOT invent Wed execution history.
4. **Note contradictions or uncertainty:**
   - If weekly intended X but Daily recorded Y: state both. Do NOT hide the discrepancy.
5. **Do not prescribe or judge:**
   - Reconstruction = forensic read of what happened
   - Do NOT rewrite messy execution as if it were ideal

---

### Step 8 — Create or Update the Weekly Execution File

1. If file does not exist, create from `<WEEKLY_TEMPLATE_FILE>`.
2. Fill sections in this order:
   - **Header:** Week name, date range, target monthly context
   - **§1 Context Carry-Forward:** Month intention + relevant carry-over from previous week
   - **§2 Weekly Goals / Outcomes:** Primary + Secondary outcomes
   - **§3 Missions This Week:** High-level anchor structure; which projects carry the week's weight
   - **§4 Constraints:** What must hold true for the week to work; what blockers or limits exist
   - **§5 Commitments:** Final list of what will be delivered (or conditional on dependency)
   - **§6 Risks & Open Questions:** What could go wrong; what is unknown
   - **§6.8 Weekly Energy Pattern:** Planning hypothesis for expected energy each day
   - **§7 Daily Anchor Map:** Row per weekday with Primary/Secondary anchors, artifact direction
   - If Mode B: **Actual Execution Summary** (per-day factual execution record from Daily files)
   - **Execution Tracker (if active week):** Space to track actual daily completion
   - **Suggested Mon Starting Anchor:** If next Monday's planning is relevant

3. Do **not** include:
   - Narrative prose about the week's emotional arc
   - Tutorial-level explanations of why things are planned this way
   - Hypothetical "what if" scenarios
   - Long lists of all possible tasks

4. Keep sections **compact**. Use tables and bullets, not prose paragraphs.

---

### Step 9 — Consistency Check

Before finalizing, verify all of the following:

- [ ] Weekly outcomes are aligned with monthly direction (not contradicting)
- [ ] Daily anchor map is realistic given expected energy pattern
- [ ] Carry-over is explicitly encoded with re-entry mode + receiving day
- [ ] No project appears in > 2 project slots per day (no hidden third project)
- [ ] Project states are not contradicted by independent sources
- [ ] Dependency handling is explicit (conditional blocks state conditions)
- [ ] Weekly focus is singular and coherent (one-sentence test: can you say "the week is about ___" clearly?)
- [ ] Evening capacity assumptions match recent Daily evidence
- [ ] Work type assignments (Structured Execution vs. Synthesis vs. Integration) are realistic
- [ ] If Mode C (rebalance): preserved existing weekly structure while updating expectations

If any check fails, fix before moving to Step 10.

---

### Step 10 — Produce Report

Write a brief generation report. Required fields:

```
## Weekly Generation Report – <WEEK_NAME> (prepared <DATE>)

**Mode:** A (New) / B (Reconstruction) / C (Rebalance)

**File created or updated:**
- <path to weekly execution file>

**Week range:** <DATE_RANGE>

**Monthly context:**
- <month commitment this week is serving>

**Primary anchor:**
- <anchor identity>

**Secondary anchor:**
- <anchor identity> / [conditional — reason] / [deferred; reason]

**Weekly outcomes:**
- Primary: <one-sentence artifact-oriented outcome>
- Secondary: <if applicable>

**Daily anchor map coherence:**
- <summary: how are Mon–Fri distributed across anchors?>
- <any hidden third project spread? no.>
- <evening capacity realistic? yes/no: explain if no.>

**Carry-over from previous:**
- <list unfinished items carried forward>
- <re-entry mode + receiving day for each>
- <does carry-over overload any receiving day? no.>

**Dependencies:**
- <blocking item 1: condition for unblock + timeline>
- <blocking item 2: ...>
- <escalation risk: none / [risk — reason]>

**Energy pattern assumptions:**
- <brief summary of week's expected energy hypothesis>

**Reconstruction notes (if Mode B):**
- <which days' Daily files were complete / missing / partial>
- <any significant discrepancies between month intent and actual execution>
- <uncertainty markers: where evidence is incomplete>

**Rebalance notes (if Mode C):**
- <what changed: blocker / capacity shift / dependency resolved / ...>
- <how does the rebalanced week serve month direction differently?>
- <what sections were updated; what stayed the same?>

**Risks or escalation:**
- <is there a weekly rebalance risk if certain conditions occur? document it.>
- <any month–week incompatibility that should be escalated? document it.>
- <assess: is this week viable as specified? yes/no: explain if no.>
```

---

## 11. Anchor Rules

- **One dominant anchor per week:** Singular enough that "what is this week about?" has one clear answer.
- **Secondary anchor must be truly secondary:** Must not compete with primary for cognitive load or calendar space. Default = evening or flexible time only.
- **Do not mix two projects into one anchor sentence:** "Zephyr + RobotOS testing" is not an anchor; it's a list. A real anchor: "Zephyr — merge tests to develop."
- **Avoid multi-project fragmentation:** If more than 2 projects want attention, either reassess which is truly secondary, or escalate one to following week explicitly.
- **If capacity is weak, reduce secondary anchor first:** Do not scale down primary; that breaks month commitment. Do not try to keep both anchors if load is clearly unsustainable; choose one.
- **Daily anchors inherit from weekly logic, not compete with it:** Each day's Primary Anchor should be the same project/phase as the week's Primary Anchor. Daily Secondary Anchors can vary, but should remain secondary.
- **Anchor identity stability:** Weekly defines the anchor identity. Daily refines or downgrade—it does not rename anchors mid-week unless escalation justified.

---

## 12. Carry-over Rules

- **Carry over only meaningful unfinished work:** Work that has real impact if not continued soon. Drop trivial carry-over explicitly.
- **Rewrite carry-over as exact next entry point:** Not "continue the design"; "review draft API schema (10 min) → confirm against test results → refine if needed."
- **Do not carry completed work:** Work that reached Its DoD (Definition of Done) does not need a carry-over entry.
- **Do not carry blocked work as active execution:** If work is blocked by a dependency (waiting for review, customer email, environment), encode it as a conditional block or checkpoint, not as an active execution anchor.
- **If carry-over conflicts with weekly priorities, escalate or rebalance:** Do not silently displace the week's intended work to absorb old unfinished items.
- **If carry-over threatens weekly viability, flag explicitly:** Example: "Mon carry-over + Wed primary anchor both require deep focus. Confidence: medium. Escalation trigger: if Mon review blocked beyond 24h."

---

## 13. Reconstruction Rules

- **Reconstruct from Daily evidence first:** What do the Daily files actually say happened?
- **State uncertainty when evidence is incomplete:** If Wed Daily is missing, write "(Wed execution partial — inferred from Thu notes)."
- **Do not invent outcomes:** If Daily files don't describe an artifact, don't assume it was produced. Write: "artifact status unclear from Daily."
- **Do not rewrite messy weeks into ideal weeks:** If the week had blockers, spillover, restarts — record that factually. Reconstruction is forensic, not cosmetic.
- **Prefer factual summaries over polished narratives:** Example: "Mon: Zephyr test write in progress (Dbugs write ✓, Dbus break ← spillover). Signee context reload blocked by pending customer info." — Not: "The week began with focused effort on Zephyr, though external factors affected Signee trajectory."
- **Mark low-confidence reconstructions explicitly:** If evidence is sparse, note it. Do not reconstruct with false certainty.

---

## 14. Definition of a Good Weekly Execution File

A weekly file is ready when:

- **The week has one coherent center of gravity:** You can state it in one sentence.
- **Outcomes are believable:** They are not aspirational; they map to realistic work distribution.
- **Daily planning can inherit cleanly:** A daily planner reads the weekly file and knows exactly which anchor to follow and what the weekly expectation is.
- **Dependency handling is explicit:** Blocked work is marked conditional, with unblock conditions stated.
- **Carry-over is concrete:** Every unfinished item has an exact next step and a receiving day.
- **Workload is realistic:** The week is not overloaded with too many projects or too much evening ambition.
- **The file supports execution, not documentation:** Reading it shortens planning, not lengthens it.
- **If reconstruction mode:** Uncertainties are stated; no fake precision.

---

## 15. Standard Checklist

Copy this checklist for each weekly generation session:

```
### Weekly Generation Checklist – <WEEK_NAME> (prepared <DATE>)

**Source reading:**
- [ ] Month file read (priority/commitment for this week identified)
- [ ] Previous week file read (if exists; hand-off understood)
- [ ] Recent Daily files scanned (energy patterns, blockers, execution style calibrated)
- [ ] Project state files reviewed if relevant
- [ ] Mode identified: A (New) / B (Reconstruction) / C (Rebalance)

**Focus and outcomes:**
- [ ] Weekly focus identified (one-sentence coherence test passed)
- [ ] Primary anchor selected (singular; 1–2 projects only)
- [ ] Secondary anchor selected OR deferred with reason
- [ ] Primary outcome defined (artifact-oriented)
- [ ] Secondary outcome defined (if valid) / deferred (if not)

**Carry-over:**
- [ ] Unfinished work from previous week identified
- [ ] Carry-over rewritten as exact next entry points
- [ ] Trivial carry-over dropped explicitly
- [ ] Blocked work marked conditional (not active)
- [ ] Carrying-over saturation checked (receiving days not overloaded?)

**Dependencies:**
- [ ] Blocking items identified and conditions stated
- [ ] Unblock timing estimated
- [ ] Conditional blocks written with fallback actions
- [ ] Escalation risk assessed (yes/no; if yes, why?)

**Daily anchor map:**
- [ ] Mon–Fri Primary Anchors assigned
- [ ] Secondary anchors (if any) assigned to appropriate days
- [ ] Max-2-project rule verified (no hidden third project spread)
- [ ] Office hours vs. evening domain separation respected
- [ ] Work types (Structured Execution, Synthesis, Integration) assigned
- [ ] Artifact direction per day clear

**Energy and capacity:**
- [ ] Expected energy pattern for week documented
- [ ] Evening capacity per day set (1×M / 2×S / S-only / none)
- [ ] Weekday evening scope conservative (no L-tasks)
- [ ] Energy dips (known patterns) acknowledged

**Consistency:**
- [ ] Weekly outcomes aligned with monthly direction (no contradiction)
- [ ] Daily map realistic given energy and workspace
- [ ] Carry-over load distributed fairly across days
- [ ] Dependency handling explicit
- [ ] All sections of weekly file filled appropriately for mode

**Reconstruction notes (if Mode B):**
- [ ] Daily evidence read completely
- [ ] Uncertainty explicitly marked
- [ ] No invented outcomes
- [ ] Factual execution summary written (not prescriptive)

**File:**
- [ ] Weekly Execution file created from template (if absent)
- [ ] All sections filled: header, context, outcomes, missions, constraints, commitments, risks
- [ ] Daily anchor map completed and tested against workspace rules
- [ ] Report produced

**Sign-off:**
- [ ] Procedure followed as specified
- [ ] No shortcuts taken
- [ ] File ready for daily planning inheritance
```

---

## 16. Reusable Execution Template

Use this command block to run weekly generation. Replace all placeholders before submitting.

```
TASK: Generate or update Weekly Execution file for <WEEK_NAME>

Procedure reference: 01_OS/04_OPERATIONS/WEEKLY_CONTROL/GENERATE_WEEKLY_EXECUTION.md
Mode: A (New) / B (Reconstruction) / C (Rebalance)

Inputs:
- MONTH_FILE: <path to month file, e.g. 03_PLANNING/02_MONTH/2026-03_March.md>
- PREVIOUS_WEEK_FILE: <path to previous week file, e.g. 03_PLANNING/03_WEEK/2026-W10_Execution.md — or N/A if Mode A startup>
- CARRY_OVER_SUMMARY: <summary of unfinished items from previous week, or N/A>
- DAILY_FILES: <list recent Daily files: 03_PLANNING/03_WEEK/2026-03-10_Daily.md, 2026-03-11_Daily.md, … — or folder path>
- PROJECT_STATE_FILES: <path to project files if relevant, e.g. 08_PROJECT_CONTEXT/Zephyr_CONTEXT.md — or SKIP>
- ANCHOR_TRACKING_FILE: <path or section reference, e.g. MONTH_FILE §ANCHOR_LOAD — or SKIP>
- WEEKLY_TEMPLATE_FILE: 05_TEMPLATES/TEMPLATE_Week_Final.md
- TARGET_WEEK_NAME: <YYYY-Www format, e.g. 2026-W11>
- TARGET_WEEK_RANGE: <date range, e.g. March 16–22, 2026>
- TARGET_WEEK_FILE: <output path, e.g. 03_PLANNING/03_WEEK/2026-W11_Execution.md OR 2026-W11_WeekPlan.md>

Instructions:
1. Follow §9 (Data Collection) completely. Do not skip data gathering.
2. Follow the generation procedure exactly as defined in §10 (Steps 1–10).
3. Apply anchor rules from §11 without exception.
4. Apply carry-over rules from §12 without exception.
5. If Mode B (Reconstruction): follow §13 reconstruction rules strictly. State uncertainty.
6. If Mode C (Rebalance): preserve existing weekly structure while updating sections.
7. Run consistency check (§10 Step 9) before finalizing.
8. Produce report as specified in §10 Step 10.
9. Commit with message:
   "gen: weekly execution <WEEK_NAME> via <MODE> — <single-sentence focus description>"
   Example: "gen: weekly execution 2026-W11 via Mode A — scope freeze response + Signee team plan"
```

---

> **Procedure version:** 1.0  
> **Created:** 2026-03-15  
> **Location:** `01_OS/04_OPERATIONS/WEEKLY_CONTROL/GENERATE_WEEKLY_EXECUTION.md`  
> **Periodic reuse trigger:** Once per week (planning window)  
> **Next review trigger:** When weekly file structure changes OR when major operational pattern shift occurs
