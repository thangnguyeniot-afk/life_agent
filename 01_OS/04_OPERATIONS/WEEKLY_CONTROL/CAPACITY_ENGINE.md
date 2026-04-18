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
- Hard boundary — **two-tier rule (planning allocation ≠ execution delegation):**
  - **Planning allocation rule:** Pool A belongs exclusively to TYPE A (Zephyr) + TYPE D overhead. No personal project (RobotOS, Signee, Project Accountant) may be *allocated* against office hours in the planning model — not "remaining capacity," not "support hours," not any other framing. This is the canonical pool ownership rule. It does NOT change mid-week or mid-month.
  - **Execution-level delegation exception:** At daily execution level, Zephyr may *delegate* a bounded portion of office time to Project Accountant (or other approved work) when ALL R9-DEL guardrails are met. This is borrowing, NOT allocation. It does NOT change the planning-level pool ownership. Execution delegation must be recorded in the daily log as "DEL:" and must never back-propagate into the planning model.
  - **Allocation, ownership, and time-domain execution are distinct concepts and must not be conflated.**

**Rule:** If a project is "office hours only," its allocation is computed **against Layer 1 gross capacity**, not against a shared pool. It is **fixed and pre-committed**.

---

#### Layer 2 — Personal Deep-Work Pool (Evenings + Weekend)

**What belongs here:**
- Architecture, design, implementation work assigned to personal time (e.g., RobotOS builds)
- Evening focus blocks (19:30–21:30 per OS daily schedule model — personal evening capacity)
- Weekend blocks: Saturday daytime + Sunday afternoon = **full project execution capacity**; declare planned hours per week. Sunday morning = review overhead (structural, not execution).

**What must NOT be placed here:**
- KTLO/maintenance work (belongs in Layer 1)
- Admin/comms (belongs in Layer 4)
- **Any work during office hours — office hours belong 100% to Layer 1 (Zephyr + overhead)**

**Capacity ceiling:**
- Evening blocks: 2h/evening (19:30–21:30), Mon–Fri
- **Gross weekday-evening baseline: 5 evenings × 2h = 10h/week** — this is a planning envelope, NOT guaranteed execution-ready capacity
- **Net planned evening capacity** is derived per week from the actual anchor/calendar structure:
  - Subtract **structural deductions** (recurring weekly patterns, not rare exceptions) — e.g., Thu = S-only energy dip; Fri = closure / S-only / none when planned that way
  - Subtract **ad hoc exceptions** (travel, events, illness) when present
  - The engine does NOT hard-code a net total; each weekly plan derives net evening capacity from its actual anchor table
- **Weekend daytime — three distinct categories:**
  - **Saturday daytime: full project execution capacity** — not optional in the sense of "only if needed"; always a real capacity source; declare planned project hours each week
  - **Sunday morning: review / closeout / planning block** (~2–3h structural weekly function); NOT project execution; NOT interchangeable with Saturday daytime or Sunday afternoon; consumed by WEEK_CLOSEOUT + next-week seed; counted in total weekly load as overhead
  - **Sunday afternoon: full project execution capacity** — always a real capacity source; declare planned project hours each week; if a given week does not use it, state that as a W## instance decision
- **Weekend evenings:** exactly ONE weekend evening is OFF (protected rest); the other is default-rest and may be explicitly opened by the weekly plan; the week plan must declare which evening is OFF; do NOT encode both as default-OFF; do NOT encode both as freely allocatable
- Morning architect block (06:30–07:15): PLANNING only — not execution capacity
- **Total personal execution capacity:** net weekday evenings (derived from anchor) + Saturday daytime (full capacity; declare planned hours) + Sunday afternoon (full capacity; declare planned hours or state "not used this week") — do NOT derive backward from a fake total; each component is an independent source
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
| **TYPE B** | Personal deep-work / architecture / design | Layer 2 | Personal evenings (19:30–21:30, Mon–Fri) + Saturday daytime + Sunday afternoon (if named). Weekend evenings: the **explicitly opened** evening only (per R10 — one must remain protected rest); office hours: FORBIDDEN. | Cannot use any office hours (all office = TYPE A Zephyr); cannot use closed weekend evening | Block-model (1 block ≈ 1.5–3h focused work); evening slots; Sat daytime = regular work capacity |
| **TYPE C** | Async / spec / review / coordination | Layer 3 | Personal evenings (19:30–21:30, Mon–Fri) + Saturday daytime + Sunday afternoon (if named). Weekend evenings: the **explicitly opened** evening only (per R10); office hours: FORBIDDEN. | Must not crowd out TYPE B deep focus; cannot use closed weekend evening | Interruptible, async-compatible; fills personal time gaps (not office gaps) |
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

