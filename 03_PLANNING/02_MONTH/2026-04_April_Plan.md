# APRIL MONTHLY PLAN — 2026-04

> **Aligned with Q1 Strategy:** Delivery Ramp + Capacity Validation Phase  
> **Month:** April 2026 (W14–W17; 1–30 April)  
> **Planning Date:** April 5, 2026  
> **Queue Phase:** Q1 Phase 1 Continuation (foundation → delivery ramp; Feature Freeze 30/4)  
> **Role:** Execute Signee demo feature path + RobotOS hardware bringup while validating capacity assumptions from March
> **Planning Time Budget:** 45–60 min  
> **Operational Principle:** April is BOTH a delivery month AND a controlled validation/evidence month for Phase 3 capacity prep

---

## 0) QUICK CONTEXT

This month marks the transition from Q1 foundation (March) to Q1 delivery acceleration. Two external deadlines shape April:
- Signee Demo: Scope Freeze 30/4 → Feature Freeze (no new work after April 30)
- RobotOS: Hardware validation begins (board bringup mid-April)

**Critical distinction:** April is NOT planned as a "business as usual" month. It is explicitly framed as:
1. A **delivery month** (execute committed features at quality)
2. A **validation month** (test capacity assumptions from March; collect Phase 3 evidence)

This dual frame prevents treating April as either "just ship what we can" or "ignore real delivery pressure for process work."

**Additional deliverable (fixed-scope demo):**
- **Project Accountant:** Single-flow demo application (fixed requirements). Built for customer validation. Execution window: W14–W15. Executed within available capacity after blocker work. Deliverable: working demo by end of month.

**Sequential distinction (W14–W15):** Weeks 14–15 operate as an **UNBLOCK + FLOW RELEASE phase** before returning to feature-focused delivery W16–18. Two critical blocker missions (Signee board stabilization + RobotOS hardware bringup) take priority in the first two weeks. This sequencing unblocks downstream work + enables delegation.

---

## PART A: APRIL PLANNING

---

## 1) MONTH IDENTITY & STRATEGIC DIRECTION (5 min)

### Month Theme

**"Execute with Discipline: Validate as You Go"**

April is the first real test of whether the March system (Daily Scope Rule, templates, 3-project coordination) holds under delivery pressure.

### Month Mission Outline

1. **Signee Demo Path:** Deliver core features at production quality; lock scope end-of-month
2. **RobotOS Hardware:** Complete board bringup + validate prototype can boot on real hardware  
3. **Zephyr Stable Base:** Maintain release cadence; provide stable foundation for both projects
4. **System Validation:** Operate the March-designed system at full capacity; measure what works and what breaks

### Month North Star (Ưu tiên tuyệt đối)

**Deliver Signee feature scope by 30/4 AND maintain system discipline under delivery pressure.**

If system breaks under load (Daily Scope Rule violated, evening overcommit emerges, third-project pressure manifests) → flag immediately rather than silently absorbing.

### Stop Doing (From Intelligence Transfer)

1. **Intensive system design/refinement** (reduce from 15% March to 5% assumed overhead)
2. **Evening overcommitment experimentation:** Target 0h planned evening work. Controlled spillover: up to 1h (wrap-up / continuation only). Caution benchmark: 1.5h (review signal — not a hard cap or automatic violation threshold). Evening is a valid serialized execution domain when activated — not a default working block and not an invalid domain. The real concern is repeated 2h+ evenings as standard planned mode, not any single night above 1.5h.
3. **Assuming daily capacity scales to 5 blocks by default** (test 3–4 sustainable; 5 only on high-energy weeks)

---

## 2) CORE OUTCOMES (April Mission-Level Definition) — 10 min

> Outcome = measurable + source-traceable. Outcomes are mission-level, not task breakdown.

### Outcome #1: Signee Demo Feature Delivery

**What:** Execute core demo features listed in Signee M3 scope (end-to-end flow).  
**Metric / DoD:**
- All core features implemented
- Feature Freeze enforced on 30/4 (no new work accepted after this date)
- 0 open P0/P1 bugs at end of month (May reserved for bug fix + final validation)
- Demo flows validated in test environment

**Deadline:** 30/4 (Feature Freeze)  
**Owner:** Project Lead (Signee)  
**Source:** Q1 Strategic Objective #1 + March Review §2 Output Review (Signee M3 prep on-track)

---

### Outcome #2: RobotOS Hardware Bringup + Baseline Demo

**What:** Board boots, runs CNC demo sequence (HOMING → RUN → STOP), stable ≥10 min.  
**Metric / DoD:**
- Board successfully boots Zephyr baseline
- CNC app compiles + starts on board by mid-April
- Demo sequence runs ≥1 cycle without crash
- Execution stability confirmed (no hard resets; graceful recovery from errors if any)

**Deadline:** 20/4 (hardware validation), 30/4 (demo integration complete)  
**Owner:** Project Lead (RobotOS)  
**Source:** Q1 Strategic Objective #2 + March Review §3.1 Portfolio Balance (RobotOS M5 on-track; M6 scope staged for May)

---

### Outcome #3: Zephyr Release Stability

**What:** Maintain release branch at CI 100% + no P0/P1 bugs.  
**Metric / DoD:**
- CI pipeline green on release branch (0 build failures)
- All regression tests pass (hardware smoke test ≥1x/week)
- No critical (P0) or high (P1) bugs blocking demo projects' use of Zephyr

**Deadline:** Rolling weekly validation (validate each Monday)  
**Owner:** Architecture Lead (Zephyr) + Signee/RobotOS consumers  
**Source:** Q1 Strategic Objective #3 + March Review Execution Output (Zephyr KTLO stable)

---

### Outcome #4: Capacity System Validation (Evidence for Phase 3)

