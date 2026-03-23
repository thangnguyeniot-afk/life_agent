# UPDATE_PROJECT_CONTEXT

> **Type:** Operating Procedure  
> **Layer:** OS / Operations  
> **Scope:** Weekly execution outcomes → project context file updates  
> **Prerequisite:** WEEK_CLOSEOUT must be complete (accurate execution evidence available)  
> **Reuse:** Run once per week, immediately after WEEK_CLOSEOUT completes  
> **Related:** [`WEEK_CLOSEOUT.md`](../WEEKLY_CONTROL/WEEK_CLOSEOUT.md) | [`GENERATE_WEEKPLAN.md`](../WEEKLY_CONTROL/GENERATE_WEEKPLAN.md) | Project context files in `08_PROJECT_CONTEXT/`

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. When to Run](#2-when-to-run)
- [3. Guardian Rules](#3-guardian-rules)
- [4. Update Targets (Allowed Sections)](#4-update-targets-allowed-sections)
- [5. Stable Identity (Forbidden Changes)](#5-stable-identity-forbidden-changes)
- [6. Inputs](#6-inputs)
- [6.5 Execution vs Plan Consistency Validation (CRITICAL)](#65-execution-vs-plan-consistency-validation-critical)
- [7. Update Decision Logic](#7-update-decision-logic)
- [8. Decision Rules by Change Type](#8-decision-rules-by-change-type)
- [9. Output Contract](#9-output-contract)
- [10. Integration Points](#10-integration-points)
- [11. Examples by Project](#11-examples-by-project)
- [12. Standard Checklist](#12-standard-checklist)

---

## 1. Purpose

**Why this procedure exists:**

Project context files flow INTO the planning system (GENERATE_WEEKPLAN reads them to understand project state) but execution results do not flow back OUT (weekly closeout doesn't update them). This creates a one-way information model where planning becomes progressively stale.

UPDATE_PROJECT_CONTEXT closes the feedback loop:
- Reads factual execution outcomes from WEEK_CLOSEOUT
- Identifies material state changes (blocker resolved, phase ready to shift, effort learning)
- Updates ONLY the dynamic sections of project context files
- Preserves stable sections (philosophy, architecture, identity)
- Produces an update summary showing what changed and why
- Ensures next week's GENERATE_WEEKPLAN reaches for fresh project state, not stale assumptions

**What it does:**
- Validate execution evidence against current project state
- Identify state transitions (blocker → resolved, phase → advanced, focus → shifted)
- Update dynamic sections with factual evidence-based changes
- Produce minimal update summary with change classifications

**What it does NOT do:**
- Rewrite project history or philosophy
- Change architecture or strategic decisions
- Rewrite scope or long-term mission
- Create narrative or storytelling
- Substitute for WEEK_CLOSEOUT (happens AFTER closeout, not instead of)

---

## 2. When to Run

**Run UPDATE_PROJECT_CONTEXT when:**
- WEEK_CLOSEOUT is complete (execution evidence finalized)
- One or more projects had material state changes during the week
- WEEK_CLOSEOUT explicitly noted project state transitions
- Before next week's GENERATE_WEEKPLAN begins (so planning has fresh context)

**Also run UPDATE_PROJECT_CONTEXT MID-WEEK when:**
- Daily execution triggers a **STRONG Context Signal** (Type B or C; must pass anti-noise filter AND strength classification)
- Same task fails ≥ 2 times in same week WITH CONFIRMED root cause (not single occurrence)
- New blocker emerges with structural impact that affects ≥ 2 future sessions
- Plan assumption proves invalid with repeatable evidence (not single-session variance)
- Carry-over saturation pattern repeats (not isolated day)
- Mid-week discovery of Type C critical blocker (exception: bypasses cooldown + budget limits)

**STABILITY CONSTRAINTS for Mid-Week Updates (Anti-Thrashing):**

Before running mid-week UPDATE_PROJECT_CONTEXT, check:

1. **Cooldown Window (24h):** 
   - Has adaptive replan occurred in last 24 hours? 
   - If YES → must wait before next replan (UNLESS Type C critical blocker)
   - Type C exceptions: Critical blockers bypass cooldown
   - Rationale: Prevent rapid thrashing/overreaction

2. **Weekly Replan Budget (Max 2 per week):**
   - How many adaptive replans completed THIS week?
   - Limit: 2 per week maximum
   - If already 2 → must escalate to project owner instead of replanning
   - Rationale: Force escalation rather than endless replanning cycles

3. **Type C Exception:** 
   - Critical structural blockers (Type C) can bypass both cooldown AND budget limits if they block immediate execution
   - Example: "S3 access down" blocks ALL remaining Zephyr work → immediate escalation + emergency replan allowed
   - Use sparingly

**Do NOT run:**
- If project state is unchanged (no commit, no blocker movement, no progress)
- Speculatively (only if execution proved something changed)
- For Type A signals (unauthorized drift is rejected, no context update)
- For WEAK signals (log only; do not update context or replan)
- As substitute for WEEK_CLOSEOUT (that's a different operation)
- For trivial updates (cosmetic edits without structural impact)

**Typical timing:**
- **Weekly (standard):** Sunday evening after WEEK_CLOSEOUT, or Monday morning before GENERATE_WEEKPLAN
- **Mid-week (adaptive):** Same day or next morning after STRONG Context Signal detected (TEMPLATE_Daily.md signals trigger this)
- Goal: Context update within 24h of signal detection to allow GENERATE_WEEKLY_EXECUTION adaptive replan (subject to cooldown + budget)

---

## 3. Guardian Rules

**Cardinal rule: Only update what execution proved changed.**

All context updates must satisfy:

1. **Evidence requirement:** Must link to WEEK_CLOSEOUT result (artifact name, blocker resolution, phase decision) OR to daily Context Signal with documented trigger
2. **Relevance requirement:** Change must matter for planning next week (not cosmetic)
3. **Honesty requirement:** Update must reflect reality, not aspirations (blockers stay until unblocked, not "eventually")
4. **Traceability requirement:** Update must be datable and reversible (include week number, date, and signal type if mid-week triggered)

**CRITICAL — Execution Priority Override Rule:**

> **If execution discovers a conflict between the original plan and current context reality → Context ALWAYS wins.**
>
> Do NOT force execution to continue following a plan that proves invalid mid-week. Instead:
> 1. Detect the conflict via Context Signal (TEMPLATE_Daily.md signal detection)
> 2. Immediately update project context with evidence (same day)
> 3. Trigger GENERATE_WEEKLY_EXECUTION Adaptive Mode (next morning, or same day if critical)
> 4. Reorder/replan remaining week anchors based on updated context
> 5. Rationale: Execution with stale context is slower than adaptive replanning

**24-Hour Adaptation Constraint:**

> If a Context Signal (Type B or C) is detected during execution, the system must adapt within 24 hours. This means:
> - Signal logged same day (TEMPLATE_Daily.md close)
> - Context updated same day or next morning (UPDATE_PROJECT_CONTEXT mid-week mode)
> - Adaptive replan completed next morning (GENERATE_WEEKLY_EXECUTION Adaptive Mode)
> - Remaining anchors reordered/adjusted before next execution cycle
> 
> **Failure to adapt within 24h means:** execution continues with invalid assumptions, leading to wasted cycles and compounding drift.

**If in doubt:**
- DO NOT update
- Document the uncertainty as "OBSERVED but NOT YET ACTIONABLE" in notes
- Let next week confirm the change
- Exception: If signal suggests active blocker or hidden dependency, escalate immediately rather than waiting

---

## 4. Update Targets (Allowed Sections)

The following sections of a project context file MAY be updated:

### ✅ Current State

- **% Completion** — if artifacts were delivered or partial progress is measurable
- **Current Phase** — if phase transition evidence is conclusive
- **Milestone status** (In Progress / Completed / Deferred) — if milestone moved
- **Blocker status** (opened / closed / escalated) — if blocker list changed

### ✅ Current Phase (Section 2, Field 1)

May advance only if:
- Prior phase milestone completed with artifact evidence, AND
- No blockers preventing next phase entry

Examples of valid transitions:
- Research → Build (spike complete + decision made)
- Build → Stabilize (feature complete + integration stable)
- Stabilize → Delivery (testing passed + documentation ready)

### ✅ Current Focus

May shift if:
- Prior focus is substantially complete (delivery evidence), AND
- New focus is unblocked and ready to start

Example:
- From "Phase 1: RobotOS Architecture Clarification" to "Phase 2: Contributor Onboarding"

### ✅ Active Blockers

- Add new blocker if execution discovered it (with date and impact)
- Remove blocker if execution achieved resolution (with evidence)
- Escalate blocker if new severity/impact emerged
- Do NOT update status to "working on it" (that's planning, not execution)
- **Carry-over pattern evidence:** If the same work item carries over across multiple weeks tied to the same weekly goal, this may indicate a blocker that was not explicitly named. Review WEEK_CLOSEOUT carry-over list and update blocker status if the pattern suggests a hidden dependency or resource constraint.

### ✅ Recent Progress (or Recent Deliverables)

May add evidence of completed work if:
- Work closure was captured in WEEK_CLOSEOUT, AND
- Artifact or status is concrete (not aspirational)

Example:
- "W11: RobotOS architecture slides drafted; contributor onboarding materials prepared"

### ✅ Next Milestone

May shift if:
- Current milestone is clearly completed (artifact evidence), AND
- Prerequisite for next milestone is satisfied or removed

### ✅ Effort Reality Notes (if section exists)

May record learning if:
- Actual effort significantly diverged from estimate (>20% variance), AND
- Learning is actionable for next iteration

Example:
- "W11: Architecture documentation took 9h (estimated 7h); contributor onboarding materials substantially underestimated"

---

## 5. Stable Identity (Forbidden Changes)

The following sections of a project context file must NOT be changed by UPDATE_PROJECT_CONTEXT:

### ❌ Project Identity

- Project name
- Project mission / core objective
- Founding rationale
- Vision statement

### ❌ Architecture & Design

- Technical architecture overview
- Design philosophy or principles
- Technology stack (unless explicitly decommissioned by decision)
- Repository structure

### ❌ Long-Term Roadmap

- v0.1, v0.2, v1.0 long-term goals
- Strategic deadlines or release targets (unless explicitly extended by decision)
- Scope freeze decisions (only update if month-level decision made)

### ❌ Resource Model

- Role assignments (who owns what work) — update only if explicit reassignment decision made
- Human team structure

### ❌ Planning & Development Environment

- Build system setup
- Development environment instructions
- Testing framework decisions

**If any of these need updating, the change is STRATEGIC and must go through decision processes (month planning, project reviews), not through WEEK_CLOSEOUT feedback.**

---

## 6. Inputs

**Required inputs from WEEK_CLOSEOUT:**
- Project name (which project(s) had state changes?)
- Outcome summary (completed / partial / incomplete)
- Artifact names and status
- Blocker changes (resolved, new, escalated)
- Phase or milestone transitions (if any)
- Effort summary (hours planned vs. actual)

**Context from Weekly Execution:**
- W## number and date range
- Goals that were outcome-mapped to project work

**From current project context file:**
- Current state sections (baseline for comparison)
- Recent progress history

---

## 6.5 Execution vs Plan Consistency Validation (CRITICAL)

**Purpose:** Ensure that no plan assumption survives contact with execution without being questioned and updated.

This validation runs BEFORE any context update is made. It answers: "Does the actual execution align with the plans we made?"

### Consistency Check Procedure

For each completed work item from WEEK_CLOSEOUT, perform three checks in order:

#### CHECK 1 — Goal Traceability

**Question:** Does this completed work map to a stated Weekly Goal (from W## WeekPlan §2)?

**Outcomes:**

- **YES → OK (expected)**
  - Work is aligned with plan
  - Proceed to Check 2
  
- **NO → INVESTIGATE**
  - Classify as one of:
    - **Drift (unauthorized):** Work was not in WeekPlan; not documented as interruption/maintenance
      - ⚠️ Action: Escalate to Decision Log; do NOT silently accept as valid
      - If justified (blocker response, incident), mark as "Type B — Necessary Adaptation"
    - **Emergent Necessity:** Work discovered during execution as prerequisite for planned work
      - Action: Document as "Hidden Dependency; discover in future planning"
      - Mark as "Type C — Hidden Dependency"

#### CHECK 2 — Exit Condition Validation

**Question:** Does the actual artifact/output match the intended Exit Condition (from Weekly Execution anchor)?

**Outcomes:**

- **YES — Exact match → COMPLETE**
  - Work closure is as intended
  - No adjustment needed
  
- **PARTIAL match (weaker than Exit Condition) → DOWNGRADE COMPLETION**
  - Example: Exit Condition was "3 tests passing locally + merged"; actual was "2 tests passing, code not merged"
  - Action: Mark in WEEK_CLOSEOUT as "partial execution" not "complete"
  - Update context as "Partial progress toward [milestone]" not "[milestone] complete"
  - Impact on next week: Carry-over includes completion of merge
  
- **DIFFERENT (scope deviation from Exit Condition) → CLASSIFY DEVIATION**
  - Example: Exit Condition was "documentation PRs merged"; actual was "documentation drafted but not reviewed"
  - Action: Classify as "Type B — Necessary Adaptation: Scope shifted due to [reason]"
  - Update context with actual deliverable, not intended deliverable
  - Impact on next week: Adjust weekly allocation for "review + merge" vs. "new documentation"

#### CHECK 3 — Carry-over Loop Detection

**Question:** Has this same task (or a predecessor of it) carried over from a previous week tied to the same Weekly Goal?

**Outcomes:**

- **NO → Normal progression**
  - Work is new or newly completed
  - Proceed with normal update logic
  
- **YES (first repeat) → FLAG for attention**
  - Item carried over once before; now completed
  - Action: Document in context update; no escalation needed
  - Impact: Confirm blocker has been resolved (or was hidden in planning)
  
- **YES (multiple repeats, 2+ weeks) → BLOCKER ESCALATION TRIGGER**
  - Same work item has now carried over 2+ times tied to same goal
  - This indicates a hidden, persistent blocker that was not explicitly named
  - ⚠️ Action: MUST trigger blocker detection
  - Create new explicit blocker entry: "Persistent carry-over on [task name] — possible hidden dependency or effort underestimate"
  - Update Active Blockers section with this finding
  - Impact on next week: GENERATE_WEEKPLAN must read this blocker and adjust allocation or explicitly resolve the dependency

### Drift Classification (NEW)

All non-aligned execution must be labeled with one of three types for traceability:

#### Type A — Unauthorized Drift (REJECT)

**Definition:** Work was executed that:
- Was NOT in the Weekly Goals or carry-over
- Is NOT a documented blocker response or maintenance item
- Could not be justified as "emergent necessity"

**Example:** "Refactored test runner performance" when this was not a weekly goal and no blocker required it.

**Action:** 
- ⚠️ Escalate to Decision Log immediately (do NOT silently accept)
- Require explicit justification from executor
- If justified retroactively → convert to Type B
- If unjustified → document as scope violation and mark for retrospective

#### Type B — Necessary Adaptation (REQUIRE justification)

**Definition:** Work was executed that:
- Was NOT explicitly in WeekPlan, BUT
- Was necessary in response to:
  - A discovered blocker or dependency
  - An incident or interruption
  - A genuine trade-off decision made during execution

**Example:** "Rewrote test environment setup (not planned)" because original environment was unavailable and this was necessary to unblock the week's primary work.

**Action:**
- Document in context update: "W##: Type B Adaptation — [description of why it was necessary]"
- Link to the blocked work it enabled
- Use this as input to next week's planning (adjust baseline assumptions)

#### Type C — Hidden Dependency (UPDATE context)

**Definition:** Work was executed that:
- Was NOT in WeekPlan, but
- Was discovered during execution as a prerequisite for planned work
- Should have been included in planning but was missed

**Example:** "Implemented test data seeding" discovered to be necessary before running RAM loading tests (not planned separately; was hidden in "RAM tests").

**Action:**
- Document in context update: "W##: Type C Hidden Dependency — [task] discovered as prerequisite for [parent goal]"
- Add to project context as "Effort Reality Notes": estimate budget for this dependency in future planning
- This becomes input to CAPACITY_ENGINE for next cycle planning

### Drift Classification Decision Tree

```
Completed work NOT in WeekPlan?
├─ YES, AND no blocker/incident justification
│  └─ TYPE A (Unauthorized) → ⚠️ ESCALATE
│
├─ YES, AND discovered as blocker response / incident
│  └─ TYPE B (Necessary Adaptation) → Document + learn
│
├─ YES, AND hidden prerequisite for planned work
│  └─ TYPE C (Hidden Dependency) → Update context + effort notes
│
└─ NO
   └─ Normal path (Check 1 passed, proceed to Check 2)
```

---

## 7. Update Decision Logic

```
For each project mentioned in WEEK_CLOSEOUT output:

1. Did execution produce artifacts? → UPDATE: Recent Progress / Milestone status
2. Did execution resolve a blocker? → UPDATE: Active Blockers (remove/close)
3. Did execution discover new blocker? → UPDATE: Active Blockers (add with date)
4. Did execution prove phase transition? → UPDATE: Current Phase
5. Did execution demand next-milestone shift? → UPDATE: Next Milestone
6. Did execution reveal effort reality gap? → UPDATE: Effort Reality Notes
7. If none of the above → NO_CHANGE (document why, leave context stable)
```

**Key principle:** Each update must answer: "Will the planner in next GENERATE_WEEKPLAN make different decisions with this new context?"

If the answer is NO, do not update (context is still accurate).

---

## 8. Decision Rules by Change Type

### STATE_UPDATE (% Completion, Phase, Milestone Status)

**Trigger:** Artifact delivery + acceptance visible in WEEK_CLOSEOUT output.

**Decision rule:**
- If milestone artifact is merged/committed/accepted → mark milestone complete
- If phase prerequisites met → allow phase transition
- If completion percentage can be incremented by artifact delivery → update it
- If completion is uncertain → use "Observed in W##" language; do not finalize

**Example:**
```
OLD: Current State → % Completion [18%]
NEW: Current State → % Completion [25%]
Evidence: W11 - RobotOS architecture slides, contributor onboarding materials delivered; 
          M1 completion evidence acquired; M2 prerequisites satisfied
```

### FOCUS_UPDATE (Current Focus, Focus Area)

**Trigger:** Prior focus substantially complete + next focus is unblocked.

**Decision rule:**
- Prior focus completion must have artifact evidence
- Next focus must not have active blockers
- Shift happens only between weeks (not mid-week)
- Document the transition reason

**Example:**
```
OLD: Current Focus → Architecture Clarification & Onboarding Preparation
NEW: Current Focus → M2 Middleware Core Implementation Initiation
Evidence: W11 - Architecture materials accepted by team; onboarding completed for 2 contributors; 
          M1 prerequisites for M2 satisfied
```

### BLOCKER_UPDATE (Active Blockers table)

**Decision rule:**

**For removing a blocker:**
- Blocker resolution evidence must be in WEEK_CLOSEOUT (artifact merged, decision made, dependency satisfied)
- Update blocker status to "RESOLVED — W##"
- Or remove row entirely if not needed for history

**For adding a blocker:**
- Blocker must have been discovered during week (noted in Daily files or WEEK_CLOSEOUT)
- Must have severity assessment (HIGH / MEDIUM / LOW)
- Must have named impact (blocks what work?)
- Include workaround if applicable

**For escalating a blocker:**
- If impact or severity increased → update severity and new impact statement
- Document evidence of escalation

**Example:**
```
OLD: Blocker 1 | Status: Unresolved | Blocked equipment delivery | MEDIUM | Workaround: mock testing setup

NEW: [RESOLVED — W11] Equipment delivery confirmed for W12 (equipment arrived Mon 3/17)

NEW: Blocker 2 | Status: Unresolved | Native developer unavailable for integration sprint | HIGH | Workaround: Signee team lead covering; rescheduling integration to W12 EOW | Opened W11
```

### MILESTONE_UPDATE (Next Milestone)

**Decision rule:**
- Current milestone completed (artifact + acceptance evidence) → advance milestone
- Prerequisite for next milestone discovered missing → shift target
- Milestone timeline needs adjustment → update target date

**Example:**
```
OLD: Next Milestone | M2: Middleware Core | Target: 2026-03-31

NEW: Next Milestone | M2: Middleware Core + Contributor Onboarding B2 | Target: 2026-04-07
Evidence: W11 - M1 completed; contributors onboarded; M2 prerequisite buffer expanded due to onboarding load
```

### EFFORT_UPDATE (Effort Reality Notes)

**Decision rule:**
- Actual effort diverged from estimate by >20% AND
- Learning is actionable for next iteration (not just "took longer than expected")

**Example:**
```
NEW: Effort Learning — W11: Architecture documentation & contributor onboarding took 12h (estimated 10h baseline + 2h optional weekend daytime). Onboarding load substantially underestimated; allocate 3–4h per new contributor in future planning. Evening capacity fully utilized; weekend daytime necessary for completion buffer.
```

### NO_CHANGE (Project State Stable)

**Decision rule:**
- Week produced carry-over (incomplete but not a state change)
- Week had expected partial progress (no new artifact completion threshold reached)
- Blockers remain active and unchanged
- Phase/milestone not ready to transition

**Action:** Document why NO_CHANGE is appropriate; leave context file untouched.

**Example logging (in closure notes, not in context file):**
```
UPDATE_PROJECT_CONTEXT: RobotOS — NO_CHANGE
Reason: W11 delivered architecture materials (IN PROGRESS toward M1); M1 not yet complete (prerequisite: team review + decision acceptance); phase remains Build; blocker status unchanged.
Next update trigger: W12 after team review completion.
```

---

## 9. Output Contract

When UPDATE_PROJECT_CONTEXT completes, produce:

### Execution Reality Report (NEW — MANDATORY)

**Purpose:** Classify and document all execution outcomes against planned anchors.

**Structure:**

```markdown
## Execution Reality Report — W## (Consistency Validation)

### Completed As Planned

- [Project]: [Goal] executed exactly as defined in WeekPlan
  - Expected Exit Condition: [condition]
  - Actual: ✓ Met
  - Artifacts delivered: [list]
  - Impact: [none / enables next phase / resolves blocker]

### Completed But Deviated

- [Project]: [Goal] completed with scope deviation
  - Expected Exit Condition: [condition]
  - Actual: [what actually delivered]
  - Deviation type: [weaker output / different output / scope shift]
  - Reason: [why deviation occurred, if captured in Daily notes]
  - Drift classification: [Type B — necessary adaptation / Type A — unauthorized (if applicable)]

### Unplanned But Executed

- [Project]: [Task] was NOT in WeekPlan but was executed
  - Strategic link: [ties to what weekly goal, if any]
  - Drift classification: [Type A — unauthorized / Type B — necessary adaptation / Type C — hidden dependency]
  - Justification: [why it was necessary]
  - Impact: [enables / delays / clarifies what work]

### Planned But NOT Executed

- [Project]: [Goal] was in WeekPlan but not completed
  - Status: [incomplete / blocked / deferred / dropped]
  - Reason: [if captured in WEEK_CLOSEOUT]
  - Blocker: [if applicable; name the blocker]
  - Carry-over plan: [carries to W##, condition for execution, re-entry mode]

### Carry-over Loop Detection

- [Project]: [Task] has carried over [N] weeks
  - Weekly goals tied to: [goals 1, 2, ...]
  - First carry-over: W##
  - Pattern: [Normal progression / Possible hidden blocker / Effort underestimate]
  - If 2+ repeats: **Escalate as hidden blocker** ⚠️
```

### Updated Project Context File

- Updated sections only (no other changes)
- Sections updated marked with date tag
- Links to WEEK_CLOSEOUT evidence if complex

### Update Summary Report

Format:

```markdown
## UPDATE_PROJECT_CONTEXT — [Project Name] — W## Update

**Date:** [closure date]  
**Week:** [W## / date range]  
**Status:** UPDATE / NO_CHANGE

### Changes Applied

**[CHANGE_TYPE]: [Section Name]**
- Old value: [what was there]
- New value: [updated to]
- Evidence: W## - [artifact/result from WEEK_CLOSEOUT]

**[CHANGE_TYPE]: [Section Name]**
- ...

### Summary

- Artifact(s) delivered: [count & names]
- Blocker(s) resolved: [count & which ones]
- Blocker(s) new: [count & which ones]
- Phase transition: [Y/N — which transition if yes]
- Milestone shift: [Y/N — which shift if yes]
- Effort learning: [Y/N — what learned if yes]

### Effect on Next Week Planning

If GENERATE_WEEKPLAN for W##+ 1 reads this context:
- [Will it make different capacity allocation decisions? How?]
- [Will it allow different scope? Why?]
- [Will it shift focus? To what and why?]

### No Changes to

- Project identity ✅
- Architecture & design ✅
- Tech stack ✅
- Long-term roadmap ✅
- (List any stable sections preserved)
```

---

## 10. Integration Points

### Into WEEK_CLOSEOUT.md

Add this note to Section 12 (Month & Project Feedback Rules):

```markdown
### Project Context Updates via UPDATE_PROJECT_CONTEXT

**When to run UPDATE_PROJECT_CONTEXT:**
- Immediately after WEEK_CLOSEOUT completes (if project state changed materially)
- Only if WEEK_CLOSEOUT identified artifact delivery, blocker resolution, or phase transition

**What UPDATE_PROJECT_CONTEXT does:**
- Updates project context files (ROBOTOS_CONTEXT.md, Signee_CONTEXT.md, Zephyr_Project_Context.md)
- Uses WEEK_CLOSEOUT evidence to inform state changes
- Does NOT rewrite project history or architecture
- Produces update summary with change classifications

**Result:** Next week's GENERATE_WEEKPLAN reads fresh project context, not stale assumptions.

See: `01_OS/04_OPERATIONS/PROJECT_CONTROL/UPDATE_PROJECT_CONTEXT.md`
```

### Into GENERATE_WEEKPLAN.md

Add this note to the "Inputs" section (Project Context Files):

```markdown
### Project Context Freshness

**Important:** Project context files should be read as current if they have been updated within
the last week by UPDATE_PROJECT_CONTEXT.md. If no update was made, context is last-updated
at the date shown in the file header.

If a project context file is stale (>1 week without update), and you suspect material changes
have occurred, flag for mid-week UPDATE_PROJECT_CONTEXT run or ask questions before treating
context as authoritative.

Project contexts are inputs to planning, not outputs. Their freshness matters.
```

---

## 11. Examples by Project

### Example 1: RobotOS (Artifact Delivery → Phase Boundary)

**WEEK_CLOSEOUT Summary:**
```
W11 Closing:
- RobotOS: Goal 1 (Architecture Clarification) scope complete
  - Artifacts: slides, architecture diagram, contributor onboarding materials
  - Team: 2 contributors onboarded
  - Next milestone: M2 Middleware Core Implementation ready to start
  - No blockers; prerequisites satisfied
```

**UPDATE_PROJECT_CONTEXT Decision:**
- STATE_UPDATE: % Completion [15% → 25%]; Milestone M1 → COMPLETE
- FOCUS_UPDATE: "Architecture Clarification" → "M2 Core Implementation"
- NO_CHANGE: Phase remains Build (prerequisites for Stabilize phase not yet met)
- EFFORT_UPDATE: Onboarding load documented as learning

**Result:**
```markdown
## UPDATE_PROJECT_CONTEXT — RobotOS — W11 Update

Changes Applied:

**STATE_UPDATE: Current State**
- % Completion: [15%] → [25%]
- Milestone 1 (Kernel & Build System Foundation): COMPLETE (W11)
- Evidence: W11 - RobotOS architecture slides, diagrams, contributor onboarding materials delivered

**FOCUS_UPDATE: Current Focus**
- [Architecture Clarification & Onboarding] → [M2: Middleware Core Implementation]
- Evidence: W11 - M1 scope complete; 2 contributors onboarded; M2 prerequisites satisfied

**EFFORT_UPDATE: Learning**
- Onboarding load significantly underestimated; future contributor additions should allocate 3–4h per person in personal evening capacity

**NO_CHANGE: Phase**
- Build phase continues (Stabilize phase requires testing infrastructure + documented Examples, not yet complete)

Effect on W12 Planning:
- GENERATE_WEEKPLAN will allocate RobotOS ~7–10h (M2 implementation) instead of ~7h (M1 architecture)
- Capacity assumes 2 active contributors available for code review
- Next blocker check: None current; prerequisites satisfied for M2 execution path
```

---

### Example 2: Signee (Blocker Resolution)

**WEEK_CLOSEOUT Summary:**
```
W11 Closing:
- Signee: Goal 3 (Testing Specification) scope complete DESPITE equipment blocker unresolved
  - Artifacts: test sets, quality gate definitions, testing checklist
  - Equipment status: Confirmed delivery W11 Mon 3/17; board available for W12
  - Blocker resolved: Equipment delivery
  - New blocker: None
```

**UPDATE_PROJECT_CONTEXT Decision:**
- BLOCKER_UPDATE: Remove "Equipment delivery" blocker; add W12 integration complexity warning
- EFFORT_UPDATE: Specification work proceeded despite external blocker (learning for future)

**Result:**
```markdown
## UPDATE_PROJECT_CONTEXT — Signee — W11 Update

Changes Applied:

**BLOCKER_UPDATE: Active Blockers**
- [RESOLVED — W11] Equipment delivery blocker
  - Resolution: Hardware delivery confirmed Monday 3/17; board available for W12 board testing phase
  
- [NEW — W11] Integration complexity with native developer implementations
  - Severity: MEDIUM
  - Impact: Board testing (TYPE E — W12) depends on native team completing Android/PWA pieces in parallel with board setup
  - Workaround: Run unit testing and mock integration first (W12 early); hardware integration later if needed

**EFFORT_UPDATE: Learning**
- W11: Testing specification proceeded independently of equipment blocker (positive learning)
- Specification effort: 5h actual (estimated 3h baseline)
- Learning: Specification complexity greater than estimated; account for inter-component specification overhead in future planning

Effect on W12 Planning:
- GENERATE_WEEKPLAN will NOT skip Signee work due to equipment blocker (it's resolved)
- W12 capacity: Add ~2–3h for board integration testing setup (equipment now available)
- Risk reduced: TYPE E conditional work can now proceed
```

---

### Example 3: Zephyr (Stable / No Change)

**WEEK_CLOSEOUT Summary:**
```
W11 Closing:
- Zephyr: Goal 2 (Test Infrastructure) ongoing
  - Artifacts: RAM loading tests merged; factory setting analysis in progress
  - Blocker status: None new; existing maintenance rhythm stable
  - Phase: Stable Delivery & Controlled Improvement (continues)
```

**UPDATE_PROJECT_CONTEXT Decision:**
- NO_CHANGE: Phase continues (Stable Delivery)
- NO_CHANGE: Focus continues (Release preparation + DBUS2 testing)
- NO_CHANGE: % Completion (incremental maintenance work)
- EFFORT_UPDATE: Testing infrastructure load on track with estimates

**Result:**
```markdown
## UPDATE_PROJECT_CONTEXT — Zephyr — W11 Update

**Status:** NO_CHANGE

Reason: W11 produced expected incremental progress toward Stable Delivery phase (tests merged, analysis on track). No milestone completion threshold reached. No blocker changes. Phase continues; no transition signal.

Context file remains valid for W12 planning.

---

**Effect on W12 Planning:**

GENERATE_WEEKPLAN will continue allocating Zephyr to office hours only (~12–15h/week maintenance + ongoing test work). No capacity or focus shifts needed.
```

---

## 12. Standard Checklist

**Before running UPDATE_PROJECT_CONTEXT:**

- [ ] WEEK_CLOSEOUT is complete and outputs are available
- [ ] W## number and exact date range are identified
- [ ] Project context files are accessible and current
- [ ] WEEK_CLOSEOUT summary identifies which projects had state changes
- [ ] Current context file section headers and structure are known (each project file may vary slightly)

**During UPDATE_PROJECT_CONTEXT:**

- [ ] Evidence-linking rule applied: each update links to WEEK_CLOSEOUT or artifact
- [ ] Stability rule applied: no changes to identity, architecture, roadmap, resource model
- [ ] Honesty rule applied: updates reflect reality (blockers stay until unblocked; uncertainties marked)
- [ ] Traceability rule applied: all updates dated and reversible

**After UPDATE_PROJECT_CONTEXT:**

- [ ] Update summary report completed (change types + evidence listed)
- [ ] Project context file updated with change(s)
- [ ] Checklist items verified
- [ ] Integration notes added to WEEK_CLOSEOUT.md and GENERATE_WEEKPLAN.md (first time only)
- [ ] Next week's GENERATE_WEEKPLAN will use fresh context

---

## Minimal Correction Principle

**State clearly: Only update what execution proved changed.**

This procedure does not:
- Guess at future state
- Assume progress without evidence
- Create aspirational context ("we will...")
- Update for potential changes

It does:
- Update based on artifacts delivered
- Update based on blockers resolved
- Update based on phase transitions proved
- Update based on effort learning discovered

When in doubt: observe, don't update.

