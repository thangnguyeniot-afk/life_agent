# W12 Hardening Patch: Weekend Pool Overflow Prevention

**Date:** March 24, 2026  
**Vulnerability:** Weekend Pool Overflow (declared slots appear realistic, but allocated effort is unsustainable)  
**Scope:** New validation checks for CAPACITY_ENGINE + enforcement mechanism  
**Status:** Ready for implementation

---

## Executive Summary

**The Issue:**

Current validation (V1–V12) requires weekend slots to be declared explicitly (R11), but does NOT verify that declared effort is realistically decomposable into those slots or that weekend capacity doesn't silently inflate to unsustainable levels.

**Example Failure Mode (Gaming Pipeline):**
1. Week plan declares: "Sat daytime 5h, Sun afternoon 4h" ✓ (passes V12 — slots declared)
2. Capacity table shows: "RobotOS 7h + Signee 2h = 9h from weekend slots" ✓ (math works)
3. But no validation that:
   - Those 9h actually decompose into realistic work units (M-sized blocks)
   - Sat 5h + Sun 4h + other weekday evenings don't total to >18h personal execution/week
   - If RobotOS test suite only needs 3 test files to be written, why is Sat 5h assigned when 2h suffices?

**Result:** Weekend effort is cosmetically unrolled but operationally infeasible. Week fails in execution, then blame lands on "bad estimates" not "the capacity model allowed it."

**The Fix:**

- **NEW V13:** Weekend effort realism check — validate declared weekend hours against project-specific scope decomposition
- **NEW V14:** Personal capacity ceiling check — validate that total personal execution (weekday evening net + weekend days) is sustainable and does not exceed realistic human capacity
- **NEW enforcement:** Slot spillover detection — if project scope grows beyond declared weekend slots, system forces choice: reduce scope, extend weekend allocation (with realism check), or defer to next week
- **Anti-gaming rule:** Weekend slot size must NOT be driven by "we need to close capacity math" — must be driven by "here's what this project actually needs to do Sat/Sun"

---

## Problem Structure

### Current Validation Gap

**V12 (Weekend Usage Decision) currently validates:**
- ✅ All five slots declared (not vague day-based language)
- ✅ Mode selected (A: Sat only, B: Sun only, C: both)
- ✅ Slot values present (not missing)
- ✅ Math proof if execution slot = 0h

**V12 does NOT validate:**
- ❌ Whether declared hours align with actual scope
- ❌ Whether weekend hours + evening hours = sustainable total
- ❌ Whether work can realistically fit in declared slots (no spillover)
- ❌ Whether weekend allocation is driven by need vs. cosmetics

**Result:** A plan can satisfy V12 perfectly while being operationally unrealistic.

### Gaming Scenarios (Pre-Patch)

#### Scenario A: Slot Inflation

**Setup:**
- RobotOS needs: "Write test file for memory management (4h work)"
- Weekday evening capacity: 4h available
- But planner wants to keep evening light…

**Gaming Move:**
- "Declare Sat daytime 4h for test file" (same work, different slot)
- V12 passes (slot declared; math works)
- V6 passes (effort estimate matches; not mismatched)
- No check catches that Sat allocation was driven by "make evenings lighter" not by "Sat is where this work must go"

#### Scenario B: Cumulative Overload

**Setup:**
- Week plan declares weekday evening: 6h personal (Thu S-only, Fri none = Mon–Wed 6h net)
- Week plan declares: Sat daytime 6h, Sun afternoon 4h = 10h weekend
- Total: 16h personal execution/week

**The trap:**
- Each component looks realistic in isolation
- But 16h/week personal execution is >200h/year sustainable load
- No V-check catches the cumulative total

**Gaming move:**
- Planner thinks: "Each day can give ~2h evening (10h gross), weekend adds 10h, so 20h available"
- But structural deductions (Thu S-only, Fri closure) mean net is really ~6h weekday
- Plans end up requiring 16h personal/week but capacity table shows 20h available
- When week fails (Sat work incomplete), blame goes to "bad anchor" not "capacity math was wrong"

#### Scenario C: Undecomposed Weekend Scope

**Setup:**
- Goal: "RobotOS architecture review + refactoring ready for Mon merge"
- Scope estimate: "~8h focused work"
- Planner thinks: "That's Sat daytime 8h; boom, done"

**Reality:**
- 8h "focused work" = 2 deep blocks of ~3.5–4h each
- But Sat daytime is ONE 5–6h block (single morning/afternoon)
- To fit 2 blocks into one day requires: start early (6:30 soft start, not hard execution) + no breaks + no context switching = unrealistic
- Should have been decomposed: Sat 4h (1 block) + Sun afternoon 4h (second block) — but planner allocated flat 8h to Sat