**What:** Operate March-designed system (Daily Scope Rule + 3-project coordination) under full delivery load; collect measurable evidence that informs Phase 3 capacity control design.  
**Metric / DoD:**
- Actual daily capacity measured (blocks per day by weekday)
- Evening capacity pattern tracked (actual evening work sessions + duration)
- Three-project allocation monitored (visible tracking of whether 2-anchor rule held)
- Plan vs. actual execution logged weekly (identify where estimates were wrong)
- No silent system failure (if Daily Scope Rule breaks, iteration is flagged explicitly within week, not discovered in month-end review)

**Deadline:** Evidence collection ongoing; checkpoint 15/4 (mid-month trend), 30/4 (full-month pattern)  
**Owner:** Self (daily execution) + weekly reviews (trend capture)  
**Source:** Phase 3 prep framework (PHASE_3_READINESS_CAPACITY_CONTROL) + March validation needs

---

## 3) CAPACITY & RHYTHM (To Prevent Overload) — 7 min

### CAPACITY MODEL: Dual-Pool Architecture (FIXED)

**MODEL DECISION:** Zephyr owns office hours exclusively as the stable foundation. All other projects execute in non-office time (evenings/weekends). This model is non-negotiable and persists across all April weeks.

**Pool A — Office Hours (Zephyr Exclusive):**

- **Occupant:** Zephyr only (KTLO, testing infrastructure, CI support, release maintenance)
- **Capacity:** ~28–32h/week (100% of office pool)
- **Role:** Primary anchor; stable foundation; non-negotiable
- **Signee/RobotOS/Project Accountant:** Do NOT occupy office-hour capacity at planning level. Office hours are Zephyr-exclusive by definition.

**Pool B — Non-Office Hours (Planning-Level Home for Signee, RobotOS, Project Accountant):**

- **Planning-level occupants:** Signee + RobotOS (shared pool); Project Accountant (if activated, resides here at planning level)
- **Capacity:** ~7–12h/week shared (weekday evenings + weekend slots)
- **Rule:** No dual-project stacking per evening (serialization enforced); 1.5h as caution benchmark only (not a hard cap); concern is repeated 2h+ planned evenings as standard mode; all evening work ≥0.5h must be tracked
- **Project Accountant execution model:** NOT allocated office hours at planning level (resides in Pool B). Execution flexibility: May request daily delegation from Zephyr to borrow office time (Zephyr may approve or defer, subject to R9-DEL guardrails). Default: not pre-planned for personal evening time; primary execution is Pool B non-evening time or borrowed office time. **Exception (activated W14+):** if morning delegation is not available that day and blocker requires unblocking, may execute in Pool B evening under serialization rules (max 1 project/night, Evening Check tracking required; treat 1.5h as caution benchmark). See §Execution Flexibility for full guardrails.

**Why Dual-Pool (Fixed Model):**
- Zephyr cannot be starved of office-hours capacity; it is the operational foundation
- Signee/RobotOS proven sustainable in March in personal-time execution model
- Prevents office-hours contamination or allocation chaos from shared percentages
- Project Accountant is true conditional overlay (not a default)

### Project Accountant Conditional Activation (W14–W15 ONLY)

**Gate: Project Accountant W14-Early (Monday EOD, April 6)**
- [ ] Boards available + blocker work is viable?
- [ ] Scope locked tightly (written scope doc)?
- [ ] Zephyr stable in maintenance mode?
- [ ] Delegation trial showing promise?

If ANY gate item fails: **Project Accountant does NOT activate; remains at 0% allocation all April.**

**If All Conditions Met:**
- Project Accountant NOT allocated office hours at planning level; resides in Pool B
- Execution flexibility: Project Accountant may negotiate daily delegation with Zephyr to borrow office time (see §Execution Flexibility below)
- Signee/RobotOS remain in Pool B (non-office only)
- Scope: Architecture design for single-flow demo + delegation setup
- Duration: W14–W15 only (hard stop)
- Time domain: Default non-office; may use borrowed office time at daily level only (NEVER personal evening time)

**W15 Mid-Gate (April 10):** If blocker closure on-track, may continue through W15. Otherwise deactivates immediately.

**W16 Hard Deactivation:** Project Accountant automatically drops to 0%. No continuance without separate May planning decision.

### Daily Rhythm Guardrails (From March Validated)

- **Office Pool (Pool A):** Zephyr ONLY. Daily anchor is Zephyr task (KTLO / CI / support). Non-Zephyr projects do NOT occupy office hours at planning level.
- **Non-Office Pool (Pool B):** Signee + RobotOS shared. Evening capacity model: **No pre-committed evening slots in the weekly plan** (evenings are activated at daily planning level, not pre-allocated); evenings remain a valid serialized execution domain for Signee and RobotOS; 1.5h treated as caution benchmark (not hard cap); concern is repeated 2h+ planned evenings as standard mode. Serialization rule: max 1 project/night (no dual-project parallel stacking). "Target 0h planned" = no planning-level pre-commitment to evenings, NOT that evenings are invalid or forbidden.
- **Project Accountant (if activated):** Resides in Pool B at planning level (NOT pre-allocated office hours). May request daily delegation from Zephyr. If approved, borrows office time for execution (not personal evening). Daily delegation is dynamic, not a permanent allocation.
- **Deep blocks per day:** 3 blocks baseline; 4 blocks on high-energy days; 5 blocks max 2–3x/week (NOT a planning assumption). Applies to Zephyr office anchor.
- **Anchors per day:** 2 maximum non-negotiable (Daily Project Scope Rule enforced for Signee/RobotOS in Pool B).
- **Evening tracking (Pool B):** All work ≥0.5h must be recorded in Evening Check block. Untracked evening = system violation; escalate immediately.
- **Blocker serialization (Pool B evening):** Only ONE Signee OR RobotOS blocker per evening (if board unavailable during office). Other defers to next office day. No dual-blocker stacking.
- **Anti-shadow workload rule:** All Pool B evening work visible via Evening Check. Prevents hidden overload in personal time.

### Monthly Scope Protection Rules

1. **No hidden projects:** If a third active focus emerges, it must replace a committed focus, not stack on top.
2. **Signee scope is locked 30/4:** After this date, any new feature work is explicitly deferred to Q2. 
3. **If capacity drifts >20% below assumption by W15:** Trigger replanning of remaining 6 weeks (see §9 Replan Trigger).
4. **Evening overcommit is visible:** If evening work exceeds 2.5h in a week, it is flagged in weekly review, not silently absorbed.

