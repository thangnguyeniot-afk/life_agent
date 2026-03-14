# TASK_INTAKE_AND_ADMISSION.md — Task Intake & Admission Subsystem

> **Version:** v1.0
> **Status:** Active
> **Placement:** Sits between backlog/mission intent and weekly/daily execution planning.
> **Canonical OS rule:** §12.11

---

## 1. Purpose

This subsystem standardizes task analysis before scheduling.

It exists to reduce drift caused by:
- vague tasks with no clear stopping point
- oversized tasks admitted directly into weekly execution
- high-ambiguity tasks scheduled without prior clarification
- artifact-less tasks that produce invisible or unverifiable progress
- project-context mismatch (e.g., Zephyr work shaped like vague architecture exploration)

It does not replace judgment.
It reduces cognitive load by applying project-aware defaults and structured admission logic.

---

## 2. When to Use Task Intake

**No intake card needed:**
- XS tasks
- S tasks with ambiguity 0–1
- Repeated routine tasks with known procedure (previously completed pattern)
- Ambiguity 0–1 and artifact already obvious

**Quick intake only (Level 1):**
- Most normal M tasks
- New but simple tasks
- Routine planning or coordination decisions

**Full analysis card required (Level 2 + Level 3):**
- Any M task with ambiguity ≥ 3
- Any L or XL task
- Any architecture / research / design task
- Any task tied to a weekly or monthly mission
- Any task that may span multiple sessions
- Any task with unclear expected artifact
- Any task that has been re-added or deferred 2+ times

**Default heuristic:** If the task will take more than one focused sitting and the artifact is not obvious, run Level 2.

---

## 3. Three-Level Model

```
Level 1 — Quick Intake
──────────────────────
Fast classification pass.
All non-trivial tasks enter here.

Level 2 — Task Analysis Card
─────────────────────────────
Deeper structured analysis.
Used for M+ / ambiguous / strategic / multi-session tasks.

Level 3 — Admission Decision
─────────────────────────────
Go / split / spike / clarify / backlog.
All non-trivial tasks must pass here before entering execution planning.
```

Not all tasks need Level 2.
All non-XS/S-routine tasks must pass Level 3.

---

## 4. Level 1 — Quick Intake

**Format (complete in under 60 seconds):**

| Field | Value |
|---|---|
| **Project** | Zephyr / RobotOS / Signee / system |
| **Phase / Mission context** | Which weekly or monthly mission this belongs to |
| **Raw task statement** | Exactly what was said or thought |
| **Intent** | execute / analyze / design / debug / validate / coordinate / document / research |
| **Expected output** | What should exist after this task runs |
| **Rough size** | XS / S / M / L / XL |
| **Rough ambiguity** | 0–5 |

**Quick intake examples:**

*Example A — passes without Level 2:*
- Project: Zephyr | Intent: validate | Output: test result log | Size: S | Ambiguity: 1
→ Admitted directly. Schedule in Office Hours.

*Example B — needs Level 2:*
- Project: RobotOS | Intent: design | Output: unclear | Size: M? | Ambiguity: 3
→ Must proceed to Level 2 before admission decision.

---

## 5. Level 2 — Task Analysis Card

Complete only for non-trivial tasks (see §2 threshold).

**1. Project Context**
- Project: Zephyr / RobotOS / Signee
- Phase / Mission / Anchor:

**2. Task Type** *(pick one)*
- Execution · Analysis · Design · Debug · Research · Validation · Coordination · Documentation

**3. Objective**
- What must become clearer / produced / verified:

**4. Done Boundary**
- What counts as a valid stop point for this session:
- What counts as "enough for this phase":

**5. Expected Artifact**
- What output must remain after the block or phase ends:
- (Examples: test log / scope draft / blockers note / ADR seed / checklist / question list / interface sketch)

**6. Ambiguity Source** *(mark all that apply)*
- [ ] Scope unclear
- [ ] Technical unknown
- [ ] Dependency unresolved
- [ ] Decision pending
- [ ] Output format unclear
- [ ] Sequencing unclear
- [ ] None — low ambiguity

