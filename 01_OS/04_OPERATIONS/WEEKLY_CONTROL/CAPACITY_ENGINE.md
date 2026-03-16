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
- Hard boundary: **ALL remaining office-hours capacity belongs exclusively to TYPE A project operation (Zephyr).** No personal projects (RobotOS, Signee) may be allocated against any part of the office pool — not "remaining capacity," not "support hours," not any other framing.

**Rule:** If a project is "office hours only," its allocation is computed **against Layer 1 gross capacity**, not against a shared pool. It is **fixed and pre-committed**.

---

#### Layer 2 — Personal Deep-Work Pool (Evenings + Weekend)

**What belongs here:**
- Architecture, design, implementation work assigned to personal time (e.g., RobotOS builds)
- Evening focus blocks (19:30–21:30 per OS daily schedule model — personal evening capacity)
- Weekend blocks (optional, if explicitly planned)

**What must NOT be placed here:**
- KTLO/maintenance work (belongs in Layer 1)
- Admin/comms (belongs in Layer 4)
- **Any work during office hours — office hours belong 100% to Layer 1 (Zephyr + overhead)**

**Capacity ceiling:**
- Evening blocks: 2h/evening (19:30–21:30), Mon–Fri
- Baseline: 5 evenings × 2h = 10h/week
- Thu: S-only due to energy dip (block exists but lower intensity; plan lighter personal work)
- Fri: valid closure-work evening — not optional by default
- Weekend daytime: Saturday daytime = substantial deep-work block; Sunday daytime = planning + execution; both are valid personal capacity if intentionally named
- Weekend evenings: **Saturday evening = OFF (protected rest)**; **Sunday evening = OFF (protected rest)**; must not be allocated as execution capacity
- Morning architect block (06:30–07:15): PLANNING only — not execution capacity
- **Total personal execution capacity: 10h/week baseline (Mon–Fri evenings 19:30–21:30) + substantial weekend daytime extension (if intentionally planned)**
- **HARD RULE: This layer does NOT include any office hours. Office = Pool A / Layer 1 only.**

**Rule for evening blocks:** If weekly goals require evening capacity, the plan **must name those blocks explicitly** (days + hours). Silent evening dependency is a validation error.

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
- Personal time only — evenings or weekend blocks; **CANNOT use office hours** (office = Pool A = Zephyr only)
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
| **TYPE B** | Personal deep-work / architecture / design | Layer 2 | Personal evenings (19:30–21:30, Mon–Fri) + weekend daytime ONLY. **Weekend evenings and office hours: FORBIDDEN.** | Cannot use any office hours (all office = TYPE A Zephyr) | Block-model (1 block ≈ 1.5–3h focused work); evening slots; weekend daytime synthesis |
| **TYPE C** | Async / spec / review / coordination | Layer 3 | Personal evenings (19:30–21:30, Mon–Fri) + weekend daytime ONLY. **Weekend evenings and office hours: FORBIDDEN.** | Must not crowd out TYPE B deep focus | Interruptible, async-compatible; fills personal time gaps (not office gaps) |
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
Capacity is split across TWO SEPARATE POOLS — they must never be combined:

POOL A — Office-Locked (Layer 1 — Zephyr + overhead):
  Realistic Zephyr capacity = [5 days × 8h] − [TYPE D admin ~4h] = ~36h effective
  This entire pool belongs to Zephyr. There is no "remaining" to share with personal projects.

POOL B — Personal Flex (Layers 2+3 — RobotOS + Signee):
  Realistic personal capacity = [named evening blocks] + [optional weekend]
  = [2h × 5 weekday evenings (19:30–21:30 Mon–Fri)] + [weekend daytime if intentionally planned]
  = 10h/week baseline evenings
  + substantial weekend daytime extension (Sat+Sun daytime; must be named explicitly)
  Note: Thu evening = S-only (energy dip); Fri evening = valid closure capacity
  Note: Weekend EVENINGS (Sat+Sun eve) = protected rest; NOT part of Pool B

If personal project goals require more than Pool B capacity:
  → Reduce scope, or span goal across multiple weeks
  → Do NOT compensate by borrowing from Pool A (office hours)
