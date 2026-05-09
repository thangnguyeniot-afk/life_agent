# Decision Memo — 2026-05 Life Agent Restructure

---

## 1. Status

| Field | Value |
|---|---|
| **Status** | ACTIVE |
| **Created** | 2026-05-09 (W18, LA-R1 Patch 1) |
| **Phase boundary** | This memo is **not Phase 4**. It records stabilization inputs that may feed a Phase 4 design after the May 15 checkpoint. Phase 4 must not be opened until that checkpoint clears. |
| **Owner** | User (final decisions). GPT (audit/framing). Copilot/Claude (implementation support). |
| **Repo anchor** | LA-R1 — Life Agent Bottleneck / Restructure Stabilization |
| **Related** | `03_PLANNING/02_MONTH/2026-05_May_Plan.md` · `03_PLANNING/03_WEEK/W18/2026-W18_WeekPlan.md` · `08_PROJECT_CONTEXT/Signee_CONTEXT.md §2026 Year-End Outlook` · `01_OS/AGENT_OPERATING_MODEL.md` · `01_OS/04_OPERATIONS/WEEKLY_CONTROL/CAPACITY_ENGINE.md §10` |

---

## 2. Why Now

The Life Agent AI working triangle (User / GPT / Copilot / Claude / GLM) has reached high operational productivity. W18 is the first week with TickTick auto-sync applied, multi-agent governance active, and the Weak-Health Mode firing live in production.

The problem is not output. The problem is load distribution and sustainability:

- The user is the resolution point for scope locking, progress collection, PEC generation, cross-project coordination, business decisions, and delegation calls — simultaneously.
- High AI productivity multiplies this bottleneck rather than absorbing it.
- Physical health is explicitly weaker than baseline (W18 Execution file: Wed 2026-05-06 Weak-Health candidate triggered; Sleep ~5h30m, Energy medium-low). Health is a P0 operating constraint per `CAPACITY_ENGINE.md §10`.
- The May–June window is also when significant business restructuring work lands (company establishment, SECC contract, year-end forecast, delegation to Anh Khương).
- No single document currently holds the cross-project restructuring workstream. It leaks across the Signee project context, the May plan delegation rule, weekly planning, and informal conversation.

**This memo is the canonical Life Agent home for that workstream.** Signee-specific signals stay in `08_PROJECT_CONTEXT/Signee_CONTEXT.md`. Cross-project restructure decisions live here.

---

## 3. Current Absorption Inventory

What the user currently performs that routes through them as a bottleneck:

| Category | Current Handling | Classification | Reduction Path |
|---|---|---|---|
| **Scope locking** | User decision per weekly gate | `INTENTIONAL_USER_GATE` | Keep — strategic |
| **Progress collection** | INTEGRATE_DAILY (10-step procedure, manual run) | `OVERHEAD_CANDIDATE` | Wrap as single `close day` command |
| **Cross-project priority synthesis** | WeekPlan §Priority Stack, user-written | `INTENTIONAL_USER_GATE` | Keep — multi-project tradeoffs require judgment |
| **Task admission / ambiguity** | §7.5 gate (3-question filter) | `INTENTIONAL_USER_GATE` | Keep — quality gate |
| **PEC generation** | Manual: fill prompt → run agent → save → validate → commit | `OVERHEAD_CANDIDATE` | Promote to `generate pec {week}` automation command |
| **TickTick dry-run/apply decision** | Manual CLI steps after PEC commit | `INTENTIONAL_USER_GATE` (decision) / `OVERHEAD_CANDIDATE` (mechanics) | Keep decision gate; wrap 3-step CLI into one command |
| **Schedule overlap detection** | Manual repair after PEC export | `ELIMINATED` | Patch 4A complete: `validate_pec.py` now errors on overlap |
| **Calendar coordination (cancel quirks)** | Manual `smoke_ticktick_task.py --delete-only` | `OVERHEAD_CANDIDATE` | Patch 4B: exporter tolerates HTTP 200/empty-body cancel |
| **Health/load reporting** | Self-report in TEMPLATE_Daily Health Telemetry | `INTENTIONAL_USER_GATE` | Keep — self-report is the input |
| **Delegation decisions** | Per-project delegation rule in May Plan §5, W18 plan §5 | `INTENTIONAL_USER_GATE` | Keep decision; template the first-contact protocol |
| **Agent routing** | AGENT_OPERATING_MODEL.md routing table | `DOCUMENTATION_GAP` | Patch 5: eliminate legacy "Agent 1/2" prose |
| **Business/contract direction** | Scattered in Signee_CONTEXT + informal | `OVERHEAD_CANDIDATE` | This memo: one canonical home |
| **Technical architecture direction** | User + GPT synthesis | `INTENTIONAL_USER_GATE` | Keep |
| **Customer-facing commitments** | User only | `INTENTIONAL_USER_GATE` | Keep — cannot delegate |
| **Retrospective / evidence filing** | WEEK_CLOSEOUT (manual, ~10 steps) | `OVERHEAD_CANDIDATE` | Patches 2/3: add health summary + bottleneck question rows |
| **Recovery discipline** | Weak-Health Mode (CAPACITY_ENGINE §10); user applies | `INTENTIONAL_USER_GATE` | Keep decisions; system signals are already live |

