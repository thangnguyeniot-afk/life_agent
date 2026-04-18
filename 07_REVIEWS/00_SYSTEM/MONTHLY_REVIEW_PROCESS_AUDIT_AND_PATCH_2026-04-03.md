# Monthly Review Process Audit & Remediation Plan — 2026-04-03

**Audit Scope:** Complete Monthly Review → Monthly Plan workflow  
**Audit Classification:** System Governance / Boundary Safety  
**Focus:** Prevent Human Layer (pilot/advisory) from leaking into binding system decisions  
**Target:** Durable, repeatable process that doesn't require manual gate-keeping each month

---

## EXECUTIVE DIAGNOSIS

### Problem Statement

**March Review boundary leak demonstrates a systemic process gap, not a one-off wording issue.**

March Review correctly identifies Human Layer insights (sleep quality, energy patterns, connection needs) but **frames them as integrated system features** (claimed "Human Layer added", included in System Change effectiveness rankings). This happens because:

1. **Templates don't separate** Execution Reality from Human Advisory Signals at the artifact level
2. **System Change Review table** has no classification field to distinguish rule-changes from pilot-experiments from advisory signals
3. **Monthly Review → Monthly Plan intake rules** have no constraints; they permit direct extraction of ANY finding into next-month decisions
4. **No exit gate** blocks a Monthly Review that conflates human signals with system decisions
5. **No promotion criteria** define when a pilot can move beyond optional → integrated

**Result:** Human Layer pilot gradually migrates from "advisory-only, monthly, optional" → "system feature" through natural process drift, not deliberate decision.

---

## CURRENT PROCESS BUG MAP

### Bug #1: Undifferentiated Finding Classification

**Location:** TEMPLATE_Month_Final.md § 2) Output & Outcome Review + § 3) System Change Review

**Problem:**
- Section 2 (Output & Outcome) doesn't distinguish:
  - Execution facts (did we ship this?)
  - Discovered constraints (can we actually sustain this capacity?)
  - Pilot observations (optional experiment data)
  - Human advisory signals (emotional/well-being patterns)
- All findings mixed in same bullet list
- Section 3 (System Change Review) table has columns: [Change | Goal | Result | Decision]
- **Missing field:** Change Type (rule-change vs pilot-experiment vs advisory signal)
- **Missing field:** Control Layer (which OS layer does this affect; is it execution-level?)
- **Missing field:** Pilot retention criteria (what would cause rollback?)

**Example of bug:**
```
- ✅ Human Reflection layer added to daily template (emotional climate, inner signals, patterns)
```
This looks like an execution fact (shipped artifact), but it's actually a pilot experiment (advisory-only practice).

**Impact:** Readers cannot distinguish "we changed how we work" from "we experimented with an optional practice".

---

### Bug #2: No Human Layer / Pilot Filtering at Monthly Plan Intake

**Location:** TEMPLATE_Month_Final.md § A) Monthly Planning (sections 1–6)

**Problem:**
- Monthly Plan reads: "Based on February Review + Monthly Context"
- No explicit intake rules for what can be extracted vs blocked
- Monthly Plan currently permitted to consume:
  - ✅ Approved rules (correct)
  - ✅ Measured capacity constraints (correct)
  - ✅ Portfolio direction (correct)
  - ❌ **Human reflection directly** (incorrect — should be "capacity adjustment derived from reflection", not raw reflection data)
  - ❌ **Unapproved pilot observations** (incorrect — should filter to "approved pilot re-evaluation points" only)
  - ❌ **Advisory narrative** without classification (incorrect — should separate "constraints" from "advisory signals")

**Example of bug:**
If March Review says "Single-threaded work energizes me" (human advisory signal), Monthly Plan could read it as "Focus next month on single-threaded" without understanding it's a subjective preference signal, not a system constraint.

**Impact:** Human preferences gradually become binding planning assumptions without re-evaluation.

---

### Bug #3: Missing Pilot Promotion Gate

**Location:** ADR-20260322 defines pilot; TEMPLATE_Month_Final.md § 3) System Change Review has no link/reference

**Problem:**
- ADR-20260322 states: Human Layer pilot ends Q2 (2026-06-30), has 5 success criteria, possible outcomes: continue vs adjust vs sunset
- System Change Review table has no field to track whether a change is "pilot vs approved"
- Monthly Review does not reference the 5 pilot success criteria
- When a pilot appears in System Change Review, there's no gating on:
  - ✅ Is this still a pilot? (yes/no)
  - ✅ Have pilot success criteria been assessed this month? (yes/no)
  - ✅ What was the assessment result? (met/not met/partial)
  - ✅ What does this mean for next month? (continue same / expand / rollback / hold)