**7. Estimated Size**
- XS (< 30 min) / S (30–60 min) / M (60–120 min) / L (half-day) / XL (multi-day)

**8. Decomposition Decision** *(pick one)*
- Keep as-is
- Split into 2 × M
- Split into M + S
- Convert to spike first
- Clarify scope first
- Not schedulable yet

**9. Scheduling Candidate** *(pick one)*
- Office Hours primary (Zephyr only)
- Office Hours support/admin (Zephyr only)
- Evening primary (RobotOS / Signee)
- Evening support/follow-up (RobotOS / Signee)
- Weekend deep block
- Backlog only

**10. First Anchor Step**
- The first concrete 10–15 min action to start this task:

**11. Re-entry Sensitivity**
- Low — single session, clean closure expected
- Medium — may span 2 sessions; re-entry pack useful
- High — multi-session; re-entry pack required when block ends unfinished

---

## 6. Level 3 — Admission Decision

**Allowed outcomes:**

| Decision | Meaning | Next action |
|---|---|---|
| **A. Ready for scheduling** | Task is clear, sized, artifact-defined, domain-valid | Produce block-ready execution spec (see §9) |
| **B. Ready only after split** | Task is valid but too large for one block | Produce child phases |
| **C. Convert to spike first** | Ambiguity too high for direct execution | Define bounded discovery artifact |
| **D. Clarify scope first** | Missing objective, artifact, or done boundary | Generate question list / constraints note / decision frame |
| **E. Waiting on dependency** | External blocker exists | Create watchpoint; do not schedule active work |
| **F. Backlog only** | Not schedulable now; no clear phase | Preserve intent; do not inject into weekly/daily execution |

**Decision logic:**

```
Ambiguity ≥ 4?                             → C or D
Size = XL?                                 → B (decompose first)
Artifact unclear?                          → D
Dependency unresolved?                     → E
Time domain invalid?                       → F or D
Evening + Evening Capacity Guard conflict? → B or F
Otherwise                                  → A
```

---

## 7. Hard Admission Rules

**Rule 1 — Artifact clarity gate:**
If the artifact is unclear, the task is NOT ready for execution planning.
Action: return to Level 2 §5; define expected artifact before proceeding.

**Rule 2 — Ambiguity gate:**
If ambiguity ≥ 4, the task may NOT be scheduled for direct execution.
It must first produce: a spike artifact / a scope clarification note / a question list / or a dependency resolution step.

**Rule 3 — XL decomposition gate:**
If size = XL, the task may NOT enter weekly/daily execution directly.
Decompose into schedulable phases (L or smaller) before admission.

**Rule 4 — Time domain gate:**
If the task does not fit a valid time domain, it is not schedulable yet.
- Zephyr tasks → Office Hours only (Mon–Fri, 9:00–17:30)
- RobotOS / Signee → Evening or Weekend
- Exception: requires explicit Morning Setup justification

**Rule 5 — Evening Capacity Guard:**
If evening scheduling is proposed, the task must respect Evening Capacity Guard.
- No L tasks on weekday evenings
- Max 1 primary (M) block per weekday evening

**Rule 6 — Re-entry sensitivity:**
If the task spans multiple sessions, re-entry sensitivity must be indicated.
- High re-entry sensitivity → re-entry pack required when block ends unfinished (OS §12.10)

---

## 8. Project-Aware Defaults

Use these defaults to reduce manual judgment when shaping tasks.

---

### Zephyr

| Property | Default |
|---|---|
| **Typical task types** | Validation · debug · blocker isolation · toolchain check · execution |
| **Typical artifacts** | Test log · repro note · blocker summary · status update · checklist |
| **Common ambiguity sources** | Environment · integration dependency · toolchain behavior |
| **Scheduling preference** | Office Hours only (Mon–Fri, 9:00–17:30) |
| **Typical done boundary** | Verified / reproduced / blocker isolated / evidence captured |
| **Anti-patterns** | Vague architecture work during office hours; scope expansion inside a verification task |

