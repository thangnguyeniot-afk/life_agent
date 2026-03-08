# TEMPLATE_Command_Pack.md — LIFE_AGENT Command Quick Reference

> **Purpose:** Copy-paste commands for daily LIFE_AGENT operation.
> Send to Agent 2 (Copilot) directly. Fill in the fields in `[brackets]`.
> For reasoning or decision support, route to Agent 1 (ChatGPT) first.

---

## Quick Instructions

1. Copy the relevant command block below.
2. Fill in the fields marked `[...]`.
3. Send to Agent 2 (Copilot). It will read the repo and generate output.
4. For commands marked **CONFIRM**, Agent 2 will present output first. Reply "ok" or adjust.
5. For commands marked **APPEND**, Agent 2 writes immediately without preview.

---

## open day
> *Creates today's daily plan from template. Pre-fills date, week, context from repo.*
> **Output:** `YYYY-MM-DD_DailyPlan.md` | **Confirm:** Light

```
open day
priority: [1 sentence — most important outcome today]
energy: [Low / Normal / High]
```

---

## close day
> *Fills shutdown section and metrics capture in today's daily plan.*
> **Output:** Daily file updated | **Confirm:** Light

```
close day
actual blocks: [N] / [N planned]
energy: [Low / Normal / High]
artifact: [name or 1-line description, or "none"]
drift: [what went off-plan, or "none"]
```

---

## plan week
> *Creates next week plan file from template, prefilled with monthly intent and project context.*
> **Output:** `YYYY-Www_WeekPlan.md` | **Confirm:** Full

```
plan week
week: [YYYY-Www]
priorities: 
  1. [top priority]
  2. [second priority]
  3. [third — optional]
capacity note: [anything unusual this week, or "normal"]
fixed events: [locked meetings/blocks, or "none"]
```

---

## close week
> *Creates weekly review file and weekly metrics instance.*
> **Output:** `WeeklyReview.md` + `WeeklyMetrics.md` | **Confirm:** Full

```
close week
week: [YYYY-Www]
wins: [top 1–2 accomplishments]
drift: [main unplanned item or delay]
energy: [Low / Normal / High / Mixed]
actual blocks/day: [avg or Mon Tue Wed Thu Fri]
```

---

## plan month
> *Creates next month plan file aligned to quarter objectives.*
> **Output:** `YYYY-MM_MonthPlan.md` | **Confirm:** Full

```
plan month
month: [YYYY-MM]
theme: [1 sentence]
outcomes:
  O1: [outcome — deadline]
  O2: [outcome — deadline]
  O3: [outcome — deadline, optional]
capacity note: [anything unusual, or "normal"]
```

---

## close month
> *Fills monthly review (Part B) and creates monthly metrics instance.*
> **Output:** Month plan Part B filled + `MonthlyMetrics.md` | **Confirm:** Full

```
close month
month: [YYYY-MM]
wins:
  1. [win]
  2. [win]
  3. [win — optional]
lessons:
  1. [lesson]
  2. [lesson]
capacity truth: conservative [N] blocks/day / spike [N] blocks/day
adjustment: [1–2 things for next month]
```

---

## update metrics
> *Aggregates recent daily captures into weekly or monthly metrics file.*
> **Output:** Metrics file updated + warning signals flagged | **Confirm:** Light

```
update metrics
level: [weekly / monthly]
week or month: [YYYY-Www or YYYY-MM]
```

*(If daily files exist, Agent reads them. Otherwise provide raw daily data below.)*

```
Mon: blocks [N/N], energy [L/N/H], unplanned [Y/N]
Tue: blocks [N/N], energy [L/N/H], unplanned [Y/N]
Wed: blocks [N/N], energy [L/N/H], unplanned [Y/N]
Thu: blocks [N/N], energy [L/N/H], unplanned [Y/N]
Fri: blocks [N/N], energy [L/N/H], unplanned [Y/N]
```

---

## create spike
> *Instantiates a Spike document for a specific open question.*
> **Output:** `SPIKE_YYYY-MM-DD_<topic>.md` | **Confirm:** Light

```
create spike
topic: [clear question or unknown]
goal: [what you need to know]
constraints: [time, tech, scope]
deadline: [24h / 48h / 72h]
```

---

## log decision
> *Appends a formatted entry to Decision_Log.md.*
> **Output:** Decision_Log.md entry appended | **Confirm:** None (append directly)

```
log decision
decision: [what was decided]
options: [what was considered]
chosen: [what was selected]
owner: [who owns it]
next: [first action within 48h]
```

---

## triage inbox
> *Reads Idea_Parking_Lot.md and categorizes all items.*
> **Output:** Categorized list (Execute / Spike / Defer / Drop) | **Confirm:** Full

```
triage inbox
```

*(No fields needed. Agent reads the parking lot and returns a categorized list with suggested actions. Human confirms fate of each item.)*

---

## drift check
> *Reads current week plan vs actuals and surfaces drift signals.*
> **Output:** Drift summary + 1–2 adjustment options | **Confirm:** Full

```
drift check
```

*(No fields needed. Agent reads current week plan, daily files if any, and recent metrics. Returns findings. Human confirms before any plan changes are made.)*

---

## prepare artifact
> *Creates a knowledge artifact stub in the correct location.*
> **Output:** Artifact file created in `knowledge/` | **Confirm:** Light

```
prepare artifact
type: [ADR / Research / Summary / Design]
topic: [name of the artifact]
context: [1–2 sentences on why this artifact is needed]
```

---

## Routing Guide

| Situation | Route to |
|---|---|
| Routine template operation (open/close day, log, spike) | Agent 2 directly |
| Ambiguous signals, multiple possible root causes | Agent 1 first, then Agent 2 |
| Weekly/monthly planning (if priorities are clear) | Agent 2 directly |
| Weekly/monthly planning (if priorities are unclear) | Agent 1 first to frame, then Agent 2 |
| Strategic decision (scope, direction, tradeoff) | Agent 1 to present options → Human decides → Agent 2 writes |
| Drift check or system review | Agent 1 for interpretation → Human confirms → Agent 2 if file change needed |

---

**Last updated:** March 8, 2026 | **Version:** 1.0
