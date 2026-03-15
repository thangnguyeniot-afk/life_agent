# WEEK_CLOSEOUT

**Purpose:** Close the active week cleanly by converting Weekly Execution reality into a validated end-of-week state, identifying meaningful carry-over, and preparing clean input for next week generation.

**When to run:** End of week (typically Sunday evening or Monday morning before next week planning); after the last Daily integration has been completed; once per week only.

**Operational relationship:**
- Reads: Active `W##_Execution.md` + Daily files (execution evidence)
- References: `W##_WeekPlan.md` (planning intent baseline, created by GENERATE_WEEKPLAN)
- Updates: `W##_Execution.md` with closeout section and carry-over notes
- Feeds: Month/Project tracking with factual weekly state changes
- Prepares: Carry-over and learnings for next GENERATE_WEEKPLAN (next week generation input)

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. When to Run](#2-when-to-run)
- [3. Prerequisites](#3-prerequisites)
- [4. Inputs](#4-inputs)
- [5. Outputs](#5-outputs)
- [6. Source-of-Truth Hierarchy](#6-source-of-truth-hierarchy)
- [7. Closeout Boundaries](#7-closeout-boundaries)
- [8. Evidence Rules](#8-evidence-rules)
- [9. Data to Collect Before Closing](#9-data-to-collect-before-closing)
- [10. Closeout Procedure](#10-closeout-procedure)
- [11. Carry-over Rules](#11-carry-over-rules)
- [12. Month & Project Feedback Rules](#12-month--project-feedback-rules)
- [13. Definition of a Good Week Closeout](#13-definition-of-a-good-week-closeout)
- [14. Standard Checklist](#14-standard-checklist)
- [15. Reusable Execution Template](#15-reusable-execution-template)

---

## 1. Purpose

**Core function:**  
This procedure closes an active `W##_Execution.md` file by validating what was accomplished, what was not, and what remains meaningful as carry-over. Closeout synthesizes weekly reality from execution evidence and prepares the ground for clean next-week generation.

**What this procedure does:**
- Validates completions against execution evidence (not memory)
- Identifies actual vs planned outcomes (completed / partial / incomplete / blocked / dropped)
- Isolates incomplete but meaningful work as carry-over
- Records dependency and distortion patterns
- Updates Weekly Execution with closeout notes
- Feeds factual state changes into Month/Project layers
- Produces concise summary for next week hint

**What this procedure does NOT do:**
- Rewrite weekly history or execution records
- Inflate completion or erase blocker reality
- Create retrospective narrative detached from evidence
- Silently convert incomplete work into completed
- Rewrite Month strategy or planning baseline
- Generate lengthy weekly narrative (conciseness required)
- Guess at work status; requires evidence

**Operational outcome:**  
After closeout, the week is formally closed with clear completion/carry-over state, factual delivery summary, and clean carry-over ready for next week generation. No ambiguity; no hidden incomplete work; no false success markers.

---

## 2. When to Run

**Run WEEK_CLOSEOUT when:**
- The active week has ended (typically Sunday evening or Monday morning)
- All meaningful Daily integrations for the week are complete
- Last Daily file has been closed (final re-entry packs resolved)
- Before next week's GENERATE_WEEKLY_EXECUTION runs
- Exactly once per week

**Do NOT run:**
- Repeatedly during the week (closeout is week-end only)
- Before final Daily file is closed
- If major rebalance is still pending (let rebalance complete first)
- As substitute for daily carry-over or integration

**Typical timing:**
- Sun evening after last Daily closes, or
- Mon morning before new week generation, or
- Wed PM if week is being formally ended early (escalation scenario)

**Runner:** Agent 2 (autonomous data collection and synthesis) or Agent 1 (if escalation or decision on carry-over priority required).

---

## 3. Prerequisites

Before running WEEK_CLOSEOUT:

- [ ] Active `W##_Execution.md` file exists for the completed week
- [ ] Paired `W##_WeekPlan.md` file exists (planning baseline for reference)
- [ ] All Daily files for the completed week are present and closed
- [ ] All Daily integrations for the week have completed
- [ ] Any major rebalance (WEEKLY_REBALANCE) has already been reflected
- [ ] Month tracking file is available if month feedback is needed
- [ ] Project state files exist and are accessible if project transitions occurred
- [ ] Closure is not being rushed; sufficient time to read evidence carefully

---

## 4. Inputs

**Required files:**
- Active `W##_Execution.md` file (the file being closed)
- Paired `W##_WeekPlan.md` file (planning baseline for reference only)
- All completed Daily files for the week (execution evidence)
- Month file (for context and feedback if needed)

**Optional files (if materially relevant):**
- Project state files (if any project transitions occurred)
- Anchor tracking file (if useful for pattern summary)
- Any rebalance notes (WEEKLY_REBALANCE) from mid-week if applied
- Previous week Review if it contains carry-forward items

**Information to gather:**
- What outcomes were planned vs what actually occurred?
- What artifacts were delivered (code, docs, decisions)?
- What work remains unfinished but still meaningful?
- What work was blocked and by what dependency?
- Did the week stay coherent or require rebalance / escalation?
- What dependency changes occurred?
- What signals matter for next week?

---

## 5. Outputs

**Expected deliverables:**

1. **Updated `W##_Execution.md` file**
   - Closeout section added with date and finality note
   - Outcomes marked: completed / partial / incomplete / blocked / dropped
   - Carry-over section added with next entry points
   - Historical execution records preserved unchanged

2. **Carry-over summary** (extracted for next week)
   - Executable carry-over (unfinished work still in scope)
   - Blocked carry-over (awaiting dependency resolution)
   - Optional secondary work (nice-to-have if space exists)
   - Dependency conditions for each carry-over item

3. **Month/Project feedback** (if updates needed)
   - Factual state changes only (not narrative)
   - Week-level artifact summaries
   - Project transition notes
   - Risk or escalation notes if applicable

4. **Closeout report** (concise, copy-rable)
   - File updated
   - Outcomes: # completed / # partial / # incomplete / # blocked
   - Major artifacts delivered
   - Carry-over count and nature
   - Blockers and new dependencies
   - Month/project updates made
   - Missing evidence notes (if any)
   - Suggested starting posture for next week

---

## 6. Source-of-Truth Hierarchy

**For closeout decisions, consult in this order:**

1. **Daily files as actual execution evidence**
   - What daily closures record as completed
   - Artifacts and deliverables from daily records
   - Spillover packs and carry-over notes
   - Highest priority

2. **Weekly Execution file (operational state)**
   - Anchor map and daily sequencing
   - Rebalance notes if applied
   - Dependency and risk notes

3. **WeekPlan as planning intent baseline**
   - Planned outcomes for comparison
   - Planned resource allocation
   - Reference only; not edited during closeout

4. **Project state files**
   - Actual project artifacts and transitions
   - Project readiness or blocker status
   - Optional but useful if project transitions occurred

5. **Month context**
   - Month-level objectives for perspective
   - Month commitments (to see if week fed into them)
   - Reference only; not rewritten

6. **Anchor tracking (optional)**
   - Historical anchor patterns
   - Useful for week-to-week consistency
   - Reference only

**Key principle:**  
Closeout is evidence-based. Do not rely on vague memory or impressions. If execution evidence does not support a completion claim, mark work as partial or incomplete honestly.

---

## 7. Closeout Boundaries

### Allowed Changes

✅ **Closeout operations:**
- Summarize what actually happened (completed / partial / incomplete outcomes)
- Mark outcomes against planning baseline for comparison (factual only)
- Identify completed artifacts and meaningful deliverables
- Extract executable and blocked carry-over from unfinished work
- Record dependency changes during the week
- Note rebalance events or escalations if they occurred
- Update Weekly Execution with closeout section (date, status, carry-over)
- Feed factual state changes to Month/Project layers
- Mark risks or signals for next week

✅ **Evidence-based marking:**
- Completed = supported by artifact, status closure, or explicit execution record
- Partial = meaningful progress but endpoint not reached
- Incomplete = deferred, dropped, or not started
- Blocked = dependency prevented execution
- Dropped = intentionally removed from scope during week

---

### Not Allowed Changes

❌ **Do not rewrite history:**
- Do not alter completed Daily execution records
- Do not change what Daily closures marked as status
- Do not "edit" completion status to look better
- Do not erase blocker evidence

❌ **Do not inflate outcomes:**
- Do not mark incomplete work as completed
- Do not use vague success language without artifact backup
- Do not convert blocked work into deferred (blocked ≠ deferred)
- Do not suppress blocker reality

❌ **Do not rewrite planning:**
- Do not edit WeekPlan (reference only)
- Do not rewrite Month strategy
- Do not silently drop planned outcomes from Month tracking
- Do not create hidden compensation in next-week planning

❌ **Do not skip important work:**
- Do not mark work as completed without evidence
- Do not assume completion based on absence of failure reports
- If evidence is incomplete, use "uncertain" or "partial" language
- Call out holes in execution record explicitly

---

## 8. Evidence Rules

**Standard for marking work completed:**
- Must have artifact (code merged, doc filed, decision recorded)
- OR explicit status closure in Daily file
- OR referenced in another completed artifact
- Absence of failure report ≠ success

**Standard for marking partial:**
- Progress occurred (commits, drafts, partial docs)
- But endpoint not reached
- Clear next entry point exists

**Standard for marking incomplete:**
- Not started, or
- Started but no material progress, or
- Intentionally dropped from scope

**Standard for marking blocked:**
- Dependency explicitly prevented execution, or
- External gate or resource unavailable, or
- Blocker is named and dated

**Standard for marking dropped:**
- Explicitly removed from scope, or
- Superseded by different decision, or
- No longer relevant (stale work)

**Uncertainty handling:**
- If evidence is sparse, use "uncertain" language
- Mark evidence gaps in closeout report
- Do not guess into completion
- Note what would be needed to validate

---

## 9. Data to Collect Before Closing

**Pre-closeout checklist — gather before starting:**

- [ ] Week name and exact date range (e.g., W10, 2026-03-09 to 2026-03-15)
- [ ] Planned primary outcome (from WeekPlan)
- [ ] Planned secondary outcomes (from WeekPlan)
- [ ] Actual primary outcome (from execution evidence)
- [ ] Actual secondary outcomes (from execution evidence)
- [ ] Completed artifacts (list from Daily records)
- [ ] Partial artifacts (list and completion %)
- [ ] Incomplete or dropped work (list)
- [ ] Blocked work and blocking reasons (list)
- [ ] Dependency changes during the week (list)
- [ ] Rebalance events (if any; dates and scope)
- [ ] Escalations or overrides (if any; what and why)
- [ ] Major blockers or risks (for next week)
- [ ] Project state transitions (if any)
- [ ] Carry-over candidates (unfinished meaningful work)
- [ ] Evidence gaps (undocumented work or ambiguous status)
- [ ] Whether week stayed coherent or required rebalance/escalation

---

## 10. Closeout Procedure

### Step 1 — Read the Week as Evidence

**Instructions:**
1. Open the completed `W##_Execution.md` file
2. Read the entire file to understand weekly intent and execution plan
3. Read the paired `W##_WeekPlan.md` as planning intent baseline
4. Read all Daily files for the week in order (Mon → Sun)
5. Reconstruct actual weekly reality from execution evidence
6. Do NOT rely on impression or memory; use documented facts only
7. Identify what the execution records show happened

**Output of Step 1:**
- Clear picture of planned weekly frame
- Clear picture of actual execution facts
- Factual gaps or inconsistencies noted

---

### Step 2 — Compare Intent vs Execution

**Instructions:**
1. List planned primary outcomes (from WeekPlan)
2. List planned secondary outcomes (from WeekPlan)
3. For each planned outcome, identify actual status from Daily evidence
   - Completed? (with artifact)
   - Partial? (progress but incomplete)
   - Incomplete? (not started or abandoned)
   - Blocked? (dependency prevented)
   - Dropped? (intentionally removed)
4. Keep comparison factual and concise
5. Do not moralize, explain, or over-narrate
6. Note disconnects between plan and execution
7. Identify whether disconnects are expected (planned rebalance) or surprising

**Output of Step 2:**
- Clear mapping of planned → actual status for each major outcome
- Factual summary of what succeeded and what didn't
- Identification of whether week stayed coherent or not

---

### Step 3 — Validate Completions

**Instructions:**
1. For each claimed completion, check for supporting evidence
   - Artifact (merged code, filed document, recorded decision)?
   - Status closure in Daily file?
   - Reference in another completed artifact?
2. Mark completed only where evidence exists
3. If evidence is weak, use "partial" or "uncertain" instead
4. Avoid vague success language; be specific about what was delivered
5. If multiple deliverables planned, itemize which were completed and which were partial/incomplete
6. Call out evidence gaps where they exist

**Output of Step 3:**
- Clear list of completed outcomes with supporting artifacts
- Clear list of partial outcomes with progress notes
- Clear list of incomplete/blocked outcomes with reasons
- No inflated completion claims

---

### Step 4 — Identify Incomplete but Meaningful Carry-over

**Instructions:**
1. From incomplete work, identify what still matters next week
2. Drop stale intentions or no-longer-relevant work explicitly
3. For meaningful carry-over, rewrite as exact next entry points
   - "Zephyr: write Dbugs Ram test" → too vague
   - "Zephyr: write Dbugs Ram test; follow Wed outline; use pattern from Dbugs write test; merge target: Thu" → actionable
4. Separate executable carry-over from blocked carry-over
   - Executable: ready to pick up next week
   - Blocked: awaiting external dependency; name the dependency
5. Estimate carry-over complexity (S / M / L if useful)
6. Identify priority if multiple carry-overs exist

**Output of Step 4:**
- List of executable carry-over (exact next entry points)
- List of blocked carry-over (with named dependencies)
- List of dropped items (explicitly called out)
- Priority or sequence if needed

---

### Step 5 — Summarize Dependency and Distortion Pattern

**Instructions:**
1. Review which dependencies changed during the week
   - New dependencies emerged?
   - Expected dependencies resolved?
   - Unexpected blockers appeared?
2. Identify major dependency management patterns
   - External gate (review, approval, customer feedback)?
   - Internal blocker (environment, broken build)?
   - Resource or capacity constraint?
3. Note if week required rebalance (WEEKLY_REBALANCE) or escalation
   - If rebalanced: summary of what changed and why
   - If escalated: what was escalated and to whom
4. Assess overall week coherence
   - Week stayed coherent (plan held)?
   - Week required rebalance (Level 2 distortion)?
   - Week suffered structural break (Level 3 distortion)?
5. Keep summary short and operational (2–4 sentences max)

**Output of Step 5:**
- List of major dependency dynamics
- Summary of whether week was coherent, rebalanced, or escalated
- Key blockers or risks that carry into next week

---

### Step 6 — Update the Weekly Execution File

**Instructions:**
1. Open the `W##_Execution.md` file
2. Add a "CLOSEOUT" section (or similar header) at the bottom or in a dedicated closeout area
3. Include: date closed, week status, finality note
4. Add subsection: **Completed Outcomes**
   - List outcomes marked completed with brief artifact notes
5. Add subsection: **Partial or Incomplete Outcomes**
   - List partial/incomplete outcomes with status and reason (if space allows)
6. Add subsection: **Carry-over for Next Week**
   - List actionable carry-over items with exact next entry points
   - List blocked carry-over separately with blocker/dependency noted
7. Preserve all historical execution records already in the file (do not rewrite)
8. Keep closeout section concise (bullets, no narrative filler)

**Output of Step 6:**
- Updated W##_Execution.md with closeout section
- Week marked closed with finality
- Carry-over visible and actionable
- Historical records preserved

---

### Step 7 — Feed Forward to Month / Project Layers

**Instructions:**
1. Identify any meaningful changes in monthly execution or project state
2. Update Month file only where week-level facts matter:
   - Major artifacts delivered? (feature merged, docs filed?)
   - Project state transition? (capability ready, blocker identified?)
   - Commitment completed or at risk?
   - Risk flagged for escalation?
3. Keep Month updates factual and concise
4. Do not turn Month into a weekly journal
5. Do not rewrite monthly strategy
6. Update Project files only if project had material transition
   - Artifact delivered or completed?
   - Capacity or readiness changed?
   - Dependency or blocker new?
7. Use existing update pattern (don't invent new structure)

**Output of Step 7:**
- Month file updated with factual week-level totals/risks if needed
- Project files updated with state transitions if applicable
- No excessive documentation; only meaningful changes

---

### Step 8 — Prepare Next Week Hints

**Instructions:**
1. From carry-over list, identify most likely primary anchor for next week
   - What unfinished work is highest priority?
   - What has dependencies resolved now?
   - What new work emerges from this week's completion?
2. Identify if secondary anchor exists or if next week should be single-anchor
3. Note key dependencies that affect next week scheduling
   - External gates not yet resolved?
   - Capacity constraints (energy dip pattern, etc.)?
   - Project transitions that open new work?
4. Note whether next week should start in normal mode or any special mode
   - Normal: standard re-entry, good energy expected
   - Careful: known blocker or dependency completion needed before proceeding
   - Recovery: weak carry-over closure or spillover from current week
5. Identify any risks that should affect next week planning
   - Blocked work may stay blocked
   - Capacity might be constrained
   - External dependency completion uncertain

**Output of Step 8:**
- Likely primary anchor for next week (as hint)
- Secondary anchor or single-anchor note
- Key dependencies for next week planner
- Suggested starting mode or risk flags
- One-sentence summary for next week planner

---

### Step 9 — Consistency Check

**Instructions:**
Verify all of the following before considering closeout complete:

- [ ] Closeout matches Daily execution evidence (no contradictions)?
- [ ] Weekly Execution is internally consistent (no impossible claims)?
- [ ] Carry-over is meaningful and actionable (not vague)?
- [ ] Blocked carry-over has named dependencies?
- [ ] WeekPlan is not rewritten (reference only)?
- [ ] Month/Project updates remain factual (no narrative)?
- [ ] Dropped/incomplete work is marked honestly (no inflation)?
- [ ] Historical records preserved (not edited)?
- [ ] Evidence gaps noted (if any undocumented work)?
- [ ] Next week hints are clear and usable?

**Output of Step 9:**
- Consistency confirmed
- Closeout is coherent and evidence-based
- Ready for next-week generation input

---

### Step 10 — Produce Report

**Instructions:**
1. Create a brief closeout report with this structure:
   - **File updated:** `<W##_Execution.md>` (timestamp)
   - **Week:** `<WEEK_NAME>` `<DATE_RANGE>`
   - **Overall status:** Completed / Partially complete / With escalation / Other
   - **Outcomes summary:** # completed / # partial / # incomplete / # blocked / # dropped
   - **Major artifacts delivered:** (list 1–3 key deliverables)
   - **Carry-over identified:** # executable / # blocked / dependencies named
   - **Blockers or new dependencies:** (list if material)
   - **Month/Project updates:** (list what was updated)
   - **Evidence gaps:** (list any undocumented work or uncertainty)
   - **Suggested next week mode:** (normal / careful / recovery / other)
   - **Suggested primary anchor:** (hint for next week planner)
   - **Report produced by:** Agent 2 | Agent 1
   - **Report timestamp:** `<date/time>`

2. Make the report concise (1–2 pages max)
3. Make the report copy-rable (suitable for logging or next-week documentation)
4. Avoid narrative or retrospective essays
5. Focus on facts: what delivered, what carried over, what changed

**Output of Step 10:**
- Concise closeout report
- Readable, loggable format
- Clarity on week completion state and next week hints

---

## 11. Carry-over Rules

**Rules for identifying and documenting carry-over:**

- **Carry over only meaningful unfinished work**
  - Not stale intentions
  - Not blocked work without dependency resolution path
  - Work still aligned with weekly/monthly intent

- **Rewrite carry-over as exact next entry points**
  - Not vague (e.g., "finish X")
  - Actionable specifics (e.g., "complete X by doing 1, 2, 3")
  - Including context (pattern to follow, blocker to resolve first, etc.)

- **Separate executable from blocked carry-over**
  - Executable: ready to resume immediately
  - Blocked: awaiting specific named dependency; explicit condition for unblocking

- **Do not carry completed work**
  - Only carry unfinished work
  - If work is done, mark it complete; do not carry it as carry-over

- **Do not carry stale intentions**
  - If work is no longer relevant, explicitly drop it
  - If weekly re-prioritization moved work out of scope, do not carry carry-over legacy items

- **If carry-over threatens next week coherence, note risk**
  - Too much carry-over?
  - Conflicting carry-over items?
  - Carry-over + new week plans = overload?
  - Mark for next-week planner's attention

---

## 12. Month & Project Feedback Rules

**When to update Month file:**
- Week delivered major artifacts aligned with monthly commitment ✅
- Week revealed blocker or risk affecting monthly objective ✅
- Week created capacity change or resource shift ✅
- Week finished planned commitment or project phase ✅

**When NOT to update Month file:**
- Week-specific daily details (store in Week file) ❌
- Descriptive narrative ("this week we...") ❌
- Internal team process notes ❌
- Carry-over details (keep in Week file) ❌

**Month update format:**
- Factual state change only
- One sentence per update
- Include results or new condition
- No explanation or storytelling needed

**Example Month updates (keep minimal):**
```
W10 result: Zephyr 3 tests merged to develop; scope freeze readiness confirmed.
W10 result: Signee team context loaded; environment setup blocker (test equipment) escalated to W11 design decision.
W10 result: RobotOS spike findings pptx complete; scope-freeze input ready.
```

**When to update Project files:**
- Project artifact delivered and acceptance complete ✅
- Project state transition (capability ready, blocked status changed) ✅
- Project resource/capacity change ✅
- Project dependency resolution or new blocker ✅

**When NOT to update Project files:**
- Weekly task-level details ❌
- Carry-over logging ❌
- Process notes ❌

**Project update format:**
- Factual state transition
- Artifact reference if applicable
- Blocker/dependency if applies
- No narrative required

---

## 13. Definition of a Good Week Closeout

A week closeout is successful when:

✅ **The week is closed without ambiguity**
- Every outcome is marked: completed / partial / incomplete / blocked / dropped
- No work is left in vague state
- Closure is explicit and dated

✅ **Actual delivery is visible**
- Completed artifacts are named
- Partial progress is quantified (% complete, next entry point)
- Incomplete work has stated reason

✅ **Incomplete work is handled honestly**
- Blocked work is marked blocked (not incomplete)
- Dropped work is marked dropped (not carried silently)
- Uncertain completion is marked uncertain (not guessed into success)

✅ **Next week receives clean carry-over**
- Carry-over items are actionable (exact next steps)
- Executable vs blocked carry-over is separated
- Dependencies for each carry-over item are named

✅ **Month/Project layers receive only useful signals**
- Only state changes that matter are fed forward
- Not every weekly detail is logged
- Updates are concise and factual

✅ **History remains traceable**
- Daily execution records not rewritten
- Weekly reality is reconstructed from evidence
- Evidence gaps are noted if they exist

✅ **No execution truth is lost**
- All meaningful completion is captured
- All unfinished work is identified
- All dependencies are recorded

---

## 14. Standard Checklist

**Use this checklist before, during, and after closeout:**

### Pre-Closeout Assessment

- [ ] Week is formally complete (last day closed)?
- [ ] All Daily files for the week present and closed?
- [ ] All Daily integrations completed?
- [ ] Any major rebalance (WEEKLY_REBALANCE) already applied?
- [ ] Month/Project context files accessible?
- [ ] Sufficient time to read evidence carefully (not rushed)?

### Closeout Execution

- [ ] Step 1 complete — read week as evidence from Daily files
- [ ] Step 2 complete — compare WeekPlan intent vs actual execution
- [ ] Step 3 complete — validate completions with supporting evidence
- [ ] Step 4 complete — identify meaningful carry-over with exact next entry points
- [ ] Step 5 complete — summarize dependency and distortion pattern
- [ ] Step 6 complete — update W##_Execution.md with closeout section
- [ ] Step 7 complete — feed forward to Month/Project only if meaningful
- [ ] Step 8 complete — prepare next week hints for planner
- [ ] Step 9 complete — consistency check passed
- [ ] Step 10 complete — closeout report produced

### Post-Closeout Validation

- [ ] W##_Execution.md marked closed with timestamp?
- [ ] Carry-over is actionable and exact (not vague)?
- [ ] Dropped/incomplete work marked explicitly?
- [ ] Blocked work has named dependencies?
- [ ] Next week hints are clear?
- [ ] Month/Project updates accurate and concise?
- [ ] Evidence gaps noted where they exist?
- [ ] Closeout report produced and copy-rable?
- [ ] No inflated completion claims?
- [ ] Historical records preserved unchanged?

### Ready for Next Week

- [ ] W##_Execution.md closed and carry-over clear
- [ ] Closeout report filed or logged
- [ ] Next week planner has clear hints and carry-over
- [ ] Month/Project tracking updated (if needed)
- [ ] No ambiguous or hidden incomplete work

---

## 15. Reusable Execution Template

Use this template for future week closeout runs. Copy, replace placeholders, and paste into Copilot or Agent 2 command:

```
TASK: Perform WEEK_CLOSEOUT for <WEEK_NAME>

Context:
- Week closed: <WEEK_NAME> (<DATE_RANGE>)
- Closeout date: <CLOSEOUT_DATE>
- Last Daily closed: <LAST_DAILY_DATE>
- Any rebalance applied? <YES/NO>

Files to read:
- Weekly Execution: <WEEK_EXECUTION_FILE>
- Planning baseline: <WEEKPLAN_FILE>
- Daily folder: <DAILY_FOLDER>
- Month file: <MONTH_FILE>
- Project files: <PROJECT_FOLDER>

Closeout scope:
- Week name: <WEEK_NAME>
- Date range: <DATE_RANGE>
- Primary anchor planned: <PRIMARY_ANCHOR>
- Secondary anchor planned: <SECONDARY_ANCHOR>
- Expected major deliverables: <LIST>

Information to validate:
- What was actually completed? (check Daily evidence)
- What was partial or incomplete? (with reason)
- What work remains meaningful as carry-over?
- What dependencies changed during the week?
- Did the week require rebalance or escalation?
- What blockers carry into next week?

Instructions:
Follow WEEK_CLOSEOUT.md Steps 1–10:
1. Read week as evidence (Daily files, execution records)
2. Compare WeekPlan intent vs actual execution
3. Validate completions (artifact + evidence only)
4. Identify meaningful carry-over (exact next entry points)
5. Summarize dependency and distortion pattern
6. Update <WEEK_EXECUTION_FILE> with closeout section
7. Feed factual updates to Month/Project if needed
8. Prepare next week hints (primary anchor, dependencies, mode)
9. Consistency check
10. Produce closeout report

Expected output:
- Updated <WEEK_EXECUTION_FILE> (with closeout section)
- Carry-over extracted (executable + blocked)
- Closeout report (copy-rable)
- Month/Project updates (if applicable)
- Next week hints (primary anchor, starting mode, risks)

Report format:
- File updated: <WEEK_EXECUTION_FILE>
- Week: <WEEK_NAME> <DATE_RANGE>
- Status: <COMPLETED/PARTIAL/WITH_ESCALATION>
- Outcomes: # completed / # partial / # incomplete / # blocked / # dropped
- Major artifacts: <LIST>
- Carry-over: # executable / # blocked / blockers named
- Month/Project updates: <LIST>
- Evidence gaps: <LIST_IF_ANY>
- Suggested next week: (primary anchor / dependencies / mode)

Timeline:
- Closeout read: <DURATION>
- Analysis: <DURATION>
- File updates: <DURATION>
- Total: <ESTIMATED DURATION>
```

---

## Appendix A: Integration with LIFE_AGENT Procedures

**Relationship to other operating procedures:**

| Procedure | Relationship | Sequencing |
|---|---|---|
| [GENERATE_WEEKLY_EXECUTION.md](GENERATE_WEEKLY_EXECUTION.md) | Generates Weekly Execution at week start; WEEK_CLOSEOUT validates it at week end | GENERATE runs once (week start); CLOSEOUT runs once (week end) |
| [WEEKLY_REBALANCE.md](WEEKLY_REBALANCE.md) | Corrects Weekly Execution mid-week if drift detected; CLOSEOUT reads the rebalanced state | REBALANCE may run mid-week; CLOSEOUT reads final state (rebalanced or not) |
| [INTEGRATE_DAILY.md](../DAILY_INTEGRATION/INTEGRATE_DAILY.md) | Daily integration feeds execution evidence; CLOSEOUT reads integrated Daily files | INTEGRATE runs daily; CLOSEOUT reads all accumulated Daily evidence at week end |
| [PREPARE_NEXT_DAILY.md](../DAILY_INTEGRATION/PREPARE_NEXT_DAILY.md) | Next-day preparation inherits from Weekly Execution; CLOSEOUT prepares carry-over for next week generation | PREPARE_NEXT_DAILY uses updated Weekly Execution daily; CLOSEOUT updates it for week transition |

**Full operational sequence:**

1. **Week start:** GENERATE_WEEKLY_EXECUTION (Mode A) → Create W##_Execution.md
2. **Daily cycle:** INTEGRATE_DAILY (after each daily closes) → PREPARE_NEXT_DAILY (prepare next day)
3. **Mid-week if needed:** INTEGRATE_DAILY detects drift → WEEKLY_REBALANCE (if Level 2/3)
4. **Week end:** Final INTEGRATE_DAILY → **WEEK_CLOSEOUT** (this procedure)
5. **Next week start:** GENERATE_WEEKLY_EXECUTION (Mode A, using CLOSEOUT carry-over as input)

---

## Appendix B: Troubleshooting

### Common closeout questions:

**Q: Should I carry over work that's been blocked for days?**  
A: Only if the blocker has a clear resolution path. If dependency is still uncertain, mark it as "blocked carry-over" and note the blocker. If dependency will take weeks or is unresolved, consider dropping from active carry-over; record in Month as risk instead.

**Q: What if a work item is 90% done but the last 10% is unclear?**  
A: Mark it partial, not complete. Note "90% complete, blocker: unclear endpoint." Carry it forward as executable but flag the blocker in carry-over detail.

**Q: How much carry-over is too much?**  
A: If carry-over is >60% of completed week+ new week content, flag it for next-week planner. Risk of overload. May need to drop lower-priority carry-over or note capacity constraint.

**Q: Should I include team notes or process learnings in the closeout?**  
A: Only if they directly affect next-week execution (e.g., "pattern X works better for test Y"). Skip process narrative; focus on execution facts and carry-over.

**Q: What if Daily evidence is incomplete or contradictory?**  
A: Note the gap in your report explicitly (e.g., "Wed execution record missing; status marked uncertain"). Use other evidence (project artifacts, Daily adjacent to it) to infer if necessary, but mark inference clearly.

**Q: Do I update the Month file with every weekly Carry-over?**  
A: No. Only update Month if week-level state change matters (artifact delivered, blocker escalated, capability changed). Carry-over detail stays in Week file.

**Q: Can I write a retrospective narrative in the closeout section?**  
A: No. Keep closeout concise and factual (bullets, short text only). If you need narrative reflection, write it separately in a personal review or log; do not bloat the closeout section.

---

## Appendix C: Historical Examples

*Examples of week closeout will be captured in real execution history. This section is placeholder for future case studies after several closed weeks.*

- Example 1: Clean week closure (all outcomes on track)
- Example 2: Partial week closure (some outcomes incomplete, clean carry-over)
- Example 3: Rebalanced week closure (mid-week distortion corrected)
- Example 4: Escalation week closure (structural break, carry-over to special review)

---

**Document version:** 1.0  
**Created:** 2026-03-15  
**Status:** Operational — ready for weekly use  
**Maintenance:** Review and update quarterly or after major LIFE_AGENT system changes
