# Daily Plan – YYYY-MM-DD

> **Readability rule (Agent-Generated Content):** Keep paragraphs ≤3–4 lines. Use bullets for multi-part items. Format times/tasks/constraints as lists. See GENERATE_WEEKLY_EXECUTION.md § Readability Guard.

> **Placement rule (CRITICAL FOR ORGANIZATION):** This file must be created at: `03_PLANNING/04_DAY/Wxx/YYYY-MM-DD_Daily.md` (where Wxx = W09, W10, W11, etc. based on the week the date belongs to). Do NOT place daily files under `03_PLANNING/03_WEEK/` folder. If target week folder does not exist, create it automatically. Folder placement is part of artifact semantics: weekly files go in `03_WEEK/Wxx/`, daily files go in `04_DAY/Wxx/`. Do not mix layers.

---

## Table of Contents

- [Context](#context)
- [Source](#source)
- [Daily Project Scope Rule (Critical)](#daily-project-scope-rule-critical)
- [Work Time Domain (Critical)](#work-time-domain-critical)
- [Morning Setup (5 min)](#morning-setup-5-min)
- [Canonical Daily Anchors](#canonical-daily-anchors)
- [Office Hours – Deep Work](#office-hours--deep-work-mon--fri-900--1730)
- [Evening – Personal Projects](#evening--personal-projects-1730-or-weekend)
- [Signals (check if occurred)](#signals-check-if-occurred)
- [Optional — Delegations / Handoffs](#optional--delegations--handoffs)
- [Shutdown (10 min)](#shutdown-10-min)
- [DoD (Daily closure)](#dod-daily-closure)
- [Human Reflection (Optional)](#human-reflection-optional)

> **Active rules:** Daily Project Scope Rule (max 2 anchors) · Work Time Domain (office = Zephyr; evening = personal) · Evening Capacity Guard (weekday evening max: 1×M or 2×S; no L tasks) · Re-entry Guard (unfinished meaningful work must leave a re-entry package) — see OS §12.7–12.10

---

## Context

**Date:** YYYY-MM-DD

**Week:** YYYY-Www

**Energy level:** [ ] Low [ ] Normal [ ] High

**Focus theme:** (optional; 1–2 words if needed)

---

## Anti-Drift Rule (CRITICAL)

**Daily files are execution artifacts, not planning sessions.**

Every meaningful daily work must trace directly to a **Weekly Goal** (from WeekPlan §2). Free-floating improvement, exploration, optimization, or refactoring tasks are prohibited unless explicitly tied to a weekly goal or labeled as:
- Interruption / incident response
- Maintenance / blocker response  
- Carry-over from a previously valid execution line

If a task cannot be traced to a weekly goal, do not execute it. Escalate or defer.

---

## Source

> Weekly commitments listed by **project and mission** — not by anchor label. Anchor labels belong in Canonical Daily Anchors only.
> Weekly commitments → Daily execution.
> Daily does NOT create new commitments without explicit escalation.
> If day collapses: capture only main artifact + unfinished + next step.
> Daily blocks should originate from admitted tasks (Task Intake & Admission passed). If a block feels artifact-less or ambiguous, flag in Signals — do not force execution on unresolved work.

**Inherited from Weekly Anchor Map** *(copy the relevant day row from WeekPlan §7)*:
- Office Hours anchor: (paste from map — `<Project> — <phase>`)
- Evening anchor: (paste from map — `<Project> — <phase>` or none)
- Artifact direction: (paste from map)
- **Expected energy mode:** (paste from map — **planning hypothesis**; if actual energy differs, downgrade capacity/work type before changing anchor identity)
- **Evening capacity:** (paste from map — e.g., `1×M` / `S-only` / `none`)
- Risk / flex note: (paste from map if relevant)

---

## Daily Project Scope Rule (Critical)

> **Operating constraint:** A normal execution day contains **max 2 active projects** (Primary Anchor + Secondary Anchor).
> - All Deep Work Blocks must map to one of these 2 anchors only.
> - All support / admin work must belong to Office Hours or Evening domain; no standalone third zone.
> - Key questions and shutdown notes should reference only these 2 anchors on normal days.
> - A third project may appear only as: incident, escalation, or administrative mention (not active work).
> - **Exception:** Planning or review days may legitimately reference 3+ projects; mark these explicitly as review-day exceptions.

---

## Work Time Domain (Critical)

> **Operating boundary:** Office hours (Mon–Fri, 8:00–17:30) are reserved for **Zephyr work only**.
> 
> **Personal projects** (RobotOS, Signee baseline, prototyping, research spikes, or experimental work) **must be scheduled in evening blocks** (17:30+ or weekend time).
> 
> - **Why:** Protects core work time for primary responsibility (Zephyr); prevents office-hours fragmentation.
> - **Rationale:** Zephyr has external dependencies and team sync windows; personal projects have flexible timing and can absorb evening energy without cost.
> - **No exceptions:** Personal projects do NOT enter office hours under any framing — not "hard deadline," not "escalation," not "remaining office capacity." Office = Zephyr. If a personal project conflict arises, escalate to the Decision Log and resolve at week-planning level; do not override office-hours boundary inline.

**Default rule (no exception needed):**
- Zephyr blocks → Office Hours section
- RobotOS, Signee, personal work → Evening section

---

## Morning Setup (5 min)

**Work Time Domain Check:**
- **Office Hours domain:** Zephyr *(domain confirmed; full anchor defined in Canonical Daily Anchors below)*
- **Evening domain:** [RobotOS / Signee / personal / none] *(domain confirmed; full anchor defined below)*
- **Exception to Work Time Domain Rule?** [ ] No (default) [ ] Yes — justify below
  - *If yes, which project? Why must it be in office hours?*

**Re-entry Block Check** *(if any spillover from previous day):*
- [ ] No inherited spillover (day starts fresh)
- [ ] Yes, inherited spillover from previous day
  - *Project/anchor:* …
  - *Re-entry mode required:* [ ] Quick (Structured/Closure — resume at last state) [ ] Analytical (Synthesis/planning — restore reasoning chain) [ ] Fragile (Integration/merge — inspect state + validate)
  - *First re-entry action:* (concrete 5–10 min context-reload step; e.g. "review Mon Shutdown notes + reopen test file + confirm current branch state")

**Evening Capacity Mode** *(weekday only; inherit from §6.8 + §7 — confirm or downgrade only; do not silently upgrade on weak-energy days):*
- [ ] `1 × M` — one meaningful block (default normal day)
- [ ] `2 × S` — two light blocks
- [ ] `S-only` — energy degraded; keep only most strategic task
- [ ] `None` — office-only day or rest evening

**Reason for tonight's capacity mode:**  
(e.g.: normal office day / poor sleep / heavy workout / heavy meetings / recovery evening)

---

## Semantic Quality Requirements (CRITICAL)

**Purpose:** Eliminate vague language that prevents execution clarity. All anchors must be specific, artifact-focused, and verifiable.

### Rule 1 — No Generic Language (FORBIDDEN)

The following patterns are **NOT ALLOWED** in any anchor:

- "work on"
- "improve"
- "optimize"
- "handle"
- "continue"
- "fix stuff"
- "do testing"
- "make progress on"

**If detected → validation FAIL**

**Examples:**

✗ BAD: "Improve test infrastructure"  
✓ GOOD: "Add RAM loading test cases to test_memory.c; target: 3 cases passing locally"

✗ BAD: "Work on RobotOS architecture"  
✓ GOOD: "Finalize adapter boundary in architecture_diagram.drawio; export diagram + document motivation"

✗ BAD: "Handle testing"  
✓ GOOD: "Run test suite for STM32 integration; document failures; prepare PR"

---

### Rule 2 — Concrete Artifact Requirement (MANDATORY)

Every anchor MUST reference at least one specific deliverable:

- **File or component name** (e.g., "architecture_diagram.drawio", "test_memory.c", "setup.md")
- **Specific output artifact** (e.g., "diagram exported", "PR created", "documentation merged")
- **Measurable state** (e.g., "3 tests passing", "merge complete", "review approved")

**Test:** If someone else reads this anchor, can they name the artifact that will exist after completion?

**If NO → rewrite until YES**

**Examples:**

✓ GOOD: "Create adapter layer class in kernel.cpp; initial implementation with boundary validation"  
✓ GOOD: "Update Signee test checklist document (test_checklist.md); add quality gate criteria; commit to docs/"  
✓ GOOD: "Zephyr: merge RAM loading tests to develop branch; confirm CI passing"

✗ BAD: "Continue work on adapter"  
✗ BAD: "Update testing stuff"  
✗ BAD: "Polish the code"

---

### Rule 3 — Exit Condition Must Be Verifiable (MANDATORY)

Exit Condition must be:

- **Observable** (checkable by visual inspection or automated tool)
- **Binary** (true/false; either met or not met)
- **Not subjective** (not "good enough" or "looks okay")

**Test:** Could a third party (or Copilot) verify this without asking for clarification?

**If NO → rewrite until verifiable**

**Examples:**

✓ GOOD: "Diagram exported to SVG and committed to docs/"  
✓ GOOD: "PR submitted to develop branch; CI pipeline passing"  
✓ GOOD: "3 test cases passing locally; all assertions green; no warnings"  
✓ GOOD: "Documentation file updated with 4 motivation paragraphs; merged to main"

✗ BAD: "Done with testing"  
✗ BAD: "Looks good"  
✗ BAD: "Mostly complete"  
✗ BAD: "Good progress"  
✗ BAD: "Improved enough"

---

### Rule 4 — Minimum Meaningful Scope

Each anchor must represent **≥ 45–90 minutes** of meaningful progress.

- If progress is smaller → merge with adjacent anchor or combine with support work
- Prevents artificial anchor fragmentation
- Ensures each anchor is worth tracking

**Example fragmentation (BAD):**
- Anchor 1: "Open test file" (5 min)
- Anchor 2: "Review requirements" (10 min)
- Anchor 3: "Create first test" (15 min)

**Corrected (GOOD):**
- Anchor: "Review test requirements, create initial test structure, first test passing locally" (45 min combined)

---

### Rule 5 — Strategic Coherence Check

Each day's anchors must answer:

> "If all anchors complete successfully, what meaningful progress toward the weekly goal is achieved?"

**If the answer is unclear → validation FAIL**

Merge or reframe until the answer is clear.

**Example coherence check:**

Day: Monday; Primary anchor: "RAM loading test prep"; Secondary anchor: "Architecture outline"

Question: "If both anchors complete, what is achieved?"

Answer: "Zephyr testing infrastructure has test scaffold ready for implementation; RobotOS team has architecture clarity for contributor onboarding." → ✓ CLEAR

If answer were: "Did some things" → ✗ VAGUE → rewrite anchors

---

## Canonical Daily Anchors

> **Single source of truth for anchor identity.** All blocks, shutdown entries, and DoD items refer back to these names.
> **Derived from:** Weekly Anchor Map (`WeekPlan §7`, today's row) — refine here; do not reinvent.
> **Anchor Stability:** Weekly defines identity. Daily confirms, refines, or downgrades. Do not redefine anchor identity unless there is an incident, hard blocker, or explicit escalation — document the reason if identity changes.
> **Format rule:** `<Project> — <task/phase>` — no cross-project purpose text; no "so X can proceed" phrasing; artifact or justification text belongs in Purpose or Expected Artifacts, not the anchor line.
> **Traceability rule:** Every meaningful anchor MUST have a Linked Weekly Goal. If work cannot be traced to a weekly goal, do not execute it.
> **Semantic Quality rule:** Every anchor must satisfy Rules 1–5 above: no generic language, concrete artifact, verifiable exit, minimum 45–90 min scope, strategic coherence.
> **Re-entry note:** If this day inherits spillover from a prior day, re-entry is a continuation **pre-step** (5–10 min), not a new anchor. It belongs to the inherited anchor path. Use the re-entry mode and first action defined in Morning Setup above; do not create a second anchor for re-entry.

### Primary Execution Anchor

**Anchor name:** [Project] — [task/phase]  
*(e.g., Zephyr — validate STM32F4 toolchain setup and flashing pipeline)*

**Linked Weekly Goal:**  
*(exact weekly goal name or exact committed sub-goal from WeekPlan §2)*
*(MANDATORY; if this anchor is not tied to a weekly goal, do not execute it)*

**Focus:**  
*(the specific focus area for today's execution of this anchor)*

**First Strike:**  
*(the exact, concrete first action to begin this anchor — specific enough to start immediately without re-analysis)*  
*(MANDATORY for deep-work anchors; may be brief for light/admin anchors)*

**Execution Window:**  
*(time window and blocks; inherited from system schedule)*

**Exit Condition:**  
*(the exact artifact or state that defines completion of this anchor's session)*  
*(MANDATORY for deep-work anchors; examples: "diagram exported", "draft committed", "3 tests passing locally")*

**Carry-over Rule:**  
*(if incomplete, what spills to next day and how it re-enters)*

**Next Step (REQUIRED — Choose One):**
- [ ] **Continue:** Define next action for tomorrow (e.g., "Resume at test case 10; implement remaining cases")
- [ ] **Transfer:** Pass to (person/role/system); define hand-off criteria
- [ ] **None:** Explicitly no follow-up; anchor is complete and closed

**Purpose / Scheduling Rationale:**  
*(why this anchor today — 1 line; downstream enablement belongs here, not in anchor identity)*

---

### Secondary Execution Anchor

**Anchor name:** [Project] — [task/phase]  
*(e.g., RobotOS — consolidate architecture spike findings)*  
*(leave blank if office-hours-only day)*

**Linked Weekly Goal:**  
*(exact weekly goal name or exact committed sub-goal from WeekPlan §2)*  
*(MANDATORY if anchor exists)*

**Focus:**  
*(the specific focus area for today's execution of this anchor)*

**First Strike:**  
*(the exact, concrete first action to begin this anchor)*  
*(MANDATORY for deep-work anchors)*

**Exit Condition:**  
*(the exact artifact or state that defines completion of this anchor's session)*  
*(MANDATORY for deep-work anchors)*

**Carry-over Rule:**  
*(if incomplete, what spills to next day and how it re-enters)*

**Next Step (REQUIRED — Choose One):**
- [ ] **Continue:** Define next action (e.g., "Complete remaining 3 test cases; resuming Wed afternoon")
- [ ] **Transfer:** Pass to (person/role); hand-off criteria
- [ ] **None:** Complete; no follow-up required

**Purpose / Scheduling Rationale:**  
*(why this anchor today — 1 line)*

---

**1 Most Important Outcome today:**
(one sentence; may reference both anchors' combined effects; must not collapse both projects into one anchor statement)

**Daily Expected Artifacts:**
- [Primary project]: [specific artifact]
- [Secondary project]: [specific artifact, if applicable]

---

## Office Hours – Deep Work (Mon–Fri 8:00–17:30)

> **Time domain:** Standard office hours. **Zephyr work only** (primary responsibility). If evening project must run here, mark exception in Morning Setup.

### Block 1 (90 min) — Zephyr Primary
- **Anchor:** [Primary Anchor from Canonical Daily Anchors above]
- **Goal:** …
- **Size (S / M / L):** …
- **Ambiguity (0–5):** …
- **Expected Artifact:** …
- **First Step:** [Must match "First Strike" from Canonical Daily Anchors above]
- **Exit Condition:** [Must match "Exit Condition" from Canonical Daily Anchors above]

### Block 2 (90 min) — Zephyr Primary
- **Anchor:** [Primary Anchor]
- **Goal:** …
- **Size (S / M / L):** …
- **Ambiguity (0–5):** …
- **Expected Artifact:** …
- **First Step:** …
- **Exit Condition:** [Block completion: artifact must match daily artifact expectation]

### Block 3 (optional) — Zephyr Primary only
- **Anchor:** [Primary Anchor] ← if exception applies, mark [ ] Exception in Morning Setup
- **Goal:** …
- **Size (S / M / L):** …
- **Ambiguity (0–5):** …
- **Expected Artifact:** …
- **First Step:** …
- **Exit Condition:** [Completion state for this block]

> If any office-hours block is unfinished at day close, capture a re-entry note in Shutdown before closing the day.

**Office Hours — Support / Admin** *(optional; Zephyr-side only; Size S)*
- **Task:** … | **Goal:** … | **Artifact:** …

---

## Evening – Personal Projects (17:30+ or weekend)

> **Time domain:** Evening blocks, weekends, or flexible-time slots. For RobotOS, Signee baseline work, prototyping, research, or secondary projects.

> **Evening Capacity Guard (weekday rule):**  
> - Max 1 primary evening block + optional 1 light support block  
> - No L-sized tasks on weekday evenings  
> - If ambiguity is high, reduce scope before scheduling  
> - Allowed patterns: `1×M` | `2×S` | `1×S` (degraded energy)  
> - Capacity mode set in Morning Setup

### Block 1 (60–90 min) — Primary evening block
- **Anchor:** [Secondary Anchor from Canonical Daily Anchors above]
- **Goal:** …
- **Size (S / M / L):** … ← no L on weekday evenings
- **Ambiguity (0–5):** …
- **Expected Artifact:** …
- **First Step:** [Must match "First Strike" from Canonical Daily Anchors above]
- **Exit Condition:** [Must match "Exit Condition" from Canonical Daily Anchors above]
- **Evening role:** [Primary]

### Block 2 (optional) — Support block only
- **Anchor:** [Secondary Anchor or support task]
- **Goal:** … ← keep this S-sized; support/admin/light only if Block 1 is M
- **Size (S / M / L):** S
- **Ambiguity (0–5):** …
- **Expected Artifact:** …
- **First Step:** …
- **Exit Condition:** [Support block completion: artifact expected]
- **Evening role:** [Support]

**Evening — Support / Follow-up** *(optional; personal projects only; Size S)*
- **Task:** … | **Goal:** … | **Artifact:** …

---

**Note:** If no evening blocks are needed, leave this section empty. If capacity mode is `S-only`, use Block 1 only and defer Block 2. If any evening block is unfinished, capture a re-entry note in Shutdown before closing.

---

## Signals (check if occurred)

- [ ] Task ambiguity unexpectedly high
- [ ] Execution blocked by dependency
- [ ] Energy collapse mid-day
- [ ] Scope creep detected
- [ ] System friction encountered
- [ ] Evening overcommitment detected
- [ ] Evening energy mismatch (planned vs actual capacity)
- [ ] Planned too much for post-work capacity
- [ ] Restart friction likely tomorrow
- [ ] Unfinished work left without clear next step
- [ ] Carry-over ambiguity detected

> If any signal persists → escalate to Weekly Review.

---

## Optional — Delegations / Handoffs

- Owner | What | By when

---

## Shutdown (10 min)

> **Scope alignment:** Key question and first step tomorrow should normally reference the Primary or Secondary Anchor. If tomorrow points to a third project, explain it as a deliberate handoff or escalation (not silent scope creep).

**Main artifact today:**  
…

**Key question raised today:**  
(from Primary or Secondary Anchor — if from elsewhere, note why)

**Unfinished work requiring re-entry pack** *(meaningful incomplete blocks only — write "None" if day closed cleanly):*  
(map to Primary / Secondary Anchor; if third project appears, mark escalation)

**Unfinished Work — Re-entry Pack** *(skip if day closed cleanly):*
- **Current phase:** (where the work stopped within the block / artifact flow)
- **Artifact state:** (not started / draft exists / partially verified / blocked / waiting response / ready for review / other)
- **Next exact step:** (concrete 10–15 min restart action; specific enough to start immediately without re-analysis)
- **Recommended re-entry mode** *(used by tomorrow's Morning Setup)*: [ ] Quick (resume at last state) [ ] Analytical (review notes, restore chain) [ ] Fragile (inspect state, validate) 
- **Receiving day constraint note** *(if spillover tomorrow):* Energy fit? Load saturated? Work-type appropriate for tomorrow's energy mode?
- **Re-entry condition:** (needs office-hours Zephyr block / needs evening primary block / needs dependency resolved / …)

**Unfinished work — re-entry package captured?**
- [ ] Yes (complete above; tomorrow's re-entry is prepared)
- [ ] No unfinished work (day closed cleanly)
- [ ] No — fix before closure

**First step tomorrow:**  
(day-level start; normally Primary Anchor if week is continuing; if handoff to Secondary or new project, note explicitly)

**Signals to escalate to Weekly Review:**  
…

**Evening plan vs actual capacity:**
- [ ] No — plan matched energy
- [ ] Slightly — minor overrun, no deferral needed
- [ ] Yes — exceeded capacity

**Evening spillover created?**
- [ ] No
- [ ] Yes → deferred: (note what was moved and where)

---

## Metrics Capture (1 min)

**Actual blocks executed today:** … / planned

**Energy level:** Low / Normal / High

**Unplanned work absorbed:** (rough % or time estimate)

---

## Drift Early Warning (30 sec)

> **Purpose:** Detect trajectory/pressure building (not events). Feeds weekly interpretation, not daily replanning.
> **Distinct from Signals:** Signals = "Did this event happen?". Drift = "Is pressure accumulating toward weekly realism breakdown?"

**Quick scan checklist:**
- [ ] Anchor progress: On track / Slightly behind / Meaningfully behind
- [ ] Spillover pressure: Low / Medium / High (work accumulating into tomorrow)
- [ ] Dependency pressure: Low / Medium / High (blockers affecting flow)
- [ ] Capacity confidence: High / Medium / Low (energy vs plan mismatch)
- [ ] Weekly integrity: Yes / No (plan still realistic, or corrective action needed)
- [ ] Smallest corrective move: (1–2 line action, if any: defer block / downgrade task / confirm dependency / none)

---

## Context Signal Detection (CRITICAL)

> **Purpose:** Detect execution signals that require IMMEDIATE mid-week context update, not waiting for week-end closure.
> Real-time context adaptation prevents 3-day wasted execution loops and hidden blockers from cascading.
> 
> **STABILITY CONTROL:** Not all signals trigger adaptation. Weak signals are logged but do NOT trigger replan. Only strong signals with confirmed patterns trigger context update + replan. This prevents overreaction and thrashing.

### Detection Checklist (5 min at close)

Check each signal type. If ANY triggered → classify as WEAK or STRONG signal (see strength classification below).

**Signal 1 — Repeated Failure Pattern**
- [ ] Same anchor failed to reach Exit Condition ≥ 2 days this week?
- [ ] Same blocker appeared ≥ 2 separate daily sessions?
- If YES, AND root cause is confirmed → **STRONG Signal (Type B/C)**
- If YES, BUT single occurrence → **WEAK Signal** (log, do not replan)

**Signal 2 — Stale Exit Condition**
- [ ] Did Exit Condition need re-definition mid-execution (original was too vague or unrealistic)?
- [ ] Did different artifacts emerge as actual completion markers than originally stated?
- If YES, AND pattern affects ≥ 2 future sessions → **STRONG Signal (Type B)**
- If YES, BUT only this session → **WEAK Signal** (log, do not replan)

**Signal 3 — Hidden Dependency Discovery**
- [ ] Did execution require prerequisite work NOT in original plan?
- [ ] Did new tool/access/permission requirement emerge?
- [ ] Did new complexity spike appear (effort > 20% variance)?
- If YES, AND dependency blocks future work (≥ 2 sessions) → **STRONG Signal (Type C)**
- If YES, BUT already resolved mid-day → **WEAK Signal** (log, do not replan)

**Signal 4 — Plan Assumption Invalidated**
- [ ] Did execution prove a weekly goal assumption wrong?
- [ ] Did a dependency prove unreliable or unavailable?
- [ ] Did capacity assumption fail (energy much lower/higher than planned)?
- If YES, AND invalidation affects remaining week (≥ 2 future sessions) → **STRONG Signal (Type B/C)**
- If YES, BUT only affected this session → **WEAK Signal** (log, do not replan)

**Signal 5 — Carry-over Saturation Warning**
- [ ] Did 2+ significant work items spill into tomorrow?
- [ ] Is incoming carry-over from yesterday still unfinished?
- [ ] Would incoming carry-over overload tomorrow's capacity?
- If YES, AND pattern repeats tomorrow → **STRONG Signal (Type B)**
- If YES, BUT tomorrow looks clear → **WEAK Signal** (log, do not replan)

### Signal Strength Classification (CRITICAL FOR STABILITY)

#### WEAK Signal (Log Only → NO Replan)

- **Criteria:**
  - Single occurrence (not repeated pattern)
  - Temporary/resolved mid-session (not structural)
  - Does NOT affect ≥ 2 future sessions
  - Minor delay or confusion
  
- **Examples:**
  - Single day's execution was 15 min slower (energy dip, not systematic)
  - Tool took longer to start (temporary issue, resolved next attempt)
  - Misunderstood Exit Condition, fixed same day (learning, not blocker)
  
- **Immediate Action:**
  - [ ] Log in Daily notes with classification "WEAK signal"
  - [ ] Do NOT update project context
  - [ ] Do NOT trigger context update or replan
  - [ ] Do NOT escalate
  - Move to next day

#### STRONG Signal (Triggers Replan)

- **Criteria:**
  - CONFIRMED repeatable pattern (≥ 2 occurrences of same root cause)
  - Structural issue (not personal state or temporary)
  - Will affect ≥ 2 future sessions if not addressed
  - Blocker persists across multiple daily cycles
  
- **Examples:**
  - Same test environment setup issue appeared Mon AND Tue (structural, not temporary)
  - Exit Condition undefined/vague, required daily re-interpretation both Mon and Tue (pattern, not one-off confusion)
  - Dependency promised by Thu still unavailable Wed EOD (pattern, trust broken)
  - Capacity assumption proved wrong Mon (energy much lower), confirmed Tue (still low)
  
- **Immediate Action:**
  - [ ] Log in Daily notes with classification "STRONG signal"
  - [ ] Check replan budget (max 2 per week; if exceeded, escalate instead)
  - [ ] Check cooldown window (24h since last replan? exception if Type C)
  - [ ] Classify as Type B or Type C (adapt vs escalate)
  - [ ] IF allowed by budget + cooldown: Update project context same day/next morning
  - [ ] IF allowed: Trigger GENERATE_WEEKLY_EXECUTION Adaptive Mode next morning
  - [ ] IF blocked by budget/cooldown: Escalate to project owner instead

### Anti-Noise Filter (BEFORE LOGGING ANY SIGNAL)

Before classifying ANY signal, must pass this filter:

- [ ] **Is this repeatable?** Will the same issue occur if same conditions repeat? (NOT: "I was tired today" but YES: "this test setup always needs manual fix")
- [ ] **Is this structural?** Is the root cause in the system/plan/context, not personal state? (NOT: "I had bad sleep" but YES: "environment has access issue")
- [ ] **Multi-session impact?** Will this affect ≥ 2 future work sessions if not addressed? (NOT: "5 min delay today" but YES: "same blocker blocks tomorrow")

**If signal fails ANY of these filters → DO NOT LOG. Discard as noise.**

Example noise filtering:
- Single slow day (energy/sleep) → NOISE (personal state, not structural)
- Tool slow to start (computer was slow) → NOISE (one-time, not repeatable pattern)
- Misread task description → NOISE (human error, not system issue)
- BUT: Environment access broken AND still broken next day → SIGNAL (repeatable, structural, multi-session)

---

## Signal Classification + Immediate Action

#### Type A — Unauthorized Drift (REJECT)
- **Signal:** Work appeared that wasn't in plan, not labeled as blocker response
- **Immediate Action:** 
  - Do NOT accept execution as valid
  - Log rejection reason in daily notes
  - No context update (nothing to learn if drift is unauthorized)

#### Type B — Necessary Adaptation (DOCUMENT + LEARN)
- **Signal (WEAK):** Blocker response, capacity learning, scope adjustment that is temporary or single-session
- **Action:** Log only; do NOT update context or replan
- 
- **Signal (STRONG):** Blocker response or capacity learning that is repeatable, structural, ≥ 2 sessions
- **Action:**
  - Check replan budget (max 2/week) and cooldown (24h since last replan)
  - If allowed: Log + update project context same day + seed adaptive replan data
  - If blocked: Escalate to project owner instead
  - Example: "Discovered test environment setup needed (2.5h learnings, repeating pattern). Check budget before context update."

#### Type C — Hidden Dependency (UPDATE + ESCALATE)
- **Signal (WEAK):** Dependency discovered but already resolved mid-session
- **Action:** Log only; treat as learning for next week
- 
- **Signal (STRONG):** Structural blocker discovered; blocks ≥ 2 future sessions; requires replan or escalation
- **Action:**
  - Log with evidence (what work revealed it, when)
  - **EXCEPTION:** Type C signals bypass cooldown/budget limits (critical blockers take priority)
  - ADD TO ACTIVE BLOCKERS in project context immediately
  - Determine if replan is possible: 
    - IF replan budgets allow → Trigger GENERATE_WEEKLY_EXECUTION Adaptive Mode
    - IF replan blocked by limits → Escalate immediately to project owner
  - Example: "S3 bucket access required before any testing. Critical blocker. Check replan budget; if none available, escalate immediately."

### Actions Immediately After STRONG Signal Detected

**Before triggering any replan, verify constraints:**

1. **Anti-Thrashing Check:**
   - Has a replan occurred in the last 24 hours?
   - If YES, need to wait (unless this is Type C critical blocker)
   - Type C exceptions bypass cooldown

2. **Weekly Replan Budget Check:**
   - How many adaptive replans have occurred this week?
   - Current limit: max 2 per week
   - If already 2: must escalate instead of replanning

3. **Partial Stability Protection (if replan allowed):**
   - Keep ≥ 50% of remaining uncompleted anchors unchanged
   - Only reorder/replace anchors directly affected by the signal
   - Prevents full system reset/chaos

**If allowed by constraints:**

1. **Log signal** in Daily notes with timestamp, strength classification, and constraint check results
2. **Update project context** (same day or next morning) — do NOT wait for WEEK_CLOSEOUT
   - Add evidence to Current State or Active Blockers
   - Update Effort Reality Notes if learning is capacity-related
3. **Trigger adaptive mode** (next morning)
   - GENERATE_WEEKLY_EXECUTION Adaptive Mode must run
   - Reorder/rebalance remaining anchors (keep 50%+ stable)
   - Document adjustment in weekly file with signal evidence link
4. **Check escalation need** (if budget/cooldown blocked replan)
   - If signal blocks weekly goal delivery: escalate to Project Owner immediately
   - Provide: Signal type, evidence, impact, why replan not available

### Execution Commitment Rule (ANTI-PANIC-SWITCHING)

Once an anchor **starts execution in a block**, it CANNOT be replaced mid-session by replan.

- **Rule:** Ongoing work in current block completes as planned (or fails/blocks naturally)
- **Replan applies to:** Remaining blocks/days AFTER current block closes
- **Rationale:** Prevents context panic-switching from disrupting active focus
- **Example:**
  - Mon 8:00 AM: Start Zephyr test anchor (currently executing)
  - Mon 9:30 AM: STRONG signal detected (hidden dependency discovered)
  - 9:30 AM replan analysis runs, identifies this anchor is affected
  - Action: Do NOT interrupt the anchor mid-execution
  - Instead: Anchor completes (or naturally blocks); replan affects remaining blocks/Tue+
  - Next anchor (or same anchor's next session) executes updated plan

---

---

## Anti-Drift Validation (CRITICAL)

**Purpose:** Ensure this daily file remains an execution artifact tied to weekly goals, not a mini-plan. Check before closing day.

- [ ] **Goal traceability:** Every meaningful anchor maps to a weekly goal (from WeekPlan §2) — check "Linked Weekly Goal" field is populated for both anchors
- [ ] **No free-floating improvement work:** No untraced tasks labeled improve, optimize, refactor, polish, explore, investigate without explicit weekly goal linkage
- [ ] **Office anchors = Zephyr only:** No personal projects (RobotOS/Signee) scheduled during office hours except escalation exceptions (marked in Morning Setup)
- [ ] **Personal anchors = RobotOS/Signee only:** No Zephyr work scheduled in evening blocks
- [ ] **Evening capacity not exceeded:** Weekday night blocks do not exceed planned capacity mode (1×M, 2×S, S-only, or none)
- [ ] **First Strike defined:** Every deep-work anchor (office primary block + evening primary block) has concrete First Strike defined in Canonical Daily Anchors
- [ ] **Exit Condition defined:** Every deep-work anchor has concrete Exit Condition defined in Canonical Daily Anchors
- [ ] **Carry-over rules clear:** If any anchor will spill into tomorrow, Carry-over Rule is defined (shows what spills, when it re-enters, expected re-entry mode)
- [ ] **Daily file is not a mini-plan:** This file executes committed weekly goals; it does not introduce new weekly goals or invent strategy
- [ ] **Max 2 active projects maintained:** Only Primary and Secondary Anchor are active execution (third project only as incident/escalation/admin mention)
- [ ] **Context Signals checked:** Applied signal detection checklist; classified signals as WEAK or STRONG; updated context only if STRONG signal allowed by budget + cooldown constraints

---

## DoD (Daily closure)
- [ ] Main artifact captured
- [ ] Unfinished work documented (with re-entry pack if applicable; re-entry mode specified)
- [ ] Tomorrow's first step clear
- [ ] Any escalation signals noted
- [ ] If spillover tomorrow: re-entry doesn't violate receiving day saturation (check weekly load)

---

## CLOSURE CHECK (MANDATORY for Daily Completion)

**Purpose:** Ensure no cognitive load carries over into evening; achieve explicit mental closure.

**Task Completion Confirmation:**
- [ ] **All tasks have DONE criteria:**
  - [ ] Artifact defined (yes/no)
  - [ ] Exit condition verifiable (yes/no)
  - [ ] Next Step defined (yes/no)
- [ ] **No vague "continue later"** without explicit next-step definition

**Cognitive Closure:**
- [ ] **I have NO remaining open loops** regarding today's anchors  
  (Example open loop: "Did I finish the test cases?" DO NOT leave day without knowing answer)
- [ ] **Nothing I need to think about tonight**  
  (If something lingers mentally, capture it + add to tomorrow's schedule, then check again)

**If EITHER cognitive closure item is NOT checked:**
- ❌ Do NOT close the day
- ❌ Task is NOT considered DONE
- ✅ Fix by: (a) completing task, (b) creating explicit next-step + re-entry package, or (c) explicitly deferring to specific future day with written rationale
- ✅ Then return and re-check closure

**Day may NOT end until BOTH closure items are checked ✓**

---

---

## Human Reflection (Optional)

**Governance note (ADR-20260322 — Q2 PILOT):**
Human Reflection sections are optional Q2 pilot elements (advisory-only, not binding).
- Primary integration point: Monthly Human Reflection template → Monthly Review (not daily execution, not weekly planning)
- This section will NOT affect task admission, priority decisions, or scheduling
- All reflection data is tagged [ADVISORY] and re-confirmed monthly; do not assume patterns persist
- Q2 pilot re-evaluation: 2026-06-30 per 5 success criteria in ADR-20260322
- Usage: If this reflection genuinely helps your daily review, use it. If not, skip it.
- Monthly extraction rule: Reflection informs capacity *adjustments*, not binding decisions

Related: TEMPLATE_Month_Human_Final.md | ADR-20260322_HUMAN_LAYER_Q2_PILOT.md | MONTHLY_REVIEW_PROCESS_GOVERNANCE.md

> **Not a task log. Not planning.** A few lines to capture the human side of today.
> 
> This space records your lived experience: emotions, mental state, challenges, small insights,
> meaningful moments, growth signals.

**Reflective prompts** (choose 1–2 to guide your thinking; ignore if not relevant):
- What emotion or mood dominated today?
- What challenged me mentally or emotionally?
- Was there a moment worth remembering?
- Did I notice any personal growth or shift today?
- How am I feeling about the anchors and pace this week?

**Reflection:**  
(2–4 sentences. Keep it light and natural, not heavy.)

```
(leave blank if reflection doesn't feel necessary today)
```