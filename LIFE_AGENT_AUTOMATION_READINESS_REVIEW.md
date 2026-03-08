# LIFE_AGENT Automation Readiness Review

> **Purpose:** Analyze the LIFE_AGENT repo from the perspective of automation readiness.
> Identify what currently exists, what is still manual, and what should be automated first.
> Based on the actual repo state as of March 8, 2026.

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. Current System Snapshot](#2-current-system-snapshot)
- [3. What Is Already Strong Enough to Automate](#3-what-is-already-strong-enough-to-automate)
- [4. What Is Still Too Manual](#4-what-is-still-too-manual)
- [5. Candidate Automation Flows](#5-candidate-automation-flows)
- [6. Constraints and Risks](#6-constraints-and-risks)
- [7. Recommendation](#7-recommendation)

---

## 1. Purpose

This document reviews the LIFE_AGENT repository from the perspective of automation readiness.

The system has reached a mature documentation and planning state. It now has:
- A formal OS spec (14 sections)
- A full planning cadence (Quarter → Month → Week → Day)
- A metrics engine with 8 core metrics
- Canonical templates for every cadence level
- Context docs for all 3 active projects
- An architecture map and navigation system

The next question is practical: **which parts of this system can be reliably handled by an agent, and which parts must remain human-driven?**

This review answers that question and defines the first automation targets.

**New target operating model:**

```
Human            → provides minimal input, confirms decisions, approves direction
Agent 1 (ChatGPT) → reasoning, triage, framing, interpretation, decision support
Agent 2 (Copilot) → repo reading, file creation, template instantiation, structured writes
```

---

## 2. Current System Snapshot

### 2.1 Philosophy and OS

- **File:** `01_OS/operating_system_thang_nguyen_v1_1.md` (14 sections, ~750 lines)
- **Maturity:** High. Fully formalized. Covers: Laws, Cadence, Review Flows, Execution System (Task/Backlog/Priority/Scheduler), Knowledge System, Anti-Gravity Rules.
- **Relevance to automation:** §9 Task Standard, §12 Scheduler Engine, and §14 Anti-Gravity Rules directly constrain what automation should and should not do.

### 2.2 Planning Cadence

- **Quarter:** `Q1_Review_Q2Planning.md` — 4 strategic objectives, Stage Gates, Scorecard, protection rules. Structured, complete.
- **Month:** `2026-03_March_Planning.md` — 3 outcomes with DoD/artifacts, capacity budget, weekly intent, risks. Production-ready structure.
- **Week:** Template exists (`TEMPLATE_Week_Final.md`). Current week file (`2026-W10_WeekPlan.md`) is empty — no content yet.
- **Day:** Template exists (`TEMPLATE_Daily.md`). No daily plan instances currently in repo. Daily files are optional and kept hot (≤15 days).

**Observation:** The quarter and month plans have been manually authored and are high quality. The week and day levels are where the operational gap is most visible — the templates exist but the actual execution artifacts are not being created or tracked in the repo.

### 2.3 Metrics Layer

- **Files:** `metrics/METRICS_ENGINE.md`, `metrics/TEMPLATE_Weekly_Metrics.md`, `metrics/TEMPLATE_Monthly_Metrics.md`
- **Maturity:** Designed, not yet in active use. Pilot Mode guidance exists (2.1), but no metric instance files have been created yet (no `2026-W10_Metrics.md`, no `2026-03_Metrics.md`).
- **Relevance to automation:** The metric schemas are very structured (tables, defined fields, discrete values). This is ideal for agent-driven instantiation and rollup.

### 2.4 Templates

All canonical templates exist and are well-structured:

| Template | Location | Status |
|---|---|---|
| TEMPLATE_Daily.md | 05_TEMPLATES/ | Ready. Metrics Capture section added. |
| TEMPLATE_Week_Final.md | 05_TEMPLATES/ | Ready. Full planning + review structure. |
| TEMPLATE_Month_Final.md | 05_TEMPLATES/ | Ready. Part A + Part B structure. |
| TEMPLATE_Quarter_Final.md | 05_TEMPLATES/ | Ready. Stage Gate governance. |
| TEMPLATE_Spike.md | 05_TEMPLATES/ | Ready. Minimal 7-section structure. |
| TEMPLATE_Weekly_Metrics.md | metrics/ | Ready. Decision Output section added. |
| TEMPLATE_Monthly_Metrics.md | metrics/ | Ready. Decision Output section added. |

### 2.5 Architecture Map

- `LIFE_AGENT_ARCHITECTURE.md` — 6-layer diagram, Document Role Map, navigation entry points. Current and accurate.
- Provides the orientation context any agent needs before operating in the repo.

### 2.6 Project Contexts

| Project | Status | Relevant Deadlines |
|---|---|---|
| Signee | Build phase. Android scaffold 15%, PWA 0%. Sprint 1 Foundation. | Demo Q1: 2026-05-30 |
| RobotOS | Build phase. 15% complete. v0.1 Alpha target 2026-04-30. | Prototype Q1: 2026-05-31 |
| Zephyr | Maintenance mode. DBUS2 testing, release stability. Office hours only. | Ongoing releases |

---

## 3. What Is Already Strong Enough to Automate

These structures are well-defined, structured, and repeatable. They are safe to hand to an agent.

### 3.1 Daily Plan Instantiation

- `TEMPLATE_Daily.md` has all required fields pre-defined.
- Date and week number are always known from input.
- Morning setup, block structure, and metrics capture are templated.
- **Agent action:** Read template → substitute date/week → create `YYYY-MM-DD_DailyPlan.md`.
- **Human input needed:** Top priority, optional energy override.

### 3.2 Weekly Plan File Creation

- `TEMPLATE_Week_Final.md` is fully structured.
- Monthly intent (Weekly Intent section in month plan), project contexts, and capacity budget are all readable from the repo.
- **Agent action:** Read current month plan + project contexts → instantiate week plan with pre-filled context.
- **Human input needed:** Top priorities, known fixed events, capacity notes.

### 3.3 Metrics Template Instantiation

- `TEMPLATE_Weekly_Metrics.md` and `TEMPLATE_Monthly_Metrics.md` have clearly defined table schemas.
- Metric captures (actual blocks, energy, unplanned %) are structured fields.
- **Agent action:** Create instance file from template, pre-fill targets from current week/month plan.
- **Human input needed:** Daily actuals (3 fields per day from close day command).

### 3.4 Weekly Metrics Rollup

- If daily close data is captured (actual blocks / energy / unplanned), weekly totals and completion rate can be computed.
- Warning signal checklist (7 items) maps directly to threshold comparisons.
- **Agent action:** Aggregate 5 daily captures → fill Weekly Snapshot table → flag warning signals.
- **Human input needed:** Confirmation that signals are correct before writing.

### 3.5 Spike Document Creation

- `TEMPLATE_Spike.md` has 7 sections: Context, Goal, Constraints, Options, Risks, Deadline, Next 48h.
- No strategic judgment required to instantiate — only topic and framing.
- **Agent action:** Create `SPIKE_YYYY-MM-DD_<topic>.md` from template.
- **Human input needed:** Topic, goal, constraints, deadline.

### 3.6 Decision Log Entry

- `04_LOGS/Decision_Log.md` uses a simple single-line schema.
- Format: `YYYY-MM-DD | Deadline | Decision | Options | Chosen | Owner | Next 48h`
- **Agent action:** Append formatted entry.
- **Human input needed:** Decision, options, chosen, rationale (can be minimal).

### 3.7 Carry-Over and Risk Flags at Week/Month Close

- Unfinished tasks in weekly plan → carry-over list for next week.
- Unresolved risks in month plan → risk flags for next month.
- **Agent action:** Scan current plan for incomplete items → generate structured carry-over + flag list.
- **Human input needed:** Confirmation of what to carry vs. drop.

---

## 4. What Is Still Too Manual

These areas require human judgment, strategic context, or qualitative interpretation that should not be delegated to an agent without confirmed input.

### 4.1 Strategic Priority and Scope Decisions

- Which outcomes to commit to in any given month/quarter.
- Scope tradeoffs (what to drop when capacity is exceeded).
- New scope additions or project direction changes.
- **Why not automate:** These directly affect delivery direction. Wrong automation = silent scope drift.

### 4.2 Weekly Signal Interpretation

- The weekly review requires judgment: "Is this signal noise or a pattern?"
- Signals like "task repeated 3x" may mean SPOF risk OR legitimate ongoing work.
- Anti-Anchor assessment (Dopamine Leaks, Sleep Killers) is qualitative.
- **Why not automate:** Context-dependent. Agent 1 (ChatGPT) can assist with framing, but human must confirm.

### 4.3 Project Context Updates

- Signee, RobotOS, Zephyr context files are manually curated snapshots.
- Project state changes (new blockers, new team state, phase transitions) require human awareness of external events.
- **Why not automate:** The context files are the agent's grounding — automating them without confirmed data creates misinformation risk.

### 4.4 Monthly and Quarterly Review Narrative

- Executive Summary of the Month, System Change Review, Capacity Reality Review — all require qualitative synthesis.
- Week-by-week trend interpretation requires memory of what actually happened.
- **Why not automate:** A wrong narrative is worse than no narrative. Agent 1 can draft; human must confirm.

### 4.5 Backlog Selection and Priority Scoring

- The Priority Score (§11) uses 4 factors, but applying it correctly requires knowing strategic alignment.
- Backlog selection for next week involves judgment about what the month's north star actually requires.
- **Why not automate:** Automating selection without alignment verification creates "busy but misaligned" failure mode.

### 4.6 Energy and Life Anchor Assessment

- Daily energy, sleep quality, life anchor checks — these are intrinsic observations.
- No structured data source exists in the repo for these.
- **Why not automate:** Would require input from human anyway; no gain from wrapping in automation.

---

## 5. Candidate Automation Flows

Listed in priority order (highest frequency + lowest risk first):

| Priority | Flow | Trigger | Agent Action | Human Confirms? |
|---|---|---|---|---|
| 1 | open day | Human sends `open day` command | Create daily plan file from template | On key priorities |
| 2 | close day | Human sends `close day` + 3-field input | Fill shutdown + metrics in daily file | On signals |
| 3 | plan week | Human sends `plan week` command | Create week plan file with prefilled context | On priorities |
| 4 | close week | Human sends `close week` + summary input | Create weekly review file + metrics rollup | On drift signals |
| 5 | create spike | Human sends `create spike [topic]` | Instantiate spike template | On options/deadline |
| 6 | log decision | Human sends `log decision` + fields | Append to Decision_Log.md | No (append only) |
| 7 | update metrics | Human sends `update metrics` | Aggregate recent daily data into weekly metrics | On warning signals |
| 8 | triage inbox | Human sends `triage inbox` | Read Idea_Parking_Lot → categorize + propose | Human decides fate |
| 9 | drift check | Human sends `drift check` | Read recent plan vs actuals → surface 1–2 options | Human confirms action |
| 10 | plan month | Human sends `plan month` | Create month plan file with quarter alignment | On outcomes + capacity |

---

## 6. Constraints and Risks

### 6.1 What Must NOT Be Automated Blindly

- **Strategic priority changes** — altering which project gets capacity without explicit human direction
- **Scope decisions** — dropping or adding outcomes without confirmed tradeoff
- **Context file updates** — changing project state without verified external input
- **Signal interpretation** — classifying signals as "noise" or "pattern" without human confirmation
- **Carrying forward tasks without asking** — a carried-over task may no longer be relevant

### 6.2 Agent Boundary Rules

- Agent 2 (Copilot) must NOT make strategic content decisions.
- Agent 2 reads existing repo state before acting — no assumptions about current state.
- If input is ambiguous, Agent 2 proposes options; it does NOT choose silently.
- Agent 1 (ChatGPT) should frame decisions before Agent 2 writes files.
- All file creation must be reversible (never delete without explicit instruction).

### 6.3 Pilot Mode Risk

- The metrics layer is new and not yet validated with real data.
- Initial automation of metrics rollup may produce misleading signals if capture is inconsistent.
- Run `open day` + `close day` for at least 2 weeks before attempting automated rollup.

---

## 7. Recommendation

**Implement in this order:**

1. **Pilot: `open day` + `close day`** (Week 1–2)
   - Lowest risk. Creates habit of daily capture without strategic judgment.
   - Validates that template instantiation works correctly.
   - Produces the daily data needed for all downstream flows.

2. **Add: `plan week` + `close week`** (Week 2–4)
   - Once daily data accumulates, week-level operations become meaningful.
   - Weekly metrics rollup can be tested against real data.

3. **Add: `create spike` + `log decision`** (Ongoing)
   - High value per use. Low overhead. Directly supports decision hygiene.

4. **Add: `drift check`** (After 2 weeks of data)
   - Only useful once there's real execution data to compare against plans.

5. **Add: `plan month` + `triage inbox`** (Month boundary)
   - Monthly plan creation is the highest-leverage single agent action per cycle.
   - Inbox triage clears accumulated noise without requiring deep human attention.

**Do NOT automate in the first cycle:**
- Monthly/quarterly review narrative (requires synthesized judgment)
- Backlog selection scoring (requires strategic alignment check)
- Project context updates (requires external ground truth)

---

**Last updated:** March 8, 2026 | **Version:** 1.0