**Gaming move:**
- Planner states: "Sat daytime 8h for RobotOS refactor"
- V12 passes (slot declared; Mode A valid)
- V6 passes (effort estimate = allocation)
- No check catches that 8h into one daytime slot is operationally impossible (not 2 distinct blocks)

---

## New Validation Checks

### V13 — Weekend Effort Realism Check

**Purpose:** Ensure declared weekend hours align with actual scope decomposition and are realistically executable in declared slots.

**Validation:**

1. **Decomposition Rule:** Each project allocated to weekend must have explicitly decomposed tasks (M-sized missions or phases) that fit the declared slots.
   - Sat daytime 5h = max 1 focused M-block (3–4h execution + 1–1.5h setup/breaks) OR 2 small tasks (2h each, with setup)
   - Sun afternoon 3h = max 1 focused M-block if fresh, or 2 small tasks if second session
   - If declared weekend hours > 2 M-blocks per day, scoping is probably wrong
   - **Failure condition:** "8h weekend RobotOS work" with no breakdown of which tasks fit where

2. **Scope-Allocation Consistency:**
   - Each project's scope (from project context or goals) must be traceable to weekend slots
   - If RobotOS goal is "test file written (4h)" and Sat is allocated 6h to RobotOS, justify the +2h
   - **Failure condition:** Sat daytime 6h RobotOS allocated with only 4h of identified scope ("leftover for cleanup")

3. **Spillover Scenario Check:**
   - Assume work exceeds declared slot by ~10% (realistic overrun)
   - Q1: Does spillover fit in the other weekend slot?
   - Q2: If not, does spillover fit in a named evening block?
   - Q3: If not, is deferral to next week explicitly documented?
   - **Failure condition:** Sat 6h RobotOS + Sun 0h afternoon + plan assumes "if it runs over, it fits Sunday" (implicit spillover)

**When to apply V13:**
- Run AFTER V6 (goal-allocation match)
- Run AFTER V9 (capacity sum)
- Run BEFORE accepting weekend mode and slot allocation

**Output:** 
- PASS: Declared weekend hours match decomposed scope; spillover path exists or not needed
- WARN: Declared weekend hours exceed identified scope by >20%; proceed with assumption documented
- FAIL: Declared weekend hours cannot be decomposed into realistic day-blocks; or spillover has no path

---

### V14 — Personal Capacity Ceiling Check

**Purpose:** Ensure total personal execution (weekday evening net + weekend days) does not exceed sustainable human capacity.

**Validation:**

1. **Sustainable Personal Capacity Calculation:**
   - Baseline: 10h/week weekday evenings (gross)
   - Minus: structural deductions per anchor (Thu S-only, Fri closure, etc.)
   - Result: net weekday evening capacity (typically 5–8h/week realistically executable)
   - Plus: weekend daytime (Sat, Sun afternoon) — declared hours per week plan
   - Plus: explicitly opened weekend evening (if Mode A/B/C allows + planning needs it)
   - Minus: Sunday morning overhead (~2–3h structural review/planning)
   - **Realistic sustainable total:** net evening (5–8h) + weekend day (typically 6–10h for normal weeks) = **11–18h/week personal execution**
   - Burnout threshold: >20h/week personal execution (indicating unsustainable sprint)

2. **Allocation Check:**
   - Sum all TYPE B + TYPE C hours from capacity table
   - Compare to sustainable range: 11–18h/week ✓ (normal), 18–20h/week ⚠️ (stretched), >20h ❌ (unsustainable)
   - If personal total > 18h, document assumption and escalate

3. **Trend Detection:**
   - Check if this week's personal load is consistently higher than past 3 weeks
   - If trending upward for 3+ weeks, flag as unsustainable pattern

**When to apply V14:**
- Run AFTER V9 (capacity sum) and V13 (weekend effort realism)
- Run BEFORE finalizing capacity model

**Output:**
- PASS: Personal capacity 11–18h/week (sustainable)
- WARN: Personal capacity 18–20h/week (stretched week; document rationale; escalate if trend >3 weeks)
- FAIL: Personal capacity >20h/week (unsustainable; scope reduction required OR explicit decision to accept sprint; escalate to month context)

---

### V13/V14 Integration Point: Capacity Model Finalization

When V13 or V14 returns WARN or FAIL, the workflow is:

