# WEEKLY_REBALANCE

**Purpose:** Perform controlled mid-week correction of the active Weekly Execution file when actual execution has drifted far enough to threaten the operational usefulness of the current weekly frame.

**When to run:** During an active week (Mon–Fri typically); triggered when Daily integration reveals weekly-level distortion that exceeds local drift handling capacity.

**Operational relationship:**
- Reads: `W##_WeekPlan.md` (created by GENERATE_WEEKPLAN; planning intent baseline)
- Updates: Active `W##_Execution.md` (operational reality artifact)
- Preserves: Month file (monthly strategy baseline)
- Inputs: Recent Daily files (execution truth)
- Related procedures: [`GENERATE_WEEKPLAN.md`](GENERATE_WEEKPLAN.md) (weekly planning) | [`GENERATE_WEEKLY_EXECUTION.md`](GENERATE_WEEKLY_EXECUTION.md) | [`WEEK_CLOSEOUT.md`](WEEK_CLOSEOUT.md) (week-end) | [`INTEGRATE_DAILY.md`](../DAILY_INTEGRATION/INTEGRATE_DAILY.md)

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. When to Run](#2-when-to-run)
- [3. Distortion Levels & Trigger Thresholds](#3-distortion-levels--trigger-thresholds)
- [4. Prerequisites](#4-prerequisites)
- [5. Inputs](#5-inputs)
- [6. Outputs](#6-outputs)
- [7. Source-of-Truth Hierarchy](#7-source-of-truth-hierarchy)
- [8. Rebalance Boundaries](#8-rebalance-boundaries)
- [9. Data to Collect Before Rebalancing](#9-data-to-collect-before-rebalancing)
- [10. Rebalance Procedure](#10-rebalance-procedure)
- [11. Allowed vs Forbidden Changes](#11-allowed-vs-forbidden-changes)
- [12. Escalation Rules](#12-escalation-rules)
- [13. Definition of a Good Rebalance](#13-definition-of-a-good-rebalance)
- [14. Standard Checklist](#14-standard-checklist)
- [15. Reusable Execution Template](#15-reusable-execution-template)

---

## 1. Purpose

**Core function:**  
This procedure reconciles an active `W##_Execution.md` file with real execution reality when the gap between plan and actual outcome has grown large enough that the current weekly operating frame is no longer coherent or believable.

**What this procedure does:**
- Adjusts remaining daily anchors to match actual capacity and constraints
- Resequences remaining work to reflect real dependency and blocker states
- Reduces scope commitments if capacity has been materially consumed
- Updates carry-over notes to reflect changed conditions
- Records the rebalance explicitly so next Daily files inherit correctly
- Preserves traceability (does not erase or hide the drift)

**What this procedure does NOT do:**
- Silently rewrite the WeekPlan goals
- Rewrite Monthly strategy to look cleaner
- Pretend blocked work is executable
- Create false progress records
- Erase evidence of drift
- Introduce hidden emotional compensation (overloading remaining week)

**Operational outcome:**  
After rebalance, the Weekly Execution file reflects coherent, believable remaining-week intent grounded in real execution evidence, without contradiction to planning baseline or historical daily truth.

---

## 2. When to Run

**Run WEEKLY_REBALANCE when:**
- Daily integration has revealed a gap between Weekly Execution and actual daily reality
- **AND** the gap is large enough that continuing with the current weekly frame would be operationally incoherent
- **AND** the remaining days of the week still exist (not end-of-week Review/Closeout)

**Do NOT run for:**
- Single task slip (handle via next-day re-entry pack)
- Expected spillover from Daily carry-over (handle via PREPARE_NEXT_DAILY)
- Normal dip-day energy patterns (handle via work-type downgrade in next daily)
- Small capacity misses (handle via small deferred-work notes)

**Typical trigger situations:**
- Major dependency failure invalidates the planned weekly anchor map
- Significant blocker changes force meaningful resequencing of remaining work
- Project priority has been explicitly shifted (not drifted, but shifted)
- Unexpected capacity drop (illness, urgent context switch) threatens remaining week credibility
- 30–50% or more of the weekly execution frame has become unrealistic

> **Capacity drift re-check:** If actual capacity has materially drifted from the plan (TYPE A work overran office hours, evening blocks were unavailable, a project took >2x estimated effort), re-check against CAPACITY_ENGINE before rebalancing the anchor hypothesis. Do not rebalance without a grounded capacity model — see [`CAPACITY_ENGINE.md`](CAPACITY_ENGINE.md) §8 (Decision Logic When Capacity Does Not Close).

**Runner:** Agent 2 (autonomous operational procedure) or Agent 1 (strategic decision if escalation needed).

---

## 3. Distortion Levels & Trigger Thresholds

### Level 1 — Local Drift

**Indicators:**
- One or two tasks slip to next day
- One planned block spills over
- One day executes at 70–80% of plan
- Re-entry is small and contained (< 20 min)
- Anchor pattern holds for most of the week

**Impact:**
- No weekly-level coherence loss
- Daily carry-over + next-day re-entry pack sufficient

**Action:**
- Absorb via PREPARE_NEXT_DAILY (next daily file inherits spillover pack)
- **Do not run WEEKLY_REBALANCE**
- Document in next Daily file as normal spillover

---

### Level 2 — Weekly Distortion

**Indicators:**
- Multiple tasks delayed (2+ days have spillover)
- Anchor pattern broken for 2+ days
- Dependency changes force meaningful resequencing of remaining work
- Project state has shifted (not planned)
- 30–50% of the weekly execution frame is no longer realistic
- Remaining week cannot absorb carry-over without saturation

**Impact:**
- Weekly operating frame is no longer coherent
- Continuing with current plan would require daily micro-rescopes every day
- Risk to weekly outcomes visible

**Action:**
- **Run WEEKLY_REBALANCE**
- Rebalance the remaining week to restore coherence
- Preserve planning baseline; update operational reality only
- Record rebalance explicitly

---

### Level 3 — Structural Break

**Indicators:**
- Critical dependency failure (not just delay)
- Explicit priority override from outside normal flow
- Capacity drop > 50% (major illness, emergency context switch)
- > 50% of weekly execution invalidated
- Monthly objective or emergency window is threatened
- Multiple projects in jeopardy simultaneously

**Impact:**
- Weekly execution cannot be rebalanced inside normal frame
- Rebalance must be accompanied by escalation
- Some weekly outcomes may need to be explicitly deferred

**Action:**
- Run WEEKLY_REBALANCE to stabilize remaining week
- **Record escalation explicitly** (to Month / Emergency / explicit review layer)
- Do not hide structural break inside normal operational language
- Document the override or blocker clearly

**Example escalation note:**  
> "Structural Break detected: <PROJECT> critical dependency failed 3/15 PM. Weekly Rebalance applied to salvage remaining capacity. Month-level <OUTCOME> flagged at risk. Escalation to Month Review required."

---

## 4. Prerequisites

Before running WEEKLY_REBALANCE:

- [ ] Active `W##_Execution.md` file exists for the current week
- [ ] Paired `W##_WeekPlan.md` file exists (planning baseline)
- [ ] All Daily files for days already executed are present and closed
- [ ] Daily integration has already captured recent reality (no pending Daily files)
- [ ] Major dependency or capacity changes are known (not still being discovered)
- [ ] Current date is not on Review/Closeout day (rebalance should not run Sun/end-of-week)
- [ ] Month context file is available if needed

---

## 5. Inputs

**Required files:**
- Active `W##_Execution.md` file (the file being rebalanced)
- Paired `W##_WeekPlan.md` file (planning baseline for reference)
- All completed Daily files for the current week (execution truth)
- Current date and time
- Any explicit escalation or override note (if Level 3 / Structural Break)

**Optional files (if materially relevant):**
- Month file (for monthly context only)
- Project state files if project priority or readiness has changed
- Anchor tracking file if useful for historical comparison
- Previous week Review if it contains carry-forward items

**Information to gather:**
- What has actually changed since the week started?
- Which days have been executed? Which remain?
- What work has actually been completed?
- What work remains unfinished?
- What work is blocked and why?
- What dependencies have changed?
- What capacity has been consumed unexpectedly?

---

## 6. Outputs

**Expected deliverables:**

1. **Updated `W##_Execution.md` file**
   - Remaining-day anchor map revised (if needed)
   - Carry-over / sequencing notes updated
   - Risk notes appended
   - Explicit rebalance note added with timestamp and scope

2. **Revised anchor map (if extracted separately)**
   - Remaining primary anchor
   - Remaining secondary anchor (if realistic)
   - Day-by-day assignments for remaining days
   - Work type and capacity notes

3. **Rebalance report** (concise, copy-rable into log or Daily file)
   - File updated
   - Distortion level detected
   - Days affected
   - Anchors changed
   - Work deferred / downgraded
   - Dependencies affecting rebalance
   - Escalation notes (if Level 3)
   - Unresolved uncertainties

4. **Escalation note (if Level 3)**
   - Clear statement of structural change
   - Reference to relevant blocker or decision
   - Flag to next-layer review (Month / Emergency / explicit escalation)

---

## 7. Source-of-Truth Hierarchy

**For rebalance decisions, consult in this order:**

1. **Explicitly acknowledged current execution reality from Daily files**
   - What actually happened this week (not inference)
   - Forensic evidence from daily closures
   - Highest priority

2. **Active Weekly Execution file (current operational state)**
   - The file being rebalanced
   - Subject to correction when Daily evidence contradicts

3. **WeekPlan as planning intent baseline**
   - Remains the planning reference
   - Not rewritten by rebalance
   - Can be noted as "plan intent vs actual" but not altered

4. **Dependency reality and project readiness**
   - Actual blocker states
   - Real project capacity constraints
   - Not inferred; must be verified

5. **Month context**
   - Monthly strategy as reference only
   - Not rewritten; escalation note added if threatened

6. **Anchor tracking history (optional)**
   - Previous week patterns useful for calibration
   - Not binding on rebalance decision

**Key principle:**  
Daily files are the source of truth for what happened. Weekly Execution is the editable operational layer. Rebalance must reconcile the two without rewriting the daily evidence.

---

## 8. Rebalance Boundaries

### Allowed Changes

✅ **Operational corrections:**
- Adjust remaining daily anchors to match real capacity
- Resequence remaining tasks to respect dependencies
- Reduce scope to fit actual remaining capacity
- Convert blocked tasks to conditional or deferred status
- Move meaningful unfinished work later in the same week (if other days have capacity)
- Mark explicit risk to weekly outcomes
- Append rebalance note with timestamp and scope
- Update carry-over notes to reflect new constraints

✅ **Reality alignment:**
- Mark work as blocked explicitly (not ignored)
- Acknowledge capacity consumed unexpectedly
- Note dependency changes clearly
- Record which planned anchors are no longer viable
- Capture what remains realistic vs what must defer

---

### Not Allowed Changes

❌ **Do not rewrite history:**
- Do not alter completed daily execution records
- Do not erase evidence of drift
- Do not inflate progress that didn't happen
- Do not create fake "recovery" narratives

❌ **Do not rewrite planning baselines:**
- Do not silently change WeekPlan goals (add a reference note if needed, but do not edit WeekPlan)
- Do not rewrite Monthly strategy
- Do not pretend blocked work is executable
- Do not create hidden third or fourth project spread to absorb scope

❌ **Do not hide strategic decisions:**
- Do not bury priority overrides inside operational language
- Do not hide structural breaks inside normal rebalance wording
- Do not create false certainty about unresolved dependencies
- Do not overload remaining week to compensate emotionally for early-week losses

❌ **If strategic direction must change:**
- Create escalation note explicitly
- Record the decision / override requirement
- Do not hide it; make it visible for next-layer review

---

## 9. Data to Collect Before Rebalancing

**Operational checklist — gather before starting rebalance:**

- [ ] Week name and exact date range (e.g., W10, 2026-03-09 to 2026-03-15)
- [ ] Today's date and day of week (confirm rebalance is not on Review/Closeout day)
- [ ] Active primary anchor (from current Weekly Execution)
- [ ] Active secondary anchor if any (from current Weekly Execution)
- [ ] Days already executed (e.g., Mon, Tue, Wed by Wed PM)
- [ ] Days remaining (e.g., Wed PM, Thu, Fri)
- [ ] Actual completed work (list from daily closures)
- [ ] Actual unfinished meaningful work (list from daily spillover packs)
- [ ] Blocked work and blocking reason (e.g., "Signee context pending customer email")
- [ ] Dependency changes since week start (list any new or changed dependencies)
- [ ] Capacity changes since week start (e.g., "Thu energy dip confirmed; S-only evening appropriate")
- [ ] Project state changes (any project priority or readiness shift?)
- [ ] Risk to weekly goals (are outcomes still achievable? If not, by how much?)
- [ ] Risk to month-level commitments (is monthly objective threatened?)
- [ ] Distortion level classification (Local / Weekly / Structural?)
- [ ] Escalation required? (Level 3 only)

---

## 10. Rebalance Procedure

### Step 1 — Read Current State

**Instructions:**
1. Open the active `W##_Execution.md` file (the file being rebalanced)
2. Read the complete current weekly execution state
3. Note the current primary anchor, secondary anchor, remaining schedule
4. Read the paired `W##_WeekPlan.md` file as planning baseline reference (for context only)
5. Read all relevant Daily files already completed this week
6. Identify factually what has changed since the week started

**Output of Step 1:**
- Clear picture of planned weekly frame
- Clear picture of actual execution to date
- Explicit list of gaps between plan and reality

---

### Step 2 — Confirm Rebalance Scope

**Instructions:**
1. Review the distortion level (Local / Weekly / Structural)
2. Confirm the situation exceeds Local Drift and warrants rebalance
3. Ask: "Does the remaining week look coherent with current Weekly Execution?"
   - If yes, do not rebalance; handle as carry-over
   - If no, proceed
4. Define the scope of the rebalance:
   - Affects anchor map only? (keep anchors, adjust days)
   - Affects task sequencing? (reorder remaining work)
   - Affects capacity shape? (reduce project spread)
   - Affects outcomes realism? (defer some weekly goals explicitly)
   - Triggers escalation? (Level 3 structural break)

**Output of Step 2:**
- Confirmation rebalance is warranted
- Clear scope definition
- Distortion level classification recorded

---

### Step 3 — Preserve Planning Baseline

**Instructions:**
1. Keep `W##_WeekPlan.md` intact (do not edit it)
2. Do not rewrite WeekPlan goals, commitments, or intent
3. If you must note mismatch between plan and execution, add a separate reference note in Weekly Execution (e.g., "Plan intent: X anchors; Actual capacity achieved: Y; see rebalance note")
4. Keep the distinction between plan (intent) and execution (reality) visible and separate

**Output of Step 3:**
- WeekPlan remains unchanged
- Distinction between plan and execution is clear

---

### Step 4 — Recompute the Remaining Week

**Instructions:**
1. Focus entirely on the remaining days of the current week (not completed days)
2. List all unfinished meaningful work (not carry-over noise)
3. Identify the minimum coherent operating frame for the remaining days
4. Determine if the current primary anchor is still viable
   - If yes, keep it; adjust scope only
   - If no, replace it with the most viable next anchor
5. Determine if the secondary anchor still fits real capacity
   - If yes and space remains, keep it
   - If no, move it to conditional status or defer to next week
6. Encode dependency-aware sequencing explicitly:
   - Mark work that depends on unresolved blockers
   - Mark work that must happen before other work
   - Include re-entry block notes if spillover is inherited
7. Identify minimum completable outcomes for the week given real constraints
8. Mark explicitly what must defer to next week, and why

**Output of Step 4:**
- Recomputed remaining-week anchor map
- Realistic day-by-day assignments
- Explicit dependency and sequencing notes
- Clear distinction between must-complete and can-defer outcomes

---

### Step 5 — Update the Weekly Execution File

**Instructions:**
1. Add a clearly labeled "REBALANCE" section or timestamp note (e.g., "REBALANCED 2026-03-13 PM by DAILY INTEGRATION")
2. Update the remaining-day anchor map (if changed)
   - Keep completed-day records unchanged
   - Insert updated anchor assignments for remaining days
   - Note which anchors were revised and why
3. Update carry-over and dependency notes to reflect new constraints
4. Mark what has been:
   - Deferred (to later week)
   - Downgraded (from must-complete to conditional)
   - Made conditional (blocked, pending external dependency)
   - Resequenced (moved to different day)
5. Keep all already-completed daily records unchanged
6. Preserve traceability (reader should understand what changed and why)

**Output of Step 5:**
- Updated Weekly Execution file
- Changes clearly marked
- Historical accuracy maintained
- Remaining week is coherent

---

### Step 6 — Detect Escalation Conditions

**Instructions:**
1. Ask: "Is this a Structural Break (Level 3)?"
   - Did a critical dependency fail?
   - Was an explicit priority override received?
   - Is monthly objective threatened?
   - Is emergency response needed?
2. If Level 3: Record the escalation explicitly
   - State what the structural change is
   - Note the source (dependency failure, priority override, capacity drop, etc.)
   - Flag explicitly that this requires next-layer review (Month / Emergency)
   - Do not hide it in normal operational language
3. If Level 2 (Weekly Distortion only): No escalation needed; rebalance completes

**Output of Step 6:**
- Escalation note (if Level 3)
- Clear structure preserved (escalation is visible, not hidden)

---

### Step 7 — Consistency Check

**Instructions:**
Verify the following before considering rebalance complete:

- [ ] Weekly Execution reflects recent Daily reality (no contradiction)
- [ ] Remaining week is realistic (not overloaded to compensate)
- [ ] WeekPlan is not silently rewritten (planning baseline preserved)
- [ ] Month strategy is not silently rewritten (monthly context preserved)
- [ ] Project states are not contradicted (rebalance respects actual project capability)
- [ ] Dependency handling is explicit (not glossed over)
- [ ] No false certainty introduced (uncertainties marked as such)
- [ ] Traceability maintained (reader can understand what changed and why)
- [ ] Escalation note is present (if Level 3)
- [ ] Daily files can inherit cleanly from revised Weekly Execution

**Output of Step 7:**
- Consistency confirmed
- Rebalance is internally coherent
- Ready for next Daily file or week closeout

---

### Step 8 — Produce Report

**Instructions:**
1. Create a brief rebalance report with the following structure:
   - File updated: `<filename>` with timestamp
   - Distortion level detected: Local | Weekly | Structural
   - Days affected: <list of days where changes apply>
   - Anchors changed: <list of changed anchors with before/after>
   - Work deferred: <list of work moved to later week or next week>
   - Work downgraded: <list of tasks moved from must-complete to conditional>
   - Dependencies affecting rebalance: <list of blockers or changed dependencies>
   - Escalation notes: <if Level 3, state clearly>
   - Unresolved uncertainties: <list anything still unknown>
   - Report produced by: <Agent 2 | Agent 1 | explicit decision maker>
   - Report timestamp: <date/time>

2. Make the report copy-able; it may be logged or included in next Daily file

**Output of Step 8:**
- Concise rebalance report
- Readable, loggable format
- Clarity on what changed, what stayed, what escalated

---

## 11. Allowed vs Forbidden Changes

### Summary Table

| Change type | Allowed? | Example | Constraint |
|---|---|---|---|
| Adjust remaining daily anchors | ✅ | Move Zephyr from Wed to Thu if Wed was consumed by Signee | Must respect project state and dependencies |
| Resequence remaining tasks | ✅ | Move pptx skeleton to Fri if Thu has unexpected blocker | Sequencing must be realistic |
| Reduce scope to fit capacity | ✅ | Mark RobotOS pptx detail as deferred, keep skeleton | Keep most critical outcomes |
| Convert blocked tasks to conditional | ✅ | Signee context becomes "pending customer email" | Blocker must be real, not assumed |
| Move unfinished work later in week | ✅ | Move test merge from Tue to Wed if blocked | Other day must have actual capacity |
| Mark risk to weekly outcomes | ✅ | "W10 RobotOS pptx detail at risk; focus on skeleton" | State the risk clearly |
| Append rebalance note | ✅ | "REBALANCED 3/13 PM: Thu blocker moved Fri anchor" | Note must be explicit and timestamped |
| Update carry-over notes | ✅ | "Updated re-entry: Fri AM = check merge approval; Sat = verify compile" | Notes must be actionable |
| Alter completed daily records | ❌ | Do not change what Mon/Tue actually accomplished | Completed days are historical truth |
| Erase drift evidence | ❌ | Do not remove spillover records | Keep evidence visible |
| Inflate progress | ❌ | Do not claim work was done if it wasn't | Report actual state |
| Create hidden project | ❌ | Do not slip in a fourth project to absorb scope | Max 2 projects per day rule maintained |
| Rewrite WeekPlan | ❌ | Do not edit WeekPlan file itself | Add reference note in Execution only |
| Rewrite Month strategy | ❌ | Do not alter Monthly commitments | Escalate if threatened |
| Pretend blocked work is executable | ❌ | Do not plan "finish Signee docs" if email still blocked | Mark as conditional or deferred |
| Hide priority override | ❌ | If strategic direction changes, record escalation | Do not bury inside normal language |

---

## 12. Escalation Rules

**Stay inside Weekly Rebalance when:**
- Distortion is Level 2 (Weekly Distortion)
- Root cause is execution drift, not strategic shift
- Weekly goals remain achievable with adjusted sequencing
- No external priority override or emergency
- Month strategy and objectives unaffected

**Add escalation note when:**
- Structural Break (Level 3) detected
- Critical dependency failed
- Explicit priority override received (from Agent 1, user, or external requirement)
- Monthly objective at risk
- Emergency response required

**Escalation language example:**
> "Escalation: Zephyr critical dependency failed 3/13 PM (develop branch build broken). Weekly Rebalance applied to salvage remaining capacity. Month-level test merge commitment flagged at risk. Requires Month Review 3/16."

**Route escalation to:**
- **Month Review layer:** If monthly objective threatened
- **Emergency control:** If urgent context switch required
- **Explicit decision maker:** If priority override needed from outside normal ops flow
- **Agent 1 review:** If Level 3 involves strategic decision (not just execution correction)

---

## 13. Definition of a Good Rebalance

A rebalance is successful when:

✅ **Coherence:** Remaining week looks realistic and believable (not aspirational or overloaded)

✅ **Reality alignment:** Weekly Execution reflects Daily evidence (no contradiction between files)

✅ **Traceability:** Reader can understand what changed, what stayed, and why

✅ **Baseline preservation:** WeekPlan and Month strategy remain intact (only operational execution layer edited)

✅ **Inheritance ready:** Next Daily file can inherit from revised execution cleanly (no hidden surprises)

✅ **Anchor structure:** Remaining primary anchor is defensible; secondary anchor is realistic or explicitly deferred

✅ **No emotional overcompensation:** Remaining week does not attempt to magically recover lost capacity; goals are resized to reality

✅ **Escalation visible:** If structural change occurred, it is noted explicitly (not hidden)

✅ **Uncertainty marked:** Unresolved blockers and dependencies are called out (not assumed resolved)

✅ **Completeness:** All material work is accounted for (deferred, downgraded, continued, or blocked)

---

## 14. Standard Checklist

**Use this checklist before and after rebalancing:**

### Pre-Rebalance Assessment

- [ ] Distortion level confirmed (Weekly or Structural)?
- [ ] Situation exceeds Local Drift?
- [ ] Current date is not Review/Closeout day?
- [ ] All completed Daily files are present and closed?
- [ ] Major changes are known (not still being discovered)?
- [ ] Understand actual completed work vs remaining work?

### Rebalance Execution

- [ ] Step 1 complete — read current state and identify gaps
- [ ] Step 2 complete — confirm scope and distortion level
- [ ] Step 3 complete — preserve WeekPlan and Month intact
- [ ] Step 4 complete — recompute coherent remaining week
- [ ] Step 5 complete — update Weekly Execution file with changes marked
- [ ] Step 6 complete — detect escalation conditions (if Level 3)
- [ ] Step 7 complete — consistency check passed
- [ ] Step 8 complete — report produced

### Post-Rebalance Validation

- [ ] Weekly Execution reflects Daily reality (no contradiction)?
- [ ] Remaining week is realistic (not overloaded)?
- [ ] WeekPlan not silently rewritten?
- [ ] Month strategy not silently rewritten?
- [ ] Project states not contradicted?
- [ ] Anchor structure believable?
- [ ] Escalation note present (if Level 3)?
- [ ] Rebalance report produced and timestamped?
- [ ] Report is copy-rable (loggable)?

### Next Steps

- [ ] Next Daily file can inherit cleanly (no surprises)?
- [ ] Rebalance report logged or filed?
- [ ] Escalation routed (if Level 3)?
- [ ] One-line summary prepared for Day Closeout?

---

## 15. Reusable Execution Template

Use this template for future weekly rebalance runs. Copy, replace placeholders, and paste into Copilot or Agent 2 command:

```
TASK: Perform WEEKLY_REBALANCE for <WEEK_NAME>

Context:
- Active week: <WEEK_NAME> (<START_DATE> to <END_DATE>)
- Current date: <TODAY_DATE> <DAY_NAME>
- Today's status: <DAYS_COMPLETED>/<TOTAL_DAYS> days executed
- Distortion trigger: <DISTORTION_REASON>

Files to update:
- Weekly Execution: <WEEK_EXECUTION_FILE>
- Planning baseline (reference only): <WEEKPLAN_FILE>
- Completed daily files: <DAILY_FOLDER>/2026-<MM>-<DD>_Daily.md (all executed days)

Context files (if relevant):
- Month context: <MONTH_FILE>
- Project files: <PROJECT_FOLDER>
- Anchor tracking: <ANCHOR_TRACKING_FILE>

Rebalance scope:
- Days affected: <AFFECTED_DAYS>
- Distortion level: <LEVEL_2_OR_LEVEL_3>
- Rebalance focus: <REBALANCE_SCOPE>
  (e.g., "anchor map only", "resequence + capacity reduction", "escalation required")

Specific constraints:
- Primary anchor current status: <CURRENT_PRIMARY>
- Known blockers: <BLOCKER_LIST>
- Dependency changes: <DEPENDENCY_CHANGES>
- Capacity state: <CAPACITY_STATE>
- Risk to weekly outcomes: <OUTCOME_RISK>
- Risk to month objectives: <MONTH_RISK>

Instructions:
Follow WEEKLY_REBALANCE.md Steps 1–8:
1. Read current state; identify gaps
2. Confirm rebalance scope and distortion level
3. Preserve WeekPlan and Month baseline
4. Recompute coherent remaining week
5. Update <WEEK_EXECUTION_FILE> with changes marked
6. Detect escalation conditions (if Level 3)
7. Consistency check
8. Produce rebalance report

Expected output:
- Updated Weekly Execution file (with rebalance note and timestamp)
- Rebalance report (concise, copy-rable)
- Escalation note (if Level 3)
- One-line summary for logging

Report format:
- File updated: <FILENAME>
- Distortion level: Level <N>
- Days affected: <LIST>
- Anchors changed: <BEFORE> → <AFTER>
- Work deferred: <LIST>
- Work downgraded: <LIST>
- Dependencies: <LIST>
- Escalation: <IF LEVEL 3>
- Unresolved uncertainties: <LIST>
```

---

## Appendix A: Integration with LIFE_AGENT Procedures

**Relationship to other operating procedures:**

| Procedure | Relationship | Sequencing |
|---|---|---|
| [GENERATE_WEEKLY_EXECUTION.md](GENERATE_WEEKLY_EXECUTION.md) | Creates baseline Weekly Execution at start of week (Mode A); rebalance corrects it mid-week | GENERATE runs once (week start); REBALANCE runs if/when needed (mid-week) |
| [INTEGRATE_DAILY.md](../DAILY_INTEGRATION/INTEGRATE_DAILY.md) | Daily integration may trigger rebalance if Daily evidence shows weekly-level distortion | INTEGRATE runs daily; if distortion detected, may trigger REBALANCE |
| [PREPARE_NEXT_DAILY.md](../DAILY_INTEGRATION/PREPARE_NEXT_DAILY.md) | Next daily preparation inherits from Rebalanced Weekly Execution | REBALANCE updates Weekly Execution; PREPARE_NEXT_DAILY then reads updated Weekly Execution |

**Cross-reference notes:**
- If weekly execution has drifted significantly, INTEGRATE_DAILY should flag for rebalance
- REBALANCE updates the Weekly Execution file that PREPARE_NEXT_DAILY will inherit from
- GENERATE_WEEKLY_EXECUTION is run at week start and (rarely) at week end for reconstruction; REBALANCE is mid-week correction only

---

## Appendix B: Troubleshooting

### Common rebalance questions:

**Q: Should I rebalance or just update the next Daily file?**  
A: If the gap is Local Drift (one day, one task, <30% scope impact), handle via next Daily carry-over. If weekly-level coherence is lost (2+ days affected, 30%+ scope impact, anchor pattern broken), run REBALANCE.

**Q: What if the remaining week is unrealistic even after rebalance?**  
A: That's fine. The goal of rebalance is coherence, not magic recovery. If remaining week is still challenging, mark that in the rebalance report and record any escalation needed.

**Q: Can I rebalance if I'm not sure what will happen tomorrow?**  
A: Rebalance based on what you know today. Mark unresolved uncertainties explicitly. Tomorrow may require another PREPARE_NEXT_DAILY re-entry pack if new information arrives.

**Q: Does rebalance change the WeekPlan?**  
A: No. Rebalance updates the Weekly Execution file (operational reality). Rebalance may note that actual execution differed from plan intent, but does not alter WeekPlan itself.

**Q: What if a Level 3 Structural Break happens late in the week?**  
A: Still run REBALANCE to stabilize remaining days. Escalation note is added. Month Review may determine what to do with end-of-week outcomes. Do not hide the structural change; make it visible.

---

## Appendix C: Historical Examples (Not Required Reading)

*Examples of rebalance scenarios will be captured in real execution history. This section is placeholder for future case studies.*

- Example 1: Level 2 rebalance (dependency delay mid-week)
- Example 2: Level 3 rebalance (capacity drop due to illness)
- Example 3: Level 3 rebalance (project priority override)

---

**Document version:** 1.0  
**Created:** 2026-03-15  
**Status:** Operational — ready for weekly use  
**Maintenance:** Review and update quarterly or after major LIFE_AGENT system changes
