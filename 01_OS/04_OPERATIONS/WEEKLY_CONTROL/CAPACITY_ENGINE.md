# CAPACITY_ENGINE

> **Type:** Engine / Reusable Primitive  
> **Layer:** OS / Operations  
> **Scope:** Capacity modeling and validation for weekly planning  
> **Called by:** GENERATE_WEEKPLAN (mandatory) | WEEKLY_REBALANCE (mandatory when load drifts) | GENERATE_WEEKLY_EXECUTION (optional, for inherited constraint awareness)  
> **Must NOT be:** Duplicated inline in weekly planning procedures. Capacity logic lives here, not there.

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. Position in System Architecture](#2-position-in-system-architecture)
- [3. Engine Inputs](#3-engine-inputs)
- [4. Capacity Model](#4-capacity-model)
  - [4.1 Capacity Layers](#41-capacity-layers)
  - [4.2 Project Time Model Types](#42-project-time-model-types)
- [5. Engine Rules](#5-engine-rules)
- [6. Validation Checks](#6-validation-checks)
- [7. Output Contract](#7-output-contract)
- [8. Decision Logic When Capacity Does Not Close](#8-decision-logic-when-capacity-does-not-close)
- [9. Integration Points](#9-integration-points)
- [10. Minimal Correction Principle](#10-minimal-correction-principle)
- [11. Example — W11-style mismatch and corrected model](#11-example--w11-style-mismatch-and-corrected-model)

---

## 1. Purpose

CAPACITY_ENGINE is the canonical capacity modeling primitive for the LIFE_AGENT operating system.

**It exists because:**

Without a shared capacity model, weekly planning procedures generate allocation tables that:
- Mix projects with fundamentally different time constraints into one undifferentiated pool
- Label baseline work as contingent (creating false optionality in weekly goals)
- Imply evening/flex capacity is available without explicitly naming it
- Produce capacity sections that contradict goal effort estimates in the same document
- Allow office-hours-only projects (KTLO / maintenance) to be scheduled in flexible evening blocks
- Create daily anchor structures that assume a different time model than the capacity section

CAPACITY_ENGINE prevents all of these. It is not optional.

**Problems this engine solves (concrete):**
1. `RobotOS (50%) + Zephyr (35%) + Signee (15%)` inside one 40h pool — hides that Zephyr is office-only and RobotOS uses evening blocks
2. `Effort estimate: 9h` in Goals section vs. `5h contingent` in Capacity section — internal contradiction
3. Anchor hypothesis assigning all projects every day without distinguishing time slot ownership
4. Baseline work labeled conditional because a tangentially related blocker is unresolved
5. Evening/weekend capacity implicitly required to close the numbers but never modeled

---

## 2. Position in System Architecture

```
WEEKLY PLANNING CHAIN:
─────────────────────────────────────────────────────────
Month File + Project Contexts + Carry-over
        │
        ▼
┌─────────────────────┐
│  CAPACITY_ENGINE    │  ← YOU ARE HERE (runs before allocation)
│  (this file)        │
└─────────────────────┘
        │
        │  Output: validated capacity summary + project-tier allocation
        ▼
GENERATE_WEEKPLAN (Step 6, 7, 8)
        │
        ▼
W##_WeekPlan.md  ← Capacity & Constraints section inherits engine output
        │
        ▼
GENERATE_WEEKLY_EXECUTION (inherits constraints already resolved)
        │
        ▼
Daily Loop (INTEGRATE_DAILY / PREPARE_NEXT_DAILY)
        │
        ▼
WEEKLY_REBALANCE → re-runs CAPACITY_ENGINE if load has materially drifted
        │
        ▼
WEEK_CLOSEOUT
─────────────────────────────────────────────────────────
```

**The engine is a primitive, not an orchestrator.**  
- It consumes inputs → validates → produces a structured summary  
- It does not write weekly plan files  
- Consuming procedures (GENERATE_WEEKPLAN, WEEKLY_REBALANCE) own the output and embed it in the week plan

**The engine's output must not be duplicated across files.**  
Once GENERATE_WEEKPLAN embeds engine output in `W##_WeekPlan.md`, downstream procedures (GENERATE_WEEKLY_EXECUTION, WEEKLY_REBALANCE) read the plan file — they do not re-derive capacity from scratch.

---

## 3. Engine Inputs

The engine must receive all of the following before producing output.

### Mandatory Inputs

| Input | Source | Reason |
|---|---|---|
| Active projects this week | Project Context files | Each project contributes to a different capacity tier |
| Project type classification | Project Context + OS model | Determines which Capacity Layer each project belongs to |
| Weekly goal effort estimates | Preliminary goals (from Step 5 of GENERATE_WEEKPLAN) | Used to verify allocation sum is realistic |
| Available office-hours capacity | OS daily schedule model | Establishes the office-hours layer ceiling |
| Optional flex/evening availability | OS daily schedule + weekly exception check | Establishes whether flex capacity is available this week |
| Admin/comms overhead | Weekly estimate (standard or adjusted for exceptions) | Subtracted from office capacity before allocation |
| KTLO budget | Project Context (Zephyr or equivalent fixed project) | Must be pre-committed before flexible allocation starts |
| Carry-over effort estimate | WEEK_CLOSEOUT output from previous week | Added to capacity demand before checking headroom |
| Blockers and conditional work | Project Context + carry-over list | Determines what is truly conditional vs. baseline |
| Weekly exceptions | Vacation, meetings, reduced capacity days | Adjusts office-hours layer downward |

### Optional Inputs (used when available)

| Input | Source | Use |
|---|---|---|
| Historical anchor adherence | Anchor tracking file | Validates that anchor structure is consistent with real daily capacity |
| Previous week utilization | W##-1_Execution.md | Anchors effort estimates in reality, not templates |
| Project phase information | Project Context files | Informs whether a project is in heavy-execution vs. maintenance vs. specification mode |

---

## 4. Capacity Model

### 4.1 Capacity Layers

The LIFE_AGENT capacity model is **tiered, not flat.** Projects belong to specific layers. Layers must not be mixed.

---

#### Layer 1 — Office-Hours Pool (Fixed)

**What belongs here:**
- Core job / KTLO responsibilities (e.g., Zephyr: "executed during office hours only")
- Fixed meetings, standups, team sync
- Release-driven tasks that must occur inside office hours
- Any work explicitly defined as "no evening load" in project context

**What must NOT be placed here:**
- Flexible architecture/design work (belongs in Layer 2)
- Async specification or review (belongs in Layer 3)
- Evening blocks (Layer 2)

**Capacity ceiling:**
- Standard: 5 days × 8 hours = 40 hours gross
- Minus: KTLO-fixed project allocation (pre-committed, first-before-flex)
- Minus: Admin/comms overhead (standard 4h; adjust for exceptions)
- Remaining: flex-within-office capacity for RobotOS/Signee office support

**Rule:** If a project is "office hours only," its allocation is computed **against Layer 1 gross capacity**, not against a shared pool. It is **fixed and pre-committed**.

---

#### Layer 2 — Flexible Deep-Work Pool

**What belongs here:**
- Architecture, design, implementation work (e.g., RobotOS, Signee builds)
- Protected focus blocks (typically 2 × 1.5h deep-work slots per day in office hours)
- Optional evening extension blocks (e.g., 20:00–21:30 per OS daily schedule model)
- Weekend blocks (optional, when synthesis or continuation is needed)

**What must NOT be placed here:**
- KTLO/maintenance work (belongs in Layer 1)
- Admin/comms (belongs in Layer 4)

**Capacity ceiling:**
- Office deep-work slots: 2 × 1.5h per day = 3h/day × 5 days = ~15h/week
- Plus: Evening extension (1.5h/day × available evenings; optional, not guaranteed)
- Plus: Weekend work (if explicitly planned; must be decision-based, not implied)
- **Total max with evenings: ~22–24h/week (if all evenings used)**

**Rule for evening blocks:** If weekly goals require evening capacity to close the allocation, the plan **must name those blocks explicitly**. Silent evening dependency is a validation error.

---

#### Layer 3 — Async / Specification / Coordination Pool

**What belongs here:**
- Specification writing, documentation, testing structure (e.g., Signee testing spec)
- Code review, PR feedback, architecture comments
- Team coordination, async communication with external teams
- Cross-team handoff work that does not require synchronous office presence

**What must NOT be placed here:**
- Implementation that requires deep uninterrupted focus (belongs in Layer 2)
- Fixed office-hours commitments (belongs in Layer 1)

**Capacity ceiling:**
- Flexible: can use office hours, evenings, or weekend blocks
- Typical range: 5–10h/week (depending on coordination load)
- Compatible with Layer 2 on the same day if timing is non-overlapping

**Rule:** Layer 3 work is flexible in scheduling but must have explicit time planned. "Signee will fit in" is not a capacity plan.

---

#### Layer 4 — Admin / Comms / System Overhead

**What belongs here:**
- Email, Slack, decision logs
- Weekly planning and review cycles
- Ticket grooming, status updates, stakeholder comms
- Synthesis work (weekly/monthly reviews — prefer weekend)

**Capacity:**
- Standard allocation: 4h/week (office hours)
- Adjust upward: if external dependencies or communication load is high
- Synthesis reviews (monthly/quarterly): prefer weekend blocks

**Rule:** Admin/comms overhead must be subtracted from office-hours Layer 1 capacity before project allocation begins. It is not a percentage; it is a concrete subtraction.

---

### 4.2 Project Time Model Types

| Type | Description | Layer | Allowed Time Slots | Disallowed | Scheduling Behavior |
|---|---|---|---|---|---|
| **TYPE A** | Fixed office-hours / KTLO / maintenance | Layer 1 | Office hours only | Evening, weekend | Pre-committed, allocated first; non-negotiable time slot |
| **TYPE B** | Flexible deep-work / architecture / design | Layer 2 | Office deep blocks + evening optional | Cannot displace TYPE A within office slot | Block-model (1 block ≈ 2–4h focused work); protected from interruptions |
| **TYPE C** | Async / spec / review / coordination | Layer 3 | Any slot (office, evening, weekend) | Must not crowd out TYPE B deep focus | Interruptible, async-compatible; can fill office gaps |
| **TYPE D** | Admin / comms / system overhead | Layer 4 | Office hours (prefer morning/EOD) | Must not use deep-work slots | Fixed deduction; not a flexible allocation |
| **TYPE E** | Conditional / blocked work | Any layer at activation | Only when unblock trigger fires | Must not be pre-allocated as baseline if truly blocked | Parked until explicit unblock event; effort is NOT in baseline plan |

**TYPE E rule (critical):**  
Work is TYPE E only if execution cannot begin until an external event resolves (e.g., equipment arrives, decision is made, third-party delivers).  
Work is NOT TYPE E if only a related aspect is blocked (e.g., board testing is blocked but testing specification writing is unblocked). In that case, the specification is TYPE C and should be allocated as baseline.

---

#### Project Assignments (this repo)

| Project | Type | Rationale | Source |
|---|---|---|---|
| **Zephyr** | TYPE A | "Core Job — Office Hours"; "executed during office hours only"; "no regular evening deep work"; "must not create after-hours cognitive load" | Zephyr_Project_Context §1, §5, §7 |
| **RobotOS** | TYPE B | Block model (1 block ≈ 4h focused); architecture + design + implementation; evening/weekend allowed when needed | ROBOTOS_CONTEXT §3 |
| **Signee** | TYPE C (specification/coordination phases) | PM/Tech Lead role; testing spec, documentation, cross-team coordination; async-compatible | Signee_CONTEXT §3; role = PM/Tech Lead |
| **Admin/Comms** | TYPE D | Standard overhead: email, decision logs, planning meetings | OS model §4 |
| **Board Testing (Signee)** | TYPE E (when equipment blocked) | Board testing cannot start without hardware; conditional on equipment delivery | Signee project state; project context |

---

## 5. Engine Rules

These rules are mandatory. A weekly plan that violates them has a structural defect.

### R1 — TYPE A projects must be allocated before flexible projects

TYPE A capacity is **pre-committed and fixed**. It must be assigned to Layer 1 before any flexible project allocation begins. TYPE B and TYPE C projects receive only the capacity remaining after TYPE A and TYPE D are satisfied.

### R2 — TYPE A projects must not receive evening or weekend allocation

Any plan that assigns evening capacity to a TYPE A project violates the project's operating constraint. This is detected by Validation Check V4.

### R3 — Baseline work must not be labeled contingent

Work that must be completed regardless of external conditions is baseline. Labeling it "contingent" suppresses its effort estimate, creates fake optionality, and distorts capacity accounting.  
Apply the TYPE E test: if work can start now, it is baseline (TYPE B or TYPE C). If it cannot start without a named external event, it is TYPE E.

### R4 — Goal effort estimates must equal capacity allocations

The effort estimate in the Goals section of a WeekPlan must match the hours allocated in the Capacity section. If they do not match, either the estimate or the allocation is wrong. Validate both before finalizing.

### R5 — Evening / flex capacity must be named explicitly if required

If total planned work exceeds the office-hours Layer 1 + Layer 2 office capacity, the difference must be sourced explicitly from named evening or weekend blocks. "Will fit in" is not valid. State:  
- Which project uses which evening slots  
- How many hours those slots provide  
- That they are optional extensions (not office capacity)

### R6 — Signee splitting rule

Signee is a multi-component project. When splitting effort:
- Specification, documentation, testing structure → TYPE C (baseline, allocate fully)
- Board testing that requires physical hardware → TYPE E (conditional, do not pre-allocate)
- Android implementation (if blocked by equipment) → TYPE E
- Testing review / quality gate design (equipment-independent) → TYPE C

Do not apply a single TYPE to all Signee work if sub-components have different constraints.

### R7 — Allocation sum rule

The sum of all layer allocations must be ≤ total realistic capacity. Realistic capacity is:

```
Realistic capacity = Office Layer 1 (gross - admin) + named evening blocks
= [5 days × 8h] - [TYPE D admin ~4h] + [Named evening h, if planned]
= 36h base + explicit evening extension
```

If goals require more than 36h + named evening, scope must be reduced or deferrals must be documented.

### R8 — Daily anchor must be consistent with layer assignments

The daily anchor structure in the WeekPlan must be consistent with which projects belong to which layers:
- TYPE A should appear in the anchor as an office-hours block, not listed alongside TYPE B as if interchangeable
- TYPE B should appear in deep-work blocks (morning/afternoon focus blocks)
- TYPE C should appear in flexible slots (between deep blocks, after TYPE A, or in evening)

If the anchor table mixes TYPE A and TYPE B as equivalent daily anchors without time-slot distinction, it is a V7 validation failure.

---

## 6. Validation Checks

Run all checks before accepting capacity model output.

| Check | ID | What to Verify | Failure Condition |
|---|---|---|---|
| KTLO pre-commitment | V1 | TYPE A project hours are committed before any other allocation | TYPE A hours mixed in same pool as TYPE B/C |
| Office-hours ceiling | V2 | Sum of Layer 1 (TYPE A + TYPE D) does not exceed office-hours gross | Layer 1 > 40h (or adjusted for exceptions) |
| Evening dependency hidden | V3 | If total planned effort > (36h threshold), named evening blocks exist | Evening blocks implied but not named |
| No evening for TYPE A | V4 | TYPE A project has zero evening/weekend allocation | TYPE A assigned to evening or weekend slot |
| Baseline vs. contingent | V5 | All TYPE E items have a named external trigger; TYPE B/C items are not labeled contingent | Baseline work labeled conditional without true block |
| Goal-allocation match | V6 | Each goal's effort estimate equals the capacity allocated | |Goal effort| − |capacity allocated| > 1.5h per goal |
| Anchor-layer consistency | V7 | Daily anchor time slots are consistent with project type assignments | TYPE A and TYPE B listed as equivalent daily anchors with no time-slot distinction |
| Daily scope rule | V8 | Max 2 projects active per day can be verified given layer assignments | Ambiguous which 2 projects are active in which time slots |
| Capacity sum | V9 | Total allocated hours ≤ realistic weekly capacity (office + named evening) | Total allocation exceeds modeled capacity |
| Split-Signee rule | V10 | Signee sub-components with different types are allocated separately | All Signee work assigned one TYPE; blocks baseline allocation |

---

## 7. Output Contract

The engine produces a **Capacity Summary block** that the weekly plan's `## Capacity & Constraints` section must include.

### Required Output Fields

```markdown
## Capacity & Constraints — ENGINE OUTPUT

### Office-Hours Layer (Layer 1 — Fixed)

| Component | Type | Hours | Constraint |
|---|---|---|---|
| [KTLO/TYPE A project] | TYPE A | [h/week] | Office hours only. No evening. Structural constraint from project context. |
| Admin / comms | TYPE D | [h/week] | Standard overhead. Subtracted before flexible allocation. |
| **Layer 1 total committed** | — | [sum] | Pre-committed before flexible allocation. |
| **Layer 1 remaining (for flexible projects)** | — | [40 − sum] | Available for TYPE B/C office-hours support. |

### Flexible Project Allocation (Layer 2+3)

| Project | Type | Office Support | Evening/Flex | Total | Notes |
|---|---|---|---|---|---|
| [TYPE B project] | TYPE B | [h in office] | [h in named evening, or "not required"] | [total] | Deep blocks: [when] |
| [TYPE C project] | TYPE C | [h in office] | [h in named async, or "not required"] | [total] | Baseline; spec/coordination work |
| [TYPE E items] | TYPE E | — | — | 0 (conditional) | Activates if: [trigger event] |

### Capacity Totals

| Pool | Capacity | Allocated | Utilization | Status |
|---|---|---|---|---|
| Office-hours Layer 1 | 40h | [TYPE A + TYPE D] | [%] | KTLO committed |
| Office remaining (flexible support) | [40 − Layer 1] | [TYPE B + TYPE C office] | [%] | Within bounds / exceed |
| Evening extension (named) | [h or "none"] | [TYPE B + TYPE C evening] | [%] | Optional; explicit |
| **Total operative** | [sum] | [sum] | [%] | PASS / WARN / FAIL |

### Validation Status

| Check | ID | Status | Notes |
|---|---|---|---|
| KTLO pre-commitment | V1 | PASS / FAIL | |
| Office-hours ceiling | V2 | PASS / FAIL | |
| Evening dependency hidden | V3 | PASS / WARN | |
| No evening for TYPE A | V4 | PASS / FAIL | |
| Baseline vs. contingent | V5 | PASS / FAIL | |
| Goal-allocation match | V6 | PASS / FAIL | |
| Anchor-layer consistency | V7 | PASS / FAIL | |
| Daily scope rule clarity | V8 | PASS / WARN | |
| Capacity sum | V9 | PASS / FAIL | |
| Split-Signee rule | V10 | PASS / N/A | |

### Warnings & Reconciliation Notes

[List any conditions that are PASS but carry ongoing risk, any evening dependency that is explicitly named, any scope assumptions made during modeling]
```

### Output Pass / Warn / Fail Meaning

| Status | Meaning | Action Required |
|---|---|---|
| **PASS** | All validation checks pass; model is consistent | Proceed with plan generation |
| **WARN** | Model is usable but contains a named risk or approximation | Note the warning; document assumption; proceed with caution |
| **FAIL** | At least one hard validation check fails | Do NOT finalize plan until failure is resolved |

---

## 8. Decision Logic When Capacity Does Not Close

When total planned effort exceeds realistic capacity (Validation V9 fails), the planner must choose one of these resolutions. They are listed in order of preference.

### Resolution 1 — Correct the labels (lowest risk)

If a goal is labeled contingent but is actually baseline (R3 violation), fix the label. Then re-run V9. The numbers may now close if contingent work was previously excluded.

### Resolution 2 — Name the evening extension (explicit)

If baseline work requires evening blocks, name them explicitly:
- Which project
- Which days
- Roughly how many hours
- That they are optional extensions (not office capacity)

Run V3 and V4. If TYPE A work is not in the evening pool, the model is valid.

### Resolution 3 — Reduce scope

If naming evening blocks still doesn't close, scope must be reduced.  
Options:
- Convert a TYPE B/C goal to TYPE E (defer if a reasonable trigger can be named)
- Split a goal: deliver partial scope this week, carry the rest to next week
- Drop a carry-over item (if it is "nice-to-have" not "must-have")

Document the reduction explicitly in the plan (not silently).

### Resolution 4 — Escalate

If scope cannot be reduced without violating a project commitment, or if two project deadlines are incompatible with available capacity, escalate:
- Document the conflict in the Decision Log
- Raise for explicit prioritization decision
- Do not generate a WeekPlan that pretends the conflict doesn't exist

### Prohibited Resolutions

- Do NOT over-expand office hours implicitly (e.g., "work harder" without naming hours)
- Do NOT label baseline work contingent to make numbers appear to close
- Do NOT place TYPE A work in evening blocks to free up office time for other projects
- Do NOT ignore the gap and hope execution "figures it out"

---

## 9. Integration Points

### Called by GENERATE_WEEKPLAN

**When:** Mandatory before Step 6 (Assess Capacity) and before Step 7 (Anchor Design).

**How:**
1. Collect engine inputs (project types, goal estimates, office exceptions, blocker status)
2. Run CAPACITY_ENGINE classification and validation
3. If FAIL: resolve before proceeding
4. If PASS/WARN: embed Capacity Summary block in WeekPlan `## Capacity & Constraints` section
5. Use layer assignments to inform Step 7 (Anchor Hypothesis) — anchors must respect layer assignments

**Produces:** The `## Capacity & Constraints` section of `W##_WeekPlan.md`

---

### Called by WEEKLY_REBALANCE

**When:** Required when WEEKLY_REBALANCE detects that actual capacity has materially drifted from plan (e.g., TYPE A work overran; evening blocks were unavailable; a goal took >2x estimated effort).

**How:**
1. Re-collect inputs using current execution state (not original plan state)
2. Re-run CAPACITY_ENGINE with updated actuals (hours consumed, hours remaining)
3. Validate: does the remaining capacity support remaining goals?
4. If not: apply Decision Logic (§8) to rebalance scope, not hide the drift

---

### Referenced by GENERATE_WEEKLY_EXECUTION

**When:** Execution file is generated (Mode A — new week).

**How:**
- GENERATE_WEEKLY_EXECUTION inherits capacity constraints already resolved by CAPACITY_ENGINE in the WeekPlan
- It does not re-run the engine
- It should note in Execution file: "Capacity model validated in WeekPlan (CAPACITY_ENGINE V-checks: PASS)"
- If execution reveals a new constraint not present during planning (e.g., unexpected TYPE A overrun), trigger WEEKLY_REBALANCE

---

## 10. Minimal Correction Principle

CAPACITY_ENGINE must not force a full redesign of a working weekly plan.

**When to apply full engine run:**
- New week generation (every time)
- Material drift during rebalance

**When to apply targeted fix only:**
- Discovered inconsistency is isolated to one section (e.g., Signee effort mismatch)
- Validation shows WARN, not FAIL
- Anchor structure is correct; only labeling is imprecise

**Precise principle:**
> Fix what is provably wrong. Leave what works.

Concretely: if a plan's goals and deliverables are sound, and the anchor table is operationally correct, but the capacity section uses percentage notation instead of layer notation, **correct the section wording** — do not rebuild the goals or anchors.

The engine is not a trigger for perfectionism. It is a guard against structural errors.

---

## 11. Example — W11-Style Mismatch and Corrected Model

### What the broken model looked like

```
Gross work week = 40h
Admin deduction = 4h
Available = 36h

RobotOS (primary) = 50% = 18h  ←  
Zephyr (secondary) = 35% = 12.5h  ← all treated as fungible slices of one pool
Signee (contingent) = 15% = 5h  ←

Total = 100% = 36h
```

**Problems:**
1. Zephyr is "office hours only" but is listed as a floating percentage alongside RobotOS (**V1 fail: TYPE A not pre-committed first**)
2. Signee labeled "contingent" but Goal section says 9h baseline work (**V5 fail: R3 violation**)
3. Goal effort = 9h (Signee) but capacity = 5h — contradiction (**V6 fail**)
4. 18 + 12.5 + 9 = 39.5h > 36h — numbers require ~3.5h evening capacity (**V3 fail: hidden**)
5. Daily anchors list TYPE A and TYPE B as equivalent secondary/primary — no time-slot distinction (**V7 fail**)

### What the corrected model looks like

```markdown
### Office-Hours Layer (Layer 1 — Fixed)

| Component | Type | Hours | Constraint |
|---|---|---|---|
| Zephyr (TYPE A, KTLO) | TYPE A | 12.5 | Office hours only. No evening. Source: Zephyr_Project_Context §5, §7. |
| Admin / comms | TYPE D | 4.0 | Standard overhead. |
| Layer 1 total committed | — | 16.5 | Pre-committed. |
| Layer 1 remaining | — | 23.5 | Available for TYPE B/C office support. |

### Flexible Project Allocation (Layer 2+3)

| Project | Type | Office Support | Evening/Flex | Total | Notes |
|---|---|---|---|---|---|
| RobotOS (architecture + onboarding) | TYPE B | 5–6h | 12–13h (evening blocks: named) | ~18h | Evening: 20:00–21:30 Mon–Wed + optional Sat; Required for closure |
| Signee (testing specification) | TYPE C | 2–3h | 5–6h (evening or async) | ~8–9h | Baseline; independent of equipment blocker |
| Board testing (Signee) | TYPE E | — | — | 0 conditional | Activates when: hardware delivered |

### Capacity Totals

| Pool | Capacity | Allocated | Utilization |
|---|---|---|---|
| Office Layer 1 (Zephyr + Admin) | 40h gross | 16.5h | 41% |
| Office remaining (RobotOS + Signee office) | 23.5h | 8–9h office support | 36–38% |
| Evening extension (named: Mon–Wed + Sat) | ~7–8h | 12–13h (RobotOS) + 5–6h (Signee async) | Allocated across 2 projects |
| Total operative | ~43–44h | ~43.5h | Closes with named evening blocks |

Validation status: V1 PASS | V2 PASS | V3 PASS (evening named) | V4 PASS | V5 PASS | V6 PASS | V7 requires anchor update | V8 WARN (document office vs evening in anchor table) | V9 PASS | V10 PASS
```

**Key corrections:**
- Zephyr is pre-committed as TYPE A; not competing with RobotOS in a shared pool
- Signee specification is labeled baseline (TYPE C, 9h); board testing is TYPE E (0h conditional)
- Evening capacity named explicitly (Mon–Wed evening blocks + optional Sat)
- Goal effort (9h Signee) matches capacity (9h Signee) — V6 passes
- Anchor table must distinguish office-hours TIME A slots vs. TYPE B deep blocks

---

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-03-16 | 1.0 | Initial creation: capacity modeling engine for LIFE_AGENT weekly planning system. Created in response to W11 capacity audit findings. Defines TYPE A–E classification, 4 capacity layers, 10 validation checks, output contract, and integration points. |
