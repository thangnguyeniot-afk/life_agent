# W12 System Hardening: Executive Summary & Vision

**Context:** The LIFE_AGENT operating system has been progressively hardened (W11 ambiguity rules, size rules, fallback patches, realism QA). This document addresses the remaining **Weekend Pool Overflow vulnerability** — the final major gap in capacity model validation.

---

## What Was Broken

### The Gap

The current capacity validation (V1–V12) requires weekend slots to be explicitly declared (R11), but **does not verify that declared effort is realistically executable** or that personal capacity isn't silently overloaded.

**Example of what passes current validation but fails in practice:**

```
Declared: Sat daytime 8h, Sun afternoon 4h (12h weekend)
Plus: Weekday evening 6h (net after deductions)
Total: 18h personal execution/week

Validation Results (Current System):
✅ V12 PASS — all weekend slots declared (Mode A/B/C selected)
✅ V9 PASS — total allocation fits within modeled capacity
✅ Capacity looks "full but reasonable"

Reality Check (Actual Execution):
❌ Sat 8h requires 2 deep M-blocks (~4h each), but one daytime slot can only hold 1 block + setup (5–6h realistic max)
❌ Second 4h block should move to Sun, but planner already allocated Sun to different project
❌ Spillover absorbed silently; either Sun work gets postponed or Sat work incomplete
❌ 18h/week personal execution is at edge of sustainable; any friction causes full week failure
```

**Why this matters:**
- Current system allowed this plan to pass validation
- Planner believed it was achievable (validation "approved" it)
- Week fails → blame assignment (bad estimates? bad anchor?) misses real issue (capacity model allowed unrealistic allocation)

### Root Cause

**V12 validates DECLARATION**, not REALISM:
- ✓ Checks: "Are slots named? Mode chosen? Math works?"
- ✗ Missing: "Can this scope actually fit in these slots? Is cumulative personal load sustainable?"

---

## What This Hardening Fixes

### Two New Validation Checks

#### V13 — Weekend Effort Realism

**What it checks:**
1. Weekend-allocated projects have M-level task breakdown (decomposed into realistic focus-blocks)
2. Each task fits within declared slot boundaries (Sat daytime 5–6h max for 1–2 M-blocks; Sun afternoon 3–4h max)
3. If work exceeds declared slot by ~10% (realistic overrun), spillover path exists (other weekend slot or escalated)

**What it catches:**
- Gaming: "Sat 8h declared" with scope that clearly requires 2 days → FAIL (must decompose or reduce scope)
- Unplanned spillover: "Sat 6h, Sun 0h" with 10h scope → FAIL (spillover has no path)
- Load inflation: "Weekend slots sized to close capacity math, not to fit actual scope" → FAIL (must justify project-driven reason)

**Outcome:**
- Weekend allocations are now decomposable + realistic
- Planner can't allocate "8h to Saturday" wishfully; must show how tasks fit

---

#### V14 — Personal Capacity Ceiling

**What it checks:**
1. Total personal execution (net weekday evening + weekend daytime) = sustainable range (11–18h/week normal)
2. If >18h: explicit assumption documented
3. Trend detection: personal load trending upward >2h/week for 3+ weeks triggers escalation

**What it catches:**
- Silent overload: Week 1: 12h, Week 2: 14h, Week 3: 16h, Week 4: 18h (trending up) → Flag as unsustainable pattern
- Cumulative overflow: Weekday evening 8h + Sat 6h + Sun 4h = 18h sustained (not one-off) → Escalate if pattern continues
- Unsustainable sprint: >20h/week personal → must escalate to month context; cannot proceed without strategic decision

**Outcome:**
- Personal load is now transparent and bounded
- Planner can't silently create 3-week upward trend without escalation
- Month context can make informed decision: is this Q1 crunch sustainable? Or must we rebalance?

---

## Business Value

### Before Hardening

| Scenario | Outcome | Learning |
|---|---|---|
| **Plan allows 18h/week personal (edge case)** | Week fails mid-execution; spillover absorbed silently | "Bad planning," not "capacity model was loose" |
| **Planner allocates 8h to Sat daytime without task decomposition** | Task list too big; Sat incomplete; Sun absorbs overflow | "Scope estimation off," not "allocation was unrealistic" |
| **Personal load trends 12h → 14h → 16h → 18h over 4 weeks** | Month goal at risk; no warning signal until week 3–4 when crisis hits | "Didn't anticipate project load," not "system allowed silent buildup" |

### After Hardening