---

### Execution Flexibility (Daily Level Only)

**Planning-level model:** Dual-pool (Zephyr = office exclusive; Signee/RobotOS/Project Accountant = non-office).

**Execution-level flexibility:** At daily planning level, projects may negotiate within constraints:

- **Project Accountant execution options (if activated):**
  - Primary: Execute outside office hours (Pool B time)
  - Flexibility: May borrow Zephyr office time via daily delegation (subject to guardrails below)
  - Evening execution: May execute in non-office hours (Pool B) if needed, BUT must follow Pool B serialization (max 1 project/night) and Evening Check tracking; 1.5h treated as caution benchmark (not a hard cap or violation threshold)
  
- **Signee/RobotOS execution options:**
  - Primary: Execute in evenings (Pool B, serialized)
  - Flexibility: May use office hours if board/hardware available during office
  - Constraint: NEVER overrides Zephyr anchor time

**Key principle:** Execution-level borrowing is dynamic and NOT pre-allocated. Daily decisions about delegation happen in morning planning, not in monthly plan. This flexibility prevents artificial blocking while preserving planning-level ownership.

**Delegation Approval Criteria:** Zephyr may approve delegation to Project Accountant only if ALL conditions hold:
1. Zephyr's daily KTLO baseline (08:00-09:15) remains untouched and fully protected
2. No active P0/P1 issues require immediate Zephyr response  
3. Daily CI health check, smoke test, and release support work is already scheduled/protected
4. Remaining available office time after delegation is sufficient for unplanned support work

**Zephyr Protection Floor (Non-Delegable):** Daily 08:00-09:15 (1h 15min) is NON-DELEGABLE. This protected baseline allows CI health checks (~15-20 min), smoke test execution (~20-30 min), and responsive P0/P1 support (~10-30 min as needed). Only time after 09:15 may be borrowed for Project Accountant delegation. If KTLO work cannot fit in 08:00-09:15 on any day, escalate immediately.

**Early-Warning Escalation Triggers:** Trigger immediate escalation if ANY of these occur:
- Project Accountant borrows Zephyr office time on >2 consecutive days
- Zephyr delegation occurs on >3 days in a single week  
- Actual Zephyr office time (outside KTLO floor) falls below ~3 hours/day on any single day
- Weekly allocation divergence exceeds 15%

**Enforcement:** Daily Evening Check tracks all delegation approvals and actual Zephyr office allocation. Weekly reviews compare planned vs. actual allocation. Any trigger above activates escalation for replanning decision (is plan wrong? Or is execution creeping into hidden model corruption?). Do not silently absorb drift.

---

### Planning vs. Execution Separation (Anti-Drift Rule)

**Principle:** Monthly and weekly plans define capacity structure and ownership. Daily plans optimize execution within that structure. No execution-level borrowing is back-propagated into planning-layer allocation.

**What this means:**
- **Planning layer:** "Zephyr owns office hours (100%); Project Accountant is in Pool B" — this NEVER changes mid-month
- **Execution layer:** "Today, Project Accountant borrows 2 blocks from Zephyr; Zephyr delegates" — this is a daily decision, not a re-allocation
- **Back-propagation rule:** If Project Accountant borrows office time daily for a week, this does NOT become "Project Accountant is now allocated 15% of office" in the planning model. It remains "Project Accountant is in Pool B; daily delegation happens to occur frequently" in the plan

**Critical:** If execution patterns hit ANY of the early-warning triggers (>2 consecutive days, >3 days/week, <3h/day available, or >15% weekly divergence), stop and replans. Do NOT allow silent creep into model corruption.

---

## 4) WHAT MUST CONTINUE (From Intelligence Transfer) — 5 min

1. **Daily Project Scope Rule (max 2 anchors/day):** Proved effective March; prevent 3-project fatigue. KEEP permanent (non-negotiable). | Source: March Review §3 System Change, March Human Reflection emotional climate

2. **Three-Project Portfolio Model (Zephyr KTLO + RobotOS + Signee concurrent):** March proved this is sustainable with discipline. Continue full allocation across all three. | Source: March Review §3.1 Portfolio Balance + Intelligence Transfer §1

3. **Execution-First Framework:** System architecture is operational (templates lived-in, gates established, human layer piloting). April focus shifts toward delivery intensity; maintain framework discipline (do NOT rebuild). | Source: March Review §3 + Intelligence Transfer §1

---

## 5) WHAT MUST CHANGE (From Intelligence Transfer) — 5 min

1. **Evening Capacity Realistic Benchmark: 1.5–2h, not 2–2.5h** → Adjust evening-task commitments. Plan conservatively at 1.5h firm + 0.5h optional (not aspirational 2h+). This is backed by W09 measured reality. | Source: March Review §2.1 Drift Check + Anti-Anchors

2. **Deep Work Blocks Ceiling: 3–4 blocks baseline, not aspirational 5** → April planning uses 3–4 blocks as capacity base; 5 blocks is viable 2–3x/week ONLY on high-energy weeks, not a planning assumption. | Source: March Review §2 Output Review + Appendix (W09 validation)

---

## 6) WHAT MUST STOP / REDUCE (From Intelligence Transfer) — 3 min

1. **System Design / Framework Work: 15% (March) → 5% (assumed overhead)** → March's 15% was one-time system launch cost (templates, Daily Scope Rule, Human Reflection layer formalization). April returns to standard 5% maintenance/improvement. Stop intensive template refinement cycle; focus execution. | Source: March Review §2.1 Drift + Portfolio Balance

2. **Evening Overcommitment Exploration (Unbounded):** → Stop unbounded evening expansion attempts (especially planning 2× M-blocks as a normal post-work pattern); keep weeknight after-work bounded and disciplined (1× S or 1× M only). March W09 showed overcommit risk under unbounded use, while W10+ suggests evening became more stable when constraints were respected. April therefore treats evening as a bounded resource, not an expandable capacity reserve. | Source: March Review §5 Anti-Anchors + TEMPLATE_Week_Final recommendations

