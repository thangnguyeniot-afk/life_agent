# 2026-W14 — Weekly Plan (April UNBLOCK Phase — Week 1)

**Week:** April 6–11, 2026 (Monday–Saturday)
**Quarter Phase:** Q1 Phase 1 Continuation / April UNBLOCK Phase
**Status:** REPLANNED (updated 2026-04-07 noon — Project Accountant activated; evening capacity model refined)
**Theme:** UNBLOCK + DELEGATED FLOW — Blocker resolution + delegated support (Project Accountant now live)

---

## Table of Contents

- [W14 Replanning Summary](#w14-replanning-summary)
- [Weekly Context](#weekly-context)
- [Evening Capacity — HARD CONSTRAINT (Refined)](#evening-capacity--hard-constraint-refined)
- [Goals (Updated Priority & Status)](#goals-updated-priority--status)
- [Capacity & Constraints (Revised)](#capacity--constraints-revised)
- [Daily Anchor Map (Mon Apr 7 onward)](#daily-anchor-map-mon-apr-7-onward)
- [Gate: W14-End (Apr 10–11)](#gate-w14-end-apr-1011)
- [Definition of Done](#definition-of-done)

---

## W14 Replanning Summary

**Date:** 2026-04-07 noon  
**Trigger:** Gate W14-Early evaluation (Apr 6 EOD) cleared; Project Accountant now activated  
**Changes made:**

1. **Project Accountant ACTIVATED** — Starting Tue Apr 7 (immediate)
   - Scope: Single-flow CNC input architecture design (fixed scope, high clarity)
   - Residence: Pool B at planning level (NO office hours pre-allocated)
   - Execution: Daily morning delegation negotiation with Zephyr (if guardrail conditions met)
   - Evening: May execute in Pool B if needed (subject to serialization + Evening Check tracking; 1.5h caution benchmark)
   - Deliverable: Architecture doc + delegation setup by EOW

2. **Signee & RobotOS blocker work resumes** — Tue–Fri (continuation from Mon if board access interrupted)
   - Signee: Evening wrap-up/continuation focus; test results + protocol + handoff guide
   - RobotOS: Evening wrap-up/continuation focus; boot + basic functions + handoff guide

3. **Evening capacity model refined**
   - Now includes Project Accountant as Pool B resident (not office-allocated)
   - Serialization rule enforced: Only 1 project (Signee OR RobotOS OR Project Accountant) max per evening
   - Caution benchmark per evening: 1.5h (review signal; not a hard cap); concern is repeated 2h+ evenings as standard mode
   - Expected evening pattern: Light spillover Tue–Thu; possible planning Fri

4. **Zephyr role unchanged**
   - Office hours exclusive (08:00–09:15 KTLO baseline protected; remaining blocks available for support/delegation)
   - Smoke test target: Thu or Fri (moved from original "by Thu" to accommodate evening review)

5. **Rebalance trigger prep** — If any of these occur, immediate escalation:
   - >2 consecutive days Project Accountant borrows office time
   - >3 days/week Zephyr delegation occurs
   - Actual daily Zephyr available office time falls <3h
   - Weekly allocation divergence >15%

---

## Weekly Context

### Month Strategy Alignment

**April Mission:** Execute Signee demo feature path + RobotOS hardware bringup + Project Accountant single-flow architecture while validating capacity assumptions.

**W14 Evolution:** Started as UNBLOCK PHASE (blockers + Zephyr KTLO). Transitioned to UNBLOCK + DELEGATED SUPPORT (blockers + Project Accountant delegation active + Zephyr coordination).

**Projects in flight (W14):**
1. **Signee:** Board stabilization (BLOCKER) — evening/convenience access
2. **RobotOS:** Hardware bringup (BLOCKER) — evening/convenience access
3. **Zephyr:** CI health + smoke test (KTLO anchor) — office hours
4. **Project Accountant:** Single-flow CNC input architecture design (NEW) — Pool B + daily delegation negotiation

### Key Decision: Gate W14-Early (Apr 6, EOD)

✅ **PASSED** — All gate conditions met:
- Signee board available; testing can proceed
- RobotOS hardware available; bringup can proceed  
- Project Accountant scope locked (single-flow CNC input architecture)
- Zephyr stable in KTLO mode (non-disruptive)
- Delegation trial (Project Accountant) ready to initiate

**Action:** Project Accountant enters W14 execution starting Tue Apr 7 (noon replanning allows Mon baseline stabilization to complete first).

---

## Evening Capacity — HARD CONSTRAINT (Refined)

> **Model (unchanged):** Plan for 0h (office-hours-only focus) + Allow up to 1h controlled spillover + Caution benchmark at 1.5h (review signal; not a hard cap or violation threshold)
>
> **Serialization (NEW):** Only 1 project per evening: Signee OR RobotOS OR Project Accountant. Never 2+ blocker projects same night. Never Project Accountant + blocker same night.

### The Rule (Revised — 1.5h is caution, not violation)

| Threshold | Status | Action |
|---|---|---|
| **0h** | ✅ Target baseline | No planned evening work (all projects = office hours only) |
| **0–1h** | ✅ OK — Controlled spillover | Wrap-up / light continuation / planning only; **must log in Evening Check block** |
| **1–1.5h** | ⚠️ CAUTION | Heavy spillover; reduce next-day load proactively; log cause |
| **>1.5h** | ⚠️ REVIEW | Heavy evening; document cause; acceptable once-off but do NOT normalize; if 2h+ occurs on 2+ nights this week → flag at weekly review |

### Enforcement Rules (Updated)

1. **All main projects target office-hours-only:** Signee, RobotOS, Zephyr, Project Accountant → 0h planned evening.
2. **Evening = controlled spillover buffer.** Allows natural wrap-up, continuation, or light planning. NOT a second shift. NOT a capacity reserve presumed executable.
3. **Project Accountant evening work:** ~~If design work spills past 17:30 → defer to next morning.~~ **EXCEPTION: May execute in Pool B evening IF that day has no Signee/RobotOS evening work AND is within 1h wrap-up limit AND is tracked in Evening Check. Treat 1.5h as caution benchmark; if >1.5h occurs, document cause at weekly review.**
4. **Blocker serialization rule (if board requires evening access):**
   - Only ONE blocker project allowed per evening (Signee OR RobotOS, not both)
   - The other blocker shifts to next office day
   - **NEW:** Also respect Project Accountant serialization — no blocker + Project Accountant same evening
   - Priority if conflict: RobotOS > Project Accountant > Signee (hardware access more constrained than design work)
5. **Max 1 task in any evening slot.** No dual-task stacking. No multi-project stacking.
6. **All evening work must be tracked.** If evening work occurs, it MUST be recorded in Evening Check block. Untracked evening = system violation.

### Serialization Priority (Conflict Resolution)

If multiple projects want evening access on the same night, priority order:
1. **RobotOS** (hardware-dependent; cannot be deferred without cascading to next day)
2. **Signee** (board-dependent but slightly more flexible timing)
3. **Project Accountant** (design-based; can shift to Pool B or office delegation next day)

Example: If both RobotOS and Project Accountant want evening Tue → RobotOS takes it; Project Accountant defers to Wed evening or Wed morning delegation from Zephyr.

### Evening Usage Types (Unchanged)

**Allowed:**
- **Wrap-up:** Finishing an incomplete block started in office hours (e.g., final 15 min to close a task)
- **Continuation:** Returning to same task (no new context switch)
- **Light planning:** Reflective noting, no design or problem-solving

**NOT Allowed:**
- Starting new high-ambiguity work
- Multi-project stacking
- Work initiated in evening (must originate in office hours)

### Daily Evening Pre-Check (Morning Setup)

Add to morning setup: *"Is there evening work planned today? If yes → is it ≤1h wrap-up / continuation only? AND is it the only task? AND is there no other blocker/Project Accountant evening same day? If not → move to morning."*

---

## Goals (Updated Priority & Status)

### Goal 1 (PRIMARY — PRIORITY 1): Signee Board Stabilization Blocker

**Project:** Signee | **Pool:** Non-office (evening primary; office-hours if board unavailable evening) | **Effort:** ~6–8h (spread evenings Mon–Fri, spillover into office only as needed) | **Status:** IN PROGRESS (Mon test phase underway) | **Criticality:** BLOCKER

**Mission scope:**
- ✅ Test board environment stability (started Mon; continue if needed)
- Test protocol draft (target: Tue–Wed evening if troubleshooting needed; Thu if stable)
- Handoff guide (target: Fri planning evening)
- Document test results + any failure modes

**Execution model:** Default to evening wrap-up/continuation if board inaccessible during office. If board available office, prioritize there. NEVER run parallel blocker work (Signee + RobotOS same evening).

**Success criterion:** Board stable; test protocol written; handoff guide complete; others can run demo independently.

**EOW checkpoint:** Test results + protocol available for handoff review Fri evening or Sat morning.

---

### Goal 2 (PRIMARY — PRIORITY 2): RobotOS Hardware Bringup Blocker

**Project:** RobotOS | **Pool:** Non-office (evening primary; office-hours if hardware unavailable evening) | **Effort:** ~4–6h (spread evenings Mon–Fri, spillover into office only as needed) | **Status:** IN PROGRESS (Mon bringup phase underway) | **Criticality:** BLOCKER

**Mission scope:**
- ✅ Hardware board boots (started Mon; verify consistency Tue–Wed if needed)
- Basic functions testable (target: Wed–Thu evening if bringup stable; earlier if unblocked Mon)
- Handoff guide for prototype team (target: Fri evening)
- Document boot sequence + any known issues

**Execution model:** Default to evening wrap-up/continuation if hardware unavailable evening. If hardware available office, prioritize there. NEVER run parallel blocker work (RobotOS + Signee same evening).

**Success criterion:** Board boots consistently; basic functions testable; handoff guide complete; prototype team unblocked.

**EOW checkpoint:** Boot confirmation + basic function test + handoff guide ready Fri or Sat.

---

### Goal 3 (SECONDARY): Zephyr KTLO Maintenance

**Project:** Zephyr | **Pool:** Office hours (exclusive, Pool A anchor) | **Allocation:** Maintains office-hour base (blocker missions don't reduce Zephyr office allocation) | **Effort:** ~1.5–2.5h/week | **Status:** ACTIVE | **Criticality:** KTLO

**Mission scope:**
- Daily CI health check (~15–20 min/day, 08:00–09:15 baseline)
- Smoke test weekly (target: Thu or Fri, ≥1x EOW)
- Triage any P0/P1 if opened (same-day response, within office hours)
- Support Project Accountant with daily delegation (if guardrails met)

**Evening:** NEVER. Zephyr is office-hours-only by definition.

**Success criterion:** CI green end-of-week; no P0/P1 bugs open; smoke test passed; delegation model working.

---

### Goal 4 (NOW ACTIVE — PRIORITY 3): Project Accountant Single-Flow CNC Input Architecture

**Project:** Project Accountant | **Pool:** Pool B at planning level (NO office hours pre-allocated); execution: daily delegation from Zephyr + Pool B time | **Status:** ACTIVATED (starting Tue Apr 7) | **Criticality:** ALIGNMENT — unblocks downstream engineer on-boarding + demo prep

**Mission scope:**
- Single-flow CNC input architecture design (scope: fixed, high clarity — input → command pipeline)
- Architecture doc (target: draft Wed–Thu; final Fri EOD)
- Delegation setup (learning daily approval workflow; target: 2–3 successful delegations by Fri)
- Handoff ready for Q2 setup

**Execution model:** 
- **Morning negotiation:** Each morning (Tue–Fri), check Zephyr guardrail conditions; if met, request 1 block time for architecture work (typically 09:30–12:00 or 14:00–17:00 range)
- **Evening backup:** If morning delegation not available that day, may execute up to 1h in Pool B evening (if no Signee/RobotOS evening work; must track in Evening Check)
- **Expected rhythm:** Likely 3–4 successful delegations Tue–Fri + 0–1 evening blocks if delegation stressed

**Success criterion:** Architecture doc complete; delegation model validated; prototype team can use handoff doc to continue.

**EOW checkpoint:** Architecture doc ready for review Fri; delegation pattern clear for W15 rebalance.

---

## Capacity & Constraints (Revised)

**KEY PRINCIPLE:** Dual-pool capacity model (locked). Zephyr OWNS office hours as exclusive stable anchor. Signee + RobotOS + Project Accountant execute in non-office time (Pool B) or via daily delegation negotiation.

### Pool A — Office Hours (Mon–Fri, ~36h effective)

**Zephyr exclusive anchor:**
- Daily KTLO allocation: ~30–45 min/day (08:00–09:15 baseline; CI health + smoke test + P0/P1 triage if needed) = ~2.5–3.75h/week baseline
- Remaining office capacity: Available for Project Accountant delegation (if guardrails met) OR Zephyr support work
- Model: Zephyr is ALWAYS office-hours based
- Project Accountant negotiation: May request daily delegation for office time via morning guardrail check (NOT pre-allocated)

| Time Block | Owner | Notes |
|---|---|---|
| **Daily 08:00–09:15** | Zephyr KTLO | CI health check + smoke test + P0/P1 triage (untouchable) |
| **Daily 09:15–17:30** | Zephyr primary | Available for Project Accountant delegation (if guardrails met) OR support/overflow |
| **Buffer allocation** | Dynamic | Unplanned interrupts, context switches |

### Pool B — Non-Office Time (Evenings/Weekends, Blocker Missions + Project Accountant)

**Signee + RobotOS + Project Accountant shared (SERIALIZED):**
- Planned pool: 0h (all work should occur in office hours if possible)
- Controlled spillover: Max 1h/night (wrap-up / continuation only)
- Caution boundary per night: 1.5h (review signal; not a hard violation threshold)
- Serialization rule: ONLY 1 project per evening (Signee OR RobotOS OR Project Accountant, never 2+)
- Priority if conflict: RobotOS > Signee > Project Accountant

| Day | Primary Blocker (Evening) | Project Accountant (Evening) | Hard Ceiling | Notes |
|---|---|---|---|---|
| **Mon Apr 6** | Signee/RobotOS (Mon work complete) | 0h | 0h | Gate eval day; no evening work |
| **Tue Apr 7** | Signee wrap-up (if needed) | 0h (delegation focus) | Caution: 1.5h | Project Accountant activated; negotiates morning delegation |
| **Wed Apr 8** | Signee wrap-up (if needed) | 0h (delegation focus) | Caution: 1.5h | Mid-week blocker checkpoint |
| **Thu Apr 9** | RobotOS wrap-up (if needed) | 0h (delegation focus) | Caution: 1.5h | Energy mid-point; serialized if blocker active |
| **Fri Apr 10** | Signee planning (if needed) | 0h (delegation focus) | Caution: 1.5h | Gate W14-End prep; final blocker evidence |
| **Sat Apr 11** | 0h | 0h | 0h | Rest; optional W15 seed only |

**Total planned Pool B evening: 0h (all 0h planned; actual may include minimal spillover if wrap-up needed). Controlled spillover Pool B: up to 1h/night if needed (one project only, serialized). Caution benchmark: 1.5h/night (review signal; not violation threshold). All Pool B evening work tracked in Evening Check.**

### Capacity Validation (CAPACITY_ENGINE Checks — Updated)

| Check | Status | Note |
|---|---|---|
| **V1: Pool A (Office)** | ✅ | Zephyr KTLO owns 08:00–09:15 baseline (protected). Remaining blocks available for Project Accountant delegation. Signee/RobotOS blocker missions in Pool B (evening), not office. |
| **V2: Pool B baseline** | ✅ | Signee + RobotOS + Project Accountant: 0h planned; ≤1h controlled spillover/night (one project only, serialized); 1.5h caution benchmark; all tracked in Evening Check. |
| **V3: Project Accountant domain (NEW)** | ✅ | Pool B residence at planning level (NOT pre-allocated office hours); executes via daily delegation (if guardrails met) OR Pool B evening (if no other project that night). Delegation approval criteria: (1) KTLO floor protected, (2) no P0/P1 open, (3) support work scheduled, (4) sufficient available time. |
| **V4: Blocker + Project Accountant serialization (NEW)** | ✅ | Only 1 project per evening (Signee OR RobotOS OR Project Accountant, never 2+ stacked). Priority: RobotOS > Signee > Project Accountant. No parallel stacking. 1.5h caution benchmark (not hard cap). |
| **V5: Work-domain independence** | ✅ | Allocation context (effort %, scope) and time domain (office vs evening) are separate axes. Time-domain rule (0h planned, ≤1h spillover, 1.5h cap, serialization) applies regardless of project. |
| **V6: Ambiguity** | ✅ | High-ambiguity work (Project Accountant design, Signee troubleshooting) prioritized in AM office blocks (peak energy). Evening = wrap-up/continuation only (low ambiguity). |
| **V7: Weekend** | ✅ | Sat: optional planning only (≤1h Pool A); Sun: rest; zero evening work either day. |

### Execution Flexibility (Daily Level Only — Unchanged)

**Planning-level model:** Dual-pool (Zephyr = office exclusive; Signee/RobotOS/Project Accountant = Pool B + delegation).

**Execution-level flexibility:** At daily planning level, projects may negotiate within constraints:

- **Project Accountant execution (if activated):**
  - Primary: Daily morning delegation request from Zephyr (subject to guardrails)
  - Backup: Execute up to 1h in Pool B evening if: (1) no other project evening that day, (2) within 1h wrap-up limit, (3) tracked in Evening Check, (4) <1.5h hard cap
  - Constraint: Never +2 consecutive delegation days or >3 days/week
  
- **Signee/RobotOS execution options:**
  - Primary: Execute in evenings (Pool B, serialized)
  - Flexibility: May use office hours if board/hardware available during office (if not conflicting with Zephyr)
  - Constraint: NEVER overrides Zephyr KTLO baseline

**Key principle:** Execution-level borrowing (delegation) is dynamic, negotiated daily, and subject to early-warning escalation triggers.

**Delegation Approval Criteria (Zephyr):** Approve Project Accountant delegation only if ALL conditions hold:
1. Daily KTLO baseline (08:00–09:15) remains untouched and fully protected
2. No active P0/P1 issues require immediate Zephyr response
3. Daily CI health check, smoke test (if scheduled), and release support work already scheduled/protected  
4. Remaining available office time after delegation is sufficient for unplanned support work (target: ≥3h/day)

**Early-Warning Escalation Triggers (NEW — Must escalate immediately if ANY occur):**
- Project Accountant borrows Zephyr office time on >2 consecutive days  
- Zephyr delegation occurs on >3 days in a single week
- Actual Zephyr office time (outside KTLO floor) falls below ~3h/day on any single day
- Weekly allocation divergence exceeds 15%

**Enforcement:** Daily Evening Check + morning delegation tracking. Weekly review compares planned vs. actual. If any trigger fires, escalate for immediate replanning (is the plan wrong? Is execution creeping?). Do not silently absorb drift.

---

## Daily Anchor Map (Mon Apr 7 onward)

| Day | Pool A (Office) Primary Anchor | Pool B (Evening) Optional | Evening Cap | Notes |
|---|---|---|---|---|
| **Mon Apr 6** | Zephyr gate eval (30 min review) | None | 0h | [Historical; Gate PASSED] |
| **Tue Apr 7** | Zephyr CI check + Project Accountant delegation negotiation | Signee wrap-up only (if needed) | 1.5h | Project Accountant enters; requests morning block if possible |
| **Wed Apr 8** | Zephyr CI check + Project Accountant delegation negotiation | Signee wrap-up only (if needed) | 1.5h | Mid-week blocker checkpoint; Project Accountant continues |
| **Thu Apr 9** | Zephyr CI health + possible smoke test | RobotOS wrap-up only (if needed) | 1.5h | Energy mid-point; blocker serialization (RobotOS priority if conflict) |
| **Fri Apr 10** | Zephyr smoke test (if not done Thu) | Signee closure planning (if needed) | 1.5h | Gate W14-End prep; final blocker evidence capture |
| **Sat Apr 11** | Optional: W15 seed (≤1h planning) | None | 0h | Rest-first; non-delivery day |

**Pool A anchor:** Zephyr KTLO in 08:00–09:15 (protected); remaining blocks available for Project Accountant delegation or support  
**Pool B anchor:** Blocker spillover ONLY if board/hardware inaccessible during office + <1h + serialized (one project/evening) + hard cap 1.5h  
**Expected energy mode:** HIGH Tue–Wed (Project Accountant fresh start + momentum), NORMAL–HIGH Thu (blocker wind-down), NORMAL Fri (closure sprint)  
**Negotiation checkpoint:** Each morning Tue–Fri, morning setup includes: "Does Project Accountant need office delegation today? (Check guardrails → Signee/RobotOS evening status + Zephyr available time)"

---

## Gate: W14-End (Apr 10–11)

**Verify by EOD Friday Apr 10:**

- [ ] Signee blocker: Test results documented? Test protocol written? Handoff guide ready?
- [ ] RobotOS blocker: Board boots confirmed? Basic functions testable? Handoff guide ready?
- [ ] Zephyr: CI green? Smoke test passed? No P0/P1? KTLO baseline protected?
- [ ] Project Accountant: Architecture doc drafted? Scope locked? Delegation model validated (2+ successful delegations)?
- [ ] Evening check: Any days >1.5h? Log cause. If 2h+ occurred on 2+ nights → flag for W15 planning.
- [ ] Serialization check: No parallel evening work (Signee + RobotOS same night, or blocker + Project Accountant same night)?
- [ ] Capacity inference: Weekly allocation tracking shows pattern emerging? (+/- 10% drift acceptable?)
- [ ] W15 Go/No-Go: Blocker progress strong? Handoff docs sufficient for W15 closure? Project Accountant delegation rhythm sustainable?

**Output:** W15 Weekly Plan seed + rebalance evaluation (continue dual-pool + Project Accountant? Or adjust?).

---

## Definition of Done (W14)

| Item | DoD |
|---|---|
| **Signee blocker** | Board test results documented; test protocol written; handoff guide (others can run demo independently) |
| **RobotOS blocker** | Board boots consistently; basic functions testable; handoff guide (prototype team can continue) |
| **Zephyr KTLO** | CI green end-of-week; smoke test passed (≥1x by Fri); no P0/P1 opened; 08:00–09:15 baseline protected all week |
| **Project Accountant (NEW)** | Architecture doc drafted (design choices + trade-offs documented); scope locked; delegation model tested (≥2 successful delegations) |
| **Evening compliance** | All spillover logged with cause; no 2h+ evenings recurring on 2+ nights; serialization rule enforced (no parallel evenings); tracking complete |
| **Capacity tracking** | Daily block counts noted; morning delegation approvals tracked; evening log complete; weekly divergence <15% |
| **Gate W14-End** | All gate items verified; W15 seed ready; rebalance decision documented |

---

**Replanned:** 2026-04-07 noon  
**Status:** ACTIVE — execution Tue Apr 7 onward (Mon Apr 6 baseline baseline established; gate cleared)  
**Source:** Gate W14-Early passed (Apr 6 EOD); Project Accountant activation decision + evening capacity model refinement (Apr 7 noon)  
**Next:** 2026-W15_WeekPlan.md (to be created EOW Apr 10–11)