| Scenario | Outcome | Learning |
|---|---|---|
| **Plan would require 18h/week personal** | V14 WARN: requires documented assumption + trend check; if trend >3 weeks, escalate to month | Time to rebalance or make strategic decision early |
| **Planner tries to allocate 8h to Sat daytime** | V13 FAIL: must decompose into realistic bounds or move tasks to Sun; must be explicit | Scope realism is enforced; allocation is defensible |
| **Personal load trends 12h → 14h → 16h** | V14 detects trend by W12; escalates before W13 crisis; month can rebalance | Proactive intervention, not reactive damage control |

---

## How It Works (Conceptual Flow)

```
GENERATE_WEEKPLAN creates goal list
        ↓
(Step 5: Effort estimates needed)
        ↓
CAPACITY_ENGINE receives inputs
        ↓
Run V1–V9 (existing checks)
        ↓
Run V10–V12 (pool isolation, weekend declaration)
        ↓
NEW → Run V13 (Weekend effort realism)
        ├→ Does weekend scope decompose realistically? 
        ├→ Can tasks fit in slots?
        ├→ Does spillover have a path?
        └→ Fail → reduce scope or reallocation
        ↓
NEW → Run V14 (Personal capacity ceiling)
        ├→ Total personal execution ≤18h/week?
        ├→ If >18h, assumption documented?
        ├→ Trend: is personal load increasing >2h × 3 weeks?
        └→ Fail → escalate to month; success → proceed
        ↓
Output: Capacity Summary (with V13/V14 results)
        ↓
GENERATE_WEEKPLAN embeds summary
        ↓
W##_WeekPlan.md finalized with constraints visible
        ↓
GENERATE_WEEKLY_EXECUTION uses constraints
        ↓
Daily execution references weekend boundaries
        ↓
If spillover detected → pre-defined escalation path (not silent absorption)
```

---

## Implementation Surface Area

### Changes Required

- **CAPACITY_ENGINE.md:** +2 validation checks (50 lines of logic)
- **GENERATE_WEEKPLAN.md:** +step 6 integration, +checklist items (20 lines)
- **NEW:** TEMPLATE_WEEKEND_DECOMPOSITION.md (support template for planners)

### Complexity

- **Low:** Checks are straightforward validations (not heavy math)
- **Fast:** Each check takes <2 min to run
- **Non-disruptive:** Doesn't change R1–R11 rules or existing workflow

### Integration

- Backward-compatible: W11 can be re-validated against new checks (should pass)
- First live use: W12 (first week with new checks active)
- Feedback cycle: Weeks 1–4 of use; refinement if needed

---

## What Planners Experience

### Before

- "My weekend capacity is X hours. I have Y hours of work. They fit."
- No breakdown of what "fits"; weekend slots treated as fungible capacity
- Week fails → blame lands on "bad estimates" or "bad anchor"

### After

- "My weekend scope: Sat 4h (1 M-block on testing), Sun 3h (1 M-block on spec review). Spillover if Sat +10%: moves to Sun available time (1h buffer). Total personal: 6h eve + 4h Sat + 3h Sun = 13h sustainable."
- Each allocation tied to specific work; spillover path visible; sustainability range checked
- Week fails → can trace back to: "Sat scope grew past 4h margin" → "V13 would have caught this" → fix is clear

### Planner Workload

- **New burden:** +5 min per week plan to decompose weekend scope + fill template (once, before capacity engine)
- **Return on investment:** Hours saved in debugging week failures + clarifying allocation decisions = much higher ROI

---

## Gap Prevention (What Can't Happen Anymore)

### Gaming Pipeline A: Slot Inflation

**Before:** Planner moves work to weekend without justifying why (just to "balance" weekday load)
- V12 passes (slot declared)
- V6 passes (effort matches)
- No check catches game

**After:**
- V13 requires decomposition + project-driven justification
- Planner must explain why Sat is better than evening (focus, complexity, etc.)
- If answer is "evening was already 6h," V13 fails (not a project reason)

---

### Gaming Pipeline B: Cumulative Overload

**Before:** Planner creates 12h weekend + 6h evening = 18h total personal; each looks OK in isolation; cumulative load is silent
- V9 passes (allocation ≤ capacity)
- No running total of personal execution
- Week fails; blame goes to "bad anchor"

**After:**
- V14 calculates 18h personal total; flags as WARN (stretched)
- Trend detection shows if this is sustained across weeks
- Planner must document assumption (deadline reason) or reduce scope
- If trend continues 3 weeks, escalates automatically

---

### Gaming Pipeline C: Undecomposed Scope

**Before:** "8h RobotOS architecture work, Sat daytime" → treated as valid allocation
- V12 passes (slot declared)
- No check for whether 8h is realistic for one daytime slot
- Execution fails; 4h moves to Sun anyway