### R4 — Goal effort estimates and capacity allocation are TYPE-aware

**For TYPE B and TYPE C projects:**
The effort estimate in the Goals section must equal the hours allocated in the Capacity section. If they do not match, either the estimate or the allocation is wrong. Validate both before finalizing.

**For TYPE A projects (office-baseline, e.g., Zephyr):**
TYPE A projects own the entire assigned pool (Pool A = ~36h effective). Two values must be tracked separately and must NOT be collapsed into one number:
- **Pool Ownership Hours:** The full effective pool size (~36h). This is what goes in the capacity table Hours column.
- **Focused Mission Effort:** The scoped weekly deliverable inside the pool (e.g., ~12h for RAM test extension + factory analysis). This is what appears in the Goals effort estimate.
- **Reactive / KTLO / maintenance load:** The remainder (Pool Ownership − Focused Mission ≈ ~24h). Not a goal line; always present as structural baseline context.

Setting the capacity table Hours column to the goal effort number for a TYPE A project is a model error — it implies TYPE A only has ~12h of context, which contradicts pool ownership.

**TYPE A Truth Model Example:**
- Pool A effective: ~36h
- TYPE A owner: Zephyr (owns 100% of Pool A)
- Focused mission this week: ~12h (e.g., RAM tests + factory analysis + docs)
- Reactive / KTLO / maintenance: ~24h remainder (standups, code review, support, unplanned context)
- Capacity table shows: Pool Ownership = ~36h + sub-row "Focused mission: ~12h" (see §7 template)
- Goal effort estimate in Goals section = ~12h (focused mission only — not the pool size)

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
  Realistic personal capacity = [net evening blocks] + [Sat daytime] + [Sun afternoon if planned]
  Gross weekday-evening baseline = 10h (2h × 5 evenings, 19:30–21:30 Mon–Fri)
  Net planned evening capacity = gross − structural deductions (derive per week from anchor table)
    Structural deductions: Thu = S-only (energy dip); Fri = closure/none when planned that way
    These are recurring patterns, NOT rare exceptions; most weeks net ≈ 6–8h from weekday evenings
  Saturday daytime = full project execution capacity; declare planned hours in the week plan
  Sunday morning = review/closeout/planning (~2–3h; NOT Pool B execution capacity; overhead)
  Sunday afternoon = full project execution capacity; declare planned hours or state "not used"
  Weekend evenings: exactly 1 is OFF (protected rest); 2nd = default-rest, may be opened by week plan
    The week plan must declare which evening is OFF (Sat or Sun)

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
- **Planning allocation:** Pool A office hours must be allocated **only to TYPE A (Zephyr)** and TYPE D overhead. Personal project planning allocation (RobotOS, Signee) against office hours violates this rule regardless of framing — "remaining capacity," "support hours," or any other label.
- **Execution delegation (exception — not a contradiction to the above):** At daily execution level, Zephyr may delegate a bounded slice of office hours to Project Accountant under R9-DEL guardrails. This borrowing is tracked daily and does NOT constitute planning-level allocation for Project Accountant. Correct framing after delegation: "Project Accountant is Pool B; daily delegation occurred" — NOT "Project Accountant now has office hours."
- Framing like "Project Accountant borrows office time regularly → it now has office allocation" is a back-propagation violation.
- Framing like "Zephyr evening work to free up office time" violates this rule (Pool A is office-only; Pool B is personal-only in both directions).
- If Pool B capacity is insufficient for personal project goals: reduce scope or span goal to next week.

---

### R9-DEL — Delegation Guardrails (Execution Level Only)

Delegation is the mechanism by which Zephyr allows Project Accountant to borrow a bounded slice of office time on a given day. It is an execution-level action, not a planning-level re-allocation.

**Delegation conditions (ALL must be satisfied):**
- Delegation is approved on a per-day basis during morning daily planning — never as a weekly or monthly pre-commitment
- Zephyr KTLO floor is verified first: if Zephyr has an unresolved critical blocker for today, delegation is suspended
- Delegation window is bounded: ≤2h per day maximum
- Delegation is recorded in the daily log entry as: `DEL: [project] borrowed [Xh] office time on [date]`
- Delegation does NOT appear in weekly capacity totals as office allocation for the borrowed project

**Back-propagation guard:**
- Weekly review must not accumulate delegation totals into planning-level allocation (e.g., "Project Accountant used 8h office over W14 → it now gets 8h office in W15" = violation)
- Delegation history informs scope judgment but does NOT alter pool ownership
- CAPACITY_ENGINE planning model remains: Project Accountant = Pool B; delegation = execution-level event

