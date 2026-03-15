# Daily Plan – YYYY-MM-DD

---

## Table of Contents

- [Context](#context)
- [Source](#source)
- [Daily Project Scope Rule (Critical)](#daily-project-scope-rule-critical)
- [Work Time Domain (Critical)](#work-time-domain-critical)
- [Morning Setup (5 min)](#morning-setup-5-min)
- [Canonical Daily Anchors](#canonical-daily-anchors)
- [Office Hours – Deep Work](#office-hours--deep-work-mon--fri-900--1730)
- [Evening – Personal Projects](#evening--personal-projects-1730-or-weekend)
- [Signals (check if occurred)](#signals-check-if-occurred)
- [Optional — Delegations / Handoffs](#optional--delegations--handoffs)
- [Shutdown (10 min)](#shutdown-10-min)
- [DoD (Daily closure)](#dod-daily-closure)
- [Human Reflection (Optional)](#human-reflection-optional)

> **Active rules:** Daily Project Scope Rule (max 2 anchors) · Work Time Domain (office = Zephyr; evening = personal) · Evening Capacity Guard (weekday evening max: 1×M or 2×S; no L tasks) · Re-entry Guard (unfinished meaningful work must leave a re-entry package) — see OS §12.7–12.10

---

## Context

**Date:** YYYY-MM-DD

**Week:** YYYY-Www

**Energy level:** [ ] Low [ ] Normal [ ] High

**Focus theme:** (optional; 1–2 words if needed)

---

## Source

> Weekly commitments listed by **project and mission** — not by anchor label. Anchor labels belong in Canonical Daily Anchors only.
> Weekly commitments → Daily execution.
> Daily does NOT create new commitments without explicit escalation.
> If day collapses: capture only main artifact + unfinished + next step.
> Daily blocks should originate from admitted tasks (Task Intake & Admission passed). If a block feels artifact-less or ambiguous, flag in Signals — do not force execution on unresolved work.

**Inherited from Weekly Anchor Map** *(copy the relevant day row from WeekPlan §7)*:
- Office Hours anchor: (paste from map — `<Project> — <phase>`)
- Evening anchor: (paste from map — `<Project> — <phase>` or none)
- Artifact direction: (paste from map)
- **Expected energy mode:** (paste from map — **planning hypothesis**; if actual energy differs, downgrade capacity/work type before changing anchor identity)
- **Evening capacity:** (paste from map — e.g., `1×M` / `S-only` / `none`)
- Risk / flex note: (paste from map if relevant)

---

## Daily Project Scope Rule (Critical)

> **Operating constraint:** A normal execution day contains **max 2 active projects** (Primary Anchor + Secondary Anchor).
> - All Deep Work Blocks must map to one of these 2 anchors only.
> - All support / admin work must belong to Office Hours or Evening domain; no standalone third zone.
> - Key questions and shutdown notes should reference only these 2 anchors on normal days.
> - A third project may appear only as: incident, escalation, or administrative mention (not active work).
> - **Exception:** Planning or review days may legitimately reference 3+ projects; mark these explicitly as review-day exceptions.

---

## Work Time Domain (Critical)

> **Operating boundary:** Office hours (Mon–Fri, 8:00–17:30) are reserved for **Zephyr work only**.
> 
> **Personal projects** (RobotOS, Signee baseline, prototyping, research spikes, or experimental work) **must be scheduled in evening blocks** (17:30+ or weekend time).
> 
> - **Why:** Protects core work time for primary responsibility (Zephyr); prevents office-hours fragmentation.
> - **Rationale:** Zephyr has external dependencies and team sync windows; personal projects have flexible timing and can absorb evening energy without cost.
> - **Exception:** If a personal project has hard deadline, customer priority, or blocking dependency (e.g., "RobotOS STM32 environment blocks Zephyr integration Friday"), may be escalated to office hours. Requires explicit justification in Morning Setup.

**Default rule (no exception needed):**
- Zephyr blocks → Office Hours section
- RobotOS, Signee, personal work → Evening section

---

## Morning Setup (5 min)

**Work Time Domain Check:**
- **Office Hours domain:** Zephyr *(domain confirmed; full anchor defined in Canonical Daily Anchors below)*
- **Evening domain:** [RobotOS / Signee / personal / none] *(domain confirmed; full anchor defined below)*
- **Exception to Work Time Domain Rule?** [ ] No (default) [ ] Yes — justify below
  - *If yes, which project? Why must it be in office hours?*

**Re-entry Block Check** *(if any spillover from previous day):*
- [ ] No inherited spillover (day starts fresh)
- [ ] Yes, inherited spillover from previous day
  - *Project/anchor:* …
  - *Re-entry mode required:* [ ] Quick (Structured/Closure — resume at last state) [ ] Analytical (Synthesis/planning — restore reasoning chain) [ ] Fragile (Integration/merge — inspect state + validate)
  - *First re-entry action:* (concrete 5–10 min context-reload step; e.g. "review Mon Shutdown notes + reopen test file + confirm current branch state")

**Evening Capacity Mode** *(weekday only; inherit from §6.8 + §7 — confirm or downgrade only; do not silently upgrade on weak-energy days):*
- [ ] `1 × M` — one meaningful block (default normal day)
- [ ] `2 × S` — two light blocks
- [ ] `S-only` — energy degraded; keep only most strategic task
- [ ] `None` — office-only day or rest evening

**Reason for tonight's capacity mode:**  
(e.g.: normal office day / poor sleep / heavy workout / heavy meetings / recovery evening)

---

## Canonical Daily Anchors

> **Single source of truth for anchor identity.** All blocks, shutdown entries, and DoD items refer back to these names.
> **Derived from:** Weekly Anchor Map (`WeekPlan §7`, today's row) — refine here; do not reinvent.
> **Anchor Stability:** Weekly defines identity. Daily confirms, refines, or downgrades. Do not redefine anchor identity unless there is an incident, hard blocker, or explicit escalation — document the reason if identity changes.
> **Format rule:** `<Project> — <task/phase>` — no cross-project purpose text; no "so X can proceed" phrasing; artifact or justification text belongs in Purpose or Expected Artifacts, not the anchor line.
> **Re-entry note:** If this day inherits spillover from a prior day, re-entry is a continuation **pre-step** (5–10 min), not a new anchor. It belongs to the inherited anchor path. Use the re-entry mode and first action defined in Morning Setup above; do not create a second anchor for re-entry.

**Primary Execution Anchor:** [Project] — [task/phase]
*(e.g., Zephyr — validate STM32F4 toolchain setup and flashing pipeline)*

**Secondary Execution Anchor:** [Project] — [task/phase]
*(e.g., RobotOS — consolidate architecture spike findings)*
*(leave blank if office-hours-only day)*

**Purpose / Scheduling Rationale:**
- Primary: (why this anchor today — 1 line; downstream enablement of other projects belongs here, not in anchor identity)
- Secondary: (why this anchor today — 1 line)

**1 Most Important Outcome today:**
(one sentence; may reference both anchors' combined effects; must not collapse both projects into one anchor statement)

**Daily Expected Artifacts:**
- [Primary project]: [specific artifact]
- [Secondary project]: [specific artifact, if applicable]

**First Execution Step (Primary Anchor):**
(concrete 10–15 min action to start the morning; Zephyr block start action)

---

## Office Hours – Deep Work (Mon–Fri 8:00–17:30)

> **Time domain:** Standard office hours. **Zephyr work only** (primary responsibility). If evening project must run here, mark exception in Morning Setup.

### Block 1 (90 min) — Zephyr Primary
- **Anchor:** Zephyr
- **Goal:** …
- **Size (S / M / L):** …
- **Ambiguity (0–5):** …
- **Expected Artifact:** …
- **First Step:** …

### Block 2 (90 min) — Zephyr Primary
- **Anchor:** Zephyr
- **Goal:** …
- **Size (S / M / L):** …
- **Ambiguity (0–5):** …
- **Expected Artifact:** …
- **First Step:** …

### Block 3 (optional) — Zephyr Primary only
- **Anchor:** Zephyr ← if exception applies, mark [ ] Exception in Morning Setup
- **Goal:** …
- **Size (S / M / L):** …
- **Ambiguity (0–5):** …
- **Expected Artifact:** …
- **First Step:** …

> If any office-hours block is unfinished at day close, capture a re-entry note in Shutdown before closing the day.

**Office Hours — Support / Admin** *(optional; Zephyr-side only; Size S)*
- **Task:** … | **Goal:** … | **Artifact:** …

---

## Evening – Personal Projects (17:30+ or weekend)

> **Time domain:** Evening blocks, weekends, or flexible-time slots. For RobotOS, Signee baseline work, prototyping, research, or secondary projects.

> **Evening Capacity Guard (weekday rule):**  
> - Max 1 primary evening block + optional 1 light support block  
> - No L-sized tasks on weekday evenings  
> - If ambiguity is high, reduce scope before scheduling  
> - Allowed patterns: `1×M` | `2×S` | `1×S` (degraded energy)  
> - Capacity mode set in Morning Setup

### Block 1 (60–90 min) — Primary evening block
- **Anchor:** RobotOS / Signee / Personal project
- **Goal:** …
- **Size (S / M / L):** … ← no L on weekday evenings
- **Ambiguity (0–5):** …
- **Expected Artifact:** …
- **First Step:** …
- **Evening role:** [Primary]

### Block 2 (optional) — Support block only
- **Anchor:** RobotOS / Signee / Personal project
- **Goal:** … ← keep this S-sized; support/admin/light only if Block 1 is M
- **Size (S / M / L):** S
- **Ambiguity (0–5):** …
- **Expected Artifact:** …
- **First Step:** …
- **Evening role:** [Support]

**Evening — Support / Follow-up** *(optional; personal projects only; Size S)*
- **Task:** … | **Goal:** … | **Artifact:** …

---

**Note:** If no evening blocks are needed, leave this section empty. If capacity mode is `S-only`, use Block 1 only and defer Block 2. If any evening block is unfinished, capture a re-entry note in Shutdown before closing.

---

## Signals (check if occurred)

- [ ] Task ambiguity unexpectedly high
- [ ] Execution blocked by dependency
- [ ] Energy collapse mid-day
- [ ] Scope creep detected
- [ ] System friction encountered
- [ ] Evening overcommitment detected
- [ ] Evening energy mismatch (planned vs actual capacity)
- [ ] Planned too much for post-work capacity
- [ ] Restart friction likely tomorrow
- [ ] Unfinished work left without clear next step
- [ ] Carry-over ambiguity detected

> If any signal persists → escalate to Weekly Review.

---

## Optional — Delegations / Handoffs

- Owner | What | By when

---

## Shutdown (10 min)

> **Scope alignment:** Key question and first step tomorrow should normally reference the Primary or Secondary Anchor. If tomorrow points to a third project, explain it as a deliberate handoff or escalation (not silent scope creep).

**Main artifact today:**  
…

**Key question raised today:**  
(from Primary or Secondary Anchor — if from elsewhere, note why)

**Unfinished work requiring re-entry pack** *(meaningful incomplete blocks only — write "None" if day closed cleanly):*  
(map to Primary / Secondary Anchor; if third project appears, mark escalation)

**Unfinished Work — Re-entry Pack** *(skip if day closed cleanly):*
- **Current phase:** (where the work stopped within the block / artifact flow)
- **Artifact state:** (not started / draft exists / partially verified / blocked / waiting response / ready for review / other)
- **Next exact step:** (concrete 10–15 min restart action; specific enough to start immediately without re-analysis)
- **Recommended re-entry mode** *(used by tomorrow's Morning Setup)*: [ ] Quick (resume at last state) [ ] Analytical (review notes, restore chain) [ ] Fragile (inspect state, validate) 
- **Receiving day constraint note** *(if spillover tomorrow):* Energy fit? Load saturated? Work-type appropriate for tomorrow's energy mode?
- **Re-entry condition:** (needs office-hours Zephyr block / needs evening primary block / needs dependency resolved / …)

**Unfinished work — re-entry package captured?**
- [ ] Yes (complete above; tomorrow's re-entry is prepared)
- [ ] No unfinished work (day closed cleanly)
- [ ] No — fix before closure

**First step tomorrow:**  
(day-level start; normally Primary Anchor if week is continuing; if handoff to Secondary or new project, note explicitly)

**Signals to escalate to Weekly Review:**  
…

**Evening plan vs actual capacity:**
- [ ] No — plan matched energy
- [ ] Slightly — minor overrun, no deferral needed
- [ ] Yes — exceeded capacity

**Evening spillover created?**
- [ ] No
- [ ] Yes → deferred: (note what was moved and where)

---

## Metrics Capture (1 min)

**Actual blocks executed today:** … / planned

**Energy level:** Low / Normal / High

**Unplanned work absorbed:** (rough % or time estimate)

---

## Drift Early Warning (30 sec)

> **Purpose:** Detect trajectory/pressure building (not events). Feeds weekly interpretation, not daily replanning.
> **Distinct from Signals:** Signals = "Did this event happen?". Drift = "Is pressure accumulating toward weekly realism breakdown?"

**Quick scan checklist:**
- [ ] Anchor progress: On track / Slightly behind / Meaningfully behind
- [ ] Spillover pressure: Low / Medium / High (work accumulating into tomorrow)
- [ ] Dependency pressure: Low / Medium / High (blockers affecting flow)
- [ ] Capacity confidence: High / Medium / Low (energy vs plan mismatch)
- [ ] Weekly integrity: Yes / No (plan still realistic, or corrective action needed)
- [ ] Smallest corrective move: (1–2 line action, if any: defer block / downgrade task / confirm dependency / none)

---

## DoD (Daily closure)
- [ ] Main artifact captured
- [ ] Unfinished work documented (with re-entry pack if applicable; re-entry mode specified)
- [ ] Tomorrow's first step clear
- [ ] Any escalation signals noted
- [ ] If spillover tomorrow: re-entry doesn't violate receiving day saturation (check weekly load)

---

## Human Reflection (Optional)

> **Not a task log. Not planning.** A few lines to capture the human side of today.
> 
> This space records your lived experience: emotions, mental state, challenges, small insights,
> meaningful moments, growth signals.

**Reflective prompts** (choose 1–2 to guide your thinking; ignore if not relevant):
- What emotion or mood dominated today?
- What challenged me mentally or emotionally?
- Was there a moment worth remembering?
- Did I notice any personal growth or shift today?
- How am I feeling about the anchors and pace this week?

**Reflection:**  
(2–4 sentences. Keep it light and natural, not heavy.)

```
(leave blank if reflection doesn't feel necessary today)
```