**After:**
- V13 requires explicit task breakdown: "M1: architecture review (4h), M2: refactoring (4h)"
- Check: can 2×4h blocks fit in Sat daytime slot? No.
- Resolution: either Sat 4h + Sun 4h (if Sun available), or reduce to 1 block
- Decomposition is now enforced upfront

---

## Context for Month Planning

### Month Impact

Once V13 + V14 are active, month context has new information:

**Before:** "RobotOS + Signee need 48h this month. Allocate across 4 weeks."
- No visibility into personal load sustainability
- May propose: 15h W1, 16h W2, 14h W3, 13h W4 (looks balanced)
- W2 fails; doesn't know why

**After:** "RobotOS + Signee need 48h this month, but personal load must stay 11–18h/week sustainable band. If any week >18h, requires one-off sprint decision + recovery time afterward."
- Can model: 12h W1, 15h W2, 14h W3, 12h W4 = 53h (too much; reduce to 48h)
- Or: 13h W1, 13h W2, 13h W3, 9h W4 = 48h, all sustainable
- Or: 15h W1, 15h W2, 10h W3, 10h W4 = 50h with explicit sprint weeks (W1–W2) + recovery (W3–W4)
- **Decision is now informed, not guessing**

---

## Success Metrics (Post-Implementation)

### Quantitative

- **Week execution adherence:** Weeks with V13/V14 passing at plan should have >85% anchor adherence (vs. ~70–80% pre-hardening)
- **Spillover detection:** 100% of weekend overruns now have pre-planned path (not silent absorption)
- **Personal load stability:** Personal execution stays within 11–18h band or is explicitly escalated (no sneaky trending)

### Qualitative

- **Planner confidence:** "I can explain why weekend allocation is here" (not "capacity math required it")
- **Debugging clarity:** Week failure can be traced to specific root cause (scope grew, anchor drifted, vs. "capacity model was too optimistic")
- **Month coordination:** Month context can make informed decisions about personal project load (not absorbing surprises)

---

## Timeline

### Week 12 (This Week)

- ✅ Design V13 + V14 checks (this document)
- ✅ Design implementation (implementation guide)
- ⏭ Apply changes to CAPACITY_ENGINE.md + GENERATE_WEEKPLAN.md (~1 hour)
- ⏭ Create TEMPLATE_WEEKEND_DECOMPOSITION.md (support document)
- ⏭ Test on W12 capacity model (first live use)

### Week 13+

- Collect feedback on V13/V14 usability
- Refinement if needed
- Ongoing use as standard validation

---

## FAQs

### Q1: Won't this make planning slower?

**A:** +5 min to decompose weekend scope once (done before capacity engine). Total impact: <10 min/week plan. Return: hours saved debugging week failures + clearer decision-making. Net positive.

### Q2: Can I ignore V13/V14 if they return WARN?

**A:** WARN requires explicit documentation + assumption. If V14 WARN AND trend is rising, you must escalate (not a "proceed anyway" signal). FAIL always requires action (scope reduction or escalation).

### Q3: What if my week genuinely needs >20h personal execution?

**A:** Escalate to month context with:
- Reason (deadline, project phase)
- Duration (how many weeks this is necessary)
- Recovery plan (how capacity returns to normal after)
- Month approves or reallocates scope

This is now a **strategic decision**, not a silent assumption.

### Q4: How is this different from just "being more careful with weekends"?

**A:**
- **Being careful:** Subjective; depends on planner discipline
- **V13/V14:** Objective checks enforced in validation gate; cannot pass without addressing them

Difference: structured enforcement vs. wishful thinking.

---

## Next Steps

1. **Review + approval** of hardening design & implementation guide
2. **Apply changes** to CAPACITY_ENGINE.md + GENERATE_WEEKPLAN.md
3. **Create template** (TEMPLATE_WEEKEND_DECOMPOSITION.md)
4. **Test on W12** capacity model
5. **Collect feedback** weeks 13–16
6. **Iterate** if needed
7. **Document** as standard part of system (archive this design in reference library)

---

## Conclusion

**The Weekend Pool Overflow vulnerability is the last major gap in the hardened system.** Once V13 + V14 are active:

- Weekend scope is decomposed + realistically bounded
- Personal capacity cumulative load is visible + trending analyzed
- Spillover paths are explicit (no silent absorption)
- Month context has clear signal when personal projects are approached at sustainable limits or exceeded
- Week failures can be debugged to root cause (scope grew, not "capacity model was loose")

This completes the system hardening vision: **a capacity model that is honest (doesn't hide complexity), bounded (enforces realism), and traceable (decisions are documented).**

---

**Status:** Ready for implementation  
**Owned by:** System Architect  
**Review:** [Month context stakeholder]