**Sources confirming pool separation:**
- OS daily schedule: Job 1 (08:30–17:00) = Zephyr; Personal evening (19:30–21:30) = RobotOS/Signee
- Zephyr_Project_Context §5: "Executed during office hours only. No regular evening deep work."
- Zephyr_Project_Context §7: "Do not schedule Zephyr work in evening blocks. Protect capacity for Signee (Phase 1) and RobotOS (Phase 2)."

---

### R10 — Weekend Calendar Pattern and Sustainability

Weekend daytime and evening slots serve distinct functions and must be modeled explicitly.

**Weekend daytime:**
- **Saturday daytime: full project execution capacity** — not optional; always a real capacity source; declare planned project hours in each week plan; do not shrink or label as "mini-block"
- **Sunday morning: review / closeout / planning capacity** — structural weekly function (~2–3h); consumed by WEEK_CLOSEOUT + next-week seed; NOT project execution; counted as overhead in total weekly load; do NOT merge with Sunday afternoon execution
- **Sunday afternoon: full project execution capacity** — not optional; always a real capacity source; declare planned project hours or explicitly state "not used this week" as a W## instance decision

**Weekend evenings:**
- Exactly ONE weekend evening is OFF (protected rest); the week plan must name which one (Sat or Sun)
- The other weekend evening is default-rest and may be explicitly opened by the weekly plan when genuinely needed
- Do NOT treat both weekend evenings as always hard-OFF
- Do NOT treat both weekend evenings as freely allocatable
- If a weekend evening is opened, it must be named explicitly in the plan (not implied)

If a plan requires weekend evening execution to close, first check whether scope reduction is a better option. If genuinely used, it must be named explicitly.

**Sustainability balance principle:**
- Do NOT model personal capacity so low (~6–8h) that the engine systematically underestimates achievable personal work and forces unnecessary multi-week spans
- Do NOT model personal capacity so high (all evenings + all weekend day + all weekend evening) that burnout becomes the hidden cost of meeting weekly goals
- Correct gross baseline: 10h/week weekday evenings (Mon–Fri 19:30–21:30) + explicitly named weekend daytime + named Sunday review block
- Net execution baseline: lower than gross most weeks; derive from anchor reality; do not plan personal work against 10h gross as if fully executable

---

### R11 — Weekend Usage Decision Policy (Slot-Based Modeling)

**CRITICAL RULE: Weekend must be modeled by SLOT, not by day.**

Weekend is not "Saturday" and "Sunday" as single units. It is **five distinct time slots**, each with a different function:

1. **Saturday daytime** — project execution capacity (same as Sun afternoon)
2. **Saturday evening** — weekend evening OFF/OPEN decision (Friday/Sat evening pair)
3. **Sunday morning** — review/closeout/planning overhead (structural, ~2–3h)
4. **Sunday afternoon** — project execution capacity (same as Sat daytime)
5. **Sunday evening** — weekend evening OFF/OPEN decision (Sat/Sun evening pair)

**Anti-Conflation Invariant (MUST BE ENFORCED):**
- Sunday afternoon and Sunday evening are **completely separate slots with different functions**. They must never be conflated.
  - "Sunday used" could mean either afternoon (execution) or evening (rest decision) — FORBIDDEN wording
  - "Sunday unused" could mean either afternoon (execution) or evening (rest decision) — FORBIDDEN wording
  - Always use slot-level language: "Sunday afternoon execution = Xh" and "Sunday evening = [OFF/OPEN]"
- Saturday daytime and Saturday evening are **completely separate slots with different functions**. They must never be conflated.
  - Same rule: always slot-level language "Saturday daytime = Xh" and "Saturday evening = [OFF/OPEN]"
- Sunday morning is a separate **review/control slot** and must never be merged into execution or evening-rest logic.

Weekend capacity is **not optional by default.** Saturday daytime and Sunday afternoon are full execution capacity classes and must be treated as primary execution surfaces, not overflow buffers.

A week must explicitly choose **one of three modes** for how it uses available weekend capacity:

#### MODE A — Full Utilization (All Day-Slots Active)
- **Saturday daytime:** Fully used for planned project execution
- **Sunday morning:** Review/closeout as scheduled
- **Sunday afternoon:** Used for planned project execution
- **Weekend evening decision:** One of {Sat evening, Sun evening} is OFF; the other may be OPEN or default-rest
- **Use when:** Personal project portfolio is substantial (~10h+ allocation) and requires full system capacity
- **Slot declaration:** Sat daytime = [X hours], Sun afternoon = [Y hours], evening OFF = [Sat or Sun]

