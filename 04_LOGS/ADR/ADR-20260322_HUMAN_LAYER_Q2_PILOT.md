# ADR-20260322 — Human Layer Integration Decision (Q2 Pilot)

**Date:** 2026-03-22  
**Status:** APPROVED (Formal decision recorded)  
**Decision Owner:** LIFE_AGENT System Governance  
**Supersedes:** None  
**Affects:** Personal OS v1, Monthly review cadence, template policy  

---

## Context

The LIFE_AGENT system (v1.1) operates as an artifact-driven execution engine with five maturity tiers:
- Task Engine, Backlog Structure, Priority Scoring, Scheduler, Knowledge System  
- Protected by Anti-Gravity Rules (§14)

**Question:** Should a "Human Layer" (emotional reflection, inner-life tracking, operator well-being signals) be integrated into the core OS?

**Background:** March 2026 operations revealed authentic insight from operator self-reflection (three-project fatigue detection triggered system redesign). Proposal emerged to formalize human reflection into daily/weekly templates and integrate with Task/Priority engines.

**Audit conducted:** Full architectural audit (HUMAN_LAYER_AUDIT.md) evaluates fit, risks, benefits, failure modes.

---

## Decision

**Verdict: PARTIAL INTEGRATION (Monthly-Only, Q2 Pilot)**

Human Layer is **NOT** promoted to a core OS layer at this time.

**Approved scope:**
- Monthly Human Reflection remains optional reflective artifact (TEMPLATE_Month_Human_Final.md)
- Monthly reflection output becomes advisory input for next-cycle capacity planning
- No integration into daily, weekly, quarterly templates (execution layer stays clean)
- No changes to Task Engine, Priority Engine, Scheduler Engine
- No "Human Mode" decision flag, no subjective task admission criteria

**Duration:** Q2 2026 (April 1 – June 30)

**Pilot success metrics:**
1. Operator genuinely uses reflection (not skipped 3+ months)
2. ≥50% of reflections contain actionable patterns (not narrative-only)
3. Monthly reflection informs ≥2–3 capacity decisions in subsequent month
4. No template adoption abandonment (reflection sections not skipped)
5. Net positive time use: benefit > 45–90 min monthly overhead

**Re-evaluation:** 2026-06-30 end-of-Q2 review

---

## Allowed Scope (Q2 Pilot)

✅ **Explicitly permitted:**
- Operator completes monthly human reflection (optional, not mandatory)
- Reflection structured per TEMPLATE_Month_Human_Final.md
- Reflection output reviewed during Monthly Review session
- Capacity discussion in month-end planning includes: "Any fatigue/energy patterns to adjust for next month?"
- Legitimate adaptations to next month's plan: extend timebox, add recovery block, reduce project count
- Human signal escalation to Weekly Review if acute stress detected mid-cycle (not allowed to bypass executive decision)
- Data quality flagging: reflection marked as "strong / partial / preliminary" when capacity decisions are based on it

✅ **Allowed decision flows:**
```
Monthly Reflection → Capacity Adjustment Discussion → Next Month Anchor Map
(one-way input; output remains planning-owned)
```

---

## Explicit Non-Goals / Forbidden Changes

❌ **Strictly prohibited (will trigger system audit if attempted):**
- Adding human reflection fields to daily planning template
- Adding human reflection synthesis to weekly anchor map
- Creating "Human Mode" decision flag or any subjective override mechanism
- Modifying Task Engine to include "emotional readiness" field
- Modifying Priority Engine to weight emotional readiness alongside Strategic/Impact/Urgency
- Modifying Scheduler Engine to support subjective task displacement
- Making monthly reflection mandatory (must remain opt-in)
- Retroactively using reflection to justify missed commitments
- Coupling human reflection to metrics dashboard (no "fatigue score" without explicit re-decision)
- Using reflected emotion as veto for delivery commitments
- Integrating human signals into scope-lock decisions (scope remains locked Friday evening through week end)

❌ **Failure modes to monitor (escalate if observed):**
- Reflection abandoned 3+ consecutive months (indicates system friction, not operator laziness)
- Reflection begins taking >2 hours/month (introspection inflation)
- Operator invoking "human needs" to override weekly scope lock (abuse case)
- Template bloat from human layer creep (systems check every 4 weeks)
- Decision ambiguity between delivery commitment and emotional signal

---

## Status Notes (Clarification on Current State)

**Reality check (as of 2026-03-22):**
- `TEMPLATE_Daily.md` includes an optional "Human Reflection (Optional)" section (added March 13)
- W10 live daily files (2026-03-10 onwards) contain this section as pilot practice
- `TEMPLATE_Month_Human_Final.md` exists and is functional
- No changes to Task/Priority/Scheduler engines have been made

**Approved state for Q2:**
- The optional Human Reflection section in daily templates is PERMITTED during Q2 pilot as long as it remains:
  - Optional (not required for DoD closure)
  - Lightweight (not a formal decision point)
  - Non-prescriptive (no feedback loop required to execution)
- This section will be reviewed as part of success criteria (criterion: "adoption abandonment" — are people using it or skipping it?)
- Final decision on whether this stays in templates: 2026-06-30 re-evaluation

