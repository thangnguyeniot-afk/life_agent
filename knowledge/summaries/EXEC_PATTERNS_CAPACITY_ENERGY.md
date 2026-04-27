# KNOWLEDGE SUMMARY — Execution Patterns: Capacity, Energy, and Project Flow

**Artifact type:** Execution Pattern Summary — summaries-layer artifact. This is not a formal §13 Research Note or Design Decision. It captures classified execution observations for planning reference only.

**Topic:** Personal execution model — capacity modes, energy leaks, recovery debt, project batching, and throughput prioritization
**Created:** 2026-04-27
**Classification type:** Mixed — see per-finding classification below
**Status:** Active observations. Some entries are under validation. Not all findings are proven operating laws.
**Source:** Real execution findings surfaced April 2026, processed via AUDIT-FIRST protocol.

---

## Purpose of This File

This file holds execution-pattern findings that are:
- Too specific to be in OS doctrine without more validation
- Too important to discard or leave unrecorded
- Correctly classified so the system does not mislearn coping patterns as healthy defaults

Each finding has a classification tag and a confidence level.

---

## Finding 1 — Capacity / Activation Modes

**Classification:** Provisional hypothesis + observation
**Confidence:** Medium — observed under favorable conditions, not yet validated across varied states
**Status:** Under validation. Do not encode as a new permanent baseline.

### Observation
When the 4-person operating model is functioning well, and the user applies high effort, deep focus, and clear motivation, actual work output can be significantly stronger than prior plans assumed.

### Structural implication
The system may need to distinguish three capacity states rather than a single baseline:

| Mode | Description | Planning implication |
|---|---|---|
| **Sustainable baseline** | Default reliable output; maintainable week after week without burning down | Use as conservative planning input |
| **Activated / high-leverage mode** | Output is elevated; operating model supporting well; motivation and clarity are high | Can absorb M/L tasks; planning may allow slightly higher ambition |
| **Push / sprint mode** | High output over a short window; unsustainable beyond 1–2 weeks | Use intentionally with explicit deload planning; never plan as default |

### Warning
Do not use activated-mode performance as the new capacity baseline for weekly planning. Planning to activated-mode output leads to systematic overestimation and eventual deload cascade.

### Where this may affect the system
- Metrics Engine (Actual Blocks): when capacity reads high for 2+ weeks, investigate whether it is mode-related or a true new baseline
- Monthly Review: distinguish "elevated output month" from "capacity baseline increase"
- Weekly planning: if entering an activated-mode period, note it explicitly and protect recovery windows

---

## Finding 2 — Dinner/Rest Mix as Energy Leak

**Classification:** Warning marker + recovery-risk marker
**Confidence:** High — directly observed as a recurring pattern with downstream effects
**Status:** Encoded in OS §12.9 as a downgrade trigger.

### Observation
Evening dinner and rest are sometimes combined into a single block of ~1.5h with no clear transition. This pattern:
- Reduces short-term stress (perceived relief)
- Does not restore capacity
- Degrades the quality of the following evening work session
- Functions as a painkiller, not a repair

### Classification note
This is not a rest strategy. It is a tension-management coping pattern that occupies the time slot that real recovery should occupy.

### Repo encoding
- OS §12.9: dinner-rest mix added as an explicit downgrade trigger in the Evening Capacity Guard
- TEMPLATE_Week_Final §4: Energy Sabotage context note added

### Planning guidance
- If this pattern occurs, apply Evening Capacity Guard downgrade (S-only mode)
- Do not plan an M-sized evening block on a day where this pattern is likely
- Track as Anti-Anchor "Energy Sabotage" in weekly review if it recurs

---

## Finding 3 — Stimulation-Shaped Sleep Entry

**Classification:** Coping pattern + tension-management debt + debt signal
**Confidence:** High — directly observed as recurring
**Status:** Debt marker only. Not encoded in OS rules. Not a preferred system routine.

### Observation
Depending on external stimulation before sleep to reduce tension — e.g., listening to high-arousal content (ghost stories, intense podcasts) instead of calming sleep-supporting input. This is:
- A short-term tension-release mechanism
- Not conducive to quality sleep entry
- A dependency-shaped decompression pattern
- A signal that the system's tension load is not being discharged during the day