#### MODE B — Saturday-Primary (Common but NOT Default)
- **Saturday daytime:** Fully used for planned project execution
- **Sunday morning:** Review/closeout as scheduled
- **Sunday afternoon:** Optional/reserve — used only if workload exceeds (net weekday evenings + Sat daytime) capacity
- **Weekend evening decision:** One of {Sat evening, Sun evening} is OFF; the other is default-rest
- **Use when:** Personal project allocation is moderate (~7–10h) and fits within net weekday evenings + Sat daytime
- **Distribution evaluation (see R11-D heuristic):** Before selecting MODE B, planner should evaluate whether MODE A (Sat + Sun) provides better load balance when weekend execution is non-trivial (≥3h)
- **Constraint:** If Sunday afternoon is stated as "0h" (not used), the math must prove that weekday evening + Saturday daytime is sufficient for stated allocation
- **Slot declaration:** Sat daytime = [X hours], Sun afternoon = "not used this week" OR [Y hours], evening OFF = [Sat or Sun]

#### MODE C — Reduced Weekend (EXPLICIT ONLY)
- **Saturday daytime:** Reduced, partial use, or zero use
- **Sunday afternoon:** Zero use OR partial
- **Sunday morning:** Review/closeout, or reduced
- **Weekend evening decision:** One of {Sat evening, Sun evening} is OFF; other is default-rest
- **REQUIRED:** Explicit justification (scope constraint, sustainability break, blocker impact)
- **REQUIRED:** Impact statement (e.g., "Saturday daytime not used this week because all RobotOS scope (~7h) fits within net evening capacity; Sunday afternoon not planned as reserve; total weekly load = ~48h vs. normal ~50–51h")
- **Use when:** Conscious decision to reduce scope or take a lighter week (not default fallback)
- **Slot declaration:** Sat daytime = "not used" OR [X hours], Sun afternoon = "not used" OR [Y hours], evening OFF = [Sat or Sun]

**Forbidden Patterns (MUST BE ENFORCED):**
- Do NOT default Saturday to partial use (~2h) without explicit scope decomposition linking the allocation to defined content (e.g., "M5 onboarding notes = ~2h")
- Do NOT set Sunday afternoon to 0h by claiming "fits within Sat + evenings" unless the math is proven in the exact numbers (not rounded) and the proof is documented
- Do NOT treat Saturday daytime as a "spillover destination" for unplanned overflow if it is already allocated as a primary execution block for defined content
- Do NOT leave weekend mode implicit; explicitly declare Mode A / B / C and justify it
- Do NOT use vague language like "Sunday unused" or "Sunday open" — must specify WHICH Sunday slot (afternoon or evening)
- Do NOT conflate Saturday evening (OFF/OPEN decision) with Saturday daytime (execution capacity)
- Do NOT conflate Sunday afternoon (execution capacity) with Sunday evening (OFF/OPEN decision)

**Traceability Requirement (All Five Slots Must Be Declared):**

Every weekly plan's weekend usage decision must include:
1. **Selected mode** — one of: Full Utilization (A), Saturday-Primary (B), Reduced Weekend (C)
2. **Slot 1 — Saturday daytime:** [X hours planned execution] OR [0h if not used]
3. **Slot 2 — Saturday evening:** [OFF (protected rest)] OR [OPEN if explicitly needed]
4. **Slot 3 — Sunday morning:** [Review/closeout ~2–3h overhead]
5. **Slot 4 — Sunday afternoon:** [Y hours planned execution] OR [0h not used this week]
6. **Slot 5 — Sunday evening:** [OFF (protected rest)] OR [OPEN if explicitly needed]
7. **Justification** — link to project scope, milestones, or sustainability decision
8. **Math closure** — if any execution slot (Sat daytime or Sun afternoon) = 0h, show the arithmetic proving remaining capacity is sufficient for that week's allocation
9. **Link to totals** — reference the total weekly load calculation that depends on this decision

**Generator Alignment Note:**

`GENERATE_WEEKPLAN`, when creating a WeekPlan, must:
- Force explicit slot-level declaration for all five weekend slots in Step 5 (Determine Weekly Goals) or Step 6 (Assess Capacity)
- NOT assume reduced weekend usage or let a plan default to Mode B / Mode C without explicit rationale
- Reject any generation that produces day-based language ("Sunday used/unused") instead of slot-based language
- NOT allow mode selection without all five slot values populated

