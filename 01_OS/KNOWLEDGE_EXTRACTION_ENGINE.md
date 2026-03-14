# KNOWLEDGE_EXTRACTION_ENGINE.md — Knowledge Extraction Engine

> **Version:** v1.0
> **Status:** Active
> **Placement:** Sits after execution/review and before future intake proposals.
> **OS reference:** §12.12 (`01_OS/operating_system_thang_nguyen_v1_1.md`)

---

## 1. Purpose

This subsystem extracts operational knowledge from execution history.

Its purpose is **not** storage for storage's sake.
Its purpose is to improve future task shaping, admission quality, estimation quality, and scheduling fit.

The engine converts repeated patterns in execution, signals, re-entry, and review into compact reusable heuristics that make future intake/admission proposals:
- more project-aware
- more estimation-aware
- more artifact-aware
- more drift-aware
- more capacity-aware

It does not track individual tasks.
It extracts patterns that matter across multiple executions.

---

## 2. What Counts as Extractable Knowledge

Only reusable decision support qualifies. The six categories:

**1. Estimation knowledge**
- Tasks often mis-sized by type or project
- Tasks that appear S but routinely become M
- Tasks safe as S follow-up after prior heavier work
- Tasks that consistently require split before admission

**2. Artifact knowledge**
- Which artifact types work best for which task types
- Which tasks fail or drift when artifact is vague
- Which output formats enable clean resumption across sessions

**3. Capacity knowledge**
- Which tasks reliably fit weekday evenings
- Which tasks repeatedly exceed evening capacity
- Which tasks are weekend-only (open-ended, cognitive-heavy)
- Which task types mismatch post-work energy (high-ambiguity debugging, open-ended architecture)

**4. Re-entry knowledge**
- Which task types have high restart friction
- Which tasks need stronger re-entry notes to resume cleanly
- Which artifact types support smooth re-entry vs. require rebuild

**5. Project-specific drift knowledge**
- Zephyr: when verification tasks expand beyond scoped S
- RobotOS: when architecture work drifts into vague exploration
- Signee: when reproduction tasks chain into unresolved dependency spirals

**6. Admission-quality knowledge**
- Which task framings repeatedly fail admission
- Which ambiguity patterns should always trigger spike-first
- Which task types are structurally too vague to schedule directly

---

## 3. What This Engine Is Not

This engine is NOT:
- a full knowledge base
- a raw note archive
- a second-brain dumping ground
- a task history dump
- a place to copy artifact content
- a chronological journal

It is a compact extraction layer focused exclusively on reusable scheduling and execution knowledge.

If an item does not change how future tasks should be shaped, sized, slotted, or admitted — it does not belong here.

---

## 4. Input Sources

The engine reads from existing system outputs. It creates no new heavy reporting requirement.

**Primary sources:**
- Task Intake & Admission outcomes (admission decision + pre-step quality)
- Daily execution blocks (expected vs. actual artifact, block completion quality)
- Signals (energy, overload, drift flags in daily and weekly review)
- Re-entry Packs (restart friction observed, what was missing)
- Weekly Intelligence (repeating blockers, intake quality, restart friction patterns)
- Monthly Reflection (anti-anchors, intake quality patterns, capacity mismatch summary)
- Admission failures (what type of task, what rule failed, what framing caused it)
- Repeated mis-sizing (what was estimated S that became M, L estimated that was XL)
- Repeated overload (what task types exceeded capacity repeatedly)
- Ambiguity leakage (execution that became confusing because intake was too shallow)

**The agent reads these outputs and extracts patterns — it does not require new form fields from the user.**

---

## 5. Output Types

Six compact operational categories:

**A. Project Heuristics Memory**
Per-project (Zephyr / RobotOS / Signee) condensed operating knowledge: common task types, best artifact mappings, common ambiguity sources, mis-sizing patterns, slot fit, drift triggers, re-entry risk.

**B. Estimation Corrections**
Learned corrections to default size estimates: task framings that are misleadingly short, task types that predictably expand, tasks safe to keep small.

**C. Artifact Mapping Corrections**
Corrections to artifact defaults: task types that produce drift when artifact is vague, artifact types that support clean resumption, artifact formats that reduce re-work.

**D. Capacity Fit Rules**
Learned slot-fit patterns: task types that work well in specific slots, task types that mismatch post-work energy, slot preferences per project per task type.

