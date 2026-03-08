# BOOTSTRAP.md – Agent Reading Sequence

> If you are an agent (ChatGPT / Copilot / Claude) entering this repo, read in this order.

---

## Table of Contents

- [1. Start with LIFE_AGENT_ARCHITECTURE.md](#1-start-with-life_agent_architecturemd)
- [1b. INDEX.md – Repo Structure](#1b-indexmd--repo-structure)
- [2. Read the main OS manual](#2-read-the-main-os-manual)
- [3. Check relevant planning files](#3-check-relevant-planning-files)
- [4. If task involves research / design / architecture](#4-if-task-involves-research--design--architecture)
- [5. If you need context on specific projects](#5-if-you-need-context-on-specific-projects)
- [Core Mental Model](#core-mental-model)
- [Working Rules (don't break these)](#working-rules-dont-break-these)
- [Canonical Templates](#canonical-templates)
- [Anti-Gravity Safeguards to Remember](#anti-gravity-safeguards-to-remember)
- [Common Scenarios](#common-scenarios)
  - ["I have a task to execute"](#i-have-a-task-to-execute)
  - ["I need to design or research something"](#i-need-to-design-or-research-something)
  - ["The system feels heavy"](#the-system-feels-heavy)
- [Quick Links](#quick-links)

---

## 1. Start with LIFE_AGENT_ARCHITECTURE.md

Understand:
- System layers and how they connect
- Big picture of Planning → Execution → Projects
- Where each document fits

**Takes 2 minutes.**

Then read [INDEX.md](INDEX.md) for file map.

---

## 1b. INDEX.md – Repo Structure

Understand:
- Folder structure
- Canonical files
- Where to write what

**Takes 5 minutes.**

---

## 2. Read the main OS manual

**File:** `01_OS/operating_system_thang_nguyen_v1_1.md`

This is the source of truth. Includes:

### Execution System
- §9: Task Standard v1 (schema, types, readiness)
- §10: Backlog Structure v1 (Inbox → Today flow)
- §11: Priority Score v1 (4-factor scoring model)
- §12: Scheduler Engine v1 (daily/weekly scheduling)

### Knowledge System
- §13: Knowledge Engine v1 (Research Notes, ADR, Summaries, Design Docs)

### Safety Layer
- §14: Anti-Gravity Rules v1 (escape hatches, friction check, proportionality)

**Takes 30–45 minutes to fully understand.**

After reading, you will know:
- What task schema is expected
- How to schedule work
- When to create knowledge artifacts
- How to prevent the system from becoming overhead

---

## 3. Check relevant planning files

Depending on your task, read:

**Weekly planning:**
→ `03_PLANNING/03_WEEK/` + `05_TEMPLATES/TEMPLATE_Week_Final.md`

**Monthly planning:**
→ `03_PLANNING/02_MONTH/` + `05_TEMPLATES/TEMPLATE_Month_Final.md`

**Daily execution:**
→ `05_TEMPLATES/TEMPLATE_Daily.md`

**Quarterly planning:**
→ `03_PLANNING/01_QUARTER/Q1_Review_Q2Planning.md`

---

## 4. If task involves research / design / architecture

Check the knowledge system:
- `knowledge/research/` — existing research notes
- `knowledge/adr/` — architecture decisions (learn before deciding)
- `knowledge/design/` — system designs (reference for patterns)

---

## 5. If you need context on specific projects

Read project contexts:
- `08_PROJECT_CONTEXT/Zephyr_Project_Context.md`
- `08_PROJECT_CONTEXT/RobotOS_CONTEXT.md`
- `08_PROJECT_CONTEXT/Signee_CONTEXT.md`

---

## Core Mental Model

The system consists of:

```
┌─ EXECUTION SYSTEM ───────────────────────────┐
│ Task Standard + Backlog + Priority + Scheduler│
│ → Move work from idea to done                │
└──────────────────────────────────────────────┘
         ↕
┌─ PLANNING CADENCE (Q / M / W / D) ───────────┐
│ Quarter → Month → Week → Day                 │
│ → Align execution with strategy              │
└──────────────────────────────────────────────┘
         ↕
┌─ KNOWLEDGE SYSTEM ──────────────────────────┐
│ Research + ADR + Summaries + Design          │
│ → Build durable technical understanding      │
└────────────────────────────────────────────┘
         ↕
┌─ ANTI-GRAVITY RULES ────────────────────────┐
│ Escape Hatches + 80/20 Rule + Proportionality│
│ + Friction Check                             │
│ → Keep overhead < execution benefit          │
└────────────────────────────────────────────┘
```

**Key principle:** System serves execution, not the other way around.

---

## Working Rules (don't break these)

1. **Follow the task schema** — every task needs Goal/Type/Size/Ambiguity/Artifact/DoD
2. **Use Priority Score** — not as absolute, but to support backlog selection
3. **Escalate ambiguity** — if Ambiguity ≥ 4, do Spike/Research first (don't execute blindly)
4. **Create knowledge artifacts only if reusable** — not every research needs a note
5. **Honor the cadence** — but use Escape Hatches when needed (quick tasks, lightweight research, skip daily formality)
6. **Check for friction** — if system becomes heavier than useful, it's valid feedback for System Change

---

## Canonical Templates

Use these; don't create variants:

- `05_TEMPLATES/TEMPLATE_Week_Final.md` — plan & governance
- `05_TEMPLATES/TEMPLATE_Month_Final.md` — plan & capacity
- `05_TEMPLATES/TEMPLATE_Daily.md` — execution & shutdown

---

## Anti-Gravity Safeguards to Remember

1. **Quick Task hatch** — small clear work doesn't need full schema
2. **Lightweight Research hatch** — reading to unblock doesn't need artifact
3. **Skip Daily Formality hatch** — messy days can keep just 1 item + artifact + next step
4. **Proportionality rule** — formalization ∝ ambiguity × importance × reusability
5. **Friction check** — if avoiding the system or it slows you down, escalate to Weekly Review

---

## Common Scenarios

### "I have a task to execute"
1. Classify: Execution / Spike / KTLO / System Change?
2. Check: Does it fit Task Standard? (Goal/Type/Size/Ambiguity clear?)
3. If Ambiguity ≥ 4 → convert to Spike first
4. If small & clear → use Quick Task escape hatch
5. Schedule into week/day
6. Capture artifact on completion

### "I need to design or research something"
1. Estimate: Will output be reusable / affect decisions?
2. If yes → create knowledge artifact (Research Note, ADR, Summaries, or Design Doc)
3. If no (just unblocking today) → lightweight research, no artifact
4. Link artifact from relevant planning file

### "The system feels heavy"
1. Note it in Weekly Review (Friction Check)
2. If pattern repeats 2+ weeks → create System Change
3. Common fixes: reduce formalization, add escape hatch, skip non-critical template field

---

## Quick Links

- **Entry point:** `00_README/INDEX.md`
- **Main OS manual:** `01_OS/operating_system_thang_nguyen_v1_1.md`
- **General context:** `02_GENERAL_CONTEXT/00_CONTEXT.md`
- **Current week plan:** `03_PLANNING/03_WEEK/2026-W10_WeekPlan.md`
- **Current month plan:** `03_PLANNING/02_MONTH/2026-03_March_Planning.md`
- **Decision log:** `04_LOGS/Decision_Log.md`
- **Knowledge base:** `knowledge/`

---

**Ready to work?** Pick your task, check the index, follow the rules, and deliver the artifact.
