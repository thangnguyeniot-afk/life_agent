# Monthly Review / Monthly Plan Process Governance

**Version:** 2026-04-03 (Enhanced process governance)  
**Scope:** End-of-month Monthly Review + Start-of-month Monthly Plan workflow  
**Purpose:** Define how findings are classified, evaluated, and extracted between review and planning to maintain boundary safety (especially Human Layer pilot separation from execution decisions)

---

## Why This Process Exists

March 2026 audit revealed that **Human Layer pilot signals were drifting into binding execution decisions** through gradual process drift, not deliberate design:

| Problem | Symptom | Solution |
|---|---|---|
| No finding classification | Human signals looked same as execution facts | Tag findings: [EXEC/RULE/PILOT/ADVISORY/UNRESOLVED] |
| No pilot gating | Pilots could become features silently | Enhanced System Change table with Type + Gate columns |
| No intake filtering | Advisory signals flowed directly into plans | Monthly Plan Intake Gate with explicit extract rules |
| No exit gate | Boundary leaks passed through as "done reviews" | Monthly Review Exit Gate checklist |

**Process patch date:** 2026-04-03  
**Effective:** Immediately for all future reviews (April month-end onwards)

---

## 4-Step Monthly Review Pipeline

### Step 1: Fact Collection (during month)
- Daily files capture execution signals
- Weekly reviews aggregate patterns
- Monthly Human Reflection (optional) captures well-being observations

**Output:** Raw findings (unclassified)

### Step 2: Finding Classification (at month-end)
- Categorize each finding: [EXEC] / [RULE] / [PILOT] / [ADVISORY] / [UNRESOLVED]
- Prepare System Change Review table with Type + Control Layer + Gate fields
- Separate Human Advisory Signals into dedicated §3.5 section

**Output:** Classified findings (ready for review exit gate)

### Step 3: Layered Writing (month-end review)
- §0.5 Review Scope Declaration: Clarify what this review covers + data quality note
- §2) Output & Outcome: Tag each finding with its category
- §3) System Change: Fill enhanced table with Type + Gate
- §3.5) Human Advisory: List [ADVISORY] signals separately (not in System Change results)
- §4–5) Life/Anti-Anchors: Tag trends
- **Exit Gate:** Verify all 6 boundary safety conditions before locking

**Output:** Boundary-safe review (published)

### Step 4: Planning Extraction (next-month planning)
- Monthly Plan Intake Gate: Extract only appropriate findings
  - [EXEC/RULE/UNRESOLVED] → Direct extract (binding basis)
  - [PILOT] → Conditional (gate check required)
  - [ADVISORY] → Transform (never extract as assumption)
- Audit trail: Every plan decision cites its source

**Output:** Source-traced plan (with intake audit trail)

---

## Finding Classification Schema

### [EXEC] — Execution Reality

**Definition:** Measured fact about execution, capacity, or outcomes.

**Binding status:** ✅ YES (binding for planning)

**Where it comes from:**
- Measured execution data (e.g., "W09 office focus = 3–4h/week")
- Performance data (e.g., "Zephyr KTLO capacity ~10% of week")
- Observed outcome patterns (e.g., "Evening capacity overestimate repeated 2+ weeks")

**Where it goes in plan:**
- Directly into capacity calculations
- Directly into next-month workload assumptions
- Examples: "70% Zephyr allocation (per March office measurement)", "Deep work blocks sustainable at 3–4/week (per confirmation)"

**Examples:**
- "Actual deep work blocks averaged 3/day Mon–Fri"
- "Office hours focus = 3–4h uninterrupted"
- "Migration task took 2× estimated effort"

---

### [RULE] — Approved System Rule Change

**Definition:** Approved change to how we work (past or proposed).

**Binding status:** ✅ YES (binding for planning and execution)

**Where it comes from:**
- ADR or formal decision (e.g., ADR-20260322)
- Decision Log entry (approved decision)
- System Change Review decision: "Giữ + Extend to April"