**E. Re-entry Risk Patterns**
Learned re-entry difficulty patterns: which task types need strong re-entry notes, which artifacts support smooth restart, which dependency patterns create re-entry traps.

**F. Admission Failure Patterns**
Recurring patterns where tasks should not pass admission directly: common disguises for over-scoped or artifact-less tasks, framing tricks that inflate ambiguity, cross-project contamination patterns.

---

## 6. Project Heuristics Memory

Compact per-project rolling heuristic summary.

---

### Zephyr

| Property | Current heuristic |
|---|---|
| **Common task types** | Validation · debug · environment check · blocker isolation · execution follow-up |
| **Best artifact mappings** | Checklist + evidence log · blocker summary · test result note · status update |
| **Common ambiguity sources** | Environment instability · integration dependency · toolchain behavior |
| **Common mis-sizing patterns** | "Quick check" phrased as S — often M when reproduction is unstable |
| **Slot fit** | Office Hours only (Mon–Fri, 09:00–17:30); never evening or weekend primary |
| **Drift triggers** | Unstable reproduction target · missing evidence standard · scope expansion inside verification |
| **Re-entry risk** | Low for procedure-driven validation; medium-high for open reproduction chains |

**Standing heuristics:**
- Environment verification tasks with an established procedure: safe as S, checklist-driven.
- Blocker isolation without stable reproduction: upgrade to M; high drift risk.
- If reproduction is unstable, ambiguity rises fast — consider upgrading to spike-first.
- Office-hours only. Do not carry Zephyr primary work into evenings.

---

### RobotOS

| Property | Current heuristic |
|---|---|
| **Common task types** | Architecture shaping · scope definition · design · analysis · boundary clarification · constraint mapping |
| **Best artifact mappings** | ADR seed · constraints note · interface sketch · open questions list · scope draft |
| **Common ambiguity sources** | Abstraction boundary · sequencing decision · architectural tradeoff · scope edge |
| **Common mis-sizing patterns** | "Review architecture" phrased as S — almost always M (or M+ requiring prior spike) |
| **Slot fit** | Evening primary or weekend deep block; not office hours |
| **Drift triggers** | Vague architecture framing without artifact boundary · insufficient scope constraint entering a session |
| **Re-entry risk** | Medium to high; open-ended design tasks require re-entry note and artifact checkpoint |

**Standing heuristics:**
- Tasks framed as "review architecture" are analysis/design tasks — treat as M by default.
- Architecture sessions without a clear artifact boundary drift; enforce artifact before scheduling.
- Evening support is poor for open-ended design; use evening primary or weekend deep block.
- Re-entry sensitivity almost always medium/high; create re-entry note when block ends mid-task.

---

### Signee

| Property | Current heuristic |
|---|---|
| **Common task types** | Validation · issue reproduction · integration check · protocol clarification · support diagnosis |
| **Best artifact mappings** | Issue summary · evidence note · integration status update · reproduction checklist |
| **Common ambiguity sources** | Protocol behavior · integration dependency · reproduction gap · missing environment baseline |
| **Common mis-sizing patterns** | Reproduction tasks look like S — expand to M+ when protocol ambiguity is high |
| **Slot fit** | Evening support or bounded evening block; not primary for unresolved chains |
| **Drift triggers** | Protocol ambiguity unresolved at start · chained dependency without checkpoint |
| **Re-entry risk** | Low for bounded verification; high for unresolved reproduction chains |

**Standing heuristics:**
- Reproduction tasks with high protocol ambiguity should trigger spike-first, not direct execution.
- Evening support works for bounded follow-up only; not for unresolved dependency chains.
- Signee work should always produce a concrete artifact (issue summary or evidence note) — "investigation" is not an artifact.

---

## 7. Estimation Corrections

Reusable corrections to default estimates. Update as patterns are confirmed.

| Task framing | Default assumption | Correction |
|---|---|---|
| "Review architecture" (RobotOS) | S | M (analysis/design task) |
| "Quick check" or "verify" with unstable reproduction | S | M (upgrade if reproduction uncertain) |
| "Document unknowns" (source notes exist) | M | S (safe if notes already structured) |
| "Document unknowns" (no source) | S | M (requires analysis before documentation) |
| "Compare design options" | S/M | Split required before admission |
| "Understand scope" (new architecture area) | M | L or spike-first |
| Zephyr procedure-driven validation | M | S (safe when checklist exists) |
| Signee reproduction (protocol ambiguous) | S | M or spike-first |
| RobotOS boundary clarification | S | M (almost always requires artifact) |