The generator instruction in `GENERATE_WEEKPLAN` §[Spillover Handling] stating "Sat daytime absorbs RobotOS spillover" must be reframed:
- If Sat daytime is already allocated to a primary milestone (e.g., M5), it is NOT available for spillover unless that milestone completes early
- If Sat daytime is not pre-allocated to primary content, it remains available for spillover, but this must be declared explicitly in the mode selection (e.g., "Sat daytime available as reserve: [Yh capacity]")
- Generators must state: "Saturday daytime is primary project capacity, not a spillover buffer" to prevent planners from defaulting to treating weekend as 'overflow only'
- Generator must prioritize Sunday afternoon as spillover destination FIRST, then Saturday only if Sunday is pre-allocated or unavailable (see R11-D)
- Generator must never produce mode declarations without explicit slot values for all five weekend slots

---

### R11-D — Weekend Distribution Heuristic (Non-Rigid Guidance)

**Purpose:** Guide weekend execution distribution between Saturday daytime (Slot 1) and Sunday afternoon (Slot 4) to reduce single-day load clustering while maintaining flexibility.

**Heuristic (guidance; not enforcement):**

1. **If weekend execution is small (≤2h):** OK to allocate fully to Saturday (Sat 2h, Sun afternoon 0h). Single-day clustering acceptable.

2. **If weekend execution is moderate (3–4h):** Planner should **consider** a Sat + Sun split to reduce single-day fatigue load. Saturday-only is permitted but SHOULDbe consciously evaluated and documented (not defaulted silently).

3. **If weekend execution is high (≥5h):** Planner MUST actively evaluate Sat + Sun distribution. Saturday-only ≥5h requires explicit justification (e.g., "All 5h allocated to RobotOS high-complexity synthesis; MODE A acceptable given project priority; fatigue risk accepted").

**Spillover Priority (NON-RIGID):**
- If scope uncertainty exists and spillover is possible:
  - **First consider:** Sunday afternoon (Slot 4) as spillover destination if available
  - **Then consider:** Saturday daytime (Slot 1) remainder capacity if Sunday is pre-allocated
  - **State explicitly:** Do not leave spillover path implicit; name which slot absorbs planned overflow

**Anti-Dual-Role Rule (CRITICAL):**
- Saturday daytime (Slot 1) MUST NOT simultaneously act as both:
  - Primary execution block (e.g., "M5 onboarding = 3h") AND
  - Implicit spillover buffer for unplanned work
  - If spillover is expected, it must be explicitly assigned (either to Sunday afternoon or stated as "no spillover path exists")
- Rationale: Conflating roles makes capacity math unclear and enables silent overload