**Net reading:** Roughly 6 of 15 bottleneck categories are overhead candidates. None of the intentional user gates should be dissolved. The reduction path is template, command, and documentation — not new policy.

---

## 4. Workstream Boundaries

### User keeps (non-delegatable)

- Final strategic decisions and priority rankings
- Final tradeoffs between projects (RobotOS vs Signee vs Zephyr)
- Contract and business commitments (SECC, Gương thần, year-end)
- Quality bar and delivery acceptance
- Final scope locks (🟢/🟡/🔴 decisions per §7.5)
- Recovery discipline decisions (override authority per CAPACITY_ENGINE §10 WH-8)
- Compensation decisions
- Final delegation decisions

### Delegate / template / automate (approved path)

- Progress collection → `close day` command (Copilot / INTEGRATE_DAILY wrapper)
- First-draft task decomposition → Copilot / Claude from approved intent
- Bounded repo patches → Copilot (narrow) or GLM (contracted, per AGENT_OPERATING_MODEL §6)
- Routine PEC generation → `generate pec {week}` command (Claude/Copilot reads WeekPlan, produces JSON)
- Schedule overlap detection → `validate_pec.py` (Patch 4A complete)
- Weekly evidence aggregation → lightweight helper + WEEK_CLOSEOUT row (Patches 2/3)
- Bounded implementation tasks → GLM under explicit contract (AGENT_OPERATING_MODEL §6–7)
- First-pass cost/accounting collection → structured template (not legal advice)
- Agent routing clarity → DOC-SYNC Patch 5

### Do not automate yet

- TickTick → repo completion sync (no source-of-truth policy for this yet; `tools/README.md` explicitly states Life Agent plans take precedence)
- Auto-apply on validate-pass (bypasses the human confirmation gate)
- Final delegation decisions (user strategic)
- Compensation decisions (user strategic)
- Contract commitments (user legal/commercial)
- Phase 4 design (blocked until May 15 checkpoint)

---

## 5. Business Setup and Forecast Track

This section records operational planning anchors — not legal or accounting advice.

### Company establishment (Signee / personal business)

| Item | Status | Timing | Notes |
|---|---|---|---|
| Business registration paperwork | In progress — cost accounting task handled in W18 prep block (2026-05-08) | May–June 2026 | W18 Fri prep block included cost/accounting input package |
| Advance payment follow-up (Signee) | Waiting — customer process | Ongoing | Not a technical task |
| SECC contract preparation | Pre-analysis phase — contract side decided by partner | June 2026 | Full analysis inputs in `Signee_CONTEXT.md §5` |
| Legal/admin steps for company | Dependent on registration status | May–June 2026 | Low technical dependency; user owns follow-up |

### Year-end forecast anchors (from repo signals)

| Signal | Source | Planning Implication |
|---|---|---|
| Gương thần June demo (basic features) | Signee_CONTEXT §2026 Year-End, W18 strategic signal | June planning must budget demo sprint scope |
| SECC 12-device deployment | Signee_CONTEXT §2 | Validate hardware/software/support model before contract; do not assume scope |
| Locator guest frontend (paid clip/photo webapp) | Signee_CONTEXT §2 | H2 2026; commercial/privacy model must be scoped before commitment |
| RBB digital signing | Signee_CONTEXT §4 | **Delegate to Anh Khương.** User must not absorb. |
| Business advertising booking mechanism | Signee_CONTEXT §4 | **Delegate to Anh Khương.** User owns decision; Anh Khương owns implementation. |
| Mirror safety / prohibited-content research | Signee_CONTEXT §2 | June 2026; required before any product commitment |
| RobotOS — year-end trajectory | May Plan §4 | Board rebuild/retest is May primary. Year-end trajectory depends on May 15 checkpoint decision. |

### Cost estimation principles (operational, not legal)

Define — for each delegated workstream:
1. Who delivers it (user / teammate / external)
2. Time commitment per week or milestone
3. Cost or compensation assumption (to be locked by Week 4 milestone)
4. What user does vs does not fund with time

These are **placeholders to be filled as the workstream progresses** — not commitments in this memo.

### Human resource sharing / workflow model (to be defined)

The user's working model involves:
- **Two teammates** (Signee technical delegation, confirmed May Plan §5 Delegation Rule)
- **Anh Khương** (RBB digital signing + booking mechanism, confirmed Signee_CONTEXT §4)
- **AI Triangle** (GPT, Copilot, Claude, GLM — per AGENT_OPERATING_MODEL.md)

Open questions to resolve by Week 3 milestone:
- What hours/week does each human teammate commit?
- How does the user verify quality without absorbing the work?
- When does a delegate own the outcome vs the user?