```

If goals require more than 36h + named evening, scope must be reduced or deferrals must be documented.

### R8 — Daily anchor must be consistent with layer assignments

The daily anchor structure in the WeekPlan must be consistent with which projects belong to which layers:
- TYPE A should appear in the anchor as an office-hours block, not listed alongside TYPE B as if interchangeable
- TYPE B should appear in personal evening/weekend deep-work blocks
- TYPE C should appear in personal async slots (evening or weekend)

If the anchor table mixes TYPE A and TYPE B as equivalent daily anchors without time-slot distinction, it is a V7 validation failure.

---

### R9 — Pool Isolation: Office and Personal Capacity Must Not Share

Pool A (office hours, weekdays 08:30–17:00) and Pool B (personal time: evenings + weekends) are structurally separate. They must never share capacity under any framing.

**Pool isolation applies in both directions:**
- TYPE B (RobotOS) and TYPE C (Signee) must draw capacity **only from Pool B** (personal evenings + weekends)
- Pool A office hours must be allocated **only to TYPE A (Zephyr)** and TYPE D overhead
- Framing like "using remaining office capacity for RobotOS" violates this rule
- Framing like "Zephyr evening work to free up office time" violates this rule
- If Pool B capacity is insufficient for personal project goals: reduce scope or span goal to next week

**Sources confirming pool separation:**
- OS daily schedule: Job 1 (08:30–17:00) = Zephyr; Personal evening (19:30–21:30) = RobotOS/Signee
- Zephyr_Project_Context §5: "Executed during office hours only. No regular evening deep work."
- Zephyr_Project_Context §7: "Do not schedule Zephyr work in evening blocks. Protect capacity for Signee (Phase 1) and RobotOS (Phase 2)."

---

### R10 — Weekend Evening Protection and Sustainability

Weekend evenings (Saturday evening and Sunday evening) are protected recovery time. They must not be allocated as personal execution capacity under any framing.

- Saturday daytime: valid personal deep-work capacity; must be explicitly named
- Sunday daytime: valid personal planning and execution capacity; must be explicitly named
- Saturday evening: OFF — rest protection; not plannable by default
- Sunday evening: OFF — rest protection; not plannable by default

If a plan requires weekend evening work to close, it is a **scope problem, not a scheduling solution**. Resolve via scope reduction (§8 Resolution 3) — do NOT consume protected rest.

**Sustainability balance principle:**
- Do NOT model personal capacity so low (~6–8h) that the engine systematically underestimates achievable personal work and forces unnecessary multi-week spans
- Do NOT model personal capacity so high (all evenings + all weekend day + all weekend evening) that burnout becomes the hidden cost of meeting weekly goals
- Correct baseline: 10h/week evenings + intentional weekend daytime = sustainable and realistic

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
| Pool isolation | V11 | Pool A (office) contains only TYPE A + TYPE D; Pool B (personal) contains only TYPE B + TYPE C; no cross-pool hours exist | Any personal project (TYPE B/C) has hours attributed to office hours; or Zephyr has hours attributed to personal blocks |

---

## 7. Output Contract

The engine produces a **Capacity Summary block** that the weekly plan's `## Capacity & Constraints` section must include.

### Required Output Fields

```markdown
## Capacity & Constraints — ENGINE OUTPUT

### POOL A — Office-Locked Capacity (Layer 1)

| Component | Type | Hours | Constraint |
|---|---|---|---|
| [TYPE A project — Zephyr] | TYPE A | ~[h effective] | **Office hours only. Gross 40h. Effective after D1 overhead: ~36h.** |
| Admin / comms (D1 overhead) | TYPE D | [h/week] | Inside Pool A. Subtracted from gross. |
| **Pool A total** | — | ~40h gross | **100% office hours. Zero remaining for personal projects.** |

> Pool A boundary: ALL office hours belong to TYPE A (Zephyr) + TYPE D overhead.
> No personal projects (TYPE B, TYPE C) may be allocated against this pool under any framing.

### POOL B — Personal Flex Capacity (Layers 2+3)

| Project | Type | Personal Blocks (Source) | Hours | Notes |
|---|---|---|---|---|
| [TYPE B project — RobotOS] | TYPE B | Evenings: [days] (19:30–21:30); weekend daytime if planned | [h] | Deep-work blocks; execution; no office hours; no weekend evenings |
| [TYPE C project — Signee] | TYPE C | Evenings: [days] (19:30–21:30); weekend daytime async | [h] | Spec/coordination; async-compatible; no office hours; no weekend evenings |
| [TYPE E items] | TYPE E | — | 0 (conditional) | Activates if: [trigger event] |
| **Pool B total** | — | Weekday evenings (baseline 10h) + weekend daytime (if named) | [sum] | Against 10h/week baseline; weekend daytime is extension |

> Pool B boundary: ALL personal project work must be sourced from named personal blocks only.
> Cannot use office hours.

### Capacity Summary

| Pool | Source | Available | Allocated | Utilization | Status |
|---|---|---|---|---|---|
| **Pool A — Office-Locked** | Office hours (weekdays) | ~40h gross / ~36h effective | Zephyr effective + D1 | ~100% | Zephyr only; no personal |
| **Pool B — Personal Flex** | Weekday evenings (19:30–21:30) + weekend daytime | 10h/week baseline + [weekend daytime h] | TYPE B + TYPE C personal | [%] | PASS / WARN / FAIL |

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
| Pool isolation | V11 | PASS / FAIL | |

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
6. RobotOS (TYPE B) and Signee (TYPE C) allocated against office hours — pool isolation violated (**V11 fail**)

### What the corrected model looks like

```markdown
### POOL A — Office-Locked Capacity (Layer 1)