---

## 7) WHAT NEW ENTERS NEXT MONTH (From Intelligence Transfer) — 3 min

1. **Factory Research Emerges as Potential Q2 Priority** → March exploration proved this feature direction is viable + worth pursuing. DECISION FOR APRIL: Treat as **OPPORTUNISTIC ONLY** (not committed). If late April shows spare capacity + Signee/RobotOS on schedule, exploratory factory work can happen. If schedule pressure remains, defer to Q2. | Source: March Review §2 Output (value assessment); allocated 0% baseline, up to 3% if available

2. **Q2 Human Layer Re-Evaluation Gate: June 30** → Human Reflection pilot runs through June 30 (per ADR-20260322). April is data-collection month. Continue optional daily reflection. Aggregate in April and May reviews. May not materially change April plan, but clarifies timing of Q2 pilot re-eval. | Source: Decision Log (ADR-20260322) + March Review §3.5

3. **Project Accountant (W14–W15 ONLY, CONDITIONAL)** → Temporary spike/demo design project. Operator role: architecture definition + unblocking (NOT implementation). Execution delegated to others. **HARD STOP end-of-W15** (no scope creep post-W15). Allocation: 10–15% W14–W15 ONLY (trades with RobotOS/Zephyr reduction during blocker phase). ACTIVATION CONDITION: Board availability confirmed + blocker progress on-track + scope locked tightly by end-W14 day 1. Deactivation: W15 end hardstop enforced (explicit decision required to continue). | Source: Controlled rebalance audit; blocker-first execution model

---

## 8) OPEN DECISIONS & STRATEGIC UNCERTAINTY — 3 min

### Decision #1: Signee vs. RobotOS Allocation Rebalance in May?

**Current state:** April keeps Q1 allocation (Signee 55% Phase 1, RobotOS 25% Phase 1). May will be Phase 2 (Signee 40%, RobotOS 40%).

**Unresolved:** If Signee feature delivery finishes early (before 30/4 Feature Freeze) → Should April allocation shift to RobotOS acceleration? Or should early completions go to buffer/risk reserve?

**Decision rule for April:** If Signee core features complete by 25/4 → Feature Freeze holds at 30/4 (no acceleration into May scope). Freed-up Signee allocation 25–30/4 goes to buffer/risk reserve (for unexpected Zephyr issues or RobotOS blocker response), NOT to new scope.

**Owned by:** April monthly review (checkpoint 15/4: is Signee on track to early finish?).

---

### Decision #2: Factory Research Scope (Resolved for April)

**Status:** OPPORTUNISTIC ONLY. Not committed. 0% baseline allocation.

**Condition for April engagement:** If by end of W16 (23/4) both Signee and RobotOS are confirmed on-schedule with <5% buffer burn → May allocate 1–2 exploratory sessions to factory research. Otherwise deferred.

**Owned by:** Week-18/19 review (late April checkpoint).

---

## 9) ASSUMPTIONS & VALIDATION CONDITIONS — 10 min

This section is **CRITICAL** for audit compliance and Phase 3 calibration.

### Assumption Set #1: Daily Capacity Baseline

| Item | Assumption | Why Used | Validation Window | Replan Trigger |
|---|---|---|---|---|
| **Daily blocks** | 3 blocks sustainable; 4 blocks achievable; 5 blocks 2–3x/week max | Backed by March W09 measured data + March Review appendix | W14–W15 (first 2 weeks) | If measured (w14+w15 avg) drops below 2.5 blocks/day → replan by W16 |
| **Block duration** | 90 min deep work baseline | Template standard; not challenged in March | Rolling (adjust if different) | If 90 min blocks drop to <60 min in >30% of blocks → flag |
| **Anchor rule (2 max/day)** | Daily Scope Rule enforced (max 2 projects/day) | Prevented 3-project fatigue March; non-negotiable | Rolling daily practice | If Daily Scope Rule violated >2 days in a week → escalate in weekly review |

---

### Assumption Set #2: Evening Capacity & Work-Time Domain

| Item | Assumption | Why Used | Validation Window | Replan Trigger |
|---|---|---|---|---|
| **Evening capacity model** | Target: 0h planned evening. Spillover allowance: ≤1h (wrap-up / continuation only). Caution benchmark: 1.5h (review signal; not a hard cap). | March W09 measured data validated; prevents 2h+ normalization while allowing natural spillover | W14–W18 (daily Evening Check tracking) | If 2h+ evening recurring on 2+ nights/week → review and replan next week; untracked evening ≥0.5h → flag at weekly review |
| **Work-time domain** | Office hours reserved for Zephyr/Signee/RobotOS/Project Accountant; evening is controlled overflow only | Scope protection + clear context boundaries | Ongoing (daily practice) | If main project work shifts to evening without board-access justification → escalate |
| **Evening work tracking** | All evening work ≥0.5h must be recorded in Evening Check block | Prevents shadow workload; system integrity | Rolling (daily; aggregated weekly) | Untracked evening ≥0.5h = tracking integrity failure; flag at weekly review

---

### Assumption Set #3: Three-Project Portfolio Sustainability