1. **Document assumption explicitly** (in Constraints section)
2. **Choose remediation:**
   - **REDUCE scope:** Move project goal to next week; reduce Sat/Sun allocation; rebalance evening/day split
   - **EXTEND weekend allocation:** If truly needed, increase declared hours BUT re-run V13 (decomposition must hold); document why extension is necessary
   - **DEFER to next week:** Document decision and impact on monthly goal timeline
   - **ESCALATE:** If constraint is external (e.g., month goal deadline requires this scope this week), escalate to month file for decision

3. **Re-validate:** After remediation, re-run V13 and V14 before accepting

---

## New Enforcement: Slot Spillover Detection

### Rule: Declared Slots Are Load-Bearing

**Principle:** If project scope is declared into weekend slots at 5h Sat + 4h Sun, then:
- Sat work must NOT exceed 5h (not 5h + spillover to evening)
- Sun work must NOT exceed 4h
- Spillover is NOT automatically absorbed by "whatever capacity remains"

### Detection Mechanism

**During week execution (through daily planning):**
1. As daily anchors are created, each mission must be assigned to a specific slot
2. If a mission assigned to "Sat" would exceed declared 5h total, system flags it
3. SLipover decision must be made:
   - **Move to Sun afternoon** (if available and not pre-allocated)
   - **Move to earlier evening block** (if available and not pre-allocated)
   - **Defer to next week** (with escalation)
   - **Override** (with explicit approval and rationale documented)

### Implementation Point

This is NOT a CAPACITY_ENGINE check (engine validates the *plan*, not execution).  
This is GENERATE_WEEKLY_EXECUTION integration:
- GENERATE_WEEKLY_EXECUTION receives weekend slot allocations from W##_WeekPlan capacity section
- When creating daily execution anchors, if mission scope would exceed declared slot, require explicit decision

---

## Example: Patch Application to Gaming Scenarios

### Scenario A Revisited: Slot Inflation

**Original Setup:**
- RobotOS test file: 4h work
- Planner declares: Sat daytime 4h (instead of weekday evening 4h)

**V13 Check (Weekend Effort Realism):**
- Scope: 1 test file = 1 M-block ≈ 3–4h ✓
- Sat 4h sufficient; no spillover needed ✓
- Decomposition check passes

**BUT the vulnerability is decision-making:**
- Why move from evening to Sat?
- If the answer is "to lighten evening load," that's not a valid capacity reason (it's preference)
- If the answer is "test file is complex; needs full Sat morning focus," that's valid

**Patch fix:** Add justification column to weekend allocation:
- "RobotOS test file (4h) → Sat daytime 4h — better focus continuity than fragmented evenings"
- "vs."
- "RobotOS test file (4h) → Sat daytime 4h — evening load was already 6h so preferred weekend"

The FIRST is defensible (project-driven); the SECOND shows gaming (load-driven).

**New rule:** Capacity table must show **why each project is allocated to weekend**, not just **that it is**.

---

### Scenario B Revisited: Cumulative Overload

**Original Setup:**
- Weekday evening: 6h net (after structural deductions)
- Weekend: Sat 6h + Sun 4h
- Total: 16h personal

**V14 Check (Personal Capacity Ceiling):**
- Range: 11–18h/week sustainable
- Allocation: 16h → WARN (stretched week; requires assumption)

**Result:**
- Planner must acknowledge: "This is a stretched week. Rationale: Q1 deliverable deadline; no multi-week span available. Escalated to month context."
- Or choose remediation: reduce scope to 13h (shift 3h goal to next week)

**Patch guarantees:** Planner cannot silently create a 16h week without explicit decision and documentation.

---

### Scenario C Revisited: Undecomposed Weekend Scope

**Original Setup:**
- Goal: RobotOS architecture review + refactoring (8h focused work)
- Declared allocation: Sat daytime 8h

**V13 Check (Weekend Effort Realism):**
- Decomposition question: How many M-blocks is 8h?
  - Answer: 2 blocks (~4h each, including breaks)
- Can 2 M-blocks fit in 1 Saturday daytime (5–6h)?
  - No: would require back-to-back focus without real break (unrealistic)
- Spillover assumption: Move second block to Sun afternoon?
  - Requires: Sat 4h (1st block) + Sun 4h (2nd block)
- But plan declared: Sat 8h, Sun 0h

**V13 Failure:** Declared allocation cannot hold undecomposed scope. Must either:
- Decompose into Sat 4h + Sun 4h (with day boundaries), OR
- Reduce scope (architecture review only, defer refactoring), OR
- Extend to weekday evening (evening + Sat)

**Result:** System forces decomposition + realism check before accepting allocation.

---

## Anti-Gaming Guard Rails

### Guard Rail 1: Justification for Weekend Allocation