**When to Document Distribution Decision:**
- If weekend execution ≥3h: note in Anchor Rationale or Soft Constraints whether Sat+Sun split was evaluated and why chosen distribution was selected
- If Sat ≥3h and Sun afternoon 0h: document the intentionality (e.g., "Sunday afternoon not used; all scope fits within Sat + weekday allocation; math proof: [values]")
- This documentation helps future weeks learn from this decision and prevents thoughtless repetition

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
| Goal-allocation match | V6 | **TYPE B/C:** each goal's effort estimate equals capacity allocated. **TYPE A:** pool ownership row = effective pool size (~36h); focused mission sub-row present AND ≤ pool ownership; focused mission ≠ pool ownership is expected and valid | **TYPE B/C:** \|goal effort\| − \|capacity allocated\| > 1.5h per goal. **TYPE A:** pool ownership row missing; OR focused mission sub-row absent; OR focused mission effort > pool ownership |
| Anchor-layer consistency | V7 | Daily anchor time slots are consistent with project type assignments | TYPE A and TYPE B listed as equivalent daily anchors with no time-slot distinction |
| Daily scope rule | V8 | Max 2 projects active per day can be verified given layer assignments | Ambiguous which 2 projects are active in which time slots |
| Capacity sum | V9 | Total allocated hours ≤ realistic weekly capacity (office + named evening) | Total allocation exceeds modeled capacity |
| Split-Signee rule | V10 | Signee sub-components with different types are allocated separately | All Signee work assigned one TYPE; blocks baseline allocation |
| Pool isolation | V11 | Pool A (office) contains only TYPE A + TYPE D; Pool B (personal) contains only TYPE B + TYPE C; no cross-pool hours exist | Any personal project (TYPE B/C) has hours attributed to office hours; or Zephyr has hours attributed to personal blocks |
| Weekend usage decision | V12 | All five weekend slots explicitly declared per R11: Mode selected (A/B/C); Sat daytime [value]; Sat evening [OFF/OPEN]; Sun morning [review]; Sun afternoon [value]; Sun evening [OFF/OPEN]; math proof if any execution slot = 0h | Weekend mode not declared; OR any slot declared vaguely or missing; OR day-based language used instead of slot-based (e.g., "Sunday unused" without specifying afternoon vs. evening); OR execution slot value not linked to project scope; OR math proof absent when execution slot = 0h |
| Weekend effort realism | V13 | Weekend-allocated work has M-level task breakdown; each task fits in declared slot capacity (Sat daytime ≤1–2 M-blocks, Sun afternoon ≤1 M-block); spillover path exists (other weekend slot or deferral documented) | Weekend scope cannot be decomposed into realistic focus-blocks; OR declared slot hours insufficient for identified scope +10% spillover scenario; OR spillover has no named path (implicit overflow) |
| Personal capacity ceiling | V14 | Total personal execution (net weekday evening + weekend day hours) ≤ 18h/week (sustainable); if >18h, assumption documented; trend analysis shows personal load not increasing >2h × 3 consecutive weeks | Personal execution >20h/week (unsustainable); OR personal load trending upward >2h/week for 3+ weeks without escalation |
| No hidden office allocation | V15 | Any non-Zephyr project appearing in office-hour blocks has an explicit `DEL:` delegation marker in the daily plan; no framing ("remaining capacity", "support hours") disguises personal project office use; R9-DEL guardrails satisfied for all flagged entries | Non-Zephyr work in office-hour block without `DEL:` marker; OR marker present but R9-DEL guardrails not satisfied |
| Delegation recorded as borrowing | V16 | All approved delegation events logged as `DEL: [project] borrowed [Xh] on [date]`; delegation totals NOT accumulated into planning-level allocation; no "Project Accountant now has Xh office" framing in weekly review | Delegation events unlogged; OR weekly review attributes delegation totals to planning allocation (back-propagation violation) |
| Pool B serialization enforced | V17 | Max 1 personal project active per evening; no dual-project stacking in weekday evenings; all Pool B evening work ≥0.5h recorded in Evening Check; evening not normalized to 2h+ as standard planned mode | Two personal projects active same evening; OR Pool B work not tracked in Evening Check; OR 2h+ evening occurring on 3+ nights/week as standard planned pattern (normalization overload) |
| Zephyr KTLO floor protected | V18 | Before any delegation is approved on a given day, Zephyr KTLO floor is satisfied (no unresolved critical Zephyr blockers today); delegation suspended if KTLO floor check fails | Delegation approved with unresolved Zephyr KTLO critical work; OR daily log shows delegation without KTLO floor verification |
| Drift trigger | V19 | CAPACITY_ENGINE.md model rules align with current month plan's capacity model; no superseded rules remain in generator documents (GENERATE_WEEKLY_EXECUTION.md §8, etc.) without explicit deprecation; delegation-exception-aware wording present in all engine boundary statements | Generator document contains superseded rules (model drift); OR "ALL remaining office hours = Zephyr exclusive" language appears without delegation exception; OR delegation model introduced in month plan not reflected in engine |

---

## 6.1 Validation Check Details: V13 — Weekend Effort Realism

**Purpose:** Ensure declared weekend hours can realistically accommodate project scope without silent spillover or artificial compression.

**Validation Steps:**

1. **Task Decomposition**
   - For each project allocated to weekend (TYPE B or TYPE C):
     - List all M-sized missions or execution phases assigned to Sat daytime and Sun afternoon
     - For each mission, state effort (hours) and focus type (architectural, implementation, specification, etc.)
   - Check: Does sum of listed tasks ≈ declared slot hours? (within ±1h margin)
   - Failure: Scope cannot be accounted for in declared slots ("8h declared but only 5h of identified work")

2. **Slot Fit Analysis**
   - Saturday daytime (5–6h available):
     - Can hold ≤1 deep M-block (3–4h execution + setup/breaks) with margin
     - Can hold 2 small independent tasks (1.5–2h each)
     - Overfull if: single 4h+ mission + another 3h+ mission = back-to-back execution (unrealistic)
   - Sunday afternoon (3–4h available, after morning review):
     - Can hold ≤1 M-block (2–3h execution given post-weekend fatigue)
     - Large second tasks should use Sat daytime, not Sun
   - Failure: Declared Sat 8h with scope list showing 2×4h tasks (impossible to execute start-to-finish Sat without spillover)

3. **Spillover Scenario (Assume +10–15% Overrun)**
   - If project work exceeds declared slot by 10% (realistic overrun margin):
     - ✓ Path exists: spillover fits in other weekend slot (Sat→Sun or vice versa)
     - ✓ Path exists: spillover fits in declared weekday evening block with identified capacity
     - ✓ Path exists: spillover deferred to next week with explicit decision + impact noted
     - ✗ Failure: "Spillover will just happen" (implicit absorption, no named path)