**Where it goes in plan:**
- Directly into next-month execution model
- Documented in Operating System (OS v1.1)
- Examples: "Daily Project Scope Rule (max 2 anchors) now permanent", "Work Time Domain enforced (office = Zephyr only)"

**Examples:**
- "Daily Project Scope Rule approved and implemented (max 2 anchors)"
- "Anti-SPOF protection rule added to OS"

---

### [PILOT] — Controlled Experiment

**Definition:** Experiment or new system element under evaluation (not permanent).

**Binding status:** 🔄 GATED (controlled by ADR or decision gate; binding only if gate permits)

**Where it comes from:**
- ADR that approves pilot (e.g., ADR-20260322)
- System Change Review: "Giữ as pilot + build data" or "Hold for Q2 evaluation"
- Must have success criteria + re-evaluation date

**Where it goes in plan:**
- Only if gate permits AND success criteria evaluated this month AND decision made (continue/rollback/adjust)
- Always tagged: "[pilot name] — PILOT PHASE — re-eval [date]"
- Example: "Continue Human Reflection pilot (per ADR-20260322, Q2 only, re-eval 2026-06-30)"

**NOT allowed:**
- Extracting as permanent feature  ("Human Reflection is now part of execution")
- Assuming continuation ("keep doing reflection")
- Without re-eval gate in plan (bare "continue reflection" without date)

**Examples:**
- "Human Reflection pilot: optional daily prompts + monthly synthesis (ADR-20260322; re-eval 2026-06-30; success criteria: criterion #1–5)"
- "Anti-Anchor Tracking: pilot data collection ongoing (evaluate Q2 end)"

---

### [ADVISORY] — Human Well-Being Signal

**Definition:** Subjective observation about operator well-being, preference, or pattern (non-binding input to capacity discussion).

**Binding status:** ❌ NO (input to capacity planning, not deterministic; must re-confirm monthly)

**Where it comes from:**
- Monthly Human Reflection template
- Operator self-observation (e.g., "sleep quality affects energy")
- Optional daily reflections (if available)

**Where it goes in plan:**
- NEVER directly as assumption
- Transforms into CAPACITY ADJUSTMENT (hypothesis + alternate scenario + re-confirmation note)
- Example change:
  - WRONG: "Operator prefers single-threaded work"
  - RIGHT: "Capacity model: 1 primary anchor/week (informed by March observation that single-threaded improves focus; testing validity Q2; will re-confirm May)"

**Key rule:** Advisory signals must be re-confirmed monthly. Do not assume persistence.

**Examples:**
- "Sleep quality is primary energy lever (7h+ → high energy; 5–6h → mid-week fatigue)"
- "Three-project load creates fatigue (tension reduced by Daily Project Scope Rule)"
- "Connection / team interaction needs weekly touch-point (prevent isolation drift)"

---

### [UNRESOLVED] — Open Question / Pending Decision

**Definition:** Question or issue requiring decision in future cycles; not ready for commitment.

**Binding status:** ❓ PENDING (tracked, not assumed)

**Where it comes from:**
- Anti-Anchor patterns (needs more data; unclear if pattern or anomaly)
- Blocked dependencies
- Risks that may escalate
- Questions that deferred to next month

**Where it goes in plan:**
- As tracking items or contingencies (not committed outcomes)
- With decision deadline or review checkpoint
- Example: "Unknown: Can we sustain 3-project portfolio long-term? (decision checkpoint: May review)"

**NOT allowed:**
- Planning around unresolved issues (e.g., "assume dependency resolves")
- Leaving unresolved without review date (must have checkpoint)

**Examples:**
- "Evening capacity pattern: needs 2nd month of data; unclear if sustainable at 1–2 hours (will evaluate May)"
- "Three-project load risk: mitigated by Daily Scope Rule; monitoring for cumulative fatigue markers (re-assess quarterly)"

---

## Monthly Review Exit Gate

**Requirements before Monthly Review is locked:**

