# Daily Plan – YYYY-MM-DD

---

## Table of Contents

- [Context](#context)
- [Source](#source)
- [Daily Project Scope Rule (Critical)](#daily-project-scope-rule-critical)
- [Work Time Domain (Critical)](#work-time-domain-critical)
- [Morning Setup (5 min)](#morning-setup-5-min)
- [Office Hours – Deep Work](#office-hours--deep-work-mon--fri-900--1730)
- [Evening – Personal Projects](#evening--personal-projects-1730-or-weekend)
- [Builder / Support Work](#builder--support-work-active-anchors-only-max-34-items-size-s)
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

> Weekly commitments → Daily execution.  
> Daily does NOT create new commitments without explicit escalation.  
> If day collapses: capture only main artifact + unfinished + next step.

---

## Daily Project Scope Rule (Critical)

> **Operating constraint:** A normal execution day contains **max 2 active projects** (Primary Anchor + Secondary Anchor).
> - All Deep Work Blocks must map to one of these 2 anchors only.
> - All Builder / Support Work must support one of these 2 anchors only.
> - Key questions and shutdown notes should reference only these 2 anchors on normal days.
> - A third project may appear only as: incident, escalation, or administrative mention (not active work).
> - **Exception:** Planning or review days may legitimately reference 3+ projects; mark these explicitly as review-day exceptions.

---

## Work Time Domain (Critical)

> **Operating boundary:** Office hours (Mon–Fri, 9:00–17:30) are reserved for **Zephyr work only**.
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
- **Office Hours anchor (Zephyr only):** [name of expected office-hours work]
- **Evening anchor (personal project):** [name of evening work, if any] ← or leave blank if day is office-only
- **Exception to Work Time Domain Rule?** [ ] No (default) [ ] Yes — justify below
  - *If yes, which project? Why must it be in office hours?*

**Evening Capacity Mode** *(weekday only; check one):*
- [ ] `1 × M` — one meaningful block (default normal day)
- [ ] `2 × S` — two light blocks
- [ ] `S-only` — energy degraded; keep only most strategic task
- [ ] `None` — office-only day or rest evening

**Reason for tonight's capacity mode:**  
(e.g.: normal office day / poor sleep / heavy workout / heavy meetings / recovery evening)

---

- **Primary Anchor:** (project — direction)
- **Secondary Anchor:** (project — direction)
- **Today's Active Projects:** Primary: [name] | Secondary: [name] ← max 2; no third project unless escalation [ ]
- **Why these anchors today?** (optional — 1-line capacity/context reason)
- **1 Most Important Outcome today:** …
- **Key artifact expected:** …
- **First execution step:** …

---

## Office Hours – Deep Work (Mon–Fri 9:00–17:30)

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

---

**Note:** If no evening blocks are needed, leave this section empty. If capacity mode is `S-only`, use Block 1 only and defer Block 2. If any evening block is unfinished, capture a re-entry note in Shutdown before closing.

---

## Builder / Support Work (active anchors only, max 3–4 items, Size S)

> **Scope lock:** Items may support the Primary Anchor, the Secondary Anchor, or daily system maintenance only. Do not introduce a third active project. Administrative mentions are allowed; active work is not.

1. **Anchor: Primary / Secondary** | **Task:** … | **Goal:** … | **Artifact:** …
2. **Anchor: Primary / Secondary** | **Task:** … | **Goal:** … | **Artifact:** …
3. **Anchor: Primary / Secondary** | **Task:** … | **Goal:** … | **Artifact:** …

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
- **Artifact state:** (not started / draft exists / partially verified / blocked / waiting response / ready for review)
- **Next exact step:** (concrete 10–15 min restart action; specific enough to start immediately without re-analysis)
- **Re-entry condition:** (needs office-hours Zephyr block / needs evening primary block / needs dependency resolved / …)

**Unfinished work — re-entry package captured?**
- [ ] Yes
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

## DoD (Daily closure)
- [ ] Main artifact captured
- [ ] Unfinished work documented (with re-entry pack if applicable)
- [ ] Tomorrow's first step clear
- [ ] Any escalation signals noted

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