**Example of bug:**
March Review scores "Human Reflection" as "Effective but partial" in System Change table. But doesn't map this to ADR-20260322 success criteria like "Genuine use (≥8/12 months)" or "Actionable insight (≥50% of reflections reveal patterns)". The evaluation is impressionistic, not criteria-driven.

**Impact:** Pilots can become pseudo-permanent features through gradual adoption, then calcify without formal re-evaluation.

---

### Bug #4: Execution Reality vs Advisory Signals Not Layered

**Location:** TEMPLATE_Month_Final.md § B) Monthly Review (full section)

**Problem:**
- Review sections are not explicitly layered by tier:
  - Tier 1 (Binding): Execution facts, measured constraints, approved rule changes
  - Tier 2 (Advisory): Human signals, pilot observations, unconfirmed patterns
  - Tier 3 (Unresolved): Open questions, pending decisions, monitoring gates
- All sections use same "bullet list" format
- Reader cannot quickly identify which findings are binding vs advisory vs pending
- This encourages treating all review content with equal weight

**Structure issue:**
```
CURRENT:
## 2) Output & Outcome Review
- ✅ Daily Scope Rule implemented (SYSTEM CHANGE)
- ✅ Human Reflection layer added to daily template (PILOT OBSERVATION)
- ✅ Anti-anchor tracking designed (PARTIAL SYSTEM CHANGE)
- Anti-anchor patterns show evening capacity overestimate (ADVISORY SIGNAL)

PROBLEM: All bullets look the same weight; reader conflates "rule" with "pilot" with "signal"
```

**Impact:** Human advisory signals get mistaken for system constraints because they're presented with same formatting authority.

---

### Bug #5: No Review Exit Gate

**Location:** TEMPLATE_Month_Final.md § B) Monthly Review

**Problem:**
- Monthly Review has a DoD (Definition of Done) checklist at the start (§ 0)
- DoD checklist includes: "output reviewed", "system change evaluated", "drift checked", "focus adjusted"
- **Missing from DoD:** Explicit gate on boundary safety
  - ❌ "All findings classified by tier (execution vs advisory vs pending)" — NOT IN DoD
  - ❌ "Human advisory signals separated from binding decisions" — NOT IN DoD
  - ❌ "Pilot experiments tagged with success criteria + re-evaluation gate" — NOT IN DoD
  - ❌ "Monthly Plan intake extracted only from Tier 1 + Tier 3 (not Tier 2)" — NOT IN DoD

**Example of bug:**
March Review passes DoD because "output discussed", "system changes evaluated", "focus adjusted". But review doesn't have a checklist item: "All System Changes classified as approved/pilot/advisory? All human signals separated?" So the classification gap is never caught at review time.

**Impact:** Boundary leaks are never detected as "incomplete work"; they flow through as "done reviews".

---

### Bug #6: Monthly Plan Lacks Source Attribution Rules

**Location:** TEMPLATE_Month_Final.md § A) Monthly Planning (sections 1–3)

**Problem:**
- Monthly Plan reads existing templates and generates priorities, outcomes, rhythm
- No field to trace **where each decision came from**:
  - "This priority came from March Review Execution Reality" ✓
  - "This priority came from March Review Human Advisory Signal, with caveat: [caveat]" ✓
  - "This capacity budget change came from measured KTLO reality, not from feeling" ✓
- No intake audit trail

**Example of bug:**
April Plan section §3) Capacity Budget could say:
```
- Zephyr KTLO: 70% (per March capacity measurement; sleep quality protected per human advisory)
```
But it doesn't distinguish:
- "70% from measured execution data" (binding)
- vs "70% from human advisory signal about sleep quality importance" (advisory → requires acknowledge + re-confirmation every month, not permanent assumption)

**Impact:** Advisory signals become hidden assumptions; no one remembers they were user-reported, not system-measured.

---

## REQUIRED SCHEMA CHANGES

### Schema Change #1: Finding Classification Layer

**Add to all review content:**

Every finding must be tagged with ONE of these:

| Tag | Definition | Binding Impact | Review | Plan Intake |
|---|---|---|---|---|
| **EXEC** | Execution Reality / Measured Fact | Binding | Cite measurement | Extract directly |
| **RULE** | Approved System Rule Change | Binding | Reference ADR/Decision Log | Extract directly |
| **PILOT** | Pilot Experiment Observation | Non-binding (controlled by ADR gate) | Reference pilot ADR + success criteria | Extract ONLY if success criteria met + re-eval passed |
| **ADVISORY** | Human Signal / Well-being Pattern / Subjective Observation | Advisory (input to capacity planning, not deterministic) | Separate from execution facts | Extract as "considered in capacity adjustment" with explicit alternate scenario |
| **UNRESOLVED** | Open Question / Pending Decision / Monitoring Gate | Non-binding | Mark what decision is needed + deadline | Defer to next month review (do not extract as plan basis) |

**Template application:**

Every System Change Review row must include: `[Change Name] — [TAG: RULE/PILOT/ADVISORY/UNRESOLVED]`

Every Life Anchor observation must include: `[Anchor] — [TAG: EXEC/ADVISORY]`

Every Anti-Anchor pattern must include: `[Pattern] — [TAG: EXEC/PILOT/ADVISORY]`

---

### Schema Change #2: System Change Review Enhanced Table

**Add columns to System Change Review table:**

Current columns: [System Change | Mục tiêu | Kết quả | Quyết định]

**NEW TABLE with mandatory fields:**

| Change Name | Change Type | Mục tiêu | Kết quả | Control Layer | Promotion Gate | Decision |
|---|---|---|---|---|---|---|
| … | [RULE/PILOT/ADVISORY] | … | [Effective/Partial/Ineffective] | [Execution / Capacity / Advisory] | [N/A / Pilot gate #1–5 / ADR gate] | [Giữ / Điều chỉnh / Rollback] |

**New field guidance:**

- **Change Type:** Is this a binding rule, a pilot experiment, or an advisory observation?
- **Control Layer:** Which system layer does this affect? (Execution = Task/Priority/Scheduler; Capacity = budget/rhythm; Advisory = well-being/signal only)
- **Promotion Gate:** What decision point controls whether this stays where it is or moves to next level?
  - For RULE: N/A (already approved)
  - For PILOT: Reference to ADR success criteria (e.g., "ADR-20260322 criterion #3: Actionable insight ≥50%")
  - For ADVISORY: None needed (advisory stays advisory; does not promote unless re-decided)

**Example (corrected March Review row):**

| Human Reflection (Q2 Pilot) | PILOT | Capture optional signals for monthly reflection without execution integration | Pilot active; data emerging | Advisory | ADR-20260322 criteria #1–5; re-eval 2026-06-30 | Giữ as Q2 pilot only; does not integrate into execution; remains monthly-primary, daily-optional, advisory-only. Re-evaluate 2026-06-30 per ADR. |

---

### Schema Change #3: Human Advisory Signals Section (Separate from Execution)

**Add to Monthly Review template:**

After § 3) System Change Review, add NEW section:

```
## 3.5) Human Advisory Signals & Well-Being Patterns

[TAG: ADVISORY — Input to capacity planning, NOT binding decisions]

### Signals observed this month
- (list 2–3 advisory observations separated from execution facts)

### Capacity planning implications (optional adjustment)
- Based on these signals, consider for next month: [ ]
- But test validity: What would be the alternate approach if this signal were not present?

### Re-confirmation required
These signals are user-reported well-being patterns, not system-measured constraints. 
Confirm validity in next month review (do not assume same pattern will repeat).
```

---

### Schema Change #4: Monthly Plan Intake Rules Explicit

**Add to Monthly Plan § A) Monthly Planning, before section 1:**

```
## INTAKE RULES — What can be extracted from previous month's review

### Approved for direct extraction (binding basis)
✅ EXEC findings: measured execution reality, capacity facts, performance data
✅ RULE findings: approved system changes, decision-log decisions, ADR content
✅ UNRESOLVED findings: open risks, pending decisions, monitoring gates

### Conditional extraction (requires transformation)
🔄 PILOT findings: Extract ONLY if:
   - ADR/decision gate permits (e.g., ADR-20260322 allows Q2 pilots)
   - Success criteria evaluated this month
   - Explicit decision made (continue/rollback/adjust)
   - Tag explicitly in plan: "[pilot name] — PILOT PHASE — re-eval [date]"

### Prohibited from direct extraction
❌ ADVISORY findings: Do NOT extract as planning assumptions
   Instead: Use to _inform_ capacity adjustments, then cite the adjustment as EXEC-level decision
   Example: ❌ "Based on human reflection, operator prefers single-threaded work"
            ✅ "Capacity adjusted to 1 primary anchor/week (based on energy pattern observation; testing validity Q2)"

### Intake audit trail
Every capacity decision in next month's plan must trace to one of the above categories.
Monthly Plan section §3 Capacity must include: "(derived from March execution measurement / based on March advisory observation / implementing March decision / etc.)"
```