| Item | Assumption | Why Used | Validation Window | Replan Trigger |
|---|---|---|---|---|
| **Three projects concurrent** | Signee 55% + RobotOS 25% + Zephyr 10% + buffer 10% = sustainable | Q1 plan + March validation; non-overload | W14–W18 (weekly portfolio audit) | If one project creeps >65% of effort for >1 week → rebalance immediately |
| **Project leakage risk** | Daily Scope Rule prevents silent 3rd anchor emergence | March Human Reflection noted "brain needs stimulation + internal pressure tendency" → Third anchor may try to emerge internally | W14–W18 (weekly execution review) | If internal scope pressure manifests (e.g., longer focus on project #3 despite rule enforcement) → escalate in weekly review |
| **Portfolio allocation accuracy** | ±15% tolerance (if allocation drifts >15% → replanning trigger) | Prevents silent drift | W14–W18 (weekly portfolio check) | If actual allocation >15% off target (e.g., Signee drops to 40%, RobotOS rises to 40%) → replan by W15 |

---

### Assumption Set #4: Ambiguity Loading (Emerging, Not Yet Fully Modeled)

| Item | Assumption | Why Used | Validation Window | Replan Trigger |
|---|---|---|---|---|
| **Ambiguity gate effectiveness** | Ambiguity Gate (PHASE 2) converts vague tasks; assumes conversion overhead is negligible | PHASE 2 deployed but overhead not yet quantified | W14–W18 (track conversions + time cost) | If ambiguity-heavy week (>5 UNBLOCK conversions) appears lower capacity than clean week → may require separate ambiguity load model |
| **Task clarity model** | Tasks with clear artifact expectations + verifiable exit take ~same time as their nominal stage estimate | Semantic quality gates active; assumption is gates prevent clarity loss | Rolling (daily practice) | If completion time consistently exceeds estimate by >20% on high-ambiguity tasks → flag for May review |
| **Ambiguity as separate dimension** | Ambiguity load is NOT yet modeled as separate "capacity dimension" (e.g., "1 clear M + 1 ambiguous M ≠ 2 clear M capacity-wise") | Phase 3 Design Question #2: "Does ambiguity count separately?" → April must collect data | W14–W18 (track ambiguity ratio + energy per work session) | If energy/session dropped noticeably higher for high-ambiguity-ratio work → indication that yes, ambiguity is separate load; feed to Phase 3 May calibration |

---

### Assumption Set #5: Human Advisory Signals → Hypotheses (NOT Planning Rules)

These are from March Human Reflection [ADVISORY] layer. Used as capacity hypotheses to test, NOT hard rules.

| Human Signal | Transformed to Hypothesis | Testing in April | Validation Method | Replan Trigger |
|---|---|---|---|---|
| **Sleep-energy correlation** ("7h+ sleep = high energy; 5–6h = fatigue") | TEST: Protect 23:00 bedtime hypothesis; assume this predicts energy shape; validate correlation | Track sleep hours + energy level by day; check correlation | April review: Does sleep quality predict next-day energy? | If correlation <0.7 (weak) → sleep timing rule not predictive; adjust May |
| **Isolation risk** ("March had zero team sync; solitude in system design sustainable but not long-term") | TEST: Weekly 30–60 min team check-in; assume this reduces isolation signal; measure drift/connection | Schedule 1× weekly sync (project sync or 1:1); track whether isolation feeling subsides | April review + subjective feedback | If isolation feeling persists despite sync → either sync not effective OR isolation not energy-critical; adjust May |
| **Ambiguity/stimulation pressure** ("Brain needs stimulation; tends to self-create scope pressure internally despite external rules") | TEST: Monitor whether Daily Scope Rule holds externally but internal scope pressure manifests (e.g., longer sessions, evening exploration); assume rule helps but doesn't eliminate root tendency | Daily practice + weekly reflection: Is third-project pressure felt despite 2-anchor rule? | Weekly review: Can operator feel clean 2-anchor days or does internal pressure persist? | If pressure persists significantly → may need explicit "stimulation budget" design in May; note for Phase 3 |

---

## 10) CAPACITY GUARDRAILS (From Audit Findings) — 5 min

These are operational limits translated from audit + March validation. Non-negotiable.

### Guardrail #1: No Hidden Evening Overcommit

**Rule:** If evening work creeps toward 2.5+ hours consistently, it is flagged in weekly review, not absorbed silently.

**How checked:** Weekly review captures "actual evening work this week" + compares to plan.

**Response if triggered:** If pattern sustained >1 week, reduce planned work load next week (do not attempt to "optimize" evening; reduce instead).

---

### Guardrail #2: No Silent Third Anchor

**Rule:** Daily Scope Rule (max 2 anchors) is operational practice (enforced via daily template). If third anchor emerges, it is visible within 1 day (noted in daily retrospective), not discovered retrospectively.

**How checked:** Daily template includes anchor count; weekly review surfaces any violation.

**Response if triggered:** If violated >1 day in a week, analyze root cause (overload signal? Planning error? External interrupt?) and adjust accordingly in next week.

---

### Guardrail #3: Ambiguity Load is Visible

**Rule:** High-ambiguity work (many UNBLOCK conversions, many open decisions) is tracked visibly. If ambiguity ratio climbs, it is noted.

**How checked:** Weekly review | track "ambiguity gate conversions this week" + energy/capacity relationship.

**Response if triggered:** If high-ambiguity week, note data for Phase 3 analysis (May review will model ambiguity as separate dimension).

---

### Guardrail #4: System Maintenance Bounded

**Rule:** System refinement work (template updates, process improvements, framework work) limited to 5% of capacity (assumed overhead).

**How checked:** Portfolio audit weekly; if system work exceeds 5% baseline → must explain trade-off (what was reduced to make room?).

**Response if triggered:** If system work exceeds 5% without explicit rebalancing → escalate in weekly review.

---

### Guardrail #5: April is a Validation Month (Not "Just Execute")

**Rule:** Evidence collection for Phase 3 is not optional. Each week, observations about capacity, fatigue, project friction must be captured.

**How checked:** Weekly review includes "observations for Phase 3 calibration" section.

**Response if triggered:** If a week has no evidence notes → flag as data gap.

---

### Guardrail #6: Evening Ambiguity Bounded

**Rule:** Evening work in W14–W15 must remain ≤60% ambiguity-heavy (design work, open-ended thinking). If ambiguity >60% of evening content → escalate; move design work to daytime blocks.

**How checked:** Daily reflection note ambiguity ratio of evening work; weekly review flags if high-ambiguity evenings persist.

**Response if triggered:** If pattern sustained >2 nights → reduce evening scope to lower-ambiguity work (synthesis, review, planning); move design to day.

---

### Guardrail #7: No Hidden 3rd/4th Stream

**Rule:** Blocker missions remain primary execution anchors. Temporary support overlays (unblocking support, design work) must not compound into a hidden 3rd project stream.

**How checked:** Daily template tracks actual anchors + support; weekly review: "Was 2-anchor rule operationally held, or did 3+ focus areas emerge?"

**Response if triggered:** If 3+ focus areas detected in a day → analyze: Is blocker work inflating? Is Accountant scope expanding? Escalate if pattern persists.

---

## 11) OBSERVATION & EVIDENCE COLLECTION FOR PHASE 3 PREP

This section operationalizes the Phase 3 observation period (April 7–May 1).

### Evidence Set #1: Real Capacity Data (W14–W15)

**What to measure:**
- Daily block count (actual, by day of week)
- Block duration (90 min? less?)
- Anchor adherence (2-anchor rule violations if any)
- Evening work sessions (count + duration)

**Capture method:** Daily template completion + weekly review summary

**By:** Checkpoint W15 (mid-April): confirm 3–4 block baseline or flag if different

---

### Evidence Set #2: Overload Pattern Recognition (W14–W18)

**What to measure:**
- Days that felt "overloaded" (subjective) vs. not (can't schedule 2+ anchors + high-ambiguity items simultaneously?)
- Root causes when overload appears (external interrupt? over-commitment? ambiguity stacking?)
- Correlation with next-day fatigue

**Capture method:** Weekly review "overload pattern" observation

**By:** Checkpoint W18 end-of-April: identify what "overload day signature" looks like for this operator

---

### Evidence Set #3: Ambiguity Gate Effectiveness (W14–W18)

**What to measure:**
- Weekly ambiguity gate conversion count (how many tasks converted from vague → UNBLOCK?)
- Time cost of conversion (does clarification take 5 min or 30 min?)
- Impact on execution (does clarity improve execution speed?)

**Capture method:** Weekly review | track "ambiguity conversions + execution clarity" correlation

**By:** Checkpoint W18 May 1: data on whether ambiguity gate cost is negligible or significant

---

### Evidence Set #4: Fatigue & Sleep Coupling (W14–W18)

**What to measure:**
- Sleep hours consumed per night
- Energy level reported next day (high / medium / low)
- Whether 23:00 bedtime target held (advisory hypothesis test)
- Correlation: does sleep quality predict next-day capacity?

**Capture method:** Daily human reflection (optional but useful) + weekly energy trend note

**By:** Checkpoint W18 May 1: validate sleep-energy hypothesis or flag if weak/absent

---

### Evidence Set #5: Failure Mode Breakdown (W14–W18)

**What to measure:**
- Tasks that failed to complete / took longer than planned (collect ~3–5 examples by end of month)
- For each failure: classify as (a) planning failure (estimate wrong), (b) execution failure (distraction / context cost), (c) ambiguity failure (unclear requirement), OR (d) external blocker
- Pattern count by category

**Capture method:** Weekly review | capture observed failures, brief root-cause assess

**By:** Checkpoint W18 May 1: categorized failure mode list for Phase 3 to use in design

---

## 12) MONTHLY RISKS — 5 min

| Risk | Probability | Impact | Mitigation | Monitor |
|---|---|---|---|---|
| **Thin-data assumption breaks** (W09 w1 only; April runs different) | MEDIUM | HIGH (capacity model fails; replanning needed mid-month) | W14–W15 early validation checkpoint; trigger replan if >20% deviation | Weekly actual vs. assumed capacity |
| **Advisory signals extracted as hard rules** (Human Reflection signals misused as planning constraint) | MEDIUM | MEDIUM (leads to false guardrails; wastes cycles on wrong problem) | Intake gate audit (did risk transformation happen correctly?) | Audit checklist in Part B review if any advisory became hidden rule |
| **Third-project leakage despite Daily Scope Rule** (internal pressure + external interrupt creates 3rd anchor) | MEDIUM | MEDIUM (silent fatigue rebuild; detected late) | Weekly review includes explicit "was 2-anchor rule clean this week?" question | Daily template anchor count + weekly escalation if violated |
| **Ambiguity load underestimate** (conversion cost + clarity-seeking overhead not accounted for) | LOW | MEDIUM (capacity drifts; discovered in May) | Track ambiguity conversions + energy/session relationship weekly | Weekly review: high-ambiguity weeks show lower output? |
| **Evening capacity relapse under delivery pressure** (W09 unstable; W10+ suggests stabilization under constraint; April delivery stress could trigger return to overcommit) | LOW | MEDIUM (burnout risk; feedback loop into fatigue) | Guardrail #1 (enforces constraint; flag if >2.5h/week); monitor weekly | Weekly evening work log |
| **Signee Feature Freeze not enforced** (scope "just one more feature" creeps post-30/4) | LOW | HIGH (May delivery miss; demo quality drops) | Feature Freeze date communicated explicitly in April plan; intake gate pre-check day-before 30/4 | Week-end-of-April review: were any features added after 30/4? |
| **Capacity expansion burnout** (push to 4–5 blocks daily without energy protection) | MEDIUM | HIGH (crash end-of-month; recovery needed into May) | Energy protection rules non-negotiable (do not trade depth for speed); if overload feels real, reduce scope not intensity | Weekly energy level + nights with <6h sleep |
| **Project Accountant scope creep beyond W15** (feels productive; stakeholders request Phase 2; scope continues silently into W16+) | MEDIUM | HIGH (invisible 4th project emerges; April assumptions invalidate) | Hard-stop written agreement; W15 end checkpoint explicit closure decision; add to plan only if hard-stop enforced | W15 end: "Accountant project formally ended?" |  
| **RobotOS blocker extends beyond expected window** (board late, hardware issues, debugging extended) | MEDIUM | HIGH (blkr work consumes W16 capacity; prototype delivery slips) | Validate board availability pre-W14; escalate if unavailable day 2 W14 | W14 gate: Board status confirmed? |  
| **Signee feature compression if blocker delayed** (board blocker takes longer; feature work W16–W18 only = 3 weeks instead of 4) | MEDIUM | MEDIUM (feature quality or deadline at risk) | W15 checkpoint identifies delays early; trigger feature replan if blocker extends | W15: "Blocker status on-track?" |  
| **Ambiguity overload + evening stress** (W14–W15: design + unblock + feature work = high-context environment; evening ambiguity >60%) | LOW | MEDIUM (energy crash; execution quality drops mid-month) | Bound evening ambiguity (Guardrail #6); track evening content daily; escalate if fragmented | Weekly: "Evening ambiguity sustainable?" |  
| **Delegation failure (delegated Accountant work incomplete; operator must execute)** | MEDIUM | HIGH (becomes deep implementation; 3rd project emerges; April slips) | Trial delegation W14 first 3 days; validate team capacity by 5/4; hard-stop if incomplete W15 end | W14 day 5: "Delegation viable?" W15: "Accountant execution complete?" |  
| **Zephyr reduced allocation insufficient** (5% maintenance-only insufficient; hidden bug emerges W14–W15; blocks all projects) | LOW | HIGH (blockers stalled; all projects stalled) | Pre-audit Zephyr branch end-of-W13; contingency (swap 5%→15% if critical issue surfaces) | Weekly: "Zephyr CI stable?" |  
| **2-anchor rule operationally invisible 3rd/4th stream** (blocker + Accountant + feature work = 4 contexts; rule preserved on paper but fragmented in practice) | MEDIUM | MEDIUM (execution fragmented; quality decreases; system feels unstable) | Daily tracking "actual anchors + support"; weekly: "Was 2-anchor held operationally?"; escalate if >2 detected | Daily template; weekly review |

---

## 13) EXIT CRITERIA / MONTH SUCCESS CONDITIONS

SUCCESS requires BOTH delivery outcomes AND evidence quality.

### Delivery Success Criteria (Must All Be True)

- ✅ Signee core features implemented at demo quality (P0/P1 bug-free)
- ✅ Signee Feature Freeze enforced 30/4 (no new work accepted post-date)
- ✅ RobotOS board boots + CNC demo baseline runs (hardware milestone passed)
- ✅ Zephyr CI green + regression tests pass (stable release)

### Evidence Quality Criteria (Must All Be Gathered)

- ✅ Daily capacity tracked (block count by day x 4 weeks)
- ✅ Evening capacity pattern documented (actual hours per night x 4 weeks)
- ✅ Ambiguity gate conversions logged weekly (at least 3 conversion examples + time cost)
- ✅ Overload signals identified (at least 2 example overload days + root cause analysis)
- ✅ Failure modes categorized (at least 3 failures classified by type)
- ✅ Sleep-energy correlation observed (at least 2 weeks of sleep/energy tracking)

### System Integrity Criteria

- ✅ Daily Scope Rule adherence >95% (max 2 anchors/day violated <1 day/week)
- ✅ Evening guardrail honored (actual evening work >2.5h <2 weeks total)
- ✅ Replanning trigger not activated (portfolio allocation stayed within ±15%; capacity didn't drop >20%)

---

## 14) TRACEABILITY & SOURCE ARTIFACTS

**Primary sources used for this plan:**

- **March Monthly Review** (07_REVIEWS/02_MONTH/2026-03_March_Review.md): Execution facts, capacity baseline, system change decisions
- **March Human Reflection** (06_MONTHS/2026-03_March_Human.md): Advisory signals (sleep-energy, isolation risk, ambiguity pressure)
- **April Intelligence Transfer** (03_PLANNING/02_MONTH/2026-04_Intelligence_Transfer.md): Forward-looking planning context (what continues/changes/stops/enters)
- **Q1 Strategic Plan** (03_PLANNING/01_QUARTER/Q1_Review_Q2Planning.md): Quarter-level direction, allocation targets, strategic objectives
- **Monthly Intake Gate Checklist** (05_TEMPLATES/MONTHLY_PLAN_INTAKE_GATE_CHECKLIST.md): Verification that plan extracts findings correctly
- **TEMPLATE_Month_Final.md** (05_TEMPLATES/TEMPLATE_Month_Final.md): Planning structure + process gates
- **Phase 3 Readiness Framework** (Session Memory / PHASE_3_READINESS_CAPACITY_CONTROL): Evidence collection requirements + observation plan

**Intake gate status:** Pre-check passed (Intelligence Transfer exists); source citations present; advisory signals transformed to hypotheses (not hard rules); factory research explicitly decided (opportunistic only).

---

## PART B: APRIL EXECUTION GATES (Checkpoints During Month)

### Gate W14-Early: W14 Day 1-2 (April 1–2) — Blocker Viability Check

**Verify:**
- [ ] Signee board available + can begin stabilization testing?
- [ ] RobotOS board available + can begin hardware bringup?
- [ ] Blocker work sequencing viable as planned?
- [ ] Temporary rebalance conditions met (if Project Accountant activation intended)?

**Output:** Go/No-Go for blocker-first phase. If NO-GO → escalate immediately; replan W14 to default feature focus.

---

### Gate W14-End: End of Week 14 (April 5) — Blocker Progress + Conditional Activation

**Verify:**
- [ ] Signee blocker progress: On track? Core test results available?
- [ ] RobotOS blocker progress: Hardware bringup started? Basic functions testable?
- [ ] Zephyr: Stable in maintenance mode (no regressions)?
- [ ] Evening ambiguity: Stayed within bounds (<2.5h)? 
- [ ] Project Accountant scope locked tightly? (required for W15 activation)
- [ ] Delegation trial underway + showing promise?

**Output:** 
- If blocker progress strong + conditions met → Project Accountant conditionally activated W15
- If blocker progress weak OR conditions fail → revert to default allocation; Project Accountant not activated; focus on blocker completion

---

### Gate W15-Mid: Mid-Week 15 (April 10) — Blocker Closure + Rebalance Decision

**Verify:**
- [ ] Signee blocker: Complete or closing? Handoff guide ready for others?
- [ ] RobotOS blocker: Complete or nearly complete? Prototype team can take over?
- [ ] Project Accountant (if activated): Design scope locked? Delegation team engaged?
- [ ] 2-anchor rule held operationally (not just on paper)?
- [ ] No hidden 3rd/4th stream emerging?
- [ ] Capacity assumptions validated or flagged?

**Output:**
- Confirm blocker closure timeline
- Verify temporary rebalance revert ready for W16
- Escalate if Project Accountant scope expanding beyond W15 hard-stop

---

### Gate A: W15 Continue + Revert Planning (April 15)

**Verify:**
- [ ] Daily capacity assumptions holding? (3–4 blocks sustainable? Or different?)
- [ ] Blockers unblocked + handoff viable?
- [ ] Evening overcommit contained?
- [ ] 2-anchor rule working?
- [ ] Project Accountant W15 hard-stop decision made (closure or explicit continuance)?

**Output:** Go/No-Go for weeks 16–18. If NO-GO signals (capacity >20% off, blocker not closed, Project Accountant scope unclear) → replan weeks 15+ immediately.

---

### Gate B: Feature Freeze Enforcement (April 30)

**Verify:**
- [ ] Signee Feature Freeze: Is the lock real? Any last-minute scope creep?
- [ ] Quality gate: Are features at demo quality (P0/P1 exit) or are bugs being pushed to May?
- [ ] Administrative: Are features documented for May transition?

**Output:** Signee handed off cleanly to May phase or flagged for May replanning.

---

### Gate C: Month-End Evidence Checkpoint (April 30)

**Verify:**
- [ ] All 5 evidence sets collected (capacity, overload, ambiguity, fatigue, failure modes)?
- [ ] Assumptions validated or flagged for revision?
- [ ] Replanning triggers checked?
- [ ] Project Accountant formally ended (written confirmation)?

**Output:** Evidence packaged for May Monthly Review + Phase 3 calibration.

---

## PART C: WEEKLY BREAKDOWN (Seeds for Weekly Planning)

Each week flows from monthly missions. Weekly plans should NOT expand April scope.

### Week 14 (Apr 1–5): UNBLOCK PHASE — Board Stabilization

**Mission seed:** Prioritize blocker unblocking; stabilize board environments; enable downstream delegation.

**Signee blocker mission:** Test board environment + stabilization (PRIORITY). Deliverable: board test results, test protocol, handoff guide. Success = board stable; others can run demo without blocker returns.

**RobotOS blocker mission:** Verify hardware bringup + basic functions (PRIORITY). Deliverable: board test log, handoff guide for prototype team. Success = board boots consistently; downstream work unblocked.

**Zephyr focus:** Release branch maintained (no critical regressions).

**Evidence:** Blocker status + baseline capacity metrics.

**Gate:** End-of-week checkpoint: Blocker progress status? Handoff readiness? Project Accountant conditional activation viable?

---

### Week 15 (Apr 8–12): Continue Blockers + Enable Handoff + Accountant Design (Conditional)

**Mission seed:** Complete/close blocker missions; enable teams to take over; activate Project Accountant design work (only if blocker progress on-track + conditions met).

**Signee focus:** Finish blocker or continue if needed; validate handoff to others is viable; may begin feature acceleration if blocker done.

**RobotOS focus:** Complete hardware bringup blocker; validate prototype team can continue without bottleneck.

**Zephyr focus:** Maintenance mode continues.

**Project Accountant (CONDITIONAL):** Architecture design + delegation setup, **only if** blocker progress valid + scope locked tightly.

**Evidence:** Blocker closure status + capacity patterns.

**Gate A checkpoint (15/4, mid-month):** Go/No-Go for weeks 16–18. Verify: Blockers unblocked? Handoff ready? Temporary rebalance revert? Project Accountant scope hard-stopped W15 end?

---

### Week 16 (Apr 15–19): Full Delivery + Evidence Deepening

**Mission seed:** Continue momentum; collect failure mode examples + ambiguity data.  
**Signee focus:** Feature completion + early QA; identify failures.  
**RobotOS focus:** CNC demo app boots on board (target milestone).  
**Zephyr focus:** Release candidates flowing.  
**Evidence:** Collect 1–2 failure mode examples; track ambiguity conversions.

---

### Week 17 (Apr 22–26): Convergence + Final Push

**Mission seed:** Converge to Feature Freeze; validate completion.  
**Signee focus:** Final features + QA sweep; 30/4 prep.  
**RobotOS focus:** Demo sequence runs (integration goal).  
**Zephyr focus:** Release passes final smoke test.  
**Evidence:** Failure modes continue; fatigue/sleep correlation check.

---

### Week 18 (Apr 29–May 3): Feature Freeze + Evidence Wrap

**Mission seed:** Lock Signee scope; finalize April evidence.  
**Signee focus:** Feature Freeze (30/4) enforced; no new work.  
**RobotOS focus:** Prototype baseline validated; transition to May Phase 2.  
**Zephyr focus:** Release branch maintained.  
**Evidence:** Complete all 5 evidence sets; package for May review.

**Gate B checkpoint (30/4):** Feature Freeze verified.  
**Gate C checkpoint (30/4):** Evidence checkpoint; transition to May.

---

## Meta Notes

**On Balance:** This plan is set at the edge of available capacity. If even one assumption breaks badly (board doesn't arrive, Signee scope expands unexpectedly, key personal energy drops), April will need mid-month replanning. This is not a failure of planning; it is an honest assessment of carrying high delivery load while collecting validation data simultaneously.

**On Validation:** The Five Evidence Sets are non-optional. They serve May calibration + Phase 3 design. If April felt like "just deliver without measuring," the month will be less useful for system improvement.

**On Discipline:** The guardrails exist because they have been violated before (or nearly violated). Evening overcommit, hidden third anchors, system maintenance scope creep — all have signatures. April execution will show whether the March-designed mitigations actually hold.

---

**Created:** 2026-04-06  
**Status:** Ready for monthly review + weekly planning gate  
**Next step:** April Week 14 planning (drill down into weekly missions) + evidence collection begins