| Component | Type | Hours | Constraint |
|---|---|---|---|
| Zephyr (TYPE A — test extension + operational) | TYPE A | ~36h effective | Office hours only. No evening. Gross 40h − 4h D1 = 36h. Source: Zephyr_Project_Context §5, §7. |
| Admin / comms (D1) | TYPE D | 4h | Inside Pool A. Standard overhead. |
| **Pool A total** | — | ~40h gross | **100% office hours. Zero allocated to personal projects.** |

> Note: Zephyr's test extension goal (~12.5h estimated effort) sits inside Pool A's ~36h effective
> capacity alongside other Zephyr operational work. The remaining ~23.5h stays as Zephyr ops time
> (meetings, reviews, KTLO monitoring) — NOT available to personal projects.

### POOL B — Personal Flex Capacity (Layers 2+3)

| Project | Type | Personal Blocks (Source) | Hours | Notes |
|---|---|---|---|---|
| RobotOS (architecture + onboarding) | TYPE B | Weekday evenings Mon–Fri (19:30–21:30); Sat daytime if planned | ~7h | W11 partial allocation (intentional scope decision); full goal (~15h) spans W11–W12; no office hours; no weekend evenings |
| Signee (testing specification) | TYPE C | Evenings Wed–Fri (19:30–21:30); optional weekend daytime | ~3h | W11 partial allocation; no office hours; no weekend evenings |
| Board testing (Signee) | TYPE E | — | 0 conditional | Activates when: hardware delivered |
| **Pool B total** | — | Weekday evenings (10h baseline) + Sat daytime if planned | ~10h | W11: uses full weekday evening baseline; weekend daytime available as extension if goals require it |

### Capacity Summary

| Pool | Source | Available | Allocated | Utilization | Status |
|---|---|---|---|---|---|
| Pool A — Office | Office hours | ~40h gross | Zephyr + overhead | ~100% | Full; contains Zephyr only |
| Pool B — Personal | Weekday evenings (19:30–21:30) + Sat daytime | ~10h (eve baseline) + [Sat daytime if named] | RobotOS ~7h + Signee ~3h | ~100% | PASS: within baseline; no ceiling breach |

Validation status: V1 PASS | V2 PASS | V3 PASS (evening blocks named) | V4 PASS | V5 PASS | V6 PASS (goal estimates reflect W11 personal scope) | V7 requires anchor restructure | V8 WARN (document office vs evening clearly in anchor table) | V9 PASS | V10 PASS | **V11 PASS (pool isolation confirmed)**
```

**Key corrections versus broken model:**
- "Layer 1 remaining" for RobotOS/Signee = ELIMINATED. Office pool is 100% Zephyr.
- RobotOS sourced from Pool B (evenings + weekend): ~6–7h in W11, not 18h
- Signee sourced from Pool B (evenings + weekend): ~2–3h in W11, not 8–9h
- Goal estimates for W11 reflect what personal capacity can deliver (multi-week goals span W11+W12)
- Pool isolation check V11 added and passes when pools are correctly separated

---

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-03-16 | 1.0 | Initial creation: capacity modeling engine for LIFE_AGENT weekly planning system. Created in response to W11 capacity audit findings. Defines TYPE A–E classification, 4 capacity layers, 10 validation checks, output contract, and integration points. |
| 2026-03-16 | 1.1 | Architecture correction: dual-pool model. Ground-truth rule applied: office hours (08:30–17:00) are exclusively Zephyr (Pool A); personal projects (RobotOS, Signee) must use personal time only (Pool B: evenings + weekends). Layer 2 renamed to "Personal Deep-Work Pool"; TYPE B/C definitions updated to forbid office hours; R9 pool isolation rule added; V11 pool isolation check added; output contract rewritten to show Pool A and Pool B separately; §11 example corrected to remove "office support" rows for personal projects. |
| 2026-03-16 | 1.2 | Personal-capacity schedule correction. Ground-truth evening schedule applied: 19:30–21:30 (not 20:00–21:30); Mon–Fri 5 evenings × 2h = 10h/week baseline (not 4 evenings × 1.5h = ~6h). Weekend model corrected: Sat+Sun daytime = substantial intentional capacity; Sat+Sun evening = OFF (protected rest). Layer 2 capacity ceiling rewritten; TYPE B/C allowed columns updated; R7 Pool B formula updated; R9 source footnote corrected; R10 (weekend evening protection + sustainability balance) added; output contract template updated; §11 example corrected to reflect 10h baseline. |