**Correction rule:** When a task framing matches a known mis-sizing pattern, upgrade the size estimate before admission and ask the user to confirm — do not accept the surface-level estimate.

---

## 8. Artifact Mapping Corrections

Corrections for bad artifact habits. Update as observations are confirmed.

| Task type | Bad artifact pattern | Correct artifact |
|---|---|---|
| Architecture analysis | "Investigation" (vague) | ADR seed · constraints note · open questions list |
| Reproduction work | "Looked into it" | Issue summary + evidence note + reproduction path |
| Validation | Vague note | Checklist + result note (pass/fail/issues) |
| Scope definition | No artifact | Scope draft with boundaries + exclusions |
| Design comparison | No resolution artifact | Options comparison + decision rationale note |
| Architecture shaping | No artifact | Interface sketch + open questions list |
| Spike work | Vague exploration note | Bounded discovery artifact: findings + open questions |

**Artifact rule:** If a task type appears on this table, the agent should actively suggest the correct artifact type during Level 2 intake. Do not accept vague artifact descriptions in admission.

---

## 9. Capacity Fit Rules

Learned slot-fit patterns. Update as mismatch patterns are confirmed.

| Task type | Preferred slot | Avoid |
|---|---|---|
| Zephyr procedure-driven validation | Office Hours support/admin | Evenings |
| Zephyr blocker isolation (stable) | Office Hours primary | Evenings |
| Zephyr blocker isolation (unstable repro) | Office Hours primary only | Evenings; do not schedule |
| RobotOS architecture shaping | Evening primary / Weekend deep | Office hours; evening support |
| RobotOS boundary clarification | Evening primary / Weekend deep | Evening support; office hours |
| Signee bounded reproduction | Evening support | Late evening (unresolved chains) |
| Signee unresolved dependency chain | Defer or spike | Any runtime slot |
| High-ambiguity debugging | Office Hours (when possible) | Late weekday evenings |
| Open-ended architecture reasoning | Weekend deep block | Weekday evening primary |
| Documentation with existing notes | Evening support | Primary block (overkill) |

**Capacity rule:** When suggesting a slot during intake, cross-check against these patterns. When a task type matches an "avoid" pattern for the proposed slot, flag it and suggest the preferred slot.

---

## 10. Re-entry Risk Patterns

Compact restart-friction knowledge.

| Task type | Re-entry risk | Minimum re-entry artifact |
|---|---|---|
| Procedure-driven checklist validation | Low | None needed; checklist state is sufficient |
| Bounded documentation (source note exists) | Low | Next sentence / section note |
| Spike work (first session) | Medium | Findings so far + open questions list |
| Architecture boundary clarification | Medium-high | Last decision made + remaining question list |
| Open-ended architecture shaping | High | State-of-model sketch + unresolved boundary list |
| Unresolved reproduction chain | High | Reproduction path attempted + next hypothesis |
| Design comparison (mid-decision) | High | Options compared so far + pending criterion |

**Re-entry rule:** Any task with re-entry risk Medium-High must include a re-entry note when the block closes unfinished. The agent should flag this in the block-ready spec and in re-entry pack creation.

**Patterns that cause re-entry traps:**
- Stopping mid-analysis without capturing the "state of thinking"
- Closing a block without noting what the next concrete first step is
- Ending a session when a dependency is unresolved without noting the exact outstanding question
- Failing to capture a partial artifact (even a half-formed sketch reduces re-entry cost significantly)

---

## 11. Admission Failure Patterns

Recurring patterns where tasks should not pass Level 3 admission directly.

