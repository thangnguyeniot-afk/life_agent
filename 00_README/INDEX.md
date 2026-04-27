# LIFE_AGENT – INDEX

> Điểm vào chính để hiểu repo structure.  
> Mục đích: biết đọc gì trước – viết gì vào đâu – cadence nào chạy – template nào dùng.

---

## Table of Contents

- [0) Architecture Map (High-Level)](#0-architecture-map-high-level)
- [1) OS Architecture (§1–14)](#1-os-architecture-114)
- [2) Canonical Templates](#2-canonical-templates)
- [3) Reading Order (for agents)](#3-reading-order-for-agents)
- [4) Context & Logs](#4-context--logs)
- [5) Planning Cadence](#5-planning-cadence)
- [6) Knowledge System](#6-knowledge-system)
- [6b) Metrics Engine](#6b-metrics-engine)
- [6c) Automation Layer](#6c-automation-layer)
- [6d) Operations Layer](#6d-operations-layer)
- [7) Reviews & Monthly Journal](#7-reviews--monthly-journal)
- [8) Writing Rules](#8-writing-rules)
- [9) Cadence](#9-cadence)
- [10) Naming Convention](#10-naming-convention)
- [11) Daily Archival (keep hot 15 days)](#11-daily-archival-keep-hot-15-days)
- [12) System Health Checklist](#12-system-health-checklist)
- [13) Starting Out](#13-starting-out)

---

## 0) Architecture Map (High-Level)

**File:** `LIFE_AGENT_ARCHITECTURE.md`

Start here for a 30-second overview.

Includes:
- System layers (Philosophy → System → Workflows → Execution → Projects)
- High-level diagram
- Operating flow
- Document role map
- Navigation guide

---

## 1) OS Architecture (§1–14)

**Main source of truth:** `01_OS/operating_system_thang_nguyen_v1_1.md`

Includes:
- §1–8: Core OS laws, cadence, review flows, templates overview
- §9–12: **Execution System** (Task Standard, Backlog Structure, Priority Score, Scheduler Engine)
- §13: **Knowledge System** (Research Notes, ADR, Summaries, Design Documents)
- §14: **Anti-Gravity Rules** (Escape Hatches, 80/20 Rule, Proportionality, Friction Check)

---

## 2) Canonical Templates

**Location:** `05_TEMPLATES/`

- `TEMPLATE_Week_Final.md` — weekly planning + system change
- `TEMPLATE_Month_Final.md` — monthly planning + governance
- `TEMPLATE_Daily.md` — daily execution + shutdown

---

## 3) Reading Order (for agents)

1. Start with `00_README/INDEX.md` (this file)
2. Then `00_README/BOOTSTRAP.md` (agent reading sequence)
3. Then `01_OS/operating_system_thang_nguyen_v1_1.md` (full OS)
4. Then relevant planning files by need

---

## 4) Context & Logs

**General Context:**
- `02_GENERAL_CONTEXT/00_CONTEXT.md`
- `02_GENERAL_CONTEXT/CONTEXT_rule.md`

**Project Context:**
- `08_PROJECT_CONTEXT/` — per-project context files (Zephyr, RobotOS, Signee, etc.)

**Logs (keep permanently):**
- `04_LOGS/Decision_Log.md` — decisions with rationale
- `04_LOGS/Idea_Parking_Lot.md` — ideas waiting to be processed
- `04_LOGS/Spike_Log.md` — research spikes & learning outcomes
- `04_LOGS/Intelligence/` — weekly intelligence transfer records (context handoff between weeks)
- `04_LOGS/ADR/` — Architecture Decision Records (canonical ADR location; *not* `knowledge/adr/`)

---

## 5) Planning Cadence

**Quarter:**
- `03_PLANNING/01_QUARTER/` — quarterly reviews & planning

**Month:**
- `03_PLANNING/02_MONTH/` — monthly plans (use `TEMPLATE_Month_Final.md`)

**Week:**
- `03_PLANNING/03_WEEK/` — weekly plans (use `TEMPLATE_Week_Final.md`)

**Day (optional):**
- Max 15 recent daily files; archive or distill older ones

---

## 6) Knowledge System

**Location:** `knowledge/`

- `knowledge/research/` — Research Notes (persistent research material; see `knowledge/research/README.md` for scope distinction from `04_LOGS/Spike_Log.md`)
- `knowledge/summaries/` — Knowledge Summaries (reusable models and execution patterns)
  - `knowledge/summaries/EXEC_PATTERNS_CAPACITY_ENERGY.md` — capacity, energy, and project flow patterns
- `knowledge/design/` — Design Documents (interface sketches, architecture notes; see `knowledge/design/README.md`)

**Note:** Architecture Decision Records live in `04_LOGS/ADR/` — not in `knowledge/`.

---

## 6b) Metrics Engine

**Location:** `metrics/`

- `metrics/METRICS_ENGINE.md` — Canonical spec: 8 core metrics, warning signals, adjustment rules
- `metrics/TEMPLATE_Weekly_Metrics.md` — Weekly capture + drift signal checklist
- `metrics/TEMPLATE_Monthly_Metrics.md` — Monthly trend summary + capacity truth

**Purpose:** Lightweight, decision-oriented metrics that feed into weekly/monthly/quarterly reviews. Overhead target: <5 min/day, <15 min/week.

---

## 6c) Automation Layer

**Location:** repo root + `05_TEMPLATES/` + `tools/`

- `LIFE_AGENT_AUTOMATION_READINESS_REVIEW.md` — Analysis of what is automation-ready vs. still manual. First-cycle targets.
- `LIFE_AGENT_AUTOMATION_INTERFACE.md` — Canonical spec: command model, team roles, input schemas, output contracts, automation boundaries.
- `05_TEMPLATES/TEMPLATE_Command_Pack.md` — Practical quick-reference: 12 copy-paste command templates for daily use.
- `05_TEMPLATES/GENERATE_PEC.prompt.md` — Prompt template for generating PEC JSON from approved week plans (TickTick bridge Phase 2C).
- `tools/README.md` — TickTick bridge script inventory, phase status, usage instructions, and security rules. Entry point for all local tooling in `tools/`.

**Model:** Human → minimal input → Agent 2 (repo read + file write), with Agent 1 (reasoning) for non-trivial decisions.

---

## 6d) Operations Layer

**Location:** `01_OS/04_OPERATIONS/`

### Weekly Control

- `01_OS/04_OPERATIONS/WEEKLY_CONTROL/GENERATE_WEEKPLAN.md` — Canonical weekly planning procedure. Generates the weekly planning artifact (`W##_WeekPlan.md`) that translates month context, project states, and previous-week carry-over into a coherent weekly plan. Defines weekly goals, mission structure, anchor hypothesis, constraints, capacity, and Definition of Done. Serves as the strategic baseline for execution. Includes 10-step procedure, planning logic, anchor generation rules, carry-over handling, consistency check, and reusable command template.

- `01_OS/04_OPERATIONS/WEEKLY_CONTROL/GENERATE_WEEKLY_EXECUTION.md` — Canonical weekly execution generation procedure. Creates or updates the Weekly Execution file from Monthly direction + execution reality (recent Daily) reconciliation. Supports 3 modes: New generation (Mode A), Week reconstruction from Daily files (Mode B), Mid-week rebalance (Mode C). Includes data collection checklist, 10-step procedure, anchor rules, carry-over rules, reconstruction rules, consistency check, and reusable Copilot command template.

- `01_OS/04_OPERATIONS/WEEKLY_CONTROL/WEEKLY_REBALANCE.md` — Canonical mid-week rebalance procedure. Performs controlled correction of an active Weekly Execution file when real execution has drifted enough to threaten operational coherence. Operates on Daily evidence (not planning baseline). Defines 3 distortion levels (Local/Weekly/Structural), trigger thresholds, allowed/forbidden changes, escalation rules, and reusable command template. Does not rewrite WeekPlan or Month strategy.

- `01_OS/04_OPERATIONS/WEEKLY_CONTROL/WEEK_CLOSEOUT.md` — Canonical week-end closeout procedure. Closes an active weekly execution cycle by validating what was accomplished, identifying meaningful carry-over, and preparing clean input for next week generation. Evidence-based validation (Daily files are ground truth). Produces closeout summary with completed / partial / incomplete / blocked outcomes; extracts executable and blocked carry-over with exact next entry points; feeds factual state changes to Month/Project layers. Includes 10-step procedure, carry-over rules, month/project feedback rules, evidence standards, consistency check, and reusable command template.

### Daily Integration

- `01_OS/04_OPERATIONS/DAILY_INTEGRATION/INTEGRATE_DAILY.md` — Canonical daily reverse-integration procedure. Run after each closed Daily file to sync execution reality into Weekly / Monthly / Project / Anchor tracking layers. Includes 8-step procedure, guardrails, consistency check, and reusable Copilot command template.
- `01_OS/04_OPERATIONS/DAILY_INTEGRATION/PREPARE_NEXT_DAILY.md` — Canonical next-day preparation procedure. Run after INTEGRATE_DAILY to create or prefill the next Daily file from carry-over + weekly state. Includes 9-step procedure, carry-over rules, anchor selection rules, overload check, and reusable Copilot command template.

**Operational sequences (5-step weekly cycle):**

1. **At week start (planning):** GENERATE_WEEKPLAN → Create `W##_WeekPlan.md` from Month context + previous closure + project states + carry-over; defines goals, anchor, DoD, constraints
2. **Week baseline:** GENERATE_WEEKLY_EXECUTION (Mode A) → Create `W##_Execution.md` from `W##_WeekPlan.md` baseline + execution reality
3. **Daily workflow:** INTEGRATE_DAILY (after each day ends) → PREPARE_NEXT_DAILY (after integration) → Next day ready
4. **Mid-week if needed:** INTEGRATE_DAILY detects weekly-level drift → WEEKLY_REBALANCE corrects active Week file (if Level 2/3 distortion)
5. **At week end:** Final INTEGRATE_DAILY + **WEEK_CLOSEOUT** (validates delivery, extracts carry-over, prepares next-week hints)

**Trigger sequence for mid-week rebalance:**
- INTEGRATE_DAILY reveals daily/weekly mismatch
- WEEKLY_REBALANCE evaluates distortion level (Local/Weekly/Structural)
- Local Drift → absorb via carry-over (no rebalance)
- Weekly/Structural → WEEKLY_REBALANCE runs; corrects Week file; escalation if needed

**Trigger sequence for week closeout → next week start:**
- Final daily of week closes; all Daily integrations complete
- WEEK_CLOSEOUT validates execution against evidence (Daily files)
- Produces closure summary, carry-over extraction, next-week hints
- Prepares ground for next GENERATE_WEEKPLAN (carry-over becomes input to planning)

**Model:** Run by Agent 2 (OS procedures). Agent 1 only when escalation, strategic decision, or rebalance justification required.

---

## 7) Reviews & Monthly Journal

**Reviews (keep permanently):**
- `07_REVIEWS/` — weekly, monthly, quarterly reviews

**Monthly Journal:**
- `06_MONTHS/` — narrative monthly logs

---

## 8) Writing Rules

| What | Where | Duration |
|---|---|---|
| OS/principles | `01_OS/` | permanent |
| General context | `02_GENERAL_CONTEXT/` | long-term |
| Project context | `08_PROJECT_CONTEXT/` | long-term |
| Logs (Decision/Idea/Spike) | `04_LOGS/` | permanent |
| Planning (Q/M/W) | `03_PLANNING/` | long-term |
| Daily plans (optional) | external tool preferred, or `03_PLANNING/04_DAILY/` | HOT 15 days |
| Reviews | `07_REVIEWS/` | permanent |
| Monthly narration | `06_MONTHS/` | long-term |
| Knowledge artifacts | `knowledge/` | permanent |

### Readability Guard (Mandatory System-Wide)

All generated planning/review artifacts (weekly plans, daily execution, monthly reviews, project contexts, etc.) must follow scan-friendly formatting rules to ensure clarity and executability:

**Core Rules:**
- Body paragraphs max 3–4 lines in normal markdown view
- Multi-idea sections split into bullets or labeled sub-blocks
- All numbers, allocations, rules, and comparisons formatted as bullets/tables/labeled blocks (not prose)
- Scan-friendly structure: short intro → bullet breakdown → explicit labels
- No walls-of-text; synthesis broken into 2–4 short bullets

**Enforcement:** Validation checklist required before finalizing any artifact (see GENERATE_WEEKPLAN.md § Readability Guard; GENERATE_WEEKLY_EXECUTION.md § Readability Guard; CHECKLIST_AntiCompliance.md § Test Block 3).

---

## 9) Cadence

**Minimum cadence:**

- **Daily (5–10'):** Read week plan → pick 2 deep blocks + builder tasks
- **Weekly (60'):** Weekly review (signals) + system change decision + next week planning
- **Monthly (45–60'):** Monthly review (3 wins / 3 lessons / 3 bottlenecks) + capacity adjustment
- **Quarterly (60–90'):** Quarterly review + next quarter planning

---

## 10) Naming Convention

- Week Plan: `YYYY-Www_WeekPlan.md`
- Month Plan: `YYYY-MM_MonthPlan.md`
- Quarter Plan: `YYYY-Qx_QuarterPlan.md`
- Daily Plan (optional): `YYYY-MM-DD_DailyPlan.md`
- Daily Review (optional): `YYYY-MM-DD_DailyReview.md`

---

## 11) Daily Archival (keep hot 15 days)

**Hot files (keep in folder):** max 15 most recent daily files

**When day #16 arrives (pick one):**
1. Delete old file after distilling 1 win + 1 lesson + 1 bottleneck → Monthly review
2. Or move to `ARCHIVE/YYYY/MM/` for long-term storage

> **Key rule:** Logs (Decision/Idea/Spike) + Weekly/Monthly reviews stay permanent. Daily can be archived or deleted since it's just execution narrative.

**Cold storage (historical files):** `99_ARCHIVE/` — for files that are complete and historical but worth preserving (design rationale, closed-phase audit records, process logs). See `99_ARCHIVE/README.md` for policy and archive index.

---

## 12) System Health Checklist

Repo is in good shape when:
- ✅ 1 correct OS manual in `01_OS/`
- ✅ Current week plan exists in `03_PLANNING/03_WEEK/`
- ✅ Current month plan exists in `03_PLANNING/02_MONTH/`
- ✅ Logs capture new Decision/Idea/Spike items
- ✅ Reviews (weekly/monthly/quarterly) are kept long-term
- ✅ Daily folder stays ≤15 files (hot) or archived (cold)
- ✅ Knowledge artifacts go into `knowledge/` by type

---

## 13) Starting Out

**First-time user or agent?**  
Read in this order:
1. `00_README/INDEX.md` (this file)
2. `00_README/BOOTSTRAP.md` (agent reading guide)
3. `01_OS/operating_system_thang_nguyen_v1_1.md` (full system)
4. Relevant planning/template files as needed

**Quick links (update as you work):**

- Current Week Plan: `03_PLANNING/03_WEEK/W14/2026-W14_WeekPlan.md`
- Current Month Plan: `03_PLANNING/02_MONTH/2026-04_April_Plan.md`
- Latest Quarterly Plan: `03_PLANNING/01_QUARTER/Q1_Review_Q2Planning.md`
- Command Quick Reference: `05_TEMPLATES/TEMPLATE_Command_Pack.md`