| Category | Requirements | Status |
|---|---|---|
| **Finding Classification** | All findings tagged [EXEC/RULE/PILOT/ADVISORY/UNRESOLVED]; tags consistent | REQUIRED |
| **System Change Clarity** | Table includes Type + Control Layer + Gate; all PILOT rows linked to ADR + re-eval date; no PILOT claims permanence | REQUIRED |
| **Human Layer Boundary** | Human Reflection tagged [ADVISORY], in separate §3.5, linked to ADR-20260322, doesn't claim integration | REQUIRED |
| **Monthly Plan Readiness** | Intake Gate section present before planning; rules clear (EXEC/RULE/UNRESOLVED extract; PILOT gated; ADVISORY transforms) | REQUIRED |
| **Anti-Noise** | No speculative language; no unapproved pilots; no hidden recommendations; all ambiguity escalated to UNRESOLVED | REQUIRED |

**Tool:** See MONTHLY_REVIEW_EXIT_GATE_CHECKLIST.md (12-point checklist; must pass all)

**Enforcement:** If checklist fails >2 items → Review cannot lock → Escalate for system audit

---

## Monthly Plan Intake Gate

**Requirements before Monthly Plan is locked:**

| Step | Requirement | Status |
|---|---|---|
| **Source identification** | Every major plan decision traces to previous month review finding | REQUIRED |
| **Category verification** | Decision's source finding is tagged (tag visible; if not: March review incomplete) | REQUIRED |
| **Rule application** | EXEC/RULE/UNRESOLVED extracted directly; PILOT gated; ADVISORY transformed | REQUIRED |
| **Audit trail** | Source notation visible in plan (e.g., "per March EXEC measurement") | REQUIRED |
| **Advisory transform** | If source is [ADVISORY], decision shows alternate scenario or re-confirmation note | REQUIRED |

**Tool:** See MONTHLY_PLAN_INTAKE_GATE_CHECKLIST.md (5-point check per decision; 3+ pass)

**Enforcement:** If 3+ decisions fail gate → Plan cannot lock → Re-review for systematic issue

---

## Promotion Paths

### PILOT → RULE (Permanent Feature)

**Allowed when:**
1. ADR gate permits promotion (ADR defines success criteria + phase 2 approval path)
2. Success criteria met across defined period (e.g., "Genuine use 8+/12 months" for Human Reflection)
3. Explicit governance decision made (ADR approval or new decision-log entry)

**Process:**
- Final evaluation at ADR re-evaluation date (e.g., 2026-06-30 for Human Layer)
- Decision: Continue / Modify / Sunset
- If Continue: Create new ADR or update OS (v1.2) with change
- Update all templates to reflect new permanent rule
- Remove [PILOT] tag; replace with [RULE]

**Example:** Human Reflection pilot re-eval (Q2 end):
- All 5 success criteria met → Approve monthly reflection as permanent feature (update OS, templates)
- 3–4 criteria met → Continue pilot into Q3 with adjustments (extend ADR, refine template)
- ≤2 criteria met → Sunset; Human Reflection becomes optional personal practice (remove from templates)

---

### ADVISORY → EXEC Capacity Fact

**Allowed when:**
1. Pattern re-confirmed across 3+ months (consistent observation)
2. Converted to measurable planning constraint (not subjective preference)
3. Explicit governance decision made (e.g., capacity rule updated)

**Process:**
- Collect data across multiple reviews
- If pattern repeats 3+ times without breaking → Candidate for promotion
- Evaluation point: Quarterly review or milestone
- Decision: Adopt as capacity fact (update OS + templates) or remain advisory
- If adopted: Remove [ADVISORY] tag; replace with [EXEC]; move from §3.5 to §2) Output

**Example:** Sleep-energy correlation (if it holds up):
- March: [ADVISORY] signal (single observation)
- April: [ADVISORY] confirmed; pattern holds
- May: [ADVISORY] confirmed again (3rd month) → Re-evaluate June
- June decision: If consistent 3+ months → Adopt "Sleep quality ≥7h = capacity constraint" as [EXEC] operating fact (update OS, capacity templates)