| Pattern | What it looks like | Correct pre-step |
|---|---|---|
| Missing artifact clarity | Task description says what to do but not what to produce | Return to Level 2; define Expected Artifact |
| Disguised execution | High-ambiguity task framed as simple execution | Convert to spike-first or clarification |
| Architecture disguised as review | "Review X architecture" framed as S review task | Reclassify as Analysis/Design M; enforce artifact |
| Size inflation through scope | Task described as M but contains multiple M subtasks | Split before admission |
| Cross-project contamination | Zephyr-type execution task framed as RobotOS design task | Re-classify project; re-apply time domain rule |
| Dependency hidden in framing | Task depends on unresolved output from another task | Classify as E (dependency wait); do not schedule |
| Repeated re-addition without reframing | Task appears in 3rd week without progress or new framing | Require Level 2 refresh before re-admitting |
| Artifact-less end state | Task description sets up process but has no defined end artifact | Block; define artifact first |

**Failure rule:** When a task matches an admission failure pattern, the agent must not propose Decision A. Propose B/C/D/E/F as appropriate and explain which pattern was detected.

---

## 12. Extraction Frequency

**Weekly (during Weekly Intelligence review):**
- Log any confirmed mis-sizing pattern (1–2 lines max)
- Log any artifact mismatch observed
- Log any slot-fit failure (evening mismatch, office-hours contamination)
- Log any re-entry trap pattern detected
- Use the "Knowledge Extraction Candidates" section in TEMPLATE_WeeklyIntelligence_Final.md

**Monthly (during Monthly Reflection):**
- Consolidate weekly extraction candidates into standing heuristics
- Update Project Heuristics Memory if a pattern is confirmed (2+ occurrences)
- Update Estimation Corrections table if a new mis-sizing pattern is confirmed
- Update Artifact Mapping Corrections if a new pattern is confirmed
- Remove or downgrade heuristics that have not been observed recently
- Use the "Knowledge Extraction — Monthly Consolidation" section in TEMPLATE_Month_Final.md

**Ad hoc (mid-week):**
- If a repeated failure pattern becomes obvious (same type of task failing twice in one week), extract immediately
- Note only; consolidation still happens at monthly review

**Never during daily execution:**
- Daily remains runtime-only
- No extraction fields in daily pages

---

## 13. How to Update the Engine

**Update by:**
- Summarizing observed patterns into compact heuristics (1–2 lines)
- Refining existing heuristics with more precise conditions
- Replacing weak generic rules with stronger project-specific rules
- Removing heuristics that stop being observed

**Prefer:**
- Compact bullet heuristics
- Project-specific corrections over generic commentary
- Slot-fit rules grounded in observed patterns
- Artifact-fit rules grounded in observed drift or clean completion

**Avoid:**
- Chronological journaling
- Duplicating daily execution data
- Copying raw task descriptions or artifact content
- Adding rules for things that have only happened once

**Heuristic confidence levels (informal):**
- Single observation → candidate (note it; do not promote to standing heuristic)
- Two or more confirmed instances → promote to standing heuristic
- Not observed in 3+ months → candidate for review/removal

---

## 14. Agent Integration Rule

Before proposing Task Intake / Admission for any non-trivial task, the agent should consult the Knowledge Extraction Engine.

**Agent behavior chain:**

1. Infer project context (Zephyr / RobotOS / Signee / system)
2. Consult Project Heuristics Memory (§6) — check task type, artifact, slot fit defaults
3. Consult Estimation Corrections (§7) — check if task framing matches a known mis-sizing pattern
4. Consult Artifact Mapping Corrections (§8) — check if task type maps to a known artifact type
5. Consult Capacity Fit Rules (§9) — check if proposed slot matches observed fit
6. Consult Re-entry Risk Patterns (§10) — flag re-entry sensitivity level
7. Consult Admission Failure Patterns (§11) — check if task framing matches a known failure pattern
8. Produce intake/admission proposal using both:
   - canonical admission rules (`01_OS/TASK_INTAKE_AND_ADMISSION.md`)
   - learned project heuristics from this engine
9. Flag any heuristic adjustment made (e.g., "size upgraded from S to M per RobotOS estimation correction")

**Critical rule: Hard OS rules always override learned heuristics.**

If a heuristic conflicts with a hard rule (§12 OS), the hard rule wins. Heuristics improve proposal quality within the envelope defined by hard rules — they do not bypass them.

**The agent proposes heuristic-informed suggestions. The user reviews outcomes and confirms or adjusts. Heuristic updates happen through review layers, not ad hoc mid-execution.**

---

## 15. Relation to Task Intake & Admission

These two subsystems are complementary — not redundant.