---

### RobotOS

| Property | Default |
|---|---|
| **Typical task types** | Analysis · design · architecture shaping · scope definition · boundary clarification |
| **Typical artifacts** | Scope draft · ADR seed · architecture note · constraints note · interface sketch · open questions list |
| **Common ambiguity sources** | Scope · architecture decision · sequencing · abstraction boundary |
| **Scheduling preference** | Evening primary block or weekend deep block |
| **Typical done boundary** | One architectural decision clearer / one artifact advanced / one boundary reduced |
| **Anti-patterns** | Scheduling during office hours; treating architecture tasks like execution tasks; admitting without artifact boundary |

---

### Signee

| Property | Default |
|---|---|
| **Typical task types** | Validation · integration check · protocol clarification · issue reproduction · support diagnosis |
| **Typical artifacts** | Issue summary · checklist · test note · integration status · evidence log |
| **Common ambiguity sources** | Protocol behavior · integration dependency · reproduction gap |
| **Scheduling preference** | Evening support/follow-up or bounded evening primary block |
| **Typical done boundary** | Verified / narrowed / reproduced / documented |
| **Anti-patterns** | Open-ended discovery without a defined reproduction target; admitting with unclear done boundary |

---

## 9. Block-Ready Output Format

When a task passes admission (Decision A), format it for execution placement:

```
- Anchor: [Project]
- Goal: [one sentence]
- Size: [XS / S / M / L]
- Ambiguity: [0–5]
- Expected Artifact: [specific output]
- First Step: [concrete 10–15 min action]
- Suggested Slot: [Office Hours primary / Office Hours admin / Evening primary / Evening support / Weekend]
- Re-entry Risk: [low / medium / high]
```

This format maps directly into weekly and daily execution pages.

---

## 10. Admission Checklist (fast validation)

Before scheduling any non-trivial task, confirm:

- [ ] Project is clear
- [ ] Objective can be stated in one sentence
- [ ] Artifact is clear and specific
- [ ] Size is schedulable (not XL without decomposition)
- [ ] Ambiguity is acceptable for direct scheduling (< 4)
- [ ] Time domain is valid (Work Time Domain rule respected, OS §12.8)
- [ ] Capacity fit is valid (Evening Capacity Guard respected if evening slot, OS §12.9)

If any item fails → do not schedule. Apply the appropriate pre-step (split / spike / clarify).

---

## 11. Examples

---

**Example 1 — Zephyr validation task (passes admission)**

Level 1:
- Project: Zephyr | Intent: validate | Output: test result log | Size: S | Ambiguity: 1

Level 3 — Admission: **A. Ready for scheduling**

Block-ready output:
```
- Anchor: Zephyr
- Goal: Run smoke test suite on mainline; confirm no regressions
- Size: S | Ambiguity: 1
- Expected Artifact: Test result log ("Green" or "Issues: [list]")
- First Step: Pull latest mainline; run build + smoke tests
- Suggested Slot: Office Hours support/admin
- Re-entry Risk: Low
```

---

**Example 2 — RobotOS architecture task (passes after Level 2)**

Level 1:
- Project: RobotOS | Intent: design | Output: unclear at first | Size: M? | Ambiguity: 2

Level 2 findings:
- Task Type: Design
- Objective: Define v0.1 layer boundaries
- Done Boundary: Layer interface sketch complete; key unknowns listed
- Expected Artifact: Interface sketch + open questions list (3–5 items)
- Ambiguity Source: Abstraction boundary
- Size: M | Decomposition: Keep as-is
- Scheduling Candidate: Evening primary

Level 3 — Admission: **A. Ready for scheduling**

Block-ready output:
```
- Anchor: RobotOS
- Goal: Draft v0.1 layer boundary interface sketch
- Size: M | Ambiguity: 2
- Expected Artifact: Interface sketch + open questions list
- First Step: Review spike notes; sketch 3-layer boundary on doc/paper
- Suggested Slot: Evening primary (not office hours)
- Re-entry Risk: Medium — re-entry pack required if block ends unfinished
```