---

## REQUIRED TEMPLATE CHANGES

### Patch #1: TEMPLATE_Month_Final.md § B) Monthly Review — Add Review Scope Declaration

**Location:** Add new section before § 0) DoD

```markdown
## REVIEW SCOPE DECLARATION

**This review covers:**
- EXEC findings (execution facts, measured capacity, observed outcomes)
- RULE findings (approved system changes that modify how we work)
- PILOT findings (approved experiments; subject to re-evaluation gates)
- ADVISORY findings (human well-being signals; input to capacity planning, not deterministic)
- UNRESOLVED findings (open questions; require decisions next cycle)

**This review does NOT cover:**
- Individual task performance (monthly is not task audit)
- Strategic re-plans (that's quarterly; monthly stays within lane)
- Proposal testing (pilots must be ADR-approved before evaluation)

**Data quality note:**
All findings are tagged [TAG: …]. Human signals are marked ADVISORY to distinguish from execution facts.
Human signals are valuable for capacity adjustment. They are NOT system constraints unless explicitly approved.
```

---

### Patch #2: TEMPLATE_Month_Final.md § 2) Output & Outcome Review — Add Finding Tags

**Location:** Modify the Output section bullet list format

**Current:**
```
- ✅ Human Reflection layer added to daily template (emotional climate, inner signals, patterns)
```

**New:**
```
- ✅ [PILOT] Human Reflection pilot prompts added to daily template (optional Q2 experimentation per ADR-20260322)
  - Status: data collection phase
  - Next evaluation: 2026-06-30 end-of-Q2 re-assessment
```

**Rule:** Every output bullet must include [TAG: …] within first 5 words.

---

### Patch #3: TEMPLATE_Month_Final.md § 3) System Change Review — Enhanced Table

**Location:** Replace simple table with enhanced table

**New columns:**

```markdown
| System Change | Type | Mục tiêu | Kết quả | Control Layer | Gate | Quyết định |
|---|---|---|---|---|---|---|
```

**Example rows (corrected):**

| Daily Project Scope Rule (max 2 anchors) | RULE | Prevent 3-project scope creep; enforce work-time domain | Effective | Execution | N/A (approved) | Giữ + Extend to April as permanent rule |
| Human Reflection (Q2 Pilot) | PILOT | Capture optional signals monthly without execution coupling | Pilot active; data emerging | Advisory | ADR-20260322 success criteria; re-eval 2026-06-30 | Giữ as Q2 pilot only (monthly-primary, daily-optional, advisory). Monthly re-confirm. |
| Anti-Anchor Tracking System | PILOT | Enable monthly pattern analysis | Partial (data collection phase) | Advisory | Evaluate Q2 patterns; decision point unknown | Giữ + Archive month-1 data; evaluate Q2 end |

---

### Patch #4: TEMPLATE_Month_Final.md § 3.5) NEW — Human Advisory Signals Section

**Location:** Insert after § 3.1) Portfolio Balance Check

```markdown
## 3.5) Human Advisory Signals & Well-Being Patterns

[Separate from Execution Reality. These are self-reported well-being observations, not system-measured constraints.]

### Observed patterns (ADVISORY-tagged)
- (derive from Monthly Human Reflection template if completed)
- Select 2–3 patterns that most inform capacity planning
- Examples: Sleep-energy correlation, loneliness/connection needs, focus/distraction triggers, calm/restlessness cycles

### Capacity planning consideration (optional)
**If signal observed, consider adjusting next month's tempo. But test the alternate:**
- Signal: "Evening capacity overestimate; actually sustainable at 1×M not 2×S"
- Adjustment considered: Reduce evening WIP next month
- Alternate scenario (test): What if this signal was job-specific, not sustainable? Set contingency.
- Decision: [ ] Apply adjustment | [ ] Hold steady | [ ] Split test (2 weeks each pattern)

### Re-confirmation required each month
ADVISORY signals must be re-confirmed in next month's review (do not assume persistence across months).
If pattern breaks, update Anti-Anchor pattern rules.
If pattern repeats 3+ months, promote to EXEC capacity fact (rule change to follow).
```

---

### Patch #5: TEMPLATE_Month_Final.md § A) Monthly Planning — Add Intake Rules Section

**Location:** Insert before § 1) Định hướng tháng này

