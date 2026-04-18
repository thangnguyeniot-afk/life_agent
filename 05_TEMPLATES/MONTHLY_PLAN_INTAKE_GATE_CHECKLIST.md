# Monthly Plan Intake Gate Checklist

**Purpose:** Verify that next month's plan extracts findings correctly from previous month's review.

**When to use:** During Monthly Plan creation (use previous month's review as source).

**Process:** For each major decision in the monthly plan (sections 1–3: Theme/Outcomes/Capacity), verify it passes the intake gate. If 3+ decisions fail the gate → Plan cannot be locked until corrected.

---

## Pre-Check: Context Completeness

- [ ] **Month-End Intelligence Transfer artifact exists** — Verify that YYYY-MM_Intelligence_Transfer.md was created after previous month's Review Exit Gate passed
  - If YES: Reference this artifact during plan creation for forward-looking planning context
  - If NO: Create it now (20–30 min) before proceeding with plan intake gate verification

---

## Process Rules

**DIRECTLY EXTRACT (binding basis):**
- ✅ [EXEC] findings (execution facts, measured capacity, performance data)
- ✅ [RULE] findings (approved system changes, decision-log entries)
- ✅ [UNRESOLVED] findings (open risks/pending decisions affecting next month)

**CONDITIONAL EXTRACT (pilot-guarded):**
- 🔄 [PILOT] findings → Extract ONLY if:
  - ADR/decision gate permits AND success criteria were evaluated this month AND explicit decision made
  - Must tag explicitly: "[pilot name] — PILOT PHASE — re-eval [date]"
  - Example: "Continue monthly reflection pilot (per ADR-20260322, Q2 only, re-eval 2026-06-30)"

**TRANSFORM, DON'T EXTRACT:**
- ❌ [ADVISORY] findings (human signals, well-being patterns, subjective observations)
  - WRONG: "Monthly plan features: Priority = single-threaded (per human reflection preference)"
  - RIGHT: "Monthly capacity plan: 1 primary anchor/week (informed by March energy observation; testing validity in Q2; will re-confirm in May review)"
  - Rule: Extract ADVISORY as input to *capacity discussion*, not as planning assumption

---

## Gate Checklist

For each major decision in §1–3 of the new Monthly Plan:

### 1) Source Identification
- [ ] **Source identified** — Does this decision trace to a finding in the previous month's review?
  - If YES: Note the source finding and its section (e.g., "from March Output", "from March System Change", "from March Risk")
  - If NO: Decision may be from quarterly strategy, external input, or new context; mark as EXTERNAL_SOURCE and verify it's appropriate for monthly plan

### 2) Category Verification  
- [ ] **Finding category identified** — Is the source finding tagged [EXEC/RULE/PILOT/ADVISORY/UNRESOLVED]?
  - If YES: Note the tag
  - If NO: Source review did not use tagging; cannot verify gate compliance; flag for March review re-audit

### 3) Intake Rule Compliance
- [ ] **Rule applied correctly** — Based on the finding's tag, is the extraction method correct?
  - **If [EXEC]:** ✅ Extract directly → Allowed
  - **If [RULE]:** ✅ Extract directly → Allowed
  - **If [UNRESOLVED]:** ✅ Extract directly (as tracking item or risk) → Allowed
  - **If [PILOT]:** 🔄 Check if ADR gate = allow; success criteria evaluated = yes; decision made = yes; if ALL yes → Allowed; if any no → Blocked
  - **If [ADVISORY]:** ❌ Extract directly → NOT allowed (must transform to capacity adjustment below)

### 4) Audit Trail in Plan
- [ ] **Source citation present** — Does this plan decision include a source notation?
  - GOOD: "Capacity budget 70% Zephyr (per March EXEC measurement)"
  - GOOD: "Capacity budget 1 anchor/week (per March RULE: Daily Scope Rule permanent)"
  - GOOD: "Capacity budget includes evening recovery (per March advisory signal: sleep-energy correlation; validating Q2)"
  - GOOD: "Evening capacity form TBD (per March UNRESOLVED: pattern needs 2nd month data)"
  - BAD: "Capacity budget 70% (no explanation)"
  - If no citation: Add one before locking plan

### 5) Advisory Transformation Check (if source is [ADVISORY])
- [ ] **Transformation visible** — If this plan decision is based on an [ADVISORY] finding, is there evidence of transformation?
  - Question: "What is the alternate scenario if this advisory signal were not present?"
  - GOOD: Alternate scenario is stated (e.g., "If sleep quality weren't critical, capacity could be 2 anchors/week; protecting sleep because de ified it as #1 lever")
  - GOOD: Re-confirmation condition is stated (e.g., "Valid only if March energy pattern repeats in April; will re-test in April review")
  - BAD: No alternate scenario or re-confirmation noted → Transform before locking

---

## Gate Decision Matrix

Count how many plan decisions PASS all 5 checks above.

| Decisions Passing | Status | Action |
|---|---|---|
| **All major decisions pass** | ✅ PASS | Approve plan for lock |
| **1–2 decisions fail** | ⚠️ FIXABLE | Fix flagged decisions (add source citation or transformation); recheck |
| **3+ decisions fail** | 🔴 MAJOR | Block plan lock; review cannot have proper intake gate; escalate |

---

## Example Walk-Through

**Example: From March Review → April Plan Intake**

March Review finding:
```
## 3.5) Human Advisory Signals
- Signal: "Sleep quality is primary energy driver (7h+ sleep = high energy; 5–6h sleep = mid-week fatigue)"
  - Capacity implication: Protect non-negotiable 23:00 bedtime
  - Decision: Apply adjustment
```
Tag: [ADVISORY] (this is a human signal, not an execution fact)

April Plan decision to audit:
```
## Capacity & Rhythm
- Sleep budget: Non-negotiable 23:00 bedtime (protect 7h+ sleep)
```

Intake gate verification:
1. **Source:** March Review, §3.5 Human Advisory Signals ✓
2. **Category:** [ADVISORY] ✓
3. **Rule:** [ADVISORY] must transform, not extract directly
   - Transformation visible?: Yes — "Sleep protection is input to capacity decision" (not "execute this sleep time") ✓
4. **Audit trail:** Should cite source
   - Current: "Sleep budget: Non-negotiable 23:00 bedtime"
   - Better: "Sleep budget: Non-negotiable 23:00 bedtime (primary energy driver per March observation; maintaining in April)"
5. **Alternate scenario:** Should be stated somewhere
   - Implicit: "If energy weren't correlated with sleep, could have more flexible evening availability"
   - Better explicit: "Assumption: March sleep-energy pattern repeats in April (will re-test in May review)"

**Result:** Plan decision PASSES intake gate after adding source citation + re-confirmation note.

---

## How to Use This Checklist

**Step 1:** After April Plan ~80% written, identify 3–5 major decisions (capacity, outcomes, scope).

**Step 2:** For each decision, trace back to source finding in March Review using these 5 checks.

**Step 3:** Count decisions that pass all 5 checks.
- All pass → Continue; proceed to lock
- 1–2 fail → Make targeted fixes (add citations, add transforms)
- 3+ fail → Stop; re-review plan source for systemic issue

**Step 4:** Before locking April Plan, verify all major decisions have source citations visible.

---

## Integration

This checklist is used:
- During Monthly Plan creation (starting April 2026)
- Referenced in TEMPLATE_Month_Final.md (§ A Intake Gate)
- Referenced in MONTHLY_REVIEW_PROCESS_GOVERNANCE.md
- Applied by reviewers before Monthly Plan lock

Archive: `05_TEMPLATES/MONTHLY_PLAN_INTAKE_GATE_CHECKLIST.md` (canonical process checklist)
