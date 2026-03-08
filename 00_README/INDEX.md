# LIFE_AGENT – INDEX

> Điểm vào chính để hiểu repo structure.  
> Mục đích: biết đọc gì trước – viết gì vào đâu – cadence nào chạy – template nào dùng.

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

- `knowledge/research/` — Research Notes (questions → findings → insights)
- `knowledge/adr/` — Architecture Decision Records
- `knowledge/summaries/` — Knowledge Summaries (reusable models)
- `knowledge/design/` — Design Documents (system architectures)

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
- Current Week Plan: `03_PLANNING/03_WEEK/2026-W10_WeekPlan.md`
- Current Month Plan: `03_PLANNING/02_MONTH/2026-03_March_Planning.md`
- Latest Quarterly Plan: `03_PLANNING/01_QUARTER/Q1_Review_Q2Planning.md`