```markdown
## MONTHLY PLAN INTAKE GATE

**Rule:** This plan extracts content only from [tagged] findings in the previous month's review.

### Source-of-truth intake rules

**✅ DIRECTLY EXTRACT (binding basis for plan):**
- EXEC findings: Execution reality, measured capacity, performance data
- RULE findings: Approved system changes, ADR decisions, decision-log entries
- UNRESOLVED findings: Open risks that affect next month; pending decisions needing closure

**🔄 CONDITIONAL EXTRACT (pilot-guarded):**
- PILOT findings: Extract ONLY if ADR gate permits AND success criteria evaluated this month
  - Example: Safe to extract "Continue Human Reflection monthly" only if ADR-20260322 gate says "active pilot, re-eval 2026-06-30"
  - Must tag: "... per ADR-[ref], pilot phase, re-eval [date]"
  - Must NOT treat as permanent feature

**❌ TRANSFORM, DON'T EXTRACT:**
- ADVISORY findings: Do NOT read as binding assumptions
  - Instead: Use to *inform* capacity adjustments, then plan the adjustment as EXEC-level decision
  - BAD: "Based on human reflection, prioritize single-threaded work"
  - GOOD: "Capacity structure: 1 primary anchor/week (informed by March energy observation; validating in Q2)"

### Intake audit trail
Every major plan decision (§1–3) must trace to one intake source above.
Use notation: `(from March EXEC measurement / from March RULE decision / from March advisory signal — testing)` etc.
```

---

### Patch #6: TEMPLATE_Month_Final.md § 0) DoD — Add Boundary Safety Gate

**Location:** Expand DoD checklist

**Current DoD:**
```
- Cái nhìn rõ ràng về xu hướng tháng
- Tất cả System Change được đánh giá
- Monthly Drift Check thực hiện
- Portfolio Balance kiểm tra
- Scope expansion có trade-off
- Focus tháng tới rõ ràng
```

**New DoD items (add):**

```
- [ ] All findings tagged with [TAG: EXEC/RULE/PILOT/ADVISORY/UNRESOLVED]
- [ ] Human Advisory Signals separated into § 3.5 (not mixed with Execution Reality)
- [ ] System Change Review includes Change Type + Control Layer + Promotion Gate fields
- [ ] Pilot experiments reference their ADR/decision gate + success criteria
- [ ] No ADVISORY finding appears in System Change Review results without explicit "[ADVISORY]" tag
- [ ] Monthly Plan intake rules applied: EXEC/RULE/UNRESOLVED extracted; PILOT gated; ADVISORY not read as binding assumptions
```

---

### Patch #7: TEMPLATE_Month_Human_Final.md — Add Governance Boundary Note

**Location:** Add at top of file after title

```markdown
---

## GOVERNANCE NOTE (ADR-20260322)

This template is for **OPTIONAL Q2 pilot reflection only** (April 1 – June 30, 2026).

**Important:** Content from this template is tagged [ADVISORY] when extracted to Monthly Review. 
Human advisory signals inform capacity planning but do NOT determine binding decisions.

All human reflection data will be re-evaluated at Q2 end (2026-06-30) per ADR success criteria.

---
```

---

### Patch #8: TEMPLATE_Daily.md — Strengthen Human Reflection Governance Note

**Location:** Expand the governance note added in P0 fix

**Current (after P0 fix):**
```
**Governance note (ADR-20260322):** Human Reflection sections are optional Q2 pilot elements. 
Monthly review is the primary integration point. Daily usage is optional, advisory-only, and must 
not be treated as part of daily DoD, task admission, priority, or scheduling logic. 
Re-evaluation date: 2026-06-30.
```

**Enhance to:**
```
**Governance note (ADR-20260322 — Q2 PILOT):** 
Human Reflection sections are optional Q2 pilot elements (advisory-only, not binding).
- Primary integration point: Monthly review (not daily execution, not weekly planning)
- This section will NOT affect task admission, priority decisions, or scheduling
- All reflection data is re-confirmed monthly; do not assume patterns persist
- Q2 pilot re-evaluation: 2026-06-30 per 5 success criteria in ADR-20260322
- Scope: If this reflection genuinely helps your daily review, use it. If not, skip it.
- Monthly extraction rule: Reflection informs capacity *adjustments*, not binding decisions

Related: TEMPLATE_Month_Human_Final.md | ADR-20260322_HUMAN_LAYER_Q2_PILOT.md
```

---

## MONTHLY REVIEW EXIT GATE

**New process step: "Boundary Safety Review" (before Monthly Review lock)**

**When:** After content writing complete, before declaring review DONE

**Checklist (all must pass):**

