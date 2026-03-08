# LIFE_AGENT Architecture Map

> **Quick Read (30 sec):** This is your map of the LIFE_AGENT OS. It shows layers (Philosophy → System → Workflows → Execution → Projects), document roles, and the operating flow. Read this first when entering the repo. Update only when architecture changes.

---

## Table of Contents

- [1. Purpose of This Map](#1-purpose-of-this-map)
- [2. System Layers](#2-system-layers)
- [3. High-Level Architecture Diagram](#3-high-level-architecture-diagram)
- [4. Core Operating Flow](#4-core-operating-flow)
- [5. Document Role Map](#5-document-role-map)
- [6. How to Use This File](#6-how-to-use-this-file)
- [7. Navigation Entry Points](#7-navigation-entry-points)
- [8. Maintenance Rules](#8-maintenance-rules)

---

## 1. Purpose of This Map

This file is the **high-level orientation map** for LIFE_AGENT.

**What it does:**
- Shows the architecture layers and their relationships
- Explains document roles and where they fit
- Clarifies who reads what and why
- Provides navigation when the system feels confusing

**What it does NOT do:**
- Explain detailed workflows (see quarter/month/week/day docs)
- Provide task lists or execution steps
- Replace INDEX.md or BOOTSTRAP.md
- Cover project-specific details (see project context files)

---

## 2. System Layers

LIFE_AGENT has 6 conceptual layers, each with a different role:

| Layer | Role | Contents |
|---|---|---|
| **Philosophy** | Why and how to think about personal operating systems | §1–8: Core laws, cadence, templates overview |
| **System** | Formal execution engines that enforce discipline | §9–12: Task/Backlog/Priority/Scheduler + §13–14: Knowledge/Safeguards |
| **Workflows** | Repeating decision loops at different cadences | Quarter/Month/Week/Day templates + review patterns |
| **Execution** | Daily work blocks, signals, and context | Daily plan artifacts, KTLO tasks, deep work blocks |
| **Metrics** | Measure execution reality and feed adjustment signals into reviews | METRICS_ENGINE.md, TEMPLATE_Weekly/Monthly_Metrics.md |
| **Projects** | Concrete delivery tracks (Signee/RobotOS/Zephyr) | Project context docs, quarterly objectives, specific deliverables |

---

## 3. High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      PHILOSOPHY LAYER                       │
│        (Why & Mindset: Tempo, Scope, Energy, SPOF)         │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                      SYSTEM LAYER                           │
│      (Task/Backlog/Priority/Scheduler + Knowledge/Safeguards)
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                    WORKFLOWS LAYER                          │
│          (Quarter → Month → Week → Day Cadence)            │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                   EXECUTION LAYER                           │
│              (Deep Work Blocks + KTLO + Signals)           │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                    METRICS LAYER                            │
│       (Measure execution reality → feed adjustment signals) │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                    PROJECTS LAYER                           │
│         (Signee Demo | RobotOS Prototype | Zephyr KTLO)     │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Core Operating Flow

```
Quarter Direction Set
   ↓ (Strategic 3-month frame)
Monthly Plan + Review
   ↓ (Translate to 4-week outcomes)
Weekly Focus + Signal Check
   ↓ (Confirm weekly commitment)
Daily Execution (Blocks + KTLO)
   ↓ (Ship work + capture output)
Artifact / Daily Review
   ↓ (DoD + shutdown)
Feedback into Week/Month/Quarter
   ↓ (Inform next cadence)
Repeat
```

**Each layer:**
- **Quarter:** Define direction + capacity + gates
- **Month:** Translate to outcomes + allocation + weekly intent
- **Week:** Commit to work + monitor signals + decision point
- **Day:** Execute blocks + capture artifacts + protect energy

---

## 5. Document Role Map

| Document Type | Purpose | Key Examples |
|---|---|---|
| **Bootstrap/Index** | Entry point + navigation | BOOTSTRAP.md, INDEX.md, LIFE_AGENT_ARCHITECTURE.md |
| **Core OS** | Philosophy + system formalization | operating_system_thang_nguyen_v1_1.md (§1–14) |
| **Context Rules** | Governance for project/context management | CONTEXT_rule.md |
| **Planning Cadence** | Templates for each time horizon | TEMPLATE_Quarter/Month/Week/Daily.md |
| **Plan Instances** | Actual quarterly/monthly/daily plans | Q1_Review_Q2Planning.md, 2026-03_March_Planning.md |
| **Metrics** | Execution reality tracking + adjustment signals | METRICS_ENGINE.md, TEMPLATE_Weekly/Monthly_Metrics.md |
| **Automation** | Command interface + readiness spec + command pack | LIFE_AGENT_AUTOMATION_INTERFACE.md, TEMPLATE_Command_Pack.md |
| **Project Context** | Snapshot of each project's state | Signee/RobotOS/Zephyr_CONTEXT.md |
| **Review Docs** | Analysis + learning at month/quarter end | Part B of plan instances |
| **Logs** | Decision/Spike/Idea records | Decision_Log.md, Spike_Log.md |

---

## 6. How to Use This File

### Read this file when:
- You're new to the repo and want the 30-second overview
- The system feels messy and you want to reorient
- You need to place a new file or understand its role
- You're deciding which layer a change belongs in

### Update this file when:
- A new system layer emerges (rare)
- Document roles fundamentally change
- You realize a critical connection is missing

### Do NOT update this file for:
- Weekly or monthly content changes
- Project status updates
- Individual task progress
- Template refinements (see those templates)

---

## 7. Navigation Entry Points

**Start here:**
- [BOOTSTRAP.md](00_README/BOOTSTRAP.md) — Agent reading sequence
- [INDEX.md](00_README/INDEX.md) — Repo structure + file map
- [LIFE_AGENT_ARCHITECTURE.md](LIFE_AGENT_ARCHITECTURE.md) — This file

**Then choose by layer:**
- **Philosophy:** [Operating System v1.1](01_OS/operating_system_thang_nguyen_v1_1.md)
- **Workflows:** [TEMPLATE_Quarter_Final.md](05_TEMPLATES/TEMPLATE_Quarter_Final.md) or current quarter plan
- **Execution:** [TEMPLATE_Daily.md](05_TEMPLATES/TEMPLATE_Daily.md) or today's plan
- **Metrics:** [METRICS_ENGINE.md](metrics/METRICS_ENGINE.md)
- **Automation:** [LIFE_AGENT_AUTOMATION_INTERFACE.md](LIFE_AGENT_AUTOMATION_INTERFACE.md) or [Command Pack](05_TEMPLATES/TEMPLATE_Command_Pack.md)
- **Projects:** [Project Contexts](08_PROJECT_CONTEXT/) (Signee/RobotOS/Zephyr)

---

## 8. Maintenance Rules

1. **Keep it high-level.** If it needs detail, link to the source doc.
2. **Prefer clarity over completeness.** Missing one small detail is better than confusion.
3. **No task lists here.** This is architecture, not execution.
4. **No project status here.** That's in project context docs.
5. **Update rarely.** This map should feel stable across quarters.

---

**Last updated:** March 8, 2026 | **Version:** 1.0 | **Scope:** Architecture orientation only