---

**Example 3 — Signee integration task (passes admission)**

Level 1:
- Project: Signee | Intent: validate | Output: reproduction note | Size: S | Ambiguity: 2

Level 3 — Admission: **A. Ready for scheduling**

Block-ready output:
```
- Anchor: Signee
- Goal: Reproduce board baseline issue; confirm reproduction path
- Size: S | Ambiguity: 2
- Expected Artifact: Reproduction note ("Confirmed: step 3 fails" or "Cannot repro: env diff")
- First Step: Flash board with latest firmware; run baseline validation checklist
- Suggested Slot: Evening support/follow-up
- Re-entry Risk: Low
```

---

**Example 4 — Fails admission: ambiguity too high**

Level 1:
- Project: RobotOS | Intent: research | Size: M | Ambiguity: 4

Level 3 — Admission: **C. Convert to spike first**

Pre-step output:
- Create bounded spike: "RobotOS/Zephyr scheduler integration — 90-min bounded discovery"
- Spike artifact: question list + preliminary findings
- Spike scope: what must be known to make the design task schedulable?
- Do not schedule the original M task until spike is complete.

---

**Example 5 — Fails admission: size too large**

Level 1:
- Project: Zephyr | Intent: execute | Size: XL | Ambiguity: 2

Level 3 — Admission: **B. Ready only after split**

Pre-step output:
- Phase 1 (M): Reproduce and isolate the issue → artifact: repro log
- Phase 2 (M): Implement fix → artifact: patch + test result
- Phase 3 (S): Write blocker summary and close → artifact: blocker summary note
- Schedule Phase 1 first; Phase 2 only after Phase 1 artifact is complete.

---

**Example 6 — Converted to spike**

Raw task: "Figure out how RobotOS should interface with the Zephyr kernel"

Level 1:
- Project: RobotOS | Intent: design | Size: L | Ambiguity: 4

Level 3 — Admission: **C. Convert to spike first**

Spike definition:
- Goal: Identify 3–5 key unknowns blocking RobotOS/Zephyr interface design
- Size: M (time-boxed, one evening primary block)
- Expected Artifact: Open questions list + any preliminary findings
- Post-spike: re-run Level 2 on design task after spike artifact is complete.

---

**Example 7 — Full block-ready spec output**

*(From Example 2 above, after Level 3 admission A):*

```
- Anchor: RobotOS
- Goal: Draft v0.1 layer boundary interface sketch
- Size: M | Ambiguity: 2
- Expected Artifact: Interface sketch + open questions list (3–5 items)
- First Step: Review spike notes; sketch 3-layer boundary
- Suggested Slot: Evening primary (not weekday office hours)
- Re-entry Risk: Medium — re-entry pack required if block ends unfinished
```

---

## 12. Agent Behavior Rule

When a raw task or idea is given, the agent should:

1. **Infer project context** (Zephyr / RobotOS / Signee / system)
2. **Classify task type** using project-aware defaults (§8)
3. **Suggest likely artifact** based on task type and project context
4. **Estimate size** (XS → XL)
5. **Estimate ambiguity** (0–5)
6. **Decide intake level** needed (none / Level 1 / Level 1 + Level 2)
7. If Level 2 needed: **produce analysis card as a proposal** — user reviews and adjusts, not constructs from scratch
8. **Run admission decision** (§6); output one of A–F
9. **If admitted (A):** produce block-ready spec (§9)
10. **If not admitted:** produce the required pre-step:
    - B: split into schedulable phases
    - C: spike definition
    - D: scope clarification note / question list
    - E: watchpoint item
    - F: backlog note with preserved intent

**The agent proposes first. The user reviews, not invents.**

---

*TASK_INTAKE_AND_ADMISSION.md is a canonical system spec. Changes to admission rules or project defaults should be made via deliberate System Change decision (see TEMPLATE_Week_Final.md §5).*