**Every project allocated to weekend Sat/Sun must state in Capacity table:**
```
| Project | Type | Personal Blocks | Hours | Justification |
|---|---|---|---|---|
| RobotOS | TYPE B | Sat daytime | 4h | Test file requires uninterrupted focus; evening fragmented across Mon–Wed; full morning block ideal |
| Signee | TYPE C | Sun afternoon | 2h | Spec review async task; lower priority; Sun slots available; preserves Mon–Fri evenings |
```

**Testing:** Justification must be **project-driven** (scope/focus needs), not **load-driven** (need to make room for other stuff).
- ✓ Valid: "uninterrupted focus required"
- ✓ Valid: "complex synthesis needs fresh mind; evening too fragmented"
- ✗ Invalid: "evening was already 6h so moved this to Sat"
- ✗ Invalid: "weekend gives more total capacity"

### Guard Rail 2: Spillover Path Requirement

**For EVERY weekend slot with allocated work ≥3h:**
```
Spillover if work exceeds declared X h by 10–20%:
  → [specify which slot receives spillover: evening block X, weekend day Y, or defer to Week N+1]
  → [if deferral, state impact on month goal]
```

**Mandatory:** No implicit spillover. Overflow must have a declared path or must be escalated.

### Guard Rail 3: Personal Load Trend Detection

**Track personal capacity (TYPE B + TYPE C hours) week-over-week:**
- W10: 12h
- W11: 15h ← +3h
- W12: 17h ← +2h
- Trend: 3-week upward slope ⚠️

**Rule:** If personal load consistently trends upward (Δ >2h/week for 3 weeks), escalate to month context for sustainability decision.

### Guard Rail 4: Decomposition Requirement for Weekend

**Before accepting weekend scope >4h:**
- Must have explicit M-sized task breakdown
- Each task must be ~3–4h (matching a focus block)
- If scope requires >4h, must decompose into multiple day-boundary tasks (Sat + Sun)

---

## Implementation Checklist

### Step 1: Update CAPACITY_ENGINE.md

**Add after V12 — Weekend Usage Decision:**
```markdown
### V13 — Weekend Effort Realism Check

[Insert validation rule from section above]

### V14 — Personal Capacity Ceiling Check

[Insert validation rule from section above]
```

**Update Validation Checks table to include V13, V14 rows**

### Step 2: Update GENERATE_WEEKPLAN.md

**Step 6 — Assess Capacity and Effort Balance:**
- Add sub-step: "Run V13 and V14 checks after V12"
- Add decision logic: if V13/V14 WARN/FAIL, document assumption and remediation choice

**Step 10 — Write WeekPlan File:**
- Update Capacity table template to include "Justification" column for weekend allocations
- Add "Spillover Plan" row under Weekend slots
- Add "Personal Load Trend" section (compare to past 3 weeks)

### Step 3: Create Weekend Decomposition Template

**New file:** `OS/04_OPERATIONS/WEEKLY_CONTROL/TEMPLATE_WEEKEND_DECOMPOSITION.md`

Purpose: Provide structure for planners to decompose weekend scope before running capacity engine.

Template sections:
- Project name, weekend slots (Sat daytime / Sun afternoon)
- For each slot: list of M-sized missions (with effort/focus type)
- Spillover scenario: what happens if slot work +10%?
- Total personal load: weekday eve + weekend = X h/week ✓ (within sustainable band)

### Step 4: Patch W11 / W12 Capacity Validation

**Test new checks on W11 (existing instance):**
- Does W11 capacity model pass V13? (decomposition check)
- Does W11 pass V14? (personal load ceiling)
- If not, document assumptions in W11 Capacity & Constraints section

**Apply to W12 (first instance with new checks):**
- W12 capacity validation must include V13 + V14
- Document any decisions / assumptions

---

## Expected Outcomes

### What Changes

| Aspect | Before | After |
|---|---|---|
| **Weekend slot validation** | V12: declared (slots named correctly) | V13 + V14: declared + realistic decomposition + sustainable total |
| **Slot inflation ability** | Can move 4h evening work to Sat without justifying | Must justify project-driven reason (not load-driven) |
| **Cumulative overload** | 16h personal/week allowed if all slots declared | 16h flagged as WARN; requires decision documentation |
| **Undecomposed weekend scope** | "Sat 8h RobotOS refactor" allowed | Must decompose: "Sat 4h M1 refactor + Sun 4h M2 testing" |
| **Spillover absorption** | Implicit (fits somewhere) | Explicit (declared slot or deferred) |

### What Stays Same

- R11 still in effect (5 weekend slots, must be declared)
- V12 still enforces slot declaration
- Pool A / Pool B separation unchanged
- TYPE A/B/C classifications unchanged