---

## Promotion Gate Prevention

### [ADVISORY] signals that should NOT be promoted

❌ **Subjective preferences** (e.g., "operator prefers X work type")
- These stay [ADVISORY] (input to planning discussion, not system constraint)
- Use to inform assignments where possible, but do not encode as rule

❌ **Context-dependent patterns** (e.g., "X works in Q1 but not Q2")
- Flag as environment-dependent, not portable rule
- Re-evaluate when context changes

❌ **One-off observations** (less than 2–3 repetitions)
- Cannot promote until confirmed pattern (minimum 3 observations)

---

## Failure Handling

### Minor Failure (1–2 items in exit/intake checklist)

**Example:** One finding missing tag; one audit trail citation missing

**Action:**
1. Report: "Minor gate failures in [section]: [specific items]"
2. Fix: Make targeted edits (estimate <30 min)
3. Recheck: Run checklist on fixed items
4. Lock: Proceed once fixed items pass

**No escalation needed.**

---

### Medium Failure (3–5 items failing)

**Example:** Multiple findings untagged; Human Reflection frame ambiguous; 2 plan decisions lacking source

**Action:**
1. Report: "Medium gate failures; [section] has systematic issue"
2. Analysis: Is failure due to template gap? Reviewer skill? System change?
3. Fix: Make targeted pattern fix (estimate 30–60 min)
4. Recheck: Run full checklist
5. Lock: Proceed once all items pass

**Escalation:** Document root cause; note in Decision Log for learning

---

### Critical Failure (≥6 items failing)

**Example:** Review has many unclassified findings; Human Layer boundary severely compromised; multiple ADVISORY leaked into plan assumptions

**Action:**
1. BLOCK: Do not lock review or plan
2. Report: "Critical gate failures; too many boundary leaks [list]"
3. Escalate: Trigger system audit (MONTHLY_REVIEW_PROCESS_AUDIT_AND_PATCH_2026-04-03.md-style investigation)
4. Fix: Systematic fix required (may involve template re-design, process clarification)
5. Recheck: Run audit + rewrite + checklist
6. Lock: Proceed only after system audit clears

**Escalation path:** System Governance → Architect → Implementation

---

## Canonical Files & Source of Truth

| Purpose | File | Role |
|---|---|---|
| **Monthly Review template** | `05_TEMPLATES/TEMPLATE_Month_Final.md` | SOT for review structure + classification schema + intake gate rules |
| **Monthly Human Reflection template** | `05_TEMPLATES/TEMPLATE_Month_Human_Final.md` | SOT for optional human reflection (advisory-only, Q2 pilot) |
| **Daily template** | `05_TEMPLATES/TEMPLATE_Daily.md` | References governance; notes Human Reflection is optional + advisory |
| **Human Layer ADR** | `04_LOGS/ADR/ADR-20260322_HUMAN_LAYER_Q2_PILOT.md` | SOT for pilot gate; success criteria; boundary prevention |
| **Review exit checklist** | `05_TEMPLATES/MONTHLY_REVIEW_EXIT_GATE_CHECKLIST.md` | SOT for exit gate verification |
| **Plan intake checklist** | `05_TEMPLATES/MONTHLY_PLAN_INTAKE_GATE_CHECKLIST.md` | SOT for plan intake verification |
| **This document** | `00_README/MONTHLY_REVIEW_PROCESS_GOVERNANCE.md` | SOT for complete process flow + classification schema + gates |

---

## Usage Workflow

### Month-End (Review time)

1. **Write** Monthly Review using TEMPLATE_Month_Final.md
   - Tag findings as you write [EXEC/RULE/PILOT/ADVISORY/UNRESOLVED]
   - Fill System Change Review table with Type + Gate columns
   - Populate §3.5 Human Advisory Signals
   - Populate §Intake Gate rules