- [ ] **Finding Classification**
  - [ ] All substantive findings are tagged [TAG: EXEC/RULE/PILOT/ADVISORY/UNRESOLVED]
  - [ ] Every ADVISORY finding is clearly separated from EXEC findings (not mixed)
  - [ ] No ADVISORY finding is presented with same formatting authority as EXEC finding

- [ ] **System Change Clarity**
  - [ ] Every row in System Change Review table includes: Change Type + Control Layer + Promotion Gate
  - [ ] Every PILOT change references its ADR or decision gate
  - [ ] Every PILOT change explicitly states: "Pilot phase through [re-eval date]"
  - [ ] No PILOT change claims "integrated into system" or "effective as permanent feature"

- [ ] **Human Layer Boundary (specific)**
  - [ ] Human Reflection is tagged [ADVISORY], never [EXEC] or [RULE]
  - [ ] Human Reflection findings are NOT in System Change Review results (they belong in § 3.5 only)
  - [ ] Human Reflection does NOT claim to be "layer", "integrated", "added to execution", or other architectural phrasing
  - [ ] Human Reflection explicitly links to ADR-20260322 and re-evaluation gate

- [ ] **Monthly Plan Intake**
  - [ ] Monthly Plan section § A) explicitly lists intake rules (approved sources)
  - [ ] Capacity decisions in §3 trace their source (EXEC measurement / RULE decision / ADVISORY input with caveat)
  - [ ] No ADVISORY signal is extracted as planning assumption without explicit re-confirmation note

- [ ] **Anti-Noise**
  - [ ] No speculative narrative (only observed facts tagged)
  - [ ] No "recommended actions" that didn't go through decision gate
  - [ ] No unapproved pilot experiments presented as findings

**Gate action:**
- All boxes checked: ✅ Review PASSES boundary safety gate; approved for lock
- 1–2 boxes unchecked: ⚠️ FIXABLE; make targeted edits (estimate <15 min)
- 3+ boxes unchecked: 🔴 REQUIRES REVIEW; escalate to system audit (too many boundary leaks to patch tactically)

---

## MONTHLY PLAN INTAKE GATE

**New process step: "Intake Audit" (during April Plan creation)**

**When:** April Plan is being synthesized from March Review

**Checklist:**

For each major plan decision in April Plan (§1–3):
  - [ ] **Source identified:** Does this decision trace to a March Review finding?
  - [ ] **Category verified:** Is the source EXEC / RULE / PILOT / ADVISORY / UNRESOLVED?
  - [ ] **Intake rule followed:**
    - EXEC / RULE / UNRESOLVED: ✅ Permitted to flow directly into plan
    - PILOT: ✅ Permitted ONLY if ADR gate passed + re-eval date set
    - ADVISORY: ✅ Permitted ONLY if transformed to "capacity adjustment" + alternate scenario noted
  - [ ] **Audit trail in plan:** Is the source explicitly cited? (e.g., "per March EXEC measurement" or "considering March advisory observation")

**Gate actions:**
- All decisions pass audit: ✅ Plan intake is compliant
- 1–2 decisions fail audit: ⚠️ Patch those decisions (add source attribution or reclassify)
- 3+ decisions fail audit: 🔴 Re-review April Plan for boundary compliance before lock

---

## PATCH ORDER & PRIORITY

### P0 (CRITICAL — Blocks system safety; apply immediately)

**Files to patch:**

1. **TEMPLATE_Month_Final.md**
   - Add § 0.5) Review Scope Declaration [10 min]
   - Expand DoD checklist with boundary safety gates [10 min]
   - Add finding classification tags to § 2) Output [10 min]
   - Replace § 3) System Change Review table with enhanced schema [20 min]
   - Add § 3.5) Human Advisory Signals section [15 min]
   - Add § A) Monthly Plan Intake Gate rules [15 min]
   - **Total: ~80 min of edits across 1 file**

2. **TEMPLATE_Month_Human_Final.md**
   - Add governance note at top [5 min]
   - **Total: ~5 min**

3. **TEMPLATE_Daily.md** (already patched in P0 fixes; verify)
   - Verify governance note is in place
   - Enhance if needed [5 min if needed]
   - **Total: ~5 min if needed**

**Timeline:** Apply before Friday EOD (before April Planning lock)

**Risk if not applied:** April Plan will inherit March Review boundary leaks without detection

---

### P1 (HIGH — Improves operability; apply this week)

