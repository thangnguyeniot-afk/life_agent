# MONTH PLAN & REVIEW – 2026-03 (March)

> **Instance file** aligned to TEMPLATE_Month_Final.md and 2026-Q1 quarter direction.
> **Month role:** Setup & Scope Freeze (Month 1 of Q1: prepare for delivery phases)

---

## Table of Contents

**PART A: MONTHLY PLANNING**
- [1) Định hướng tháng này](#1-định-hướng-tháng-này)
- [2) Core Outcomes của tháng (tối đa 3)](#2-core-outcomes-của-tháng-tối-đa-3)
- [3) Capacity & Rhythm](#3-capacity--rhythm)
- [3.1) Monthly Planning Protection Rules](#31-monthly-planning-protection-rules)
- [4) Weekly Intent (Month-level direction)](#4-weekly-intent-month-level-direction)
- [4.1) Monthly Scope Trade-off](#41-monthly-scope-trade-off)
- [5) Risk / Assumption / Decisions](#5-risk--assumption--decisions)
- [6) Reading budget](#6-reading-budget)

**PART B: MONTHLY REVIEW**
- [0) DoD for Monthly Review](#0-dod-for-monthly-review)
- [1) Executive Summary of the Month](#1-executive-summary-of-the-month)
- [2) Output & Outcome Review](#2-output--outcome-review)
- [2.1) Monthly Drift Check](#21-monthly-drift-check)
- [3) System Change Review](#3-system-change-review)
- [3.1) Portfolio Balance Check](#31-portfolio-balance-check)
- [4) Life Anchors — Monthly Trend](#4-life-anchors--monthly-trend)
- [5) Anti-Anchors — Monthly Pattern](#5-anti-anchors--monthly-pattern)
- [6) Focus Adjustment for Next Month](#6-focus-adjustment-for-next-month)
- [7) Context Compression](#7-context-compression)
- [Appendix (Optional)](#appendix-optional)

---

# PART A: MONTHLY PLANNING

---

## 1) Định hướng tháng này

**Theme:** Setup & Freeze Scope — tháng này chốt những gì sẽ delivery tháng 4–5, không mở việc mới.

**North Star:** 
By 31/3, all projects have scope frozen v1 (Signee demo criteria locked, RobotOS prototype scope locked, Zephyr release criteria clear). All boards running basic flow with runbooks.

**Stop doing this month:**
- No new features if scope not yet frozen
- No jumping between 3–4 hard tasks per day (prevent priority distortion)
- No XL task execution without breaking into phases first

---

## 2) Core Outcomes của tháng (tối đa 3)

> Outcome = measurable result, not task list. Each must have artifact.

### Outcome Map

| # | Outcome | Project | Deadline | Artifact |
|---|---|---|---|---|
| O1 | Signee Demo Scope Freeze v1 (internal) | Signee | 2026-03-14 | RFC_DemoScope_v1.md |
| O2 | Board basic flow stable + RobotOS Middleware/STM32F4 bringup | RobotOS | 2026-03-28 | RUNBOOK_BasicFlow.md + LOG_Bringup.md |
| O3 | Frontend skeleton + 1 flow (PWA ready) | Signee | 2026-03-31 | ADR_UI_Architecture.md + commit |

---

**Outcome #1: Signee Demo Scope Freeze v1**

- **Why:** Prevent scope creep → unblock April delivery
- **Success signal / DoD:**
  - Feature list (MUST + OUT-OF-SCOPE) locked and documented
  - Demo acceptance criteria defined for each feature
  - Read after 10 min: still understand what demo includes
  - Artifact: `RFC_Signee_DemoScope_v1.md` (signed off)
- **Owner:** You

---

**Outcome #2: Board Basic Flow Stable + RobotOS Middleware & STM32F4 Bringup**

- **Why:** Unblock Q1 roadmap (v0.1 Alpha deadline 2026-04-30)
- **Success signal / DoD:**
  - Both boards run basic flow repeatable ≥3 times (same conditions)
  - Logs captured: error + root cause + fix + rerun condition
  - Runbook 1-page exists (setup + rerun fast)
  - Test cases defined + quality gate clear (for dev in week 4)
  - RobotOS: Zephyr workspace setup done (west init/update, build OK on STM32F4)
  - RobotOS: Middleware core skeleton started (pub/sub interface + memory pool link OK)
  - RobotOS: STM32F4 bringup minimal (build + flash + hello world runs)
  - Artifact: `LOG_Board_Bringup_Mar.md` + `RUNBOOK_BasicFlow_1page.md` + `LOG_RobotOS_Bringup_Mar.md`
- **Owner:** You

---

**Outcome #3: Frontend Skeleton + 1 Flow (PWA Ready)**

- **Why:** Unblock demo flows April; finalize UI architecture before large effort
- **Success signal / DoD:**
  - Skeleton app runs (routing/navigation baseline)
  - 1 flow end-to-end working (mock data OK)
  - UI architecture ADR done (prevents rewrite later)
  - Artifact: `ADR_UI_Architecture.md` + code commit(s)
- **Owner:** You

---

## 3) Capacity & Rhythm

- **WIP max (concurrent):** 2–3 big things / week
- **Capacity budget (%):**
  - Signee scope/demo: 35%
  - RobotOS middleware + bringup: 30%
  - Zephyr KTLO (work): 15%
  - Buffer (breakage, emergency ≤48h): 20%
- **Deep blocks/day:** 2 blocks (90 min each)
- **Office hours (if applicable):** Tue/Thu 16:00–16:30 + Sat 10:00–10:30

---

## 3.1) Monthly Planning Protection Rules

**Scope Trade-off Rule:** If March gains new major work → existing outcome scope must shrink.

**Drift Check Rule:** If actual capacity strays >15% from 35/30/15/20 budget for >1 week → rebalance immediately.

**Anti-Wish-List Rule:** Only 3 outcomes max. If 4th seems "strategic" → defer to Q2.

---

## 4) Weekly Intent (Month-level direction)

> Not detailed weekly scheduling — just the theme/direction for each week to prevent scope creep.

**Week 1 (2026-W09): Setup + Framing**
- Signee: draft demo scope v0, test on new board
- RobotOS: Zephyr setup, STM32F4 hello world
- Zephyr: maintain stability
- Anti-goal: don't open new features

**Week 2 (2026-W10): Freeze v1 + First Loop**
- Signee: internal scope freeze v1
- RobotOS: basic flow run 2–3 times, log conditions
- Zephyr: stable on mainline
- Anti-goal: no scope creep

**Week 3 (2026-W11): Stabilize + QA Strategy**
- Signee: board stabilize top 3 blockers → runbook
- RobotOS: Middleware core skeleton (pub/sub compile/link OK)
- Zephyr: maintain CI green
- Anti-goal: no context switching

**Week 4 (2026-W12): All Apps Running + April Readiness**
- Signee: Outcome #3 done, PWA test on mobile
- RobotOS: STM32F4 bringup final confirm
- Zephyr: no P0 bugs
- Anti-goal: no new scope, close debt

---

## 4.1) Monthly Scope Trade-off

| Added Priority | Trade-off Action | What Traded Off | Reason |
|---|---|---|---|
| (none expected) | N/A | N/A | Month is scope-locked from quarter direction |

---

## 5) Risk / Assumption / Decisions

### Top strategic risks (3)

| Risk | Impact | Mitigation |
|---|---|---|
| Scope creep (demo scope not "signed off") | Outcome #1 miss, delay April | Feature freeze rule + weekly drift check |
| Board instability (basic flow can't repeat) | Outcome #2 miss, delay v0.1 | Early bringup weeks 1–2 + runbook discipline |
| Priority distortion (emergency breaks deep blocks) | Artifact loss, rework in April | Buffer 20%, escalate >4h emergency items to weekly review |

### Assumptions

- Board hardware ready for testing in March
- Demo scope v1 can be frozen internally (doesn't need to be perfect)
- RobotOS month 1 is scope freeze + Middleware skeleton + STM32F4 bringup only (no module expansion)
- Capacity assumptions from quarterly plan hold: 3–4 blocks/day sustainable

### Decisions needed (early)

| Decision | Required by | Owner |
|---|---|---|
| "Basic flow" formal definition | 2026-03-02 | You |
| Signee demo MUST list (top 10) v0 | 2026-03-03 | You |
| UI architecture choice (routing/state) | 2026-03-10 | You |

---

## 6) Reading budget

- **Quarter direction:** `03_PLANNING/01_QUARTER/Q1_Review_Q2Planning.md` (Part A)
- **Weekly plans:** `03_PLANNING/03_WEEK/2026-W09.md` through `2026-W12.md`
- **Logs:** `04_LOGS/Decision_Log.md`, `04_LOGS/Spike_Log.md`
- **Templates:** `05_TEMPLATES/TEMPLATE_Month_Final.md`, `05_TEMPLATES/TEMPLATE_Week_Final.md`

---

# PART B: MONTHLY REVIEW

---

## 0) DoD for Monthly Review

Monthly Review is **COMPLETE** when:

- [ ] Clear view of the month's direction and trajectory
- [ ] All System Changes evaluated (keep/adjust/rollback)
- [ ] Next month's focus narrowed to 1–2 clear priorities
- [ ] Capacity truth captured (what assumptions held, what broke)
- [ ] Carry forward / stop / reframe is actionable for April

---

## 1) Executive Summary of the Month

**Month narrative (1–3 sentences):** 
…

**Overall state:** [ ] Up (exceeded intent) | [ ] Flat (as planned) | [ ] Down (underperformed) | [ ] Pivoted (intentional change)

**Energy trend:** …

**One sentence summary:** …

---

## 2) Output & Outcome Review

### Completed Outputs
- Outcome #1 (Signee Demo Scope Freeze): …
- Outcome #2 (Board Basic Flow + RobotOS Bringup): …
- Outcome #3 (Frontend Skeleton): …

### What Created the Most Value?
…

### What Consumed Effort Without Proportional Value?
…

---

## 2.1) Monthly Drift Check

**Did the month stay aligned with quarterly intent?**
- [ ] Yes, mostly aligned | [ ] Partially aligned | [ ] Significantly drifted

**Did one project stream dominate unexpectedly?**
- [ ] No, allocation stayed balanced | [ ] Slightly off-balance | [ ] One stream overran others (which?)

**What capacity assumptions broke?**
…

---

## 3) System Change Review

Did any process/rule changes happen this month? How effective?

| System Change | Purpose | Result (Effective/Partial/Ineffective) | Decision (Keep/Adjust/Rollback) |
|---|---|---|---|
| … | … | … | … |

**Rule:** Each System Change must conclude this month; don't defer evaluation.

---

## 3.1) Portfolio Balance Check

| Domain | Planned % | Actual % | Status | Notes |
|---|---|---|---|---|
| Signee scope/demo | 35% | …% | OK / Drift | … |
| RobotOS dev | 30% | …% | OK / Drift | … |
| Zephyr KTLO | 15% | …% | OK / Drift | … |
| Buffer | 20% | …% | OK / Drift | … |

---

## 4) Life Anchors — Monthly Trend

| Anchor | Trend (⬆️/➖/⬇️) | Notes |
|---|---|---|
| Movement (exercise) | | |
| House Basics (sleep, eat) | | |
| Focus Flow | | |
| Recovery | | |
| Connection | | |

---

## 5) Anti-Anchors — Monthly Pattern

**Destructive pattern that appeared?**
…

**Did any anti-anchor become "new normal"?**
…

**What needs blocking early next month?**
…

---

## 6) Focus Adjustment for Next Month

### Primary focus for April (1–2)
1. …
2. …

### What to reduce / stop / avoid
- …
- …

### System Changes planned for April
- …

---

## 7) Context Compression

**Snapshot created?** (Yes/No): …

**Snapshot location:** `06_MONTHS/2026-03_End_of_March.md` (optional)

---

## Appendix (Optional)

**Important artifacts generated:**
- Commit links
- ADR/RFC links
- Jira/GitHub board snapshots
- Decision log entries
- Spike log entries