### Validation Efficiency

- V13, V14 are **quick checks** (not heavy computation)
  - V13: decomposition scan ≈ 2 min (read mission list, verify M-block fit)
  - V14: capacity sum + trend check ≈ 1 min (sum hours, compare to baseline)
- No impact on CAPACITY_ENGINE runtime
- Integrated into GENERATE_WEEKPLAN workflow; no new file required

---

## Transition Plan

### For W12+

1. **CAPACITY_ENGINE.md:** Add V13, V14 check definitions and output rows ✓
2. **GENERATE_WEEKPLAN.md:** Step 6 — add V13/V14 execution ✓
3. **WEEKEND_DECOMPOSITION template:** Create (for planner guidance) ✓
4. **W12_WeekPlan.md:** Apply new checks during planning; document assumptions ✓

### For W11 Retroactive Review (Optional)

- Run V13 + V14 against W11 capacity model
- If passed: document "legacy plan passes new hardening criteria"
- If failed: document "legacy plan created under older rules; decisions re-ratified"
- Learning: what patterns from W11 emerge with new checks?

---

## Summary: What This Prevents

| Gaming Scenario | Blocker | Outcome |
|---|---|---|
| **Slot inflation** | V13 requires project-driven justification | Cannot move work to weekend just to "make room" |
| **Cumulative overload** | V14 caps sustainable personal load; trend detection | Cannot silently grow personal execution >3 weeks |
| **Undecomposed scope** | V13 requires M-block decomposition; slot-fit check | Cannot allocate 8h to 1 daytime slot without reality check |
| **Implicit spillover** | V13 requires spillover path (named or escalated) | Cannot assume overflow "just fits" |
| **Silent weekend extension** | V14 personal ceiling; load trend reporting | Cannot let weekend grow without decision record |

---

## Questions Answered by Patch

### Q1: Is 16h/week personal execution sustainable?

**Before:** Capacity model silent (depends on planner judgment)  
**After:** V14 WARN (flags as stretched; requires decision); trend detection alerts if pattern continues 3+ weeks

### Q2: How do I know if my weekend allocation is realistic?

**Before:** No check (validation only checked declaration, not feasibility)  
**After:** V13 (requires M-block decomposition; checks slot fit; defines spillover path)

### Q3: What happens if my weekend scope grows during the week?

**Before:** Absorbed implicitly somewhere (not tracked)  
**After:** Spillover detection forces explicit choice (move to available slot, defer, or escalate)

### Q4: Why was I allowed to allocate 8h to one Saturday daytime last week?

**Before:** No validation (8h > realistic day capacity not checked)  
**After:** V13 fails (forces decomposition into realistic day-blocks or scope reduction)

---

## Success Metrics

After W12+ with new hardening:

1. **Weekend scope gaming eliminated:** 0 plans with unjustified slot inflation or undecomposed weekend scope
2. **Personal load sustainability:** Personal execution stays within 11–18h/week (normal range) or explicitly escalated
3. **Spillover captured:** 100% of weekend plans have spillover path (no implicit overflow)
4. **Trend visibility:** Month context can see personal load pattern; can decide if sustained high is acceptable or needs rebalancing
5. **Planning clarity:** Planners can trace weekend allocation back to scope (easier debugging if week fails)

---

## Appendix: V13 + V14 Quick Checklist

### Before Finalizing Weekly Capacity Model

- [ ] V13a: Each weekend-allocated project has M-level task breakdown listed
- [ ] V13b: Each task fits in declared slot (Sat daytime 4–5h max per 1–2 M-blocks; Sun afternoon 3–4h max)
- [ ] V13c: Spillover path exists (either in other weekend slot or explicitly deferred with reason)
- [ ] V14a: Sum of TYPE B + TYPE C hours calculated (net weekday eve + weekend day total)
- [ ] V14b: Personal load in sustainable band (11–18h normal, 18–20h stretched = WARN, >20h = escalate)
- [ ] V14c: Trend checked (compared to W-1, W-2, W-3; if Δ >2h × 3 weeks, escalate)
- [ ] V13/V14 result: PASS / WARN / FAIL documented in Capacity & Constraints section
- [ ] If WARN/FAIL: Remediation choice documented (reduce scope / defer / escalate)
- [ ] Justifications added for weekend allocations (project-driven rationale visible)

---

**Next Steps:**
1. Approve this patch
2. Implement V13 + V14 in CAPACITY_ENGINE and GENERATE_WEEKPLAN
3. Apply to W12 (first live instance)
4. Collect feedback on V13/V14 usability, iteration as needed
5. Archive this document as reference for future hardening