1. **ADR-20260322_HUMAN_LAYER_Q2_PILOT.md**
   - Add "See also: TEMPLATE_Month_Final.md § 3.5" reference [2 min]
   - Clarify which boundary leaks violate the ADR [5 min]
   - **Total: ~7 min**

2. **Create process checklist documents:**
   - `05_TEMPLATES/MONTHLY_REVIEW_EXIT_GATE_CHECKLIST.md` [10 min]
   - `05_TEMPLATES/MONTHLY_PLAN_INTAKE_GATE_CHECKLIST.md` [10 min]
   - **Total: ~20 min new files**

3. **Update Decision_Log.md**
   - Record decision: "Monthly Review process governance enhanced 2026-04-03" [5 min]
   - Reference: Template patches P0, processes P1

**Timeline:** Apply by end of week (by Friday 2026-04-04 EOD)

---

### P2 (MEDIUM — Cleanup; apply within 2 weeks)

1. **Audit past reviews** (March 2026 already fixed; check if earlier reviews have similar leaks)
2. **Update March_Planning.md** to use new intake rules format (retrospective audit)
3. **Create April Plan** using new intake gate process (first live use of new process)
4. **Document lessons** if new process reveals additional gaps

**Timeline:** After P0/P1 complete; target: 2026-04-14

---

## CANONICAL SOURCE-OF-TRUTH UPDATES REQUIRED

### Update #1: TEMPLATE_Month_Final.md

**Current status:** Needs P0 patches (6 sections)

**Canonical reference:** This is SOT for all Monthly Reviews going forward

**After patches:** Fully boundary-safe; includes all intake/exit gates; explicitly classifies findings

---

### Update #2: TEMPLATE_Month_Human_Final.md

**Current status:** Needs P0 patch (governance note)

**Canonical reference:** This is SOT for optional human reflection; must clearly state Q2 pilot scope

**After patches:** Governance boundary clear in template; operators understand ADVISORY scope

---

### Update #3: ADR-20260322_HUMAN_LAYER_Q2_PILOT.md

**Current status:** Already excellent; needs P1 update (cross-reference)

**Canonical reference:** This is SOT for Human Layer boundary; must reference new template sections

**After patches:** Full integration with template schema changes; easy for reviewers to reference

---

### Update #4: Create new canonical process: MONTHLY_REVIEW_PROCESS_GOVERNANCE.md

**Location:** `00_README/MONTHLY_REVIEW_PROCESS_GOVERNANCE.md`

**Content (new file):**
- Overview of 4-layer Monthly Review pipeline
- Finding classification schema (EXEC/RULE/PILOT/ADVISORY/UNRESOLVED)
- Exit gate checklist (linked)
- Intake gate checklist (linked)
- Examples of correct vs incorrect practice

**Purpose:** Single SOT for how Monthly Review process works; prevents process drift

**Timeline:** Create in P1 phase

---

## DUG DEEPER: ROOT CAUSE ANALYSIS

### Why did the boundary leak happen?

**Contributing factors:**

1. **Template structure permitted ambiguity**
   - No mandatory classification field → findings default to "equal weight" framing
   - System Change Review table had no "type" column → pilot looked same as rule

2. **No explicit exit gate**
   - Monthly Review DoD checked "completeness" but not "boundary safety"
   - Leaks passed through as "thorough review" not "failed gate"

3. **Intake rules were implicit**
   - Monthly Plan inherited all findings without filtering
   - Advisory signals flowed directly into next-month assumptions
   - No one documented "this intake source is ADVISORY; requires re-confirm"

4. **Human Layer pilot was "too effective"**
   - March reflection genuinely revealed valuable patterns (sleep energy, connection)
   - Planner naturally wanted to use those patterns
   - Without explicit guardrails, helpful data became hidden assumptions

5. **Boundary enforcement was manual**
   - ADR-20260322 stated the boundary clearly
   - But templates didn't *enforce* the boundary; they just stated it
   - Human reviewers had to read ADR, remember it, apply it manually each month
   - Manual enforcement always fails eventually

### Prevention strategy

**Solution: Move boundary enforcement from manual (ADR statement) to automated (template structure)**

- Template schema now enforces classification [TAG: …]
- Exit gate now enforces separation of EXEC/ADVISORY
- Intake rules now enforce filtering before Monthly Plan reads from Monthly Review
- Result: Boundary safety is embedded in the template; reviewers cannot accidentally leak findings

---

## APPROVAL GATES FOR TEMPLATES

### Approval path for P0 patches:

1. **File: TEMPLATE_Month_Final.md**
   - Status: Template (canonical)
   - Patch scope: 6 sections (additions + table restructure)
   - No breaking changes for existing reviews (optional new sections; enhanced table is backward-compatible)
   - Approval: ✅ Safe to apply (low risk)

2. **File: TEMPLATE_Month_Human_Final.md**
   - Status: Template (canonical)
   - Patch scope: 1 governance note (addition only)
   - No breaking changes
   - Approval: ✅ Safe to apply (zero risk)

3. **File: TEMPLATE_Daily.md**
   - Status: Template (canonical)
   - Patch scope: Already patched in P0 fixes; verify governance note is in place
   - No additional changes needed
   - Approval: ✅ Verified and ready

---

## MONTH-BY-MONTH ROLLOUT PLAN

### April 2026 (Month 1 of new process)

**Week 1 (April 3–7):**
- [ ] Apply P0 patches to TEMPLATE_Month_Final.md (Friday 4/4)
- [ ] Apply P0 patches to TEMPLATE_Month_Human_Final.md (Friday 4/4)
- [ ] Create April Plan using new intake gate checklist (Friday 4/4 planning session)
- [ ] Document any process friction observed

**Week 2–4 (April 8–30):**
- Normal execution; no template changes

**May 1 (Month end):**
- [ ] Apply Monthly Review EXIT gate checklist (May 1 review)
- [ ] Document gate results (all pass / some fail / major issues)
- [ ] Create May Plan using new intake gate checklist

### May 2026 (Month 2 of new process)

**Month end (June 1):**
- [ ] Apply Monthly Review EXIT gate checklist (June 1 review for May month)
- [ ] Document gate results (convergence expected)

### June 2026 (Month 3 + Q2 pilot re-evaluation)

**June 30 (Q2 pilot re-evaluation):**
- [ ] Human Layer pilot success criteria assessment (per ADR-20260322)
- [ ] Boundary safety assessment (has new process held boundary?)
- [ ] Decision: Continue Human Layer beyond Q2 / Rollback / Adjust scope

---

## SUMMARY OF GAPS FILLED

| Gap | Symptom | Fix | Result |
|---|---|---|---|
| Undifferentiated findings | Human signals look like system features | Finding classification schema (EXEC/RULE/PILOT/ADVISORY/UNRESOLVED) | Readers see tower tiers; can distinguish advisory from binding |
| No pilot promotion gate | Pilots drift toward permanent features | Schema Change Review: Change Type + Promotion Gate columns | All pilots linked to re-eval gates; no silent promotion |
| No monthly plan intake rules | Advisory signals become hidden assumptions | Explicit intake rules: EXEC/RULE extracted; ADVISORY transformed; source audit trail | Monthly Plan decisions traced to their source; no stray assumptions |
| No exit gate | Boundary leaks pass through as "done reviews" | Exit gate checklist: Finding classification + Human Layer separation + intake rule verification | Boundary leaks caught before review lock |
| Implicit enforcement | Boundary safety depends on manual reviewer memory | Template schema now enforces boundaries (classification fields mandatory, table structure enforces separation) | Boundary safety embedded; hard to accidentally violate |

---

## FINAL VERDICT

### Is proposed patch safe to apply?

**✅ YES.** 

Proposed changes are:
- **Structurally sound:** Schema changes are additive/clarifying, not disruptive
- **Backward-compatible:** New sections + new columns don't break existing review artifacts
- **Low risk:** No deletion of existing content; no re-writing of past reviews
- **Process improvement:** Reduces manual enforcement work for reviewers (easier to be compliant)
- **Governance aligned:** All changes reference ADR-20260322; no contradictions

### Can process be fully automated?

**Partial.** 

Exit/intake gates are **checklists** (manual verification), not fully automated. This is intentional:
- Exit gate (`→ Can this review be locked?`) — requires human judgment; checklists ensure non-obvious gaps are caught
- Intake gate (`→ Is this finding appropriate for April Plan?`) — requires categorization judgment; not all ADVISORY signals are equal; reviewer must decide what informs capacity adjustment

Automation opportunity: Template could include conditional sub-sections that appear/hide based on [TAG: …] selection (if using digital templates). But manual checklists work for now.

---

**Audit completed:** 2026-04-03  
**Recommendation:** Apply P0 patches before April Plan lock (Friday 4/4 EOD)  
**Re-audit scheduled:** 2026-06-30 (end of Q2; evaluate whether boundary safety held + pilot re-evaluation)

---

**Archive:** `07_REVIEWS/00_SYSTEM/MONTHLY_REVIEW_PROCESS_AUDIT_AND_PATCH_2026-04-03.md`