2. **Check** against MONTHLY_REVIEW_EXIT_GATE_CHECKLIST.md
   - Verify all 12 items pass
   - If <2 items fail: Fix and recheck
   - If 3+ items fail: Document and escalate

3. **Lock** review (declare DONE)
   - Mark in system: Review complete + exit gate passed
   - Archive to `07_REVIEWS/02_MONTH/` folder

---

### Start-of-Next-Month (Planning time)

1. **Read** previous month's review (published)
   - Note all tagged findings
   - Understand System Change decisions

2. **Apply** MONTHLY_PLAN_INTAKE_GATE_CHECKLIST.md
   - For each major plan decision: Trace source → Verify category → Check extraction rule → Verify audit trail
   - If 1–2 decisions fail: Fix with citations/transforms
   - If 3+ decisions fail: Take time to re-review; possible March review had gaps

3. **Write** Monthly Plan using TEMPLATE_Month_Final.md
   - §A Intake Gate: List which findings are being extracted and why
   - §1–3 Planning sections: Include source citation for each major decision
   - Before lock: Run intake checklist on all major decisions

4. **Lock** plan (declare DONE)
   - Mark in system: Plan complete + intake gate passed
   - Archive to `03_PLANNING/02_MONTH/` folder

---

## Timeline & Milestones

| Date | Milestone | Action |
|---|---|---|
| **2026-04-03** | Process patch published | Templates updated; checklist files created; this governance doc published |
| **2026-04-30** | March Review locked (past; already done) | Uses old templates (no classification schema) |
| **2026-05-01** | April Plan created | FIRST application of new Intake Gate (uses new templates) |
| **2026-05-31** | April Review locked | FIRST application of new Exit Gate; test for boundary safety |
| **2026-06-01** | May Plan created | SECOND application of Intake Gate; expect smoother |
| **2026-06-30** | May Review + Q2 Pilot Re-eval | Final Human Layer data collection; decide continuation |
| **2026-06-30** | Q2 Pilot Re-evaluation | Assess 5 success criteria; decide: Continue / Adjust / Sunset |

---

## Appendix: Common Tagging Questions

**Q: Should work output be [EXEC] or [RULE]?**  
A: Work output is [EXEC]. Rules are changes to *how you work*. Example:
- [EXEC]: "Shipped Zephyr migration test suite (23 tests passing)"
- [RULE]: "Daily Project Scope Rule now permanent (max 2 anchors)"

**Q: Should a pilot observation be [PILOT] or [ADVISORY]?**  
A: If it's an experiment or new system element under evaluation → [PILOT]. If it's a human signal / well-being pattern → [ADVISORY]. Example:
- [PILOT]: "Human Reflection pilot active; data collection phase" (this is the pilot experiment itself)
- [ADVISORY]: "Sleep-energy correlation observed" (this is a signal *from* the pilot reflection)

**Q: Can a finding be both [ADVISORY] and [UNRESOLVED]?**  
A: Not recommended; pick one primary tag. But example of both:
- [ADVISORY] (primary): "Loneliness pattern detected (connection/isolation cycle)"
- [UNRESOLVED] (secondary note): "Unknown if this is seasonal or structural; needs 2+ months to evaluate"

**Q: If I discover an ADVISORY signal that contradicts an EXEC fact, which takes priority?**  
A: EXEC facts (measured data) are used for planning; ADVISORY signals inform *capacity adjustment discussion*. If they conflict:
- EXEC: "Capacity = 3–4 office hours/week (measured)"
- ADVISORY: "Feels like work could take more (subjective sense)"
- Resolution: Work is measured at 3–4h; if advisor feels less, might indicate energy depletion or task mismatch (investigate); do not increase allocation on feeling alone

---

**Document maintained by:** System Governance  
**Last updated:** 2026-04-03  
**Next review:** 2026-06-30 (Q2 pilot re-evaluation)  
**Questions:** Reference TEMPLATE_Month_Final.md, checklists, or escalate to Decision Log