---



**Evaluation window:** 2026-06-30 (end of Q2)

**Success criteria (must satisfy ≥5/5 to continue past Q2):**

| Criterion | Rationale | Data Source |
|---|---|---|
| **Genuine use** | Reflection completed ≥8/12 months (not skipped ≥3 months) | Monthly reflection files, completion log |
| **Actionable insight** | ≥50% of reflections reveal patterns that could inform capacity planning | Reflection content review |
| **Feedback loop works** | Monthly reflection informs ≥2–3 documented capacity decisions in subsequent month | Capacity planning notes + next month's anchor map |
| **No adoption abandonment** | Reflection sections in monthly template are consistently filled (not skipped in good-execution months) | Template completion audit |
| **Positive ROI** | Operator reports net value; benefit time outweighs 45–90 min overhead | Operator feedback + time tracking |

**Decision outcomes (June 30 review):**
- **All 5 criteria met:** Continue monthly-only; can consider lightweight weekly add-on for Q3 (requires separate approval)
- **3–4 criteria met:** Continue monthly-only; investigate friction; defer any expansion
- **≤2 criteria met:** Sunset Human Layer integration; reflection becomes optional personal practice (not system obligation)

---
## See Also (Canonical References)

- **TEMPLATE_Month_Final.md** — Monthly Review template with finding classification schema + intake gate (§0.5 Scope Declaration, §3.5 Advisory Signals, §Intake Gate)
- **TEMPLATE_Month_Human_Final.md** — Human Reflection template with governance note  
- **TEMPLATE_Daily.md** — Daily template with strengthened governance note on reflection scope
- **MONTHLY_REVIEW_PROCESS_GOVERNANCE.md** — Canonical process documentation (finding classification, promotion paths, exit/intake gates)

## Boundary Leak Prevention

This ADR prevents these failure modes:
- ❌ Presenting advisory signals as binding execution decisions
- ❌ Presenting pilot prompts as integrated system features  
- ❌ Extracting raw advisory content directly into monthly plan assumptions without transformation
- ❌ Assuming human signals persist automatically across months without re-confirmation
- ❌ Using emotional readiness to override weekly scope lock or delivery commitments

Prevention mechanisms:
- ✅ All human reflection is tagged [ADVISORY] in Monthly Review
- ✅ Separate section (§3.5) for advisory signals (not mixed with exec facts)
- ✅ System Change Review explicitly marks pilot experiments with Type field + re-eval gate
- ✅ Monthly Plan Intake Gate blocks direct extraction of ADVISORY (must transform first)
- ✅ Monthly Review Exit Gate requires boundary safety verification before lock

---
## Rationale (Short Form)

**Why partial, not full integration:**
- Risk-benefit asymmetry: Full integration would cascade changes through Task/Priority/Scheduler engines, creating subjective overrides with high abuse potential
- Current evidence: March reflection is valuable signal for capacity planning, but mostly operator-centric (well-being), not system-optimizing (delivery reliability)
- Partial approach: Test monthly reflection as isolated artifact for Q2; gather data on whether it actually improves capacity planning
- Exit is clean: If pilot fails, revert to standalone reflection; no system unwinding needed

**Why monthly, not daily/weekly:**
- Daily reflection creates introspection burden without clear payoff
- Daily template is already execution-focused; adding emotion logging would violate separation of concerns
- Weekly would couple reflection to execution anchor map; risks contaminating scope-lock decisions
- Monthly boundary is natural (aligns with existing Month Review cadence)

**Why pilot ends at Q2:**
- Minimal three-month Q2 provides sufficient data to evaluate success criteria
- Early decision point prevents accidental system drift (decisions not reviewed often calcify)
- Allows Q3 to proceed with clarity (continue monthly or shut down) without ambiguity

---

## Non-Goals

This decision explicitly does NOT:
- Redefine the Personal OS v1 architecture (layers unchanged)
- Add new task types or decision criteria to Task Standard
- Change Review cadence or artifact requirements
- Mandate emotional reporting for accountability
- Create well-being as operational constraint on execution
- Modify Anti-Gravity Rules (§14)

These remain outside scope. Human Layer is experimental, separate, optional.

---

## Related Decisions & Documents

- **Audit:** `HUMAN_LAYER_AUDIT.md` (full analysis of risks, benefits, failure modes)
- **Template:** `05_TEMPLATES/TEMPLATE_Month_Human_Final.md` (reflection structure)
- **Related:** `01_OS/operating_system_thang_nguyen_v1_1.md` (current OS; unchanged)
- **Related:** `02_GENERAL_CONTEXT/CONTEXT_rule.md` (context policy; no changes)

---

## Approval & Implementation Notes

**Approved:** Yes (formal system decision, 2026-03-22)  
**Implementation status:** No implementation required; this is policy, not code/template change  
**Responsibility:** Future agents must NOT attempt any of the prohibited changes without new explicit decision  
**Audit trigger:** If any prohibited item is detected during repo review, escalate to decision review immediately  

---

**This decision record stands as the official position on Human Layer integration until explicitly superseded.**