**When Applied:**
- After V12 (slot declaration) validates slots are named
- After V6 (goal-allocation match) validates effort estimates
- Before accepting weekend mode and slot allocation

**Output:** PASS / WARN / FAIL
- **PASS:** Weekend hours fully decomposed; spillover path exists or margin is safe
- **WARN:** Declared hours moderately exceed identified scope (+20–30%); proceed if cleanup explicitly named
- **FAIL:** Scope cannot be decomposed into realistic blocks; or spillover has no path

---

## 6.2 Validation Check Details: V14 — Personal Capacity Ceiling

**Purpose:** Ensure total personal execution (weekday evening net + weekend daytime) remains sustainable and does not exhibit unsustainable trending.

**Validation Steps:**

1. **Personal Capacity Calculation**
   - Start with gross weekday evening: 10h/week (2h × 5 evenings, 19:30–21:30 Mon–Fri)
   - Subtract structural deductions (from this week's anchor):
     - Thu = S-only energy dip (typically 0–1h available)
     - Fri = closure or S-only (typically 0–1h available)
     - Result: net weekday evening capacity (typically 5–8h/week realistically executable)
   - Add weekend daytime:
     - Sat daytime: declared hours (full execution capacity)
     - Sun morning: ~2–3h (review/overhead, NOT execution capacity; separate)
     - Sun afternoon: declared hours (if used; 0h if not planned)
   - Total personal execution: [net evening] + [Sat] + [Sun afternoon] = X h/week

2. **Sustainability Bands**
   - **11–18h/week:** PASS — normal sustainable range
   - **18–20h/week:** WARN — stretched week; requires explicit decision + assumption documentation; if pattern continues 3+ weeks, escalate
   - **>20h/week:** FAIL — unsustainable; scope reduction required OR explicit strategic decision to accept sprint (must escalate to month context)

3. **Trend Analysis (Multi-Week Pattern)**
   - Compare this week's personal execution to W-1, W-2, W-3
   - Calculate trend:
     - Flat (Δ <1h): no trend concern ✓
     - Mild increase (Δ 1–2h/week): monitor ⚠️
     - Steep increase (Δ >2h/week × 3 consecutive weeks): escalate ❌
   - If personal load increases >2h/week for 3+ consecutive weeks without escalation decision, V14 fails

**When Applied:**
- After V13 (weekend effort realism) confirms weekend hours are decomposable
- After V9 (capacity sum) validates total allocation
- Before finalizing capacity model

**Output:** PASS / WARN / FAIL
- **PASS:** Personal execution 11–18h/week; trend flat or mild (Δ <2h/week); sustainable
- **WARN:** Personal execution 18–20h (stretched) requiring assumption documentation; OR personal load trending +2h × 2 weeks (monitor for escalation trigger)
- **FAIL:** Personal execution >20h/week (unsustainable sprint); OR personal load trending >2h × 3+ consecutive weeks without escalation

---

## 7. Output Contract

The engine produces a **Capacity Summary block** that the weekly plan's `## Capacity & Constraints` section must include.

### Required Output Fields

```markdown
## Capacity & Constraints — ENGINE OUTPUT

### POOL A — Office-Locked Capacity (Layer 1)

| Component | Type | Hours | Constraint |
|---|---|---|---|
| [TYPE A project — Zephyr] | TYPE A | ~36h (Pool A owner) | **Office hours only. Gross 40h. Effective after D1 overhead: ~36h. Zephyr owns this entire pool.** |
| ↳ Focused mission (W## deliverable) | — | ~[focused h] | Scoped weekly deliverable inside Pool A. NOT the pool size. Matches Goals §[n] effort estimate. Remainder (~36h − focused h) = reactive / KTLO / maintenance. |
| Admin / comms (D1 overhead) | TYPE D | [h/week] | Inside Pool A. Subtracted from gross. |
| **Pool A total** | — | ~40h gross | **100% office hours. Zero remaining for personal projects.** |

> Pool A boundary: ALL office hours belong to TYPE A (Zephyr) + TYPE D overhead.
> No personal projects (TYPE B, TYPE C) may be allocated against this pool under any framing.

### POOL B — Personal Flex Capacity (Layers 2+3)

| Project | Type | Personal Blocks (Source) | Hours | Notes |
|---|---|---|---|---|
| [TYPE B project — RobotOS] | TYPE B | Evenings: [days] (19:30–21:30); Sat daytime; Sun afternoon (if named) | [h] | Deep-work blocks; execution; no office hours; closed weekend evening FORBIDDEN |
| [TYPE C project — Signee] | TYPE C | Evenings: [days] (19:30–21:30); Sat daytime; Sun afternoon (if named) | [h] | Spec/coordination; async-compatible; no office hours; closed weekend evening FORBIDDEN |
| [TYPE E items] | TYPE E | — | 0 (conditional) | Activates if: [trigger event] |
| **Pool B execution total** | — | Net weekday evenings ([gross 10h − deductions]) + Sat daytime + Sun afternoon (if named) | [sum] | Ceiling = net evening + Sat + Sun (if planned — declare hrs or state not used); NOT gross 10h |

> Pool B boundary: ALL personal project execution must be sourced from named personal blocks only. Cannot use office hours. Cannot use closed weekend evening.
> Sunday morning review (~2–3h) is structural weekly overhead — separate from Pool B execution; included in total weekly load.

### Capacity Summary

| Pool | Source | Gross | Structural deductions | Net execution available | Allocated | Utilization | Status |
|---|---|---|---|---|---|---|---|
| **Pool A — Office-Locked** | Office hours (weekdays) | ~40h | TYPE D overhead (~4h) | ~36h effective | Zephyr + D1 | ~100% | Zephyr only; no personal |
| **Pool B — Personal Flex** | Weekday evenings + Sat daytime + Sun afternoon (if named) | 10h eve + [Sat h] + [Sun aft h] | Thu deduction + Fri deduction | Net: [h] + [Sat h] + [Sun aft if named] | TYPE B + TYPE C | [%] | PASS / WARN / FAIL |
| **Sunday review overhead** | Sun morning (structural) | ~2–3h | — | N/A (not execution) | WEEK_CLOSEOUT + planning seed | — | Required each week |

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
| Weekend usage decision | V12 | PASS / FAIL | |
| Weekend effort realism | V13 | PASS / WARN / FAIL | |
| Personal capacity ceiling | V14 | PASS / WARN / FAIL | |

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
| Zephyr (TYPE A — test extension + operational) | TYPE A | ~36h (Pool A owner) | Office hours only. No evening. Gross 40h − 4h D1 = 36h. Source: Zephyr_Project_Context §5, §7. |
| ↳ Focused mission (W11 deliverable) | — | ~12h | Test extension goal (RAM tests + factory analysis + docs). NOT the pool size. Remainder (~24h) = KTLO / ops / reactive. |
| Admin / comms (D1) | TYPE D | 4h | Inside Pool A. Standard overhead. |
| **Pool A total** | — | ~40h gross | **100% office hours. Zero allocated to personal projects.** |

### POOL B — Personal Flex Capacity (Layers 2+3)

| Project | Type | Personal Blocks (Source) | Hours | Notes |
|---|---|---|---|---|
| RobotOS (architecture + onboarding) | TYPE B | Mon–Wed evenings (19:30–21:30, ~6h full exec); Sat 3/21 daytime (planned; W11 uses ~2h for M5/onboarding prep); Sun 3/22 afternoon (W11 instance decision: not used) | ~7h | W11 partial allocation; full goal (~15h) spans W11–W12; no office hours; closed weekend evening FORBIDDEN |
| Signee (testing specification) | TYPE C | Fri 3/20 evening (~1h S-only or none); Sat daytime overlap with RobotOS if needed; Sun afternoon not planned W11 | ~3h | W11 partial allocation; no office hours; no closed weekend evenings |
| Board testing (Signee) | TYPE E | — | 0 conditional | Activates when: hardware delivered |
| **Pool B execution total** | — | Net weekday evenings (~6–7h, after Thu/Fri deductions) + Sat 3/21 daytime (~2h W11) + Sun 3/22 afternoon (0h W11 instance decision) | ~9h | Ceiling = net eve + Sat + Sun aft(if used); W11 does not use Sun afternoon execution — explicit instance decision; gross 10h eve is envelope, not ceiling; allocation ~7h+~3h within ceiling |

### Capacity Summary

| Pool | Source | Gross | Structural deductions | Net execution available | Allocated | Utilization | Status |
|---|---|---|---|---|---|---|---|
| Pool A — Office | Office hours | ~40h | D1 overhead ~4h | ~36h effective | Zephyr + overhead | ~100% | Full; contains Zephyr only |
| Pool B — Personal | Weekday evenings + Sat 3/21 daytime + Sun aft (not used W11) | 10h eve + [Sat h] + [Sun aft h] | Thu ~1h + Fri ~1h | Net eve ~6–7h + Sat ~2h + Sun aft 0h (W11) = ~8–9h exec cap | RobotOS ~7h + Signee ~3h | ~100% within ceiling | PASS |
| Sunday review overhead | Sun 3/22 morning | ~2h | — | N/A (not execution) | WEEK_CLOSEOUT + W12 seed | — | Required |

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
