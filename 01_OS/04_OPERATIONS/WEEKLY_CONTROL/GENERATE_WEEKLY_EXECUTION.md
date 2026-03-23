# GENERATE_WEEKLY_EXECUTION — Weekly Execution File Generation Procedure

> **Type:** Operating Procedure  
> **Layer:** OS / Operations  
> **Scope:** Monthly direction + execution reality → Weekly Execution file  
> **Prerequisite:** WeekPlan must exist and be accessible (created by GENERATE_WEEKPLAN)  
> **Reuse:** Run once per week, typically at week start, OR on-demand for reconstruction/rebalance  
> **Maintained by:** Agent 2 (file reads/writes + data collection) + Agent 1 (escalation decisions only)  
> **Related:** [`GENERATE_WEEKPLAN.md`](GENERATE_WEEKPLAN.md) (weekly planning) | [`WEEKLY_REBALANCE.md`](WEEKLY_REBALANCE.md) (mid-week correction) | [`WEEK_CLOSEOUT.md`](WEEK_CLOSEOUT.md) (week-end closure) | [`INTEGRATE_DAILY.md`](../DAILY_INTEGRATION/INTEGRATE_DAILY.md) | [`PREPARE_NEXT_DAILY.md`](../DAILY_INTEGRATION/PREPARE_NEXT_DAILY.md)

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
- [11.5. Drift Detection Layer: Design & Integration](#115-drift-detection-layer-design--integration)
- [12. Carry-over Rules](#12-carry-over-rules)
- [13. Reconstruction Rules](#13-reconstruction-rules)
- [14. Definition of a Good Weekly Execution File](#14-definition-of-a-good-weekly-execution-file)
- [15. Standard Checklist](#15-standard-checklist)
- [16. Reusable Execution Template](#16-reusable-execution-template)

---

## 1. Purpose

**What this procedure does:**

GENERATE_WEEKLY_EXECUTION is an **execution compiler**, not a planner.

It takes an already-approved WeekPlan (produced by GENERATE_WEEKPLAN) and compiles it into an executable weekly structure that daily files can inherit from cleanly.

**Anti-Regression Constraint (CRITICAL for Copilot):**

> **NEVER assume the Weekly plan assumptions are still valid after execution.**
> 
> Before generating the next week's execution framework, verify:
> 1. Has WEEK_CLOSEOUT completed? ✓
> 2. Has Execution Integrity Check been performed (Step 3.5)? ✓ 
> 3. Are there drift classifications (Type A/B/C)? If YES → review
> 4. Has UPDATE_PROJECT_CONTEXT run and refreshed context? ✓
> 5. Did any carry-over loop detection trigger (>1 repeat)? If YES → investigate blocker
>
> If any of these are incomplete or reveal drift, do NOT blindly compile the WeekPlan into next week's execution frame. The assumptions are stale. Either rebalance the current week or escalate for replanning.

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

### Mode A — Execution Baseline Generation

**Use when:** WeekPlan already exists; you are compiling it into an operational weekly execution frame for daily planning.

**Input:** WeekPlan (primary) + recent carry-over summary + actual recent Daily files (for energy/blocker calibration).

**Output:** Complete Weekly Execution file ready for daily planning and tracking.

**Timing:** Usually Sunday planning window, immediately after WeekPlan is finalized.

**Key constraint:** Must preserve WeekPlan as source of truth. Do not regenerate weekly goals; compile them as stated. Do not re-derive capacity; inherit CAPACITY_ENGINE constraints already embedded in WeekPlan.

**Source-of-truth order for Mode A:**
1. **WeekPlan** — weekly goals, anchor hypothesis, capacity constraints (already validated by CAPACITY_ENGINE)
   - If the WeekPlan includes an **Execution Phase Breakdown** (§4.5), consume it as the scheduling unit layer. Use M-phases to assign blocks without re-decomposing scope from scratch. If a phase is still ambiguous, resolve it minimally (preserve weekly intent; do not redefine the goal).
2. **Carry-over summary** — unfinished work from previous week (what is the actual re-entry point?)
3. **Recent Daily files** — actual energy patterns, blocker reality, execution style (for realistic daily map construction)
4. **Project context files** — supporting information only; does NOT override WeekPlan direction
5. **Month file** — referenced indirectly through WeekPlan; do NOT read month directly as co-planner here

> **Why this hierarchy:** WeekPlan has already reconciled monthly direction with capacity and constraints. Weekly Execution must not reopen that negotiation. If execution uncovers a gap between WeekPlan assumption and reality (unexpected carry-over volume, energy pattern change), trigger WEEKLY_REBALANCE rather than silently adjusting here.

### Mode B — Week Reconstruction

**Use when:** A weekly execution file is missing and must be reconstructed from Daily files alone (WeekPlan may also be missing).

**Input:** Complete set of Daily files from that week + month file (if available) + project state files (optional).

**Output:** Weekly Execution file with actual day-by-day execution summary + reconstructed weekly anchor structure (if WeekPlan is unavailable).

**Timing:** Usually after week ends; may happen days or weeks later.

**Key constraint:** Reconstruction is forensic, not prescriptive. State uncertainty explicitly. Do not invent clean history. Make clear what is evidenced vs. inferred.

### Mode C — Execution Rebalance Update

**Use when:** The week is active, but actual execution reality diverged from weekly frame enough to require controlled adjustment.

**Input:** Existing weekly execution file + mid-week execution data + new dependency/blocker information + capacity reassessment.

**Output:** Updated weekly execution file that adjusts anchor structure, rescopes secondary work, or updates daily expectations in response to new data.

**Timing:** Typically mid-week (Wed/Thu) if a major blocker or capacity change occurs.

**Key constraint:** Rebalance updates preserve WeekPlan goals unless explicitly changing scope. Update execution expectations, not strategy. Controlled adjustment, not panic revision. Escalation decision must be made before running rebalance.

### Mode D — Adaptive Replan (REAL-TIME CONTEXT SYNC + STABILITY CONTROL)

**Use when:** A mid-week STRONG Context Signal (Type B or C) is detected during daily execution (via TEMPLATE_Daily.md signal detection) and passes replan budget + cooldown constraints.

**Input:** Updated project context (from UPDATE_PROJECT_CONTEXT mid-week mode) + existing weekly execution file + signal evidence + remaining anchors + replan constraint check.

**Output:** Updated weekly execution file with reordered/adjusted remaining anchors that reflect updated context reality; ≥50% of stable anchors preserved; completed anchors unchanged.

**Timing:** Same day (if critical Type C) or next morning after Context Signal detected; goal is < 24h turnaround to allow execution to adapt.

**Key constraints:** 
- **Replan Budget:** Max 2 adaptive replans per week. If budget exhausted, escalate instead of replanning.
- **Cooldown Window:** No more than 1 replan per 24h window (exception: Type C critical blockers bypass this).
- **Partial Stability Protection:** Keep ≥ 50% of remaining uncompleted anchors unchanged. Only reorder/replace anchors directly affected by signal.
- **Execution Commitment:** Do NOT mid-session interrupt ongoing anchor. Replan applies to remaining blocks/days after current block closes.
- **Integration:** Link all changes to signal evidence (date, signal type, root cause) for traceability.

**Difference from Mode C:**
- Mode C (Rebalance): Mid-week, planned check-in; no budget/cooldown limits; comprehensive rebalance
- Mode D (Adaptive): Triggered by specific Context Signal; budget-limited (max 2/week); cooldown-gated (24h); partial stability protected (keep 50%+)

**Replan Budget Tracking (within weekly file):**
Add section at top of weekly file:
```
## Adaptive Replan Log (W##)
- Replan 1: [Tue date] — Signal: [Type B/C, description] — Budget: 1/2 used
- Replan 2: [Thu date] — Signal: [Type B/C, description] — Budget: 2/2 used (exceeds limit if third signal)
```

---

All four modes preserve the same **Weekly Execution file structure**. Mode determines which sections are filled from what sources, and how much existing execution is preserved vs. adjusted.

---

## 4. Prerequisites

All of these must be true before running this procedure:

- [ ] **WeekPlan file exists and is complete** (created by GENERATE_WEEKPLAN for the target week)
- [ ] WeekPlan Context section is finalized (monthly direction + carry-over integrated)
- [ ] WeekPlan Goals are stated (Primary + Secondary, with effort estimates)
- [ ] WeekPlan Capacity & Constraints section is complete (CAPACITY_ENGINE-derived, with pool allocations)
- [ ] Carry-over summary from previous week is available (from WEEK_CLOSEOUT output)
- [ ] Recent Daily files are available and readable (last 2–4 days of previous week, for energy calibration)
- [ ] Project context files are accessible (if referenced in WeekPlan as dependencies)
- [ ] Weekly template or canonical weekly structure is accessible (e.g., `05_TEMPLATES/TEMPLATE_Week_Final.md`)
- [ ] Target week date range is known (YYYY-Www format + calendar dates)
- [ ] Mode is identified: A (Execution Baseline) / B (Reconstruction) / C (Rebalance)

For Mode A, WeekPlan MUST exist. For Modes B & C, follow the specific prerequisites in the mode definitions. Do not proceed on incomplete information.

---

## 5. Inputs

| Input | Description | Required? | Source | Role |
|---|---|---|---|---|
| `<WEEKPLAN_FILE>` | Primary input: weekly goals, anchor hypothesis, capacity constraints (CAPACITY_ENGINE-derived) | **Required** | `03_PLANNING/03_WEEK/2026-Www_WeekPlan.md` | Source of truth; defines what to compile |
| `<CARRY_OVER_SUMMARY>` | Unfinished meaningful work from previous week with re-entry needs | Required | WEEK_CLOSEOUT output from W##-1 Shutdown | Defines entry points for daily map |
| `<RECENT_DAILY_FILES>` | Daily files from last 2–4 days of previous week | Required | `03_PLANNING/03_WEEK/YYYY-MM-DD_Daily.md` | Calibrates energy patterns, execution cadence |
| `<PROJECT_STATE_FILES>` | Project context files (if referenced in WeekPlan constraints) | Conditional | `08_PROJECT_CONTEXT/` | Supporting context only; does NOT override WeekPlan |
| `<MONTH_FILE>` | Month file (referenced indirectly through WeekPlan) | Reference only | `03_PLANNING/02_MONTH/YYYY-MM_Month.md` | Context only; do NOT read as co-planner |
| `<ANCHOR_TRACKING_FILE>` | Anchor load tracking or execution history (optional) | Optional | Section in WeekPlan or legacy tracking | Validates daily map realism |
| `<PREVIOUS_EXECUTION_FILE>` | Previous week's execution file (Mode B/C only) | Conditional | `03_PLANNING/03_WEEK/2026-W##-W#_Execution.md` | Reconstruction or rebalance context |
| `<WEEKLY_TEMPLATE_FILE>` | Canonical weekly execution structure template | Required | `05_TEMPLATES/TEMPLATE_Week_Final.md` | Output format |
| `<TARGET_WEEK_NAME>` | Week identifier in YYYY-Www format | Required | User input | Output naming |
| `<DATE_RANGE>` | Week date range (e.g., March 16–22, 2026) | Required | User input | Output header |
| `<MODE>` | Generation mode: A (Baseline) / B (Reconstruction) / C (Rebalance) | Required | User input | Determines procedure path |

**Key input hierarchy for Mode A:**  
When generating a new week's execution baseline, the WeekPlan is your primary source. Do not re-read the month file directly. Do not re-derive capacity. Compile WeekPlan as stated.

---

## 6. Outputs

**Primary output: Weekly Execution file** at `03_PLANNING/03_WEEK/Wxx/2026-Wxx_Execution.md`

**Important naming and placement rules:**
- **Weekly Plan:** `03_PLANNING/03_WEEK/Wxx/2026-Wxx_WeekPlan.md` (produced by GENERATE_WEEKPLAN)
- **Weekly Execution:** `03_PLANNING/03_WEEK/Wxx/2026-Wxx_Execution.md` (produced by GENERATE_WEEKLY_EXECUTION)
- **Daily files:** `03_PLANNING/04_DAY/Wxx/YYYY-MM-DD_Daily.md` (produced by GENERATE_DAILY; one per execution day)

> **PLACEMENT RULE (CRITICAL):** Weekly files (WeekPlan + Execution) MUST be created in `03_PLANNING/03_WEEK/Wxx/` subfolders organized by week. Daily files MUST be created in `03_PLANNING/04_DAY/Wxx/` subfolders organized by week. Mixing layers causes folder bloat and execution confusion. Do NOT place daily files under `03_WEEK/` folder.

These are separate files with distinct purposes. Do NOT overwrite or rename one for the other.

**Outputs from GENERATE_WEEKLY_EXECUTION (must include all 7 operational layers):**

1. **Phase Normalization Layer** — Every mission + daily anchor: SIZE (XS/S/M/L), Ambiguity (0–5), energy fit, dependency type
2. **Artifact Operationalization Layer** — Every anchor specifies concrete artifact (doc name, checklist, commit, PR, log, diagram) — NO vague language
3. **Start Anchor Layer** — Every deep-work anchor exposes one ≤15p first step (verb-starting action that creates immediate motion)
4. **Dependency & Escalation Layer** — Explicit blocking graph: which phases depend on which prior phases; fallback actions named
5. **Phase-Level DoD Layer** — Per phase: DONE conditions + daily stop conditions + carry-over triggers (safe-to-stop markers)
6. **Load Classification Layer** — Load split: committed (mandatory completion) / contingent (conditional on prior) / overhead (structural non-execution)
7. **Daily Inheritance Contract** — Strict handoff: inherited anchor + artifact + start step + stop condition + dependency note + fallback

**Additional standard outputs:**
- Execution framework (day-by-day distribution with work types)
- Carry-over entry points (exact re-entry mode + receiving day)
- Dependency sequences (unblock conditions + cascading actions)
- Execution tracker section (if active week)
- If Mode B: actual execution summary with uncertainty markers
- Generation report (construction methodology + assumptions)

---

## 7. Source-of-Truth Hierarchy

When information sources conflict, resolve in this rank order:

### For Execution Baseline Generation (Mode A)

1. **WeekPlan** — weekly goals, anchor hypothesis, capacity constraints (already CAPACITY_ENGINE-validated)
2. **Carry-over summary from previous week** — where execution actually stopped; concrete re-entry points
3. **Recent Daily files (last 3–4 days of previous week)** — actual energy patterns, blocker reality, execution cadence (used to tune daily distribution)
4. **Project state files** — supporting context; does NOT override WeekPlan
5. **Month file** — referenced indirectly through WeekPlan only; do NOT read as co-planner
6. **Anchor tracking history** — contextual; helps validate daily map is realistic

**Inheritance rule:** WeekPlan has already reconciled monthly direction with capacity and constraints via CAPACITY_ENGINE. Generate Weekly Execution does NOT reopen that negotiation. Compile WeekPlan as stated. If execution reveals a gap (unexpected carry-over volume, unavailable evening blocks, energy shifted), escalate to WEEKLY_REBALANCE instead of silently adjusting here.

### For Week Reconstruction (Mode B)

1. **Daily files from that week** — factual ground truth of what actually happened
2. **WeekPlan (if it exists)** — what was planned; compare against actual
3. **Month file (from that time period)** — what the month intended
4. **Project state files** — project context during that week
5. **Anchor tracking if available** — contextual; helpful but not required
6. **Inferred weekly structure only where Daily evidence is clear** — never invent history

**Reconstruction rule:** Let daily evidence speak first. If Daily files are missing, state explicitly. Do not create fake weekly structure to fill gaps. Prefer factual summary over polished narrative.

### For Execution Rebalance Update (Mode C)

1. **Existing weekly execution file** — preserve structure and coherence
2. **New mid-week execution data** — reality that triggered rebalance
3. **New dependency/blocker information** — changed conditions
4. **Capacity reassessment** — new energy/load evidence
5. **WeekPlan goals** — preserved unless explicit rescope decision made
6. **Month direction** — does not change; rebalance adjusts execution frame to serve month better, not replace it

**Rebalance rule:** Update execution expectations and daily distribution to match new reality. Rescope secondary work or adjust daily load if needed. Preserve WeekPlan goals and monthly alignment unless escalation explicitly changes them.

---

## 8. Dual-Pool Execution Rules

Weekly execution must enforce strict pool separation inherited from CAPACITY_ENGINE. These rules are not optional.

### Pool A — Office Hours (Fixed)

**What belongs in Pool A:**
- Zephyr project ONLY (TYPE A / KTLO responsibilities)
- Fixed office hours only (8:00–17:30, Mon–Fri)
- No RobotOS or Signee work here

**Execution constraint:**
- Office hours daily anchor must be Zephyr-only
- Do NOT place RobotOS or Signee work in office-hour blocks
- If Zephyr office hours are unavailable (vacation, meeting override), reduce Zephyr allocation; do NOT substitute with RobotOS/Signee in office hours

**Validation rule for daily anchor map:**
- Every office-hours slot must have **Zephyr only** in the Primary or Secondary anchor column
- If a day shows office hours anchored to RobotOS or Signee, it is an error. Fix before finalizing.

### Pool B — Personal Deep-Work (Evenings + Five Weekend Slots)

**What belongs in Pool B:**
- RobotOS project (TYPE B architecture/implementation)
- Signee project (TYPE C specification/coordination)
- Weekday evenings: Mon–Fri 19:30–21:30 (2h per evening, baseline ~10h/week gross; net derived from anchor)
- **Slot 1 — Saturday daytime: full project execution capacity** — not a mini-block or overflow slot; declare planned project hours in the week plan
- **Slot 2 — Saturday evening: PROTECTED** — either OFF (required rest) or OPEN (only if explicitly planned in weekly plan); declare which
- **Slot 3 — Sunday morning: WEEK_CLOSEOUT + review + next-week seed** (~2–3h structural overhead; **NOT execution capacity**; included in total weekly load)
- **Slot 4 — Sunday afternoon: full project execution capacity** — always a real capacity source; declare planned project hours or explicitly state "not used this week" as instance decision
- **Slot 5 — Sunday evening: PROTECTED** — either OFF (required rest) or OPEN (only if explicitly planned in weekly plan); declare which; exactly ONE of {Sat evening, Sun evening} must be OFF per R10

**Execution constraint:**
- No office hours here (office hours = Pool A only)
- Weekday evening scope must be conservative (no L-sized tasks; default 1×M or 2×S capacity)
- Thursday evening: plan lighter work (S-only or optional); account for Thu energy dip — this is a structural recurring reduction, not a rare exception; do NOT treat as a calendar anomaly
- Exactly one weekend evening is OFF (protected rest); the week plan must name which (Sat or Sun); the other is default-rest and may be opened only if explicitly named in the weekly plan
- Sunday morning: review / closeout / planning block — **not execution capacity**; consumed by WEEK_CLOSEOUT + next-week seed; declare as review-capacity, not personal project time
- **Anti-conflation:** Do NOT conflate Sunday afternoon (execution slot Slot 4) with Sunday evening (rest/open decision Slot 5); both must be declared independently

**Validation rule for daily anchor map (SLOT-BASED):**
- Weekday evening slots must have RobotOS or Signee (not Zephyr)
- **Weekend slots must be individually validated:**
  - Sat daytime (Slot 1): if used, must show time allocation
  - Sat evening (Slot 2): must declare OFF or OPEN
  - Sun morning (Slot 3): must declare as review-capacity (~2–3h), not execution
  - Sun afternoon (Slot 4): must declare time allocation or "not used" with justification
  - Sun evening (Slot 5): must declare OFF or OPEN; must be opposite of Sat evening (R10 exactly-one-OFF rule)
- Forbidden: vague language like "Sunday used/unused" or "weekend optional" — must specify WHICH slot and its value
- If all five slots are not declared in the weekly plan, the execution plan is incomplete

### Pool Separation Enforcement

**No cross-pool contamination rules:**

1. **Office hours cannot contain RobotOS/Signee work** — even if office capacity is available, personal projects do NOT use it
2. **Personal evenings cannot contain Zephyr work** — Zephyr is office-only; if office is unavailable, Zephyr itself defers, doesn't move to evening
3. **Daily anchor map must show clear pool boundaries** — one column for office (Zephyr), one column for evening/personal (RobotOS/Signee)
4. **Mixed anchors on the same day are OK** (e.g., "Office: Zephyr + Evening: RobotOS"), but each project stays in its pool

**Validation checklist before finalizing weekly execution:**
- [ ] Office-hours anchors contain Zephyr only
- [ ] Evening anchors contain RobotOS or Signee only
- [ ] No RobotOS/Signee appear in office hours
- [ ] No Zephyr appears in evenings
- [ ] No third project (beyond the three active ones) is hidden in the daily distribution
- [ ] Evening scope is conservative (no L-tasks on weekday evenings)
- [ ] **Weekend slots ALL DECLARED (slot-based, not day-based):**
  - [ ] Saturday daytime (Slot 1): declared with time value or 0h
  - [ ] Saturday evening (Slot 2): declared as OFF or OPEN
  - [ ] Sunday morning (Slot 3): declared as review/overhead ~2–3h
  - [ ] Sunday afternoon (Slot 4): declared with time value or 0h with math proof
  - [ ] Sunday evening (Slot 5): declared as OFF or OPEN
  - [ ] Exactly ONE of {Sat evening, Sun evening} is OFF; other is default-rest or OPEN
- [ ] No vague weekend language ("Sunday used/unused", "weekend optional") — all slots explicitly value-named
- [ ] No conflation of Sun afternoon (Slot 4, execution) with Sun evening (Slot 5, rest decision)
- [ ] No conflation of Sat daytime (Slot 1, execution) with Sat evening (Slot 2, rest decision)
  - [ ] Exactly one weekend evening is protected rest (OFF); if second evening is opened it must be explicitly named in the weekly plan; TYPE B/C execution only on the opened evening
  - [ ] Sunday morning declared as review overhead (not execution); included in total weekly load

**Distribution Heuristic Checks (Warning-Level; Non-Blocking):**
- [ ] If weekend execution ≥3h: Was Sat + Sun distribution evaluated per R11-D? Document choice if not split
- [ ] If Sat (Slot 1) ≥3h AND Sun afternoon (Slot 4) = 0h: Is this intentional? State justification or fatigue risk
- [ ] If Saturday is both pre-allocated (primary block) and also treated as spillover buffer: Are these roles explicitly separated and capacities stated separately?

---

## 8.5 Key Semantic Layer: Strategic Goal Rank vs Weekly Execution Role

This section clarifies a **critical semantic distinction** that prevents confusion between WeekPlan goal importance and WeekPlan execution urgency.

### Strategic Goal Rank (from WeekPlan §2)

**Definition:** Roadmap / stakeholder / multi-week importance of a goal.

- Determined during planning phase (GENERATE_WEEKPLAN)
- Examples: Goal 1 = high strategic value (professor requires architecture clarity); Goal 2 = critical infrastructure (required for W12 platform)
- NOT week-specific; stable across multiple weeks
- Indicates value if advanced, not urgency this week

### Weekly Execution Role (from WeekExecution §1 Success Conditions)

**Definition:** This week's delivery role for a goal—determined by dependency criticality, deadline urgency, and blocker status.

Allowed values:
- **PRIMARY** → owns hard gate or unblocking condition; no other goal can proceed without it; primary success condition for the week
- **SECONDARY** → depends on primary completion; secondary success condition; contingent delivery
- **SUPPORT** → independent parallel progress; non-critical-path outcome; does not block other work

### Key Principle: Strategic Rank ≠ Weekly Execution Role

**A higher strategic goal may become SECONDARY or SUPPORT in a specific week if:**
- Another goal owns a hard-gate blocker (blocks W12 platform integration, requires Wed deadline, etc.)
- This goal is independent (has no dependency connection to critical path)
- This goal's execution risk is lower than critical-path alternatives

**Why this matters:** Without explicit mapping, readers conflate "Goal 1" (high strategic value) with "Primary outcome" (this week's critical path). Confusion results: "Why is Goal 1 support?" (Answer: It's strategically important but not execution-blocking this week.)

### Goal-to-Execution-Role Mapping (Required in Weekly Summary §1)

Every Weekly Execution file MUST include a compact listing:

**Format (minimal, one line per goal):**
```
- Goal 1 (RobotOS) → SUPPORT: strategic architecture pillar, but independent this week; no hard gate
- Goal 2 (Zephyr) → PRIMARY + SECONDARY: owns Wed hard gate (primary) + contingent RAM expansion (secondary)  
- Goal 3 (Signee) → SUPPORT: independent parallel progress; specification work blocked by neither other goal
```

**Purpose:** Readers scan this once and immediately understand why goal rank may differ from execution role.

**Validation:** If a goal's execution role differs from its "importance" feel, explain briefly (2–3 words max: "independent", "no hard gate", "medium risk", etc.).

### Readability Guard (Mandatory for All Generated Output)

**Output Quality Standard:** All generated execution artifacts must conform to scan-friendly formatting rules to ensure clarity and executability.

### Pre-Finalization Readability Checklist
- [ ] No body paragraph exceeds 4 lines
- [ ] Multi-idea sections split into separate bullets/sub-blocks
- [ ] All numbers, hour allocations, slot declarations, and rules are formatted as bullets/tables/labeled blocks (not long prose)
- [ ] Scan-friendly structure: short intro + bullet breakdown + explicit labels ("Anchor", "Capacity", "Constraint", "Risk")
- [ ] No walls-of-text; synthesis broken into 2–4 short bullets
- [ ] Daily anchor descriptions are specific and actionable (not generic)
- [ ] Exit conditions are binary and observable (not subjective)
- [ ] All original meaning preserved

---

## 9. Planning Boundaries

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

- **Re-derive capacity from scratch** — capacity is already in WeekPlan via CAPACITY_ENGINE; inherit it
- **Regenerate weekly goals** — goals are in WeekPlan; compile them, don't replace them
- **Read Month as co-planner** — Month direction is already in WeekPlan; do NOT negotiate it here
- **Silently absorb unplanned monthly changes** — escalate instead
- **Violate pool separation** — Office hours = Zephyr only; Personal evenings = RobotOS/Signee only (see §8)
- **Place RobotOS/Signee in office hours** — they are personal projects; office is Pool A only
- **Place Zephyr in evenings** — it is office-only; if office is unavailable, Zephyr defers, it doesn't move
- **Overload the week with > 2 active projects in execution** — three exist but not all three execute at same intensity weekly
- **Pretend blocked work is executable** — encode all conditions explicitly
- **Create fake certainty during reconstruction** — state uncertainty where evidence is missing
- **Turn the weekly file into narrative journaling** — keep it operational (execution map, not prose)
- **Insert new strategic commitments** — those bypass month planning; escalate instead
- **Distribute unfinished work across all 5 days** — be realistic about which days can absorb carry-over
- **Absorb systemic overload silently** — if week is overloaded, flag rebalance risk or trigger WEEKLY_REBALANCE
- **Ignore energy dips** — if Thu brings lower capacity, plan lighter; don't pretend it's a normal work day
- **Replace WEEKLY_REBALANCE with execution generation** — if real drift occurs mid-week, rebalance instead of re-generating

**When weekly frame conflicts with WeekPlan or monthly strategy:** Escalate instead of silently hiding it. Record the incompatibility in the weekly file and recommend WEEKLY_REBALANCE or GENERATE_WEEKPLAN re-run.

---

## Non-Goals — What This Procedure Does NOT Do

To be clear on scope, GENERATE_WEEKLY_EXECUTION explicitly does NOT:

- **Create new weekly goals** (that is GENERATE_WEEKPLAN's job)
- **Change capacity model or constraints** (those are in WeekPlan via CAPACITY_ENGINE)
- **Re-allocate projects across pools** (Pool A / Pool B separation is fixed)
- **Absorb unresolved strategic conflict silently** (escalate instead)
- **Substitute for WEEKLY_REBALANCE** (when drift is real, rebalance instead)
- **Turn execution generation into another planning phase** (you are compiling an existing plan, not planning)
- **Renegotiate monthly direction** (that is baked into the inherited WeekPlan)
- **Carry over indefinitely blocked work as active** (block should be marked conditional, not execution entry point)
- **Create aspirational workload** (be realistic about what fits)
- **Prevent daily generation from being inheritance:** Weekly Execution must produce clear enough anchors (with First Strike, Exit Condition, Linked Weekly Goal metadata) that daily file creation is pure inheritance, not re-planning. If daily files require re-planning, weekly execution was underspecified.

If you find yourself doing any of these, stop and use the right procedure instead.

---

## 9. Data to Collect Before Writing

**Do not write anything until you have collected all of the following:**

### Week identity and scope

- [ ] Week name (format: YYYY-Www, e.g., 2026-W11)
- [ ] Date range (e.g., March 16–22, 2026)
- [ ] Mode: A (Execution Baseline) / B (Reconstruction) / C (Rebalance)

### WeekPlan (PRIMARY INPUT)

- [ ] WeekPlan file read in full (created by GENERATE_WEEKPLAN)
- [ ] Weekly Goals section understood (Primary + Secondary outcomes)
- [ ] Capacity & Constraints section reviewed (pool allocation, evening scope, CAPACITY_ENGINE rules)
- [ ] Anchor Hypothesis section assimilated (which projects carry weekly weight)
- [ ] Known Risks & Blockers section noted (what could block execution)

### Carry-over from previous week

- [ ] Carry-over summary read (from WEEK_CLOSEOUT output)
- [ ] Unfinished work identified with re-entry mode needed (Quick / Analytical / Fragile)
- [ ] Each carry-over item classified: critical (must this week) vs. important (should) vs. defer
- [ ] Carry-over load distributed fairly across receiving days (don't overload any one day)
- [ ] Blocked work marked as conditional (not active entry point)
- [ ] Drop list reviewed (what is no longer relevant carries forward)

### Recent execution reality (energy calibration)

- [ ] Recent Daily files scanned (last 3–5 days of previous week)
- [ ] Recent energy level observations recorded (full capacity days vs. dips)
- [ ] Major blockers or unexpected issues noted (context for current week)
- [ ] Execution cadence and style observed (how did the previous week actually feel?)
- [ ] Energy dips confirmed (Thu dip? Evening blocks real? Saturday/Sunday rest observed?)

### Active projects and dependencies

- [ ] All active projects listed for this week
- [ ] For each project: TYPE (A/B/C), pool (Office/Personal), estimated load
- [ ] All blocking dependencies identified (external: reviews, approvals, environment; internal: A→B sequencing)
- [ ] Unblock conditions and timing estimated (when will blockers clear?)
- [ ] Unblock consequences determined (what executes next when block clears?)

### Anchor structure and pool validation

- [ ] WeekPlan's primary anchor understood
- [ ] Secondary anchor (if any) in WeekPlan identified
- [ ] Anchor coherence validated: can explain week in one sentence?
- [ ] Pool validation: Office anchor contains Zephyr only? Personal anchors contain RobotOS/Signee?
- [ ] Project spread checked: no hidden third project seeking execution time?

### Capacity and energy patterns

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

**For Mode A (Execution Baseline):**
1. Read the WeekPlan file thoroughly in its entirety (weekly goals, capacity, anchor hypothesis, carry-over integration, risks).
2. Extract carry-over from WeekPlan's Carry-over Integration section (already consolidated; understand re-entry needs).
3. Scan recent Daily files (last 3–4 days of previous week) to calibrate actual energy patterns, blocker reality, and execution cadence.
4. Reference CAPACITY_ENGINE constraints already embedded in WeekPlan (do NOT re-derive capacity here).
5. Review project context files only if they materially affect weekly priorities and are flagged in WeekPlan (e.g., "deployment blocker").
6. Do NOT re-read the month file as if it is a co-planner; month direction is already in WeekPlan (inherited from GENERATE_WEEKPLAN).

**For Mode B (Reconstruction):**
1. Read all Daily files from the target week (every day available).
2. If WeekPlan exists from that week, read it to see what was planned; compare against actual.
3. Read the month file from that time period to understand what the month intended.
4. Scan project state files from that week if available.
5. Do NOT read Daily files from other weeks unless they provide missing context.
6. Accept incomplete data. Mark uncertainty explicitly if daily files are missing.

**For Mode C (Rebalance):**
1. Read the existing weekly execution file in full.
2. Read the mid-week (Tue/Wed) Daily file(s) that triggered the rebalance.
3. Identify what changed: blocker, new dependency, capacity shift, energy change.
4. Read month file only to confirm weekly frame is still aligned with monthly intent.
5. Do not rewrite unchallenged sections.

---

### Step 2 — Determine Weekly Focus (with SIZE & Ambiguity Normalization)

1. Identify the **single dominant activity** for the week:
   - One project taking 60–70% of weekly effort
   - One coherent phase (e.g., "merge testing," "customer presentation," "architecture consolidation")
   - **SIZE check:** Is this M (40–90 min focus blocks) or L (4+ hour continuous work)? If L, must decompose into M+M+M phases
   - **Ambiguity check:** Is this 0–2 (clear path) or 3–5 (unclear/blocking)? If 5, flag as Spike, not execution
   - One clear outcome that Friday could verify

2. Ask: "If I had to answer 'what is this week about?' in one sentence, what would it be?"

3. **For each mission (primary + secondary), evaluate SIZE and Ambiguity:**
```
Mission / SIZE (XS/S/M/L) / Ambiguity (0-5) / Dependency (Hard/Conditional/Independent/Deferred)
```
   - ⚠️ **SIZE Rules (prefer M; allow others under conditions):**
     - **M preferred:** 45–90 min focused blocks (default execution unit)
     - **XS/S allowed for:** setup, verify, review, unblock, carry-over closeout (NOT primary mission work)
     - **L allowed ONLY if:** has internal checkpoint, produces stop-safe intermediate artifact, max 4h session (then MUST pause, verify, decide re-entry)
     - **XL forbidden:** no raw 8+ hour unbroken execution blocks as single anchor
   - ⚠️ **Ambiguity Rules (honest scoring, not cosmetic):**
     - **0–2 (clear/bounded):** Standard execution; use any energy day
     - **3 (moderate uncertainty):** Allowed IF placed on ONLY high-energy day (Tue Mon) AND has explicit escalation/fallback note AND evening work keeps Ambiguity ≤2
     - **≥4 (high uncertainty):** SPIKE (not execution); requires decomposition or explicit sandbox (e.g., "bounded research spike, results in decision by Wed")
     - **5 (unexplored):** NOT schedulable as execution anchor; must be escalated to planning layer

4. Identify optional **secondary anchor** only if:
   - It genuinely fits available time domain (evening or flexible time)
   - It does not compete cognitively with primary anchor
   - It is truly independent (not blocked by same dependency as primary)
   - SIZE is M or smaller (NO L secondary anchors; XS/S OK for setup/verify/review blocks)
   - Ambiguity ≤ 2 (no Ambiguity 3+ on secondary; reserve uncertainty budget for primary)
   - You can imagine one daily block (60–90 min) sufficing for its weekly scope

5. If a third project wants attention, explicitly defer it to following week or flag as blocker.

6. State the full weekly focus as a one-sentence frame:
   - Example: "W10: Scope Freeze Prep — merge 3 tests to develop (M primary); deliver team plan + pptx (M+S secondary)"
   - Not: "Zephyr work, Signee work, RobotOS work" (that's project listing, not focus)

---

### Step 2.5 — Map Each Goal to Its Weekly Execution Role (REQUIRED)

**DO THIS BEFORE writing the summary.** This step explicitly connects strategic goals to their execution roles.

For each goal from WeekPlan §2 (usually 3 goals: Primary/Secondary/Tertiary):
1. Name the goal and project.
2. Assign its **execution role this week:** PRIMARY, SECONDARY, or SUPPORT.
3. State the assignment reason in 2–3 words max.

**Mapping rules:**
- If a goal has a hard-gate dependency (blocks next week, Wednesday deadline, etc.) → PRIMARY or SECONDARY (depending on whether it's the blocking path or contingent on blocker)
- If a goal is independent (no blocking dependency, can progress in parallel) → SUPPORT
- If a goal has medium/low urgency this week but high strategic value → typically SUPPORT (independent progress)
- If two goals appear equally urgent, choose the one with true blocking blocker → PRIMARY

**Example (W11)**
- Goal 1 (RobotOS) → SUPPORT: independent, no hard gate
- Goal 2 (Zephyr) → PRIMARY / SECONDARY: owns Wed blocker + contingent RAM
- Goal 3 (Signee) → SUPPORT: independent, parallel progress

**This mapping must appear in Weekly Summary §1, explicitly labeled.** (See Step 3 and Definition of Good Weekly Execution File §14).

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

### Step 5 — Build Daily Anchor Map (with Artifact Concreteness + Start Step + Stop Condition)

1. For each weekday (Mon–Fri) and weekend slots:
   - Define **Primary Anchor** (inherited from weekly primary)
   - Define optional **Secondary Anchor** only if it fits that day
   - Avoid: same anchor twice (no Mon/Tue duplication); hidden third project spread

2. **Use this required column structure (mandatory for all anchors):**
   - Day
   - Primary Anchor (project/phase)
   - Secondary Anchor (project/phase, if any)
   - **Artifact (MANDATORY — must be concrete, not vague)**
   - **Start Step (MANDATORY — ≤15 min verb-starting action)**
   - **Stop Condition (MANDATORY — binary observable state; includes minimum usable completeness)**
   - **Fallback (if primary blocks in first 15 min, what's operational plan B?)** 
   - Override Rule (if upstream dependency slips, what gets dropped/protected?)

3. **ARTIFACT OPERATIONALIZATION (MANDATORY):**

   **Forbidden language (vague, not operational):**
   - "architecture foundation"
   - "merge-ready"
   - "clarity achieved"
   - "progress"
   - "work on X"
   - "polish"

   **Required language (concrete, observable):**
   - "architecture_outline.md (1–2 pages + layer diagram)"
   - "dline_send/receive implementations complete; PR opened"
   - "test_sets.csv with capture/QR/auth rows; quality_gates.md complete"
   - "merge verification log; tests passing in develop branch"

   **Acid test for each anchor:** "If I stop here, what FILE/DOCUMENT/COMMIT/FIELD exists that I can hand to someone else?"

4. **START STEP LAYER (MANDATORY — ≤15 minutes, verb-starting):**

   Every deep-work anchor MUST expose one first action that takes ≤15 min and creates immediate motion.

   **Examples (GOOD):**
   - "Open handoff note + write 3 integration questions"
   - "Create test_env directory + stub dline_send test scaffold"
   - "List test-set headings for capture/QR/auth flows"
   - "Export architecture diagram template + sketch framework layers"

   **Examples (BAD):**
   - "Work on architecture" (too vague)
   - "Continue from Mon" (assumes context carry-over)
   - "Finish design" (no action verb, no bounded start)

5. **STOP CONDITION (MANDATORY — binary and observable, includes minimum usable state):**

   **Forbidden (subjective):**
   - "done with this"
   - "looks good"
   - "making progress"
   - "ready enough"

   **Required (binary/observable + minimum usable state):**
   - "All 3 tests passing locally + zero CI warnings" (minimum usable: tests running, failures clear)
   - "Architecture diagram exported to team/docs/architecture/ + layer labels filled in" (minimum usable: diagram exists with layers readable)
   - "Test sets spreadsheet complete with pass/fail criteria per set + blocker section noted" (minimum usable: framework exists, gaps identified)
   - "PR submitted + code review queue visible + CI started" (minimum usable: code appears in queue, review can begin)
   
   **Minimum usable state rule:** If you pause here, could the next person pick up work without re-reading your notes? If NO, stop state is incomplete.

6. Respect domain/pool rules:
   - Office hours = primary project only (no personal projects in Pool A)
   - Evening = secondary project or personal work only (no Zephyr in Pool B)
   - Do NOT allow primary project to sprawl into evening

7. **EVENING CONSERVATISM RULES (mandatory):**
   - No L-sized tasks on weekday evenings (XS/S only for evening main block)
   - Default: 1×M or 2×S capacity (not 2×M; evening is half-power relative to office)
   - **Ambiguity ≤ 2 on evenings ONLY** (no Ambiguity 3+ exploration at end of day; save uncertainty for high-energy slots)
   - If evening anchor is marked Ambiguity 3+, rewrite or escalate to different day
   - Adjust down based on energy pattern evidence

8. **DEPENDENCY VALIDATION (mandatory for all anchors):**
   - For any evening anchor marked "independent," justify WHY office blockers don't affect it; write in override column
   - If two anchors same day (office + evening): state explicitly if one is contingent on the other
   - If Thursday has contingent anchor: is Wednesday completion checkpoint documented? Is fallback named?
   - **Hidden question:** If the office anchor slips by 2h, does the evening anchor still execute? If NO → not independent
   - **For upstream-dependent anchors (Tue→Wed→Thu chains):** name what gets dropped first if Tue fails, what gets protected first

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

## 11.1 Execution Anchor Metadata Requirements

Every execution anchor compiled into the weekly file must include sufficient metadata for Daily files to inherit cleanly without re-planning.

**Required metadata for each weekly execution anchor:**

1. **Linked Weekly Goal:** The anchor must state which weekly goal (from WeekPlan §2) it serves.
   - Example: "Zephyr — Test Infrastructure Extension (serves Goal 2: Zephyr Testing Infrastructure)"
   - Do NOT leave this implicit; state it explicitly.
   - If an anchor cannot be linked to a weekly goal, do NOT execute it.

2. **First Strike:** The anchor must indicate the concrete first action to begin this work.
   - Example: "Open test file from W10; review test requirements documented in comments"
   - This is handed as a context-reset instruction to daily planning.
   - Essential for deep-work anchors (not needed for admin/support tasks).

3. **Exit Condition:** The anchor must state the concrete condition that defines completion of this work for its intended session.
   - Example: "Three test cases passing locally; test file ready for review"
   - Not vague: "finish testing" is not an exit condition.
   - Concrete artifact or state: "PR submitted", "diagram exported", "feedback captured and documented".
   - Essential for deep-work anchors.

4. **Carry-over Rule:** If this anchor might spill into the next day, the anchor must state explicitly:
   - What spills (subtask name, artifact state)
   - How it re-enters (Quick/Analytical/Fragile mode)
   - Which receiving day will absorb it
   - Example: "If test merge cannot complete Tue evening → defer to Wed morning (Quick 10-min re-entry: confirm merge state + resume from last branch)."

**Validation:**
- Every execution anchor must pass this test: "If I hand off this anchor to daily planning, do they have First Strike + Exit Condition?"
- If the answer is no for a deep-work anchor, add it before finalizing the weekly file.
- Failure to include this metadata creates planning friction in daily generation and increases anchor drift risk.

---

## 11.2 Anti-Drift Validation for Execution Anchors

Before finalizing the Weekly Execution file, validate that the anchor structure prevents drift and free-floating work.

**Forbidden anchor patterns:**

1. **Free-floating improvement tasks** without goal linkage
   - Example (FORBIDDEN): "Improve test runner performance"
   - Example (ALLOWED): "Optimize test runner (serves Goal 2: Test Infrastructure — improves merge feedback cycle)"
   - If a task is labeled improve/optimize/refactor/explore/polish, it MUST trace to a weekly goal or be rejected.

2. **Vague anchors without concrete First Strike or Exit Condition**
   - Example (FORBIDDEN): "Work on RobotOS architecture"
   - Example (ALLOWED): "RobotOS Architecture — Create diagrams (First Strike: open drawio template; Exit: adapter/kernel boundary diagram complete and exported)"

3. **Anchors that contradict pool separation**
   - Example (FORBIDDEN): "RobotOS deep diving during office hours Mon-Wed" (personal project in office hours)
   - Example (ALLOWED): "RobotOS architecture outline Mon-Wed evenings (19:30-21:30, 1×M capacity)"

4. **Third hidden project seeking execution time**
   - If a third project appears in daily anchor map expecting execution time (not just admin mention), fail validation and reassess weekly focus.
   - Exception: Escalation/incident response (mark explicitly as "incident response" or "maintenance", with limited time)

**Validation checklist before finalizing:**
- [ ] Every deep-work anchor has Linked Weekly Goal
- [ ] No free-floating improvement/optimization anchors exist (all tied to weekly goals)
- [ ] Every deep-work anchor has First Strike defined
- [ ] Every deep-work anchor has Exit Condition defined
- [ ] Every anchor that might spill has Carry-over Rule defined
- [ ] Office hours anchors = Zephyr only (no personal projects in Pool A)
- [ ] Evening anchors = RobotOS/Signee only (no Zephyr in Pool B)
- [ ] Max 2 projects per day (Primary + Secondary; any third is incident/admin only)
- [ ] Daily inheritance is possible: a daily planner can fill in blocks without needing to re-plan the week

If any check fails, revise the anchor before moving to Step 10.

---

## 11.3 Semantic Quality Gate for Execution Anchors (CRITICAL)

Every execution anchor must pass semantic quality validation. Vague anchors fragment execution and create drift at the daily layer.

**Rule 1 — No Generic Language (FORBIDDEN)**

The following patterns are NOT ALLOWED in any execution anchor:

- "work on"
- "improve"
- "optimize"
- "handle"
- "continue"
- "fix stuff"
- "do testing"
- "make progress on"

✗ BAD: "Work on test infrastructure"  
✓ GOOD: "Test Infrastructure — merge 3 RAM-load tests to develop; CI passing"

If detected → anchor rewrite REQUIRED before weekly file finalization.

---

**Rule 2 — Concrete Artifact Requirement (MANDATORY)**

Every execution anchor must reference exactly what will exist when the work is complete:

- **File or component name** (e.g., "test_memory.c", "architecture_diagram.drawio", "setup.md")
- **Specific deliverable state** (e.g., "3 tests merged", "PR approved", "documentation in docs/")
- **Observable completion marker** (e.g., "CI passing", "export complete", "team acknowledged")

Test: Can a third party name the artifact that will exist if this anchor completes?

If NO → rewrite until concrete.

Examples:

✓ GOOD: "Zephyr — merge 3 RAM tests to develop; all CI checks passing; merge log updated"  
✓ GOOD: "Signee — review specification draft + capture feedback in spec_v2.md"  
✗ BAD: "Improve the architecture"  
✗ BAD: "Continue the work"  
✗ BAD: "Make progress"

---

**Rule 3 — Anchor Size Constraint (MANDATORY)**

Each execution anchor must represent meaningful scope:

- **Minimum:** 45–90 minutes of focused work
- **Maximum per office block:** 2 anchors per day
- **Maximum per evening block:** 1 anchor per day (evening blocks are M-sized max and don't split)

**Fragmentation Prevention:**

If an anchor is smaller than 45 minutes:
- Merge it with adjacent anchor in the same pool
- OR combine it with support/admin work into the same time block
- DO NOT execute isolated sub-45-min anchors as separate daily trackers

Example fragmentation (BAD):
- Anchor 1: "Open test file" (5 min)
- Anchor 2: "Review requirements" (10 min)
- Anchor 3: "Create first test" (15 min)

Corrected (GOOD):
- Anchor: "Review test requirements, create initial test structure, first test passing locally" (45 min combined)

---

**Rule 4 — Verifiable Exit Condition (MANDATORY)**

Exit Condition must be observable and binary (true/false; not subjective):

✓ GOOD: "3 tests passing locally; all assertions green; no CI warnings"  
✓ GOOD: "PR submitted to develop branch; CI status checked"  
✓ GOOD: "Design document merged to docs/; team review checklist complete"  
✗ BAD: "Done with testing"  
✗ BAD: "Looks good"  
✗ BAD: "Good progress"  
✗ BAD: "Almost complete"

Test: Could a third party (or automated tool) verify this exit state without asking for clarification?

If NO → exit condition must be rewritten.

---

**Rule 5 — Anchor Compression Test (MANDATORY)**

**Before finalizing the weekly execution file, apply the Anchor Compression Test:**

For any day with 3 or more anchors (Primary + Secondary + Support):

1. Ask: "Can these 3+ anchors be merged into one coherent work unit?"
2. If YES → merge them. Combine into one anchor with unified First Strike + Exit Condition.
3. If NO → reason MUST be documented (e.g., "anchors are in different projects; cannot merge").

**Example compression:**

Original (3 anchors):
- Anchor 1: "Zephyr test environment setup"
- Anchor 2: "Zephyr initial test write"
- Anchor 3: "Zephyr test run verification"

Compressed (1 anchor):
- Anchor: "Zephyr — Environment setup + first test write + CI verification; all checks passing"

**Exception:** Anchors in DIFFERENT pools (office vs. evening) cannot be compressed; they are time-domain separated.

---

**Semantic Quality Validation Checklist (Before Finalizing):**

- [ ] No anchor contains forbidden generic language (work on, improve, optimize, etc.)
- [ ] Every anchor references a concrete artifact or observable completion state
- [ ] Every anchor is ≥45 min scope (no sub-45-min orphaned anchors)
- [ ] Max 2 office anchors per day; max 1 evening anchor per day
- [ ] Every anchor's Exit Condition is verifiable and binary (not subjective)
- [ ] Applied compression test: ≥3 anchor days were evaluated; mergeable ones merged
- [ ] All remaining multi-anchor days have explicit reason for separation

If ANY check fails → revise anchors and re-check before Step 10.

---

## 11.5. Drift Detection Layer: Design & Integration

The Weekly Execution file must not only plan work; it must detect when execution diverges from plan early enough to react. This layer defines drift, signals, states, and response rules that integrate into both the weekly file and daily inheritance.

### Drift Definition

**Execution drift** occurs when actual execution diverges from planned execution in ways that threaten weekly outcomes if unaddressed.

**Six Categories of Drift:**

1. **Schedule Drift** — Planned phase not started in intended window OR extending beyond planned end without visible artifact
2. **Dependency Drift** — Upstream anchor slipped; downstream anchor no longer valid or blocked
3. **Artifact Drift** — Time spent but expected visible artifact not produced (motion without output)
4. **Clarity Drift** — Repeated motion on same anchor without reducing ambiguity (spinning, not progressing)
5. **Load Drift** — Contingent work absorbed into committed load (week becomes overloaded invisibly)
6. **Attention Drift** — Time diverted into uncontrolled research, side work, or hidden third scope (scope creep)

### Drift Signals (Per Daily Anchor)

For each major daily anchor, define detectable drift signals. These are checked once per day, EOD, taking ~5 minutes.

**Required Signal Set (7 signals):**

| Signal | Check | Observable? | Examples |
|---|---|---|---|
| **Started on time?** | Primary anchor began in intended window | Y/N | Mon 8:30 office started? Tue evening by 20:00? |
| **Blocker in first 15p?** | Fallback triggered or escalation needed | Y/N | Blocker found = switch to fallback; fallback not used = no blocker |
| **Artifact produced?** | Visible tangible output exists | Y/N | File created? Test log? PR opened? Meeting note? |
| **Ambiguity reduced?** | Did execution reduce unknowns vs. move them? | Y/N/Increased | Morning: "API unclear"; EOD: "API mapped (3-endpoint draft)" = reduced |
| **Fallback used?** | Primary path blocked; fallback executed | Y/N | If triggered = normal; if not triggered = primary succeeded |
| **Protected scope preserved?** | Critical path items protected (hard-gate days only) | Y/N | Wed dline day: "dline PR still target" = YES |
| **Contingent held?** | Contingent work not absorbed as committed (dependent days) | Y/N | If Thu depends on Wed: was Wed completed or deferred? Did Thu start anyway? |

**Signal Collection Protocol:**
- **EOD (mandatory):** 5-minute signal check per primary anchor
- **Midday (optional):** If blocker suspected, 3-minute early check mid-session
- **Log location:** Weekly file "Drift Log" table (one row per day per anchor)

### Drift States

**Simple 4-state model with triggers and allowed responses:**

| State | Definition | Triggers | Allowed Action | Forbidden |
|---|---|---|---|---|
| **GREEN** | On track; all signals normal | Started on time + artifact produced + ambiguity reduced (or fallback executing normally) | Continue execution as planned | Relax vigilance; skip EOD checks; ignore upstream deps |
| **YELLOW** | Slipping but recoverable | 1–2 signals off (e.g., blocker found, ambiguity unchanged) but anchor still workable | Use fallback + adjust daily plan + flag for EOD review + check cascade deps | Ignore signal; assume recovery magic; hide blocker |
| **ORANGE** | Critical path threatened | 3+ signals off OR upstream prerequisite for hard gate slipped OR contingent absorbed into committed | De-escalate non-critical work + protect hard gate + escalate to Agent 1 by EOD + prepare replan | Pretend hard gate still safe; continue business-as-usual; ignore upstream slip |
| **RED** | Intent no longer valid | Hard gate failed OR mandatory commitment failed OR week cannot be recovered with current plan | Full replan required; escalate to Agent 1 immediately; trigger WEEKLY_REBALANCE | Continue executing old plan; blame external factors; hide failure |

### Drift Response Rules (By Type & Trigger)

**Operational, not aspirational. Prescribe action for each drift type.**

**If Schedule Drift (not started on time):**
- Midday assessment: Why not started? Blocker or priority shift?
  - *If blocker:* Switch to fallback anchor + log blocker + propagate to next day
  - *If priority shift:* Escalate (not normal variation); update Weekly file
- State change: GREEN → YELLOW (if recoverable) or ORANGE (if blocking upstream dependency)

**If Artifact Drift (time spent, no artifact):**
- Force stop anchor; create explicit "Residue Note" (what was done, what's blocking, what's next)
- Accept residue as partial progress; do NOT re-allocate time for "better version"
- State change: GREEN → YELLOW (if partial artifact + fallback exists) or ORANGE (if hard gate artifact missing)

**If Clarity Drift (ambiguity unchanged after 2 touches):**
- STOP execution on this anchor; convert to explicit decision point
- Create decision artifact: "Clarification needed: [open Qs]"; escalate Q&A block
- Do NOT continue spinning on ambiguous work
- State change: GREEN → ORANGE (ambiguity ≥3 not making progress)

**If Dependency Drift (upstream slipped):**
- Immediately check downstream anchor validity
  - *If downstream is contingent on upstream:* Escalate + prepare to drop downstream
  - *If downstream is independent:* Proceed normally; note upstream slip in Drift Log
- Protected scope rule: If upstream is prerequisite for hard gate, protect hard gate (drop support work first)
- State change: GREEN → YELLOW or ORANGE depending on hard-gate threat

**If Load Drift (contingent absorbed into committed):**
- Audit daily hours; separate contingent from committed work
- If contingent hours >30% of committed hours: state change to ORANGE; prepare to drop contingent
- Do NOT pre-execute contingent work (wait for blocker resolution)
- State change: GREEN → ORANGE (if week overloaded)

**If Hard Gate Day Threatened (Wed dline, critical Mon, etc.):**
- **Immediately prioritize hard-gate artifact**; all other work becomes secondary
- Drop support/contingent work first
- Activate escalation: flag to Agent 1 by Tue EOD if hard gate artifact at risk
- State change: any → ORANGE

### Daily Integration & Inheritance

**What Weekly File Specifies for Daily Inheritance:**

Each daily anchor must inherit (for the daily planner):
- Primary artifact target (concrete)
- Expected drift signals for that day (what to measure)
- Fallback anchor if primary blocks
- Protected scope marking (if hard gate day)
- Contingent status (if dependent on prior day)
- Override rule (if upstream-dependent, e.g., Tue→Wed→Thu)

**What Daily File Must Check:**

**Midday (optional, if blocker suspected):**
- Started primary anchor on time? (Y/N)
- Any blockers in first 15p? (Y/N) → if yes, switch to fallback + log

**End-of-Day (mandatory, ~5 min):**
- Artifact produced? (Y/N) — any artifact, even partial
- Ambiguity reduced? (Yes/No/Increased) — vs. morning state
- Blocker encountered? (Y/N) → fallback used? (Y/N)
- Protected scope preserved? (Y/N) — hard gate days only
- Contingent held or absorbed? (Y/N) — dependent days only

**Signal State Assignment (EOD, 2 min):**
- Count signals off: 0–1 off = GREEN | 2 off = YELLOW | 3+ off = ORANGE | hard gate failed = RED
- If state changed or is YELLOW/ORANGE: note reason in Weekly Drift Log

**End-of-Week Review:**
- Scan Drift Log for patterns (repeated blockers, ambiguity stacks, load creep)
- Did override rules activate as needed? (dropped contingent, protected hard gate, escalated)
- Lessons for next week's design

### Drift File Structure (In Weekly Execution)

**Add a new summary section to the weekly file:**

```
## [N]. Execution Drift Detection Layer

### Drift Signals Defined (Per Day & Anchor)
| Day | Anchor | Hard Gate? | Protected Scope | Signal Monitor | Fallback If Blocked |
|---|---|---|---|---|---|
| Mon | Zephyr M1 | NO | — | started/blocker/artifact | Log blocker + outline |
| Tue | Zephyr M2 dline | NO | dline path | started/artifact/ambig | Fallback: API draft |
| Wed | Zephyr M2→M3 | YES ⭐ | Protect: dline PR open | started/artifact/ambig | NA (critical path) |
| Thu | Zephyr M4 RAM | NO (contingent) | — | started (if Wed done) | Drop if Wed slipped |

### Drift Response Rules (Quick Reference)
1. Hard gate threatened → **Protect Wed dline PR** + drop contingent RAM + drop Pool B if needed
2. Blocker in first 15p → use fallback anchor + log blocker + check midday
3. No artifact after time block → force stop + residue note + log
4. Ambiguity unchanged after 2 touches → stop execution, escalate Q&A
5. Weekly overloaded (contingent absorbed) → audit, separate, drop contingent if needed

### Weekly Drift Log (Tracking Sheet)
| Day | Anchor | Signal | State | Action Taken | Notes |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
```

---

## 12. Carry-over Rules

- **Carry over only meaningful unfinished work:** Work that has real impact if not continued soon. Drop trivial carry-over explicitly.
- **Rewrite carry-over as exact next entry point:** Not "continue the design"; "review draft API schema (10 min) → confirm against test results → refine if needed."
- **Do not carry completed work:** Work that reached Its DoD (Definition of Done) does not need a carry-over entry.
- **Do not carry blocked work as active execution:** If work is blocked by a dependency (waiting for review, customer email, environment), encode it as a conditional block or checkpoint, not as an active execution anchor.
- **If carry-over conflicts with weekly priorities, escalate or rebalance:** Do not silently displace the week's intended work to absorb old unfinished items.
- **If carry-over threatens weekly viability, flag explicitly:** Example: "Mon carry-over + Wed primary anchor both require deep focus. Confidence: medium. Escalation trigger: if Mon review blocked beyond 24h."
- **CRITICAL — Do NOT blindly carry forward outdated anchors from previous week:** Before inheriting a previous week's anchor structure into this week's execution frame, validate:
  - Did the anchor execute as planned? (Check WEEK_CLOSEOUT Execution Integrity Report)
  - If NO → why did it deviate? (Type A/Type B/Type C drift?) 
  - If it deviated with Type B or Type C classification → the anchor assumptions are STALE
  - Update the anchor definition before carrying it forward (do NOT repeat the same execution plan that failed)
  - Example: If "RobotOS architecture outline" was Type C (hidden dependency: diagram work was prerequisite), do NOT carry forward "architecture outline" as-is next week; incorporate the diagram work as a prerequisite step

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

## 14.4 Canonical-Source Model (Cross-Section Consistency)

A good weekly file maintains **canonical ownership of critical fields** to prevent stale contradictions between sections. When a hardening patch updates a core rule, only the canonical source needs updating; derived sections automatically inherit via this model.

**Core Principle:**
Every critical planning property (ambiguity score, escalation time, contingency condition, success type) has ONE authoritative location. All other sections that mention it must reference or inherit from that source; they cannot independently redefine or paraphrase it.

**Canonical Sections (Authoritative):**
- **§2 Phase Normalization: Mission SIZE, Ambiguity Score, Energy Fit, Dependency Type** (see table)
- **§3 Mission Breakdown: Artifact targets, Start Steps, Stop Conditions, Fallback anchors, Escalation Triggers & Times, Carry-over Rules** (see phase detail)
- **§1 Weekly Summary + §1.1 Goal-to-Execution-Role Mapping: Strategic Goal Rank + Weekly Execution Role assignment** (see mapping; canonical source for why role may differ from goal rank)
- **§1 Weekly Summary + §9 DoD: Success types (Primary/Secondary/Support), Contingency preservation** (see definitions)
- **§5 Load Classification: Committed vs Contingent vs Overhead split** (see load summary)

**Derived Sections (Reference-Only):**
- **§4 Daily Anchor Map:** operationalizes phases; inherits artifact/start/stop/fallback/time/contingency from §3 (does not redefine)
- **§6 Daily Inheritance:** reference guide; summarizes what daily inherits (adds no new rules)
- **§7–§8 Dependency Graph & Escalation Checkpoints:** visualizes §3 logic; references canonical times/triggers (no rewording)
- **§10 Generation Report:** validates that phases were assessed; reflects actual body content (never carries legacy rule language)
- **§11 Drift Detection Layer:** monitors canonical signal targets; does not reinterpret mission semantics

**Why This Matters:**
- **Prevents stale summaries:** Report Phase 2 claim must match §2 table. If table updated, report is automatically true.
- **Prevents contingency blurring:** Secondary success type can only be stated as "contingent on primary" — once. If stated twice, both must say "if primary met."
- **Prevents temporal conflicts:** Escalation time "Mon 11:00" (canonical) must be used everywhere, not mixed with "Mon EOD" in other sections.
- **Prevents schema drift:** Weekend rows follow same schema as weekday rows; no special cases that violate daily-map structure.

**Derivation Rules (Strict):**
- Can operationalize ("schedule M1 for Mon morning") but NOT redefine ("M1 Ambiguity ≤2" when canonical shows Ambiguity 3)
- Can visualize ("Tue depends on Mon") but NOT create alternatives ("escalate Tue EOD" if canonical says "Mon 11:00")
- Can confirm ("all artifacts are concrete files") but NOT invent new rules ("also collect verbal feedback")
- Can monitor ("ambiguity is held at 3") but NOT reinterpret ("ambiguity is effectively 2 because...") 

**Example Canonical Ownership:**
| Property | Canonical Section | Stale Contradiction | How Canonical Model Prevents It |
|---|---|---|---|
| Ambiguity Score | §2 table (M1=2, M2=3) | Report claims "Ambiguity ≤2" (old rule) | Report purity gate: Phase 2 claim must reference §2 data |
| Escalation Time | §3 M1 phase ("escalate Mon 11:00") | Daily Map says "escalate Mon EOD" | Temporal consistency gate: all instances of same trigger use same time |
| Contingency | §3 M4 phase ("contingent on Wed complete") | Success statement says "all gates have equal priority" | Success semantics gate: contingent goals preserved everywhere |
| Fallback | §3 M1 phase ("fallback: spike review") | §7 Graph invents "fallback: escalate immediately" | Derived limit gate: fallbacks inherited, not created |

---

## 14.5 Operational QA Gates (BEFORE FINALIZATION — Rigorous, Not Optional)

**These gates must pass before the weekly file is considered complete. If any gate fails, the file is not ready for daily inheritance.**

### Gate 1: Dependency QA (Blocking Graph Test)

Every contingent task must name its prerequisite explicitly. This is not subjective; it is checkable.

- [ ] **Has every contingent task named its prerequisite?**
  - Example (GOOD): "Thu RAM expansion (contingent on dline_send/receive complete by Wed EOD)"
  - Example (BAD): "Thu RAM expansion (if dline done)" with no specific test/milestone named
- [ ] **Has every "independent" afternoon/evening task been justified?**
  - If evening anchor is marked independent from office anchor, write WHY in fallback column
  - Acid test: If office anchor slips 2h, does evening anchor still execute? If answer is NO, they're not independent
- [ ] **Is there any hidden third project inside a daily split?**
  - Example (BAD): Mon office: Zephyr + evening: RobotOS + hidden admin: Signee email catch-up (3 projects)
  - Fix: Move Signee to separate day or mark as contingent on time availability
- [ ] **If primary anchor blocks, is fallback explicitly named?**
  - Example (GOOD): "If dline implementation incomplete Tue → escalate Wed; shift Thu to dline rework (not RAM expansion)"
  - Example (BAD): "If blocked, adapt as needed" (too vague)

### Gate 2: Operational QA (Artifact Concreteness Test)

Every anchor must expose a concrete artifact. Vague language fails this gate.

- [ ] **Does each anchor specify a concrete artifact (doc/file/checklist/commit/log/diagram)?**
  - Scan all artifact columns. Forbidden words: "foundation", "merge-ready", "progress", "work on", "clarity"
  - Every anchor must answer: "What file/document/commit/field exists when this anchor completes?"
  - If answer is VAGUE, rewrite anchor until it's concrete
- [ ] **Does each anchor have a ≤15 minute start step?**
  - Scan all Start Step columns. Every step must begin with a VERB
  - Forbidden: "Continue from Mon", "Keep working on X", "Add more"
  - Required: "Open test file + review requirements + create scaffold", "Draft 5 test-set headings", "Export architecture diagram template"
- [ ] **Does each anchor have a binary, observable stop condition?**
  - Scan all Stop Condition columns. No subjective language
  - Forbidden: "Done", "Looks good", "Ready"
  - Required: "All tests passing locally (zero failures, zero warnings)", "PR submitted and visible in code review queue"

### Gate 3: Scheduling QA (Energy + Ambiguity Fit Test)

Ensure high-ambiguity work is placed only on suitable energy days. Ensure dips are protected. Ensure evening blocks are conservative. Ensure contingent load is not silently treated as committed.

- [ ] **Are Ambiguity ≥ 3 tasks placed ONLY on high-energy or planned-discovery days?**
  - Ambiguity ≥ 3 on low-energy day (e.g., Thursday dip) = automatic failure
  - Ambiguity ≥ 3 on evening = automatic failure (evenings should be Ambiguity 0–2 only)
  - If high-ambiguity task is mandatory that day, split it into low-ambiguity phases or escalate
  - Ambiguity 3 tasks on same day MUST be separated (morning + evening split violates consecutive-uncertainty rule)
- [ ] **Is Thursday dip protected?**
  - Thursday anchor(s) should be smaller/simpler than Mon/Tue/Wed
  - Thursday evening should be S-only or explicitly zero (recovery time)
  - If Thursday has contingent work (e.g., "proceed if Wednesday complete"), condition is documented AND fallback named
- [ ] **Are evening blocks kept conservative?**
  - No L-tasks on weekday evenings (XS/S only, not M main blocks)
  - Ambiguity ≤ 2 on all evenings (no exploration at day-end)
  - Evening anchors do NOT hang their success on office-hours completion (or dependency is explicit in override column)
- [ ] **Are contingent and committed loads clearly distinguished?**
  - Committed tasks marked "must complete this week"
  - Contingent tasks marked "only if [prerequisite] completes"
  - No contingent task appears in contingent load if prerequisite is uncertain
  - If contingent task has >50% failure risk on prerequisite, move to deferred or explicitly accept deferral
- [ ] **Are weekend slots all declared (R11 anti-conflation)?**
  - Sat daytime (Slot 1): time value stated (e.g., "3h RobotOS") or "0h"
  - Sat evening (Slot 2): OFF or OPEN declared
  - Sun morning (Slot 3): overhead hours stated (~2–3h) or "0h"
  - Sun afternoon (Slot 4): time value stated (e.g., "0h unused") or execution task named
  - Sun evening (Slot 5): OFF or OPEN declared, explicitly opposite of Sat evening
  - No vague day-based language ("weekend", "Sunday used/unused", "optional")

### Gate 4: Inheritance QA (Daily File Generation Test)

A daily planner must be able to generate daily files from this weekly file WITHOUT needing to re-read the WeekPlan or re-interpret the week.

- [ ] **Can a daily planner extract today's anchor, artifact, start step, stop condition, and fallback directly from the weekly file?**
  - Test: Pick any day from the daily anchor map and check if inherited columns are present and complete
  - If missing: primary anchor is clear, but artifact is vague, or start step is missing → FAIL
- [ ] **Are primary/secondary/fallback anchors all explicitly named (not inferred)?**
  - Daily planner should not need to guess which anchor is primary
  - If two anchors on same day: is priority clear (Primary vs Secondary), or explicitly conditional?
- [ ] **Is dependency context preserved for daily inheritance?**
  - If daily anchor depends on previous day, is that dependency stated in override/fallback column?
  - Example (GOOD): "Wed evening Signee spec (depends on Mon/Tue outline clarity; if outline incomplete, escalate Wed morning; if office slips, Signee deferred to Thu)"
  - Example (BAD): "Continue Signee spec" (assumes context carry-over; no override rule)
- [ ] **Is override rule explicit for upstream-dependent chains (Tue→Wed→Thu)?**
  - Example (GOOD): "Wed slot: If Tue implementation incomplete, move dline finalization to Wed morning; Thu RAM deferred to W12. Protect: dline quality."
  - Example (BAD): "Wed proceeds if Tue ready" (no statement of what gets dropped/protected if Tue slips)

### Gate 5: Realism QA (No Cosmetic Scoring)

Validate that the weekly frame is achievable under real execution conditions, not just neat on paper.

- [ ] **Does no single day exceed realistic human capacity?**
  - Max office day: ~7h focused mission work (28h ÷ 4 days = 7h avg, not 8–10h peaks)
  - Max evening: 2h total (1×M or 2×S, not L + admin + personal)
  - If any day exceeds realistic capacity on paper, either rebalance or mark as risk/escalation trigger
- [ ] **Is Ambiguity stacked realistically or just compressed to look clean?**
  - Example (BAD): "Mon Ambiguity 2, Tue Ambiguity 3, Wed Ambiguity 2" (high uncertainty Mon→Tue→Wed compressed; no recovery time)
  - Example (GOOD): "Mon Ambiguity 1, Tue Ambiguity 3 (high day, discovery mode), Wed Ambiguity 1 (apply learnings)"
  - If Ambiguity is sequentially high (2+ days ≥3), mark as execution risk
- [ ] **Are evening blocks actually conservative or just labeled M?**
  - Scan evening anchors: do they require fresh mental energy or can they be done tired?
  - If evening anchor requires high focus (implementation, debugging, design), NOT conservative even if labeled M
  - Evening should be: review, documentation, bounded testing, configuration, not open-ended implementation
- [ ] **Is contingent load realistically contingent or silently committed?**
  - Example (BAD): "Thu RAM proceeds if Wed dline complete" (but if Wed slips by 2h, Thu suddenly forced to make up time)
  - Example (GOOD): "Thu RAM proceeds if Wed dline complete by noon Wed; if after noon, RAM deferred to W12"
  - If prerequisite has significant slip risk (>25%), contingent task should have explicit deferral clause
- [ ] **Does fallback still fit available time if primary blocks?**
  - Example (BAD): "If Mon architecture unclear, fallback: detailed re-read + architecture spike (6h)" (doesn't fit Mon)
  - Example (GOOD): "If Mon architecture unclear by 11:00, escalate; Tue becomes rework (not new implementation)"
  - If fallback requires as much time as primary, it's not a fallback; it's a rescope
- [ ] **Does declared load align with practical execution ability?**
  - Total committed + contingent should not exceed: office 28h + evening 7h + weekend 5h = 40h weekly
  - If total >40h on paper, rescope or relabel contingent to deferred
  - If actual recent weeks ran 30–32h, do not schedule 38h as realistic "optimistic"

**Realism QA FAIL:** If scores look cosmetically neat (all Ambiguity 2, all days perfectly balanced, all contingent marked as 100% likely), the file is gaming the system. Realism must be uncomfortable; good weeks have lumpy loads, some uncertainty, some risk.

---

### Gate 6: Drift Detectability QA (Early Warning System)

Validate that the weekly file supports drift detection during live execution. This gate ensures drift signals are measurable, not aspirational.

- [ ] **Does each major daily anchor expose measurable drift signals?**
  - Check: Started on time? Blocker in first 15p? Artifact produced? Ambiguity reduced? Fallback used? Protected scope preserved?
  - If any signal column is missing or vague (e.g., "artifact: undefined"), rewrite anchor
- [ ] **Is fallback anchor explicitly defined as alternative execution?**
  - Fallback is NOT "adapt as needed"; it IS a concrete alternative anchor (e.g., "switch to log capture + blocker note")
  - If fallback requires same time/energy as primary, it's not a fallback; rewrite
- [ ] **Is protected scope explicit on hard-gate days?**
  - Hard gate day (e.g., Wed dline) must state: "protect this (dline PR), drop this (contingent RAM) if threatened"
  - If hard gate day has no protect/drop rule, add it
- [ ] **Are drift responses defined for cascading dependencies?**
  - For chains like Tue→Wed→Thu, specify: if Tue <50%, then Wed does X; if Wed fails, Thu does Y
  - If cascade is silent (assumes things work), escalation rule missing
- [ ] **Can the user detect fake progress vs real movement?**
  - Example (BAD): "worked on architecture" (motion, unclear if progress)
  - Example (GOOD): "architecture draft created; 3 unknowns documented; ambiguity reduced from 3→2"
  - If anchors describe activity not outcome, rewrite artifacts
- [ ] **Is weekly overload visible?**
  - Can user see total committed + contingent + drifted-into-committed hours?
  - If contingent work is pre-executed or ambiguous, add load audit rule

---

### Gate 7: Language QA (No Narrative Bloat)

Reduce prose where tables/fields are better. Execution documents should be scannable, not essay-like.

- [ ] **No body paragraph exceeds 4 lines?**
  - If a mission description takes 5+ lines, split into bullet format or table
- [ ] **All numbers, hour allocations, slot declarations, rules formatted as bullets/tables/labeled blocks (not prose)?**
  - Forbidden: "The week has about 36 hours of office capacity, of which roughly 12 go to focused mission work and the rest is overhead"
  - Required: "Office capacity: 28h (32h gross - 4h admin) | Committed focus mission: 12h | KTLO: 16h"
- [ ] **Daily anchor descriptions are specific and actionable (not generic)?**
  - Forbidden: "Zephyr work" (too generic)
  - Required: "Zephyr M2 dline implementation; complete dline_send/receive; comprehensive testing"
- [ ] **Exit conditions and escalation triggers are binary and observable (not subjective)?**
  - Forbidden: "If things go well" / "If team needs it"
  - Required: "If dline PR not opened by Wed EOD" / "If 15+ tests passing by Thu"

### Gate 8: Goal-to-Execution-Role Mapping Clarity (Strategic vs Execution Role)

This gate validates the explicit bridge between strategic goal importance (from WeekPlan) and weekly execution role (from Weekly Execution).

- [ ] **Is §1.1 Goal-to-Execution-Role Mapping section present in Weekly Summary?**
  - Required: Compact table or list mapping each goal to PRIMARY / SECONDARY / SUPPORT
  - Each goal must show: strategic rank, execution role, reason for any difference
  - Example (REQUIRED): "Goal 1 (RobotOS) → SUPPORT: strategic pillar, but independent this week; no hard gate"
- [ ] **If a goal's execution role differs from its strategic importance "feel", is the difference explained?**
  - Acid test: Read Weekly Plan §2 goal rank; read Weekly Execution §1.1 role. Do they match in intuitive importance?
  - If LOW/HIGH mismatch (e.g., Goal 1 = SUPPORT), is 2–3 word reason stated? (independent, no blocker, medium-risk, etc.)
  - Example (BAD): "Goal 1 → SUPPORT" with no reason
  - Example (GOOD): "Goal 1 RobotOS → SUPPORT (independent; Zephyr owns Wed hard gate)"
- [ ] **Is the mapping canonical source documented in §12 (Canonical-Source Discipline)?**
  - Required: Canonical-Source section must name §1.1 as source of truth for goal-to-role assignments
  - No other section redefines or contradicts the role without referencing §1.1 mapping
- [ ] **Do all references to goals throughout the file use the assigned execution role, not the strategic rank?**
  - Forbidden: "Goal 1 is our primary outcome" (role confusion)
  - Required: "Goal 1 (RobotOS) is strategically important; w11 execution role is SUPPORT (independent progress)"
  - Scan: Mission breakdown, success conditions, load classification for consistent role language

### Gate 9: Artifact Placement QA (File Path Correctness — CRITICAL FOR SCALABILITY)

This gate ensures weekly and daily files are placed in correct folders per the WEEKLY-vs-DAILY folder structure rule. Incorrect placement causes folder bloat and makes future generation error-prone.

- [ ] **Weekly Plan file path verification:**
  - MUST be: `03_PLANNING/03_WEEK/Wxx/2026-Wxx_WeekPlan.md` (where Wxx = W09, W10, W11, etc.)
  - NOT acceptable: `03_PLANNING/03_WEEK/2026-Wxx_WeekPlan.md` (no week subfolder)
  - NOT acceptable: Generic names like `WeekPlan.md` (must include full week identifier 2026-Wxx)
- [ ] **Weekly Execution file path verification:**
  - MUST be: `03_PLANNING/03_WEEK/Wxx/2026-Wxx_Execution.md`
  - NOT acceptable: `03_PLANNING/03_WEEK/2026-Wxx_Execution.md` (no week subfolder)
  - NOT acceptable: Generic names like `Execution.md`
- [ ] **Daily file path verification (DO NOT SKIP):**
  - MUST be: `03_PLANNING/04_DAY/Wxx/YYYY-MM-DD_Daily.md` (where Wxx = W09, W10, W11, etc. and date belongs to that week)
  - NOT acceptable: `03_PLANNING/03_WEEK/YYYY-MM-DD_Daily.md` (wrong folder; mixing layers)
  - NOT acceptable: `03_PLANNING/04_DAY/YYYY-MM-DD_Daily.md` (no week subfolder)
  - **Acid test:** Can a human see the week folder and immediately know this is daily execution for that week? If yes → placement correct.
- [ ] **Folder auto-creation rule enforced:**
  - If target week folder does not exist, generator MUST create it automatically (do not ask for permission)
  - Do NOT fail with "folder not found" error; create the folder structure as needed
- [ ] **No daily files exist under 03_WEEK/ folder:**
  - Scan `03_PLANNING/03_WEEK/` for any files matching `YYYY-MM-DD_Daily.md`
  - If found: those are misplaced; move to `04_DAY/Wxx/` and log the correction
- [ ] **No weekly files exist under 04_DAY/ folder:**
  - Scan `03_PLANNING/04_DAY/` for any files matching `*_WeekPlan.md` or `*_Execution.md`
  - If found: those are misplaced; move to `03_WEEK/Wxx/` and log the correction

**Why this matters:** Correct folder placement is part of artifact semantics, not just storage convenience. The folder path encodes the artifact type (planning vs execution) and the week it belongs to. Incorrect placement makes the system harder to navigate, increases risk of overwriting wrong files, and sets a bad precedent for future generations.

---

## 15. Standard QA + Generation Checklist (12-Phase Operational Framework)

Copy this COMPLETE checklist for each weekly generation session. All 12 phases must PASS for file to be ready. Do not skip sections.

```
### Weekly Execution Generation Checklist – <WEEK_NAME> (prepared <DATE>)

**PHASE 1: SOURCE READING & SETUP**
- [ ] Mode identified: A (New) / B (Reconstruction) / C (Rebalance)
- [ ] Month file read (priority/commitment for this week identified)
- [ ] WeekPlan read in full (Mode A) or previous week execution + daily files (Mode B/C)
- [ ] Recent Daily files scanned (last 3–4 days; energy patterns, blockers calibrated)
- [ ] Project state files reviewed if referenced in WeekPlan
- [ ] Carry-over summary collected (from WEEK_CLOSEOUT or previous week notes)

**PHASE 2: MISSION & FOCUS DEFINITION (SIZE/AMBIGUITY NORMALI ZATION)**
- [ ] Weekly focus identified (one-sentence statement passing coherence test)
- [ ] Primary mission SIZE assessed: XS / S / M / L (L missions decomposed to M-phases)
- [ ] Primary mission Ambiguity scored: 0–5 (if ≥4, flagged as Spike, not execution)
- [ ] Secondary mission(s) SIZE assessed: M or smaller (no L secondary anchors)
- [ ] Secondary mission(s) Ambiguity: ≤3 (no high-ambiguity secondary mixed with critical path)
- [ ] Dependencies between missions identified (hard/conditional/independent/deferred)
- [ ] Third projects explicitly deferred or rejected (no hidden projects in daily split)

**PHASE 3: ARTIFACT OPERATIONALIZATION (CONCRETE OUTPUTS)**
- [ ] Every mission/daily anchor has concrete artifact defined (not vague)
  - [ ] Scan for forbidden words: "foundation", "merge-ready", "clarity", "progress", "work on" — REMOVE ALL
  - [ ] Artifact specifies file/document/commit/log/diagram (specific, not generic)
- [ ] Every daily anchor has ≤15 min start step defined (verb-starting; creates immediate motion)
  - [ ] Start step is actionable (not "continue" or "finish")
- [ ] Every daily anchor has binary observable stop condition (not subjective)
  - [ ] Stop condition passes acid test: Could third party verify this is complete without argument?

**PHASE 4: DEPENDENCY QA (BLOCKING GRAPH)**
- [ ] Every contingent task explicitly names its prerequisite & completion test
- [ ] Every "independent" anchor justified in dependency column
  - [ ] Acid test applied: If office anchor slips 2h, does evening anchor still execute? If NO → not independent
- [ ] Hidden third-project spread detected and fixed (no 3+ projects on any day)
- [ ] If primary fails, fallback explicitly named (not "adapt as needed")

**PHASE 5: SCHEDULING QA (ENERGY + AMBIGUITY FIT)**
- [ ] Ambiguity ≥3 tasks placed ONLY on high-energy or discovery days (NOT evening, NOT Thu dip)
- [ ] Ambiguity is not stacked back-to-back (recovery day between Ambiguity 3 slots if possible)
- [ ] Thursday dip protected (smaller anchors, S-only evening, contingent work conditional on Wed complete)
- [ ] Evening blocks conservative (no L-tasks, Ambiguity ≤2 only, independently executable or explicit upstream dependency)
- [ ] Contingent load clearly labeled (not silently assumed as committed)
- [ ] Weekend slots ALL declared (R11 anti-conflation; all 5 slots named with values or OFF)
  - [ ] Sat Slot 1 (daytime): time value or 0h stated
  - [ ] Sat Slot 2 (evening): OFF or OPEN declared
  - [ ] Sun Slot 3 (morning): overhead hours ~2–3 stated
  - [ ] Sun Slot 4 (afternoon): time value or "unused" with math proof
  - [ ] Sun Slot 5 (evening): OFF or OPEN (opposite of Sat evening per R10)

**PHASE 5.5: REALISM QA (NO COSMETIC SCORING)**
- [ ] No single day exceeds realistic human capacity (~7h office, ~2h evening max)
- [ ] Ambiguity stacked realistically (not just compressed to look clean)
- [ ] Evening blocks actually conservative (not just labeled M; require low-focus work)
- [ ] Contingent load has realistic failure scenarios named (what if prerequisite slips?)
- [ ] Fallbacks fit available time (not requiring rescope to match fallback duration)
- [ ] Total load aligns with practical ability (commit to <40h/week objective)

**PHASE 6: INHERITANCE QA (DAILY FILE GENERATION)**
- [ ] Daily planner can extract today's anchor, artifact, start step, stop condition directly
- [ ] All primary/secondary/fallback anchors explicitly named (not inferred)
- [ ] Dependency context preserved for daily inheritance (previous-day deps / blockers / override rules stated)
- [ ] Override rule explicit for upstream-dependent chains (Tue→Wed→Thu): what drops first, what protects first
- [ ] No day requires re-reading WeekPlan to understand execution intent
- [ ] If day is contingent, prerequisite milestone named & testable
- [ ] If day slot is after major dependency, re-entry mode stated (Quick / Analytical / Fragile / Escalation)

**PHASE 7: POOL SEPARATION & CONSTRAINTS**
- [ ] Office hours contains Zephyr only (no RobotOS/Signee hidden in Pool A)
- [ ] Personal evenings/weekend contain RobotOS/Signee only (no Zephyr in Pool B)
- [ ] No cross-pool contamination in any daily split
- [ ] Max-2-project rule verified per day (Primary + Secondary max; admin/overhead does NOT count as third project)

**PHASE 8: CARRY-OVER INTEGRATION**
- [ ] Unfinished work from previous week identified with re-entry mode (Quick/Analytical/Fragile)
- [ ] Carry-over rewritten as exact next entry points (not vague "continue X")
- [ ] Trivial carry-over explicitly dropped (not carried forward)
- [ ] Blocked work marked conditional (not forced to false-execute)
- [ ] Receiving day saturation checked (no day overloaded with prior week spillover)

**PHASE 9: LOAD CLASSIFICATION**
- [ ] Total weekly load split into three categories:
  - [ ] Committed load (mandatory completion for weekly success)
  - [ ] Contingent load (only if committed completes)
  - [ ] Overhead load (structural KTLO, non-execution)
- [ ] Committed load is realistic given available capacity
- [ ] Contingent load has explicit prerequisite milestone + unblock condition named
- [ ] Load summary shows split clearly (not combined into one total)

**PHASE 10: LANGUAGE QA (NO NARRATIVE BLOAT)**
- [ ] No body paragraph exceeds 4 lines (split to bullets/tables if longer)
- [ ] All numbers/allocations/slot declarations tablularized or bulleted (not prose narrative)
- [ ] Daily anchors are specific/actionable (not generic "Zephyr work", "architecture", "testing")
- [ ] Exit conditions + escalation triggers are binary/observable (not subjective "if needed", "if team prefers")

**PHASE 11: DRIFT DETECTION LAYER INTEGRATED**
- [ ] Drift definition: 6 drift types visible (schedule, dependency, artifact, clarity, load, attention)
- [ ] Drift signals: each major anchor has signal set (started/blocker/artifact/ambiguity/fallback/protected)
- [ ] Drift states: GREEN/YELLOW/ORANGE/RED defined with trigger conditions
- [ ] Response rules: at least 5 response rules defined (hard gate, blocker, artifact, clarity, load)
- [ ] Daily inheritance: signals to check daily in summary
- [ ] Hard gate protection: hard-gate day has explicit protect/drop rules (e.g., "protect Wed dline PR, drop contingent RAM")
- [ ] Drift log table: tracking sheet provided (even if empty at generation)

**PHASE 12: SEVEN OPERATIONAL LAYERS PRESENT (HARDENED WITH REALISM)**
- [ ] Phase Normalization Layer: SIZE (with L checkpoint rule), Ambiguity (0–5 scored honestly), energy fit, dependency type visible per anchor
- [ ] Artifact Operationalization Layer: every anchor has concrete artifact + minimum usable state (no vague language)
- [ ] Start Anchor Layer: every deep-work anchor has ≤15p first step defined; if blocked, fallback is operational not abstract
- [ ] Dependency & Escalation Layer: blocking graph explicit; fallbacks named; override rules for upstream slip explicit
- [ ] Phase-Level DoD Layer: phase stop conditions + minimum usable state + safe-to-stop markers documented
- [ ] Load Classification Layer: committed/contingent/overhead split clear + contingent conditions realistic
- [ ] Daily Inheritance Contract: each day has artifact, start step, stop condition, fallback columns + override rule if upstream dependent

**PHASE 13: ARTIFACT PLACEMENT QA (FILE PATH CORRECTNESS)**
- [ ] Weekly Plan file path matches: `03_PLANNING/03_WEEK/Wxx/2026-Wxx_WeekPlan.md` (includes week subfolder + full name)
- [ ] Weekly Execution file path matches: `03_PLANNING/03_WEEK/Wxx/2026-Wxx_Execution.md` (includes week subfolder + full name)
- [ ] Daily files created in: `03_PLANNING/04_DAY/Wxx/YYYY-MM-DD_Daily.md` (includes week subfolder + date-based name)
- [ ] If target week folders do not exist, they were auto-created (not skipped)
- [ ] No daily files exist under `03_PLANNING/03_WEEK/` folder (check for misplaced YYYY-MM-DD_Daily.md)
- [ ] No weekly files exist under `03_PLANNING/04_DAY/` folder (check for misplaced *_WeekPlan.md or *_Execution.md)
- [ ] Naming follows rules: full explicit names (2026-Wxx, YYYY-MM-DD), not generic (WeekPlan, Execution, dates only)

**FINAL SIGN-OFF (ALL 13 PHASES MUST PASS)**
- [ ] Count: All 13 phases above = PASS (if any = FAIL, file not ready)
- [ ] Generation procedure followed without shortcuts
- [ ] No vague anchors remain (scan document for forbidden words: "work on", "clarity", "foundation", "progress")
- [ ] Daily generation CAN proceed without re-planning
- [ ] File ready for execution (not further planning)

**If ANY phase shows FAIL:** Do NOT finalize. Revise until all 13 pass (including Placement QA). Weekly Execution is an execution blueprint, not a planning document.

**Realism Hardness Check:** If the file feels uncomfortably tight or has risky contingencies, that's realistic. If the file feels cosmetically clean (all tasks fit perfectly, all ambiguity ≤2, no real constraints, all contingent anchors 100% likely), something is gamed. Good weeks should have visible tension.
```

---

## 16. Reusable Execution Template

Use this command block to run weekly generation. Replace all placeholders before submitting.

```
TASK: Generate or update Weekly Execution file for <WEEK_NAME>

Procedure reference: 01_OS/04_OPERATIONS/WEEKLY_CONTROL/GENERATE_WEEKLY_EXECUTION.md
Mode: A (Execution Baseline) / B (Reconstruction) / C (Rebalance)

Inputs:
- WEEKPLAN_FILE: <path to WeekPlan, e.g. 03_PLANNING/03_WEEK/W11/2026-W11_WeekPlan.md> — PRIMARY INPUT
- CARRY_OVER_SUMMARY: <from WEEK_CLOSEOUT output of previous week>
- RECENT_DAILY_FILES: <list recent Daily files: 03_PLANNING/04_DAY/W10/2026-03-10_Daily.md, W10/2026-03-11_Daily.md, …>
- PROJECT_STATE_FILES: <path to project files if referenced in WeekPlan, e.g. 08_PROJECT_CONTEXT/Zephyr_CONTEXT.md — or SKIP>
- MONTH_FILE: <reference only, e.g. 03_PLANNING/02_MONTH/2026-03_March.md>
- WEEKLY_TEMPLATE_FILE: 05_TEMPLATES/TEMPLATE_Week_Final.md
- TARGET_WEEK_NAME: <YYYY-Www format, e.g. 2026-W11>
- TARGET_WEEK_RANGE: <date range, e.g. March 16–22, 2026>
- TARGET_WEEK_FILE: <output path WITH WEEK SUBFOLDER, e.g. 03_PLANNING/03_WEEK/W11/2026-W11_Execution.md>
- TARGET_DAILY_FOLDER: <output folder for daily files, e.g. 03_PLANNING/04_DAY/W11/>

Placement Rules (MANDATORY):
- Weekly files MUST be created in: 03_PLANNING/03_WEEK/Wxx/
- Daily files MUST be created in: 03_PLANNING/04_DAY/Wxx/
- If target week folder does not exist, create it automatically (do not ask for permission)
- Do NOT place daily files under 03_WEEK/ folder
- Verify placement using Gate 9 (Artifact Placement QA) before finalizing

Instructions:
1. Follow §9 (Data Collection) completely. Prioritize WeekPlan as source of truth; do NOT re-negotiate capacity or goals.
2. Follow the generation procedure exactly as defined in §10 (Steps 1–10).
3. Enforce dual-pool rules from §8 without exception.
4. Apply anchor rules from §11 without exception.
5. Apply carry-over rules from §12 without exception.
6. If Mode B (Reconstruction): follow §13 reconstruction rules strictly. State uncertainty.
7. If Mode C (Rebalance): preserve existing weekly structure while updating expectations based on new reality.
8. Run consistency check (§10 Step 9) before finalizing.
9. **Apply Gate 9 (Artifact Placement QA) before finalizing:** verify file paths match placement rules; no daily files under 03_WEEK/; target folders created as needed.
10. Produce report as specified in §10 Step 10.
11. Commit with message:
   "gen: weekly execution <WEEK_NAME> via <MODE> — <single-sentence focus description>"
   Example: "gen: weekly execution 2026-W11 via Mode A — RobotOS architecture clarity + Zephyr testing extend"
```

---

**Integration Notes:**

**Upstream precedents:**
- GENERATE_WEEKPLAN produces the WeekPlan that is the primary source for this procedure
- CAPACITY_ENGINE constraints are embedded in WeekPlan; this procedure inherits them
- WEEK_CLOSEOUT produces carry-over summary; used as input to execution baseline generation

**Downstream consumers:**
- INTEGRATE_DAILY inherits from Weekly Execution file
- PREPARE_NEXT_DAILY uses Weekly Execution file for daily anchor structure
- WEEKLY_REBALANCE modifies Weekly Execution file when drift occurs

**End-of-week feedback loop:**
- WEEK_CLOSEOUT closes the execution week and generates evidence
- UPDATE_PROJECT_CONTEXT uses that evidence to refresh project contexts
- Next week's GENERATE_WEEKPLAN reads fresh project contexts + carries forward carry-over
- Cycle repeats

---

> **Procedure version:** 2.0 (Refactored for current LIFE_AGENT architecture)  
> **Created:** 2026-03-15 | **Updated:** 2026-03-17  
> **Location:** `01_OS/04_OPERATIONS/WEEKLY_CONTROL/GENERATE_WEEKLY_EXECUTION.md`  
> **Periodic reuse trigger:** Once per week (execution baseline generation); on-demand for reconstruction/rebalance  
> **Next review trigger:** When CAPACITY_ENGINE changes OR when pool separation rules change OR when major operational pattern shift occurs