---

## 6. Recovery Commitment

The user's physical health is explicitly weaker than baseline as of W18. Health is not optional overhead — it is a P0 operating constraint built into the capacity model.

**Rules in force (do not duplicate here; defer to source):**

For full Weak-Health Mode rules (WH-1 through WH-8), trigger conditions, and admission gate interaction, see: `01_OS/04_OPERATIONS/WEEKLY_CONTROL/CAPACITY_ENGINE.md §10`

**What this memo commits to (operational level):**

- Health telemetry signals reduce scope before plan aesthetics. The W18 Wed → Thu capacity downgrade (poor sleep + medium-low energy → S-only evening, Accountant moved to early morning) is the operational proof that this works. Protect it.
- The system must not treat all available time as executable capacity. Pool B realistic ceiling is 11–18h/week sustainable; do not plan to the ceiling.
- Recovery is not scheduled as "free time" — it is assigned capacity that is protected from task admission.
- Activated-mode output (W17 spike weeks) must not become the new planning baseline for W18+.
- Weak-Health Mode must persist until **one full recovery day** occurs (multi-day rule per §10).

**Six commitments for the restructure period (May–June):**

1. RobotOS deep-work blocks stay protected; no Signee/Accountant context switching in same half-session.
2. Weekend evenings (Sat + Sun) remain OFF unless user explicitly overrides.
3. Weak-Health Mode downgrade is applied next-day, not deferred.
4. Business/registration/accounting work is time-boxed — it does not absorb evening deep-work capacity.
5. One full rest day per week — not a stretch goal, a capacity model assumption.
6. Phase 4 is not opened until health and Phase 3 evidence support it (May 15 checkpoint is the earliest gate).

---

## 7. Six-Week Stabilization Milestones

These are planning anchors, not committed deadlines unless confirmed by the active week plan.

| Milestone week | Dates | Focus | Phase gate |
|---|---|---|---|
| **W1 (W19)** | May 11–17 | Phase 3 checkpoint (May 15) + collect restructure inputs: absorption inventory verified, first delegation map drafted | May 15 checkpoint: close/extend/escalate Phase 3 |
| **W2 (W20)** | May 18–24 | Lock business/accounting assumptions: company registration status, SECC contract pre-analysis inputs, cost model skeleton | — |
| **W3 (W21)** | May 25–31 | Define delegation map: finalize what user keeps vs delegates for H2 2026; confirm Anh Khương scope; clarify teammate model | May plan closes |
| **W4 (W22)** | June 1–7 | Define compensation / work-sharing model: per-workstream cost and time commitment | — |
| **W5 (W23)** | June 8–14 | Test reduced-user-bottleneck workflow: run one work-week where 2+ overhead categories have been reduced by template/automation; observe | Gương thần June demo sprint begins if ready |
| **W6 (W24)** | June 15–21 | Review sustainability: did overhead reduction work? Did health hold? Decision: open Phase 4 or extend stabilization | Phase 4 design may open here if evidence supports it |

**Guard:** None of these milestones authorize Phase 4 design or a new Life Agent engine. W6 is the **earliest** point that evidence could support that decision.

---

## 8. Cross-References

| Document | Relevance | Section |
|---|---|---|
| `03_PLANNING/02_MONTH/2026-05_May_Plan.md` | Monthly priority stack, delegation rule, energy guards, Phase 3 continuation | §3, §5, §9 |
| `03_PLANNING/03_WEEK/W18/2026-W18_WeekPlan.md` | First full May execution week; TickTick auto-sync pilot; Signee delegation rule; Phase 3 evidence | §3, §5, §7 |
| `03_PLANNING/03_WEEK/W18/2026-W18_Execution.md` | Weak-Health Mode first live activation (Wed 2026-05-06); Friday May 8 prep block (restructure scope inputs) | §Daily notes Wed, §3, §7 |
| `08_PROJECT_CONTEXT/Signee_CONTEXT.md` | Year-end signals (SECC, Gương thần, Locator); delegation to Anh Khương; capacity risk | §2026 Year-End Outlook |
| `01_OS/AGENT_OPERATING_MODEL.md` | Working Triangle + GLM bounded execution contract; routing table | §3, §4, §5–7 |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/CAPACITY_ENGINE.md` | Weak-Health Mode rules (WH-1…WH-8); Pool A/B capacity model; recovery rules | §10 |
| `01_OS/TASK_INTAKE_AND_ADMISSION.md` | Ambiguity gate §7.5; admission rules; task status labeling §10.5 | §7, §7.5, §10.5 |

---

**File created:** 2026-05-09 (W18, LA-R1 Patch 1)
**File status:** ACTIVE
**Owner:** User
**Next action:** W19 generation (Phase 3 checkpoint week); Week 1 milestone above
**Phase guard:** This is LA-R1 stabilization input. Phase 4 opens only after May 15 checkpoint decision.