**Task Intake & Admission (`01_OS/TASK_INTAKE_AND_ADMISSION.md`):**
- Defines the decision protocol
- Specifies the admission rules (Level 1 → Level 2 → Level 3)
- Specifies the 7 hard admission rules
- Specifies block-ready output format
- Defines what agent must do step-by-step for each task

**Knowledge Extraction Engine (this file):**
- Improves the quality of future decisions made by the intake/admission protocol
- Provides project-specific heuristics that make proposals more accurate
- Corrects estimation defaults based on observed patterns
- Improves artifact suggestions based on observed drift patterns
- Improves slot suggestions based on observed capacity fit
- Reduces the number of admission failures by front-loading pattern recognition

**One is the control protocol. The other is the learned heuristic memory.**

They must be used together for best results. Running intake/admission without consulting the extraction engine means proposals are based on generic defaults only. Consulting the extraction engine without the intake/admission protocol means there is no decision structure — only loose heuristics.

---

## 16. Examples

---

**Example 1 — RobotOS architecture task repeatedly mis-sized as S**

Pattern observed:
- "Review RobotOS layer architecture" entered weekly plan as S repeatedly
- Actual execution: always expanded to M+; artifact was always unclear at start
- Admission failure: architecture task disguised as review

Extracted heuristic (added to §7 Estimation Corrections):
> "Review architecture" (RobotOS) → override to M; reclassify as Analysis/Design task; require artifact boundary before admission.

Future agent behavior: When task mentions "review" + RobotOS + architecture, immediately suggest M, reclassify as Design/Analysis, and require Expected Artifact before Level 3 admission.

---

**Example 2 — Zephyr validation task where checklist artifact reduced drift**

Pattern observed:
- Zephyr smoke test with existing procedure: consistently completed as S, clean artifact, no drift
- Root cause: procedure checklist and evidence log were pre-defined

Extracted heuristic (reinforces §6 Zephyr memory):
> Zephyr procedure-driven validation: safe as S when checklist exists; best artifact is checklist + pass/fail evidence note.

Future agent behavior: For Zephyr validation tasks, propose checklist + evidence note by default; do not propose vague "result summary."

---

**Example 3 — Signee reproduction task should trigger spike-first when protocol ambiguity is high**

Pattern observed:
- Signee reproduction task admitted directly into execution
- Protocol behavior was ambiguous; task drifted from S to M+ and still did not produce a clean artifact
- Admission failure: ambiguity disguised as execution (ambiguity ≥ 4 not caught at intake)

Extracted heuristic (added to §11 Admission Failure Patterns):
> Signee reproduction tasks with protocol ambiguity ≥ 3: do not admit for direct execution; convert to spike-first with bounded discovery target.

Future agent behavior: When Signee task involves reproduction + protocol ambiguity ≥ 3, propose Decision C (spike-first) not Decision A.

---

**Example 4 — Evening mismatch: debugging with unstable reproduction should move away from weekday evenings**

Pattern observed:
- Zephyr blocker isolation scheduled for weekday evening primary
- Reproduction was unstable; task required more cognitive load than typical evening capacity supports
- Result: incomplete block, poor artifact, restart friction next session

Extracted heuristic (added to §9 Capacity Fit Rules):
> Zephyr blocker isolation with unstable reproduction: Office Hours primary only; do not schedule for weekday evenings.

Future agent behavior: If Zephyr debug task + unstable reproduction + proposed slot is evening → flag slot mismatch, suggest Office Hours primary instead.

---

**Example 5 — High re-entry risk for open-ended architecture thinking**

Pattern observed:
- RobotOS architecture shaping blocks repeatedly needed 10–15 min to rebuild context at session start
- Re-entry notes were missing or vague ("continue architecture thinking")
- Root cause: no state-of-model artifact captured at block close

Extracted heuristic (confirms §10 Re-entry Risk Patterns):
> Open-ended RobotOS architecture shaping: High re-entry risk; minimum re-entry artifact is "state-of-model sketch + unresolved boundary list."

Future agent behavior: For RobotOS architecture tasks with re-entry risk High, explicitly note "re-entry pack required: state-of-model sketch + unresolved boundary list" in block-ready spec.

---

*KNOWLEDGE_EXTRACTION_ENGINE.md is a canonical system spec. Updates to heuristics should reflect confirmed patterns (2+ observations). Do not add one-time observations as standing rules.*