### Classification note
This is tension-management debt. The root cause is unresolved tension accumulation during the day; the coping mechanism is stimulation-as-release rather than actual decompression.

### Tracking location
- TEMPLATE_Week_Final §4 Anti-Anchors: Sleep Killers row — the context note identifies this pattern for honest self-assessment
- If ⚠️ appears 2+ consecutive weeks, triggers System Change per existing Anti-Anchor rule

### Resolution direction (hypothesis level — not yet a rule)
If the pattern persists, the upstream question is: where is the tension coming from? Likely candidates: insufficient deload during the day, cognitive overload accumulation, or evening work extending too close to sleep time.

---

## Finding 4 — Project Phase Batching Minimum Window

**Classification:** Planning rule
**Confidence:** High — observed pattern with clear mechanism
**Status:** Encoded in OS §12.13 as a planning rule. Strong default, not absolute.

### Observation
Allocating only 1–2 days to a personal project phase is consistently insufficient for meaningful completion. A minimum batching window of ~3–4 consecutive or near-consecutive day-equivalents is required to push a phase to a collaborator-handoff-ready state.

### Mechanism
- 1–2 days: context load, start work, partial progress, leave mid-phase → collaborators cannot pick up → system stalls
- 3–4 days: reach a demoable or handoff-ready state → collaborators can continue → system flows

### Canonical planning guidance
→ See OS §12.13 for canonical planning rule and Pool B scope.

---

## Finding 5 — Unblocker-First Throughput Principle

**Classification:** Prioritization rule + throughput principle
**Confidence:** Medium-High — observed as effective; logically consistent with flow optimization
**Status:** Encoded in OS §11.3 as an override note. Applied with judgment, not automatically.

### Observation
When a blocker is preventing multiple downstream tasks or a critical handoff, removing it can have higher total system value than its raw priority score suggests. Sacrificing some local revenue optimization to keep the total workstream moving may be justified in such cases.

### Classification note
This is a throughput principle, not a task preference. A single unblocked dependency can unlock multiple downstream tasks — making its total value much higher than its local score.

### Where encoded
- OS §11.3: Unblock override note added (judgment-required)

### Application rules
- Apply when a blocker is preventing 2+ tasks or a critical collaborator handoff
- Do not apply automatically — scoring must still be used for initial triage
- Do not use as a blanket justification to drop revenue work — this is a judgment override, not a rule
- Human judgment required: what counts as a "workstream-level block" vs. a local inconvenience requires context

---

## Summary — Classification Table

| Finding | Classification | Encoded in Repo? | Validation Status |
|---|---|---|---|
| 1. Capacity Modes | Provisional hypothesis + observation | This KB note only | Under validation |
| 2. Dinner/Rest Energy Leak | Warning marker + recovery-risk marker | Yes — OS §12.9 + Template §4 context note | Observed pattern |
| 3. Stimulation Sleep Entry | Coping pattern + tension-management debt | Template §4 context note only | Observed pattern |
| 4. Project Phase Batching | Planning rule | Yes — OS §12.13 (canonical) | Strong observed pattern |
| 5. Unblocker-First Throughput | Prioritization rule + throughput principle | Yes — OS §11.3 override note | Observed, logically consistent |

---

## What was NOT done (intentionally)

- Finding 1 (Capacity Modes) was NOT added to OS doctrine — it is a provisional hypothesis and needs further observation before being converted to a capacity baseline rule
- No changes to Metrics Engine thresholds — current warning signals are sufficient; capacity mode distinction is captured here for future reference
- No changes to TEMPLATE_Daily.md — it already has the energy level field; the patterns are captured in the Anti-Anchors layer
- No changes to project context files, quarter/month plans, or LIFE_AGENT_ARCHITECTURE.md
- No Anti-Anchor ADR created here — Anti-Anchor Tracking governance remains open; the template context notes are descriptive-only to avoid governance creep

---

**Last updated:** 2026-04-27 | **Version:** 1.1
