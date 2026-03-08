# LIFE_AGENT Metrics Engine

> **Purpose:** Lightweight, decision-oriented metrics layer for the LIFE_AGENT OS.
> Metrics exist to support judgment — not to replace it.

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. Design Principles](#2-design-principles)
- [2.1 Pilot Mode (First 2–4 Weeks)](#21-pilot-mode-first-24-weeks)
- [3. Core Metrics](#3-core-metrics)
- [4. Roll-up Model](#4-roll-up-model)
- [5. Warning Signals](#5-warning-signals)
- [6. Adjustment Rules](#6-adjustment-rules)
- [7. Integration with LIFE_AGENT Cadence](#7-integration-with-life_agent-cadence)
- [8. Maintenance Rules](#8-maintenance-rules)

---

## 1. Purpose

The Metrics Engine exists to answer one question at each review level:

> **"Is what I planned matching what is actually happening — and if not, what should I adjust?"**

Specifically it:
- Measures execution reality (vs. planned assumptions)
- Detects drift early before it compounds across weeks
- Estimates real sustainable capacity (not theoretical)
- Provides evidence for planning adjustments
- Makes reviews less emotional and more grounded in data

**What it is NOT:** a productivity tracker, a performance score, or a self-judgment system.

---

## 2. Design Principles

- **Low overhead.** If it takes more than 5 minutes/week to capture, it won't survive.
- **Decision-oriented.** Every metric must map to a possible action.
- **Measure what supports action.** If a metric doesn't change a decision, drop it.
- **Prioritize leading indicators.** Catch problems before delivery impact, not after.
- **No vanity metrics.** Total tasks completed is noise. Completion rate against plan is signal.
- **Trend over signal.** One bad day is noise. Three bad days is a pattern. Act on patterns.
- **Clarity over completeness.** 5 useful metrics beat 15 partial ones.

---

## 2.1 Pilot Mode (First 2–4 Weeks)

When you start using the Metrics Engine:

- **Establish baseline, not optimize aggressively.** The first 2–4 weeks are for learning your real patterns, not for perfect execution.
- **Prioritize consistency over precision.** Capture metrics the same way each day/week. Precision adjustments come later.
- **Do not add new metrics during pilot.** Stick to the 8 core metrics. New ideas go to a backlog.
- **Adjust thresholds only after you have data.** The warning signal thresholds (e.g., "<70% completion rate") are educated guesses. Update them only after 4–8 weeks of real usage.
- **If overhead feels high, drop a metric temporarily.** Better to track 6 metrics consistently than 8 haphazardly. Resume later.

---

## 3. Core Metrics

### 3.1 Planned Blocks

- **What:** Number of deep work blocks committed in weekly plan
- **How:** Count from weekly plan (Section 6 of TEMPLATE_Week_Final)
- **Why:** Baseline for all other metrics; reflects planning ambition

### 3.2 Actual Blocks

- **What:** Number of deep work blocks actually executed
- **How:** Count from daily shutdown / DoD section
- **Why:** Reveals true capacity vs. assumed capacity

### 3.3 Block Completion Rate

- **What:** Actual Blocks ÷ Planned Blocks × 100%
- **How:** Calculated from the two metrics above
- **Why:** Primary drift indicator; <70% for 2 consecutive weeks = structural problem

### 3.4 Deep Work Hours

- **What:** Hours spent in focused, artifact-producing work (not meetings, not shallow tasks)
- **How:** Estimated from block count × avg block length (default: 1.5h/block)
- **Why:** Reveals whether execution capacity is protecting high-value work

### 3.5 Unplanned Work %

- **What:** Portion of week consumed by unplanned interrupts vs. planned capacity
- **How:** Estimated at weekly shutdown (rough %: "roughly X hours unplanned this week")
- **Why:** High unplanned work is the primary cause of completion rate collapse

### 3.6 Artifact Count

- **What:** Number of meaningful outputs produced (ADR, RFC, runbook, commit, doc)
- **How:** Count from daily logs / DoD checklist
- **Why:** Proxy for actual delivery; prevents "busy but nothing shipped" invisibility

### 3.7 Energy Stability

- **What:** Proportion of days with Normal or High energy vs. Low
- **How:** From daily `Energy level` tag (Low / Normal / High)
- **Why:** Sustained low energy = capacity inflation. Energy crash = next-week cascade.

### 3.8 Ambiguity Load

- **What:** Proportion of blocks classified as Ambiguous (no clear DoD before start)
- **How:** From daily block specs (Ambiguity field: Low / Medium / High)
- **Why:** High ambiguity → low completion rate → planning needs more Spikes upfront

---

## 4. Roll-up Model

```
Daily (5 min) → capture blocks, artifacts, energy, unplanned interrupts
    ↓
Weekly (10 min) → summarize 5 days, compute rates, check warning signals
    ↓
Monthly (15 min) → aggregate 4-5 weeks, identify trends, update capacity truth
    ↓
Quarterly (20 min) → validate planning assumptions, feed into next quarter baseline
```

| Level | What is captured | How it is used |
|---|---|---|
| Daily | Actual blocks, energy, unplanned items, artifact | Input to weekly summary |
| Weekly | Completion rate, drift signals, ambiguity load | Adjustment decision for next week |
| Monthly | Trend across 4 weeks, capacity truth, system friction | Monthly plan adjustment |
| Quarterly | Capacity baseline validation, assumption audit | Quarter planning input |

---

## 5. Warning Signals

| Signal | Threshold | What it usually means |
|---|---|---|
| Low actual capacity | Avg actual blocks/day < 3 for 2+ consecutive weeks | Capacity inflation in planning. Reduce planned blocks. |
| Low completion rate | < 70% for 2+ consecutive weeks | Too ambitious OR too many interrupts. Split or buffer. |
| High unplanned work | > 25% of weekly capacity unplanned | Buffer is insufficient. System needs more slack. |
| Sustained low energy | Low energy 3+ days in a week | Overload building. Deload before cascade. |
| High ambiguity load | > 40% of blocks marked High ambiguity | Insufficient prep. Add Spikes before deep work. |
| Low artifact count | 0–1 artifacts for 2+ consecutive weeks | Work consumed without output. Tighten task-to-artifact coupling. |

---

## 6. Adjustment Rules

| Signal | Adjustment Action |
|---|---|
| Low completion rate | Reduce planned blocks by 1–2 next week. Diagnose root cause. |
| High unplanned work | Add explicit buffer block to weekly plan. Protect at least 1 unscheduled slot/day. |
| Sustained low energy | Deload week: max 3 blocks/day, no new scope, recovery priority. |
| High ambiguity | Convert ambiguous blocks to Spikes. Define DoD before scheduling execution. |
| Low artifact count | Tighten task definition. Each block must have an artifact target before it starts. |
| Multiple signals at once | Trigger Strategic Drift Check. Escalate to weekly review decision point. |

---

## 7. Integration with LIFE_AGENT Cadence

### Daily Review (~5 min)
- Record actual blocks, energy level, unplanned work (rough estimate), artifact produced
- No analysis needed — capture only

### Weekly Review (~10 min, section 2 of TEMPLATE_Week_Final)
- Fill TEMPLATE_Weekly_Metrics.md
- Check warning signals (section 3)
- Make one adjustment decision (section 5 of weekly review)

### Monthly Review (~15 min, complementary to Part B of monthly plan)
- Fill TEMPLATE_Monthly_Metrics.md
- Review 4-week trend: is capacity truth matching planning assumptions?
- Feed capacity truth into next month's planned block count

### Quarter Review (~20 min, feeds into Part B Section 4 of quarter template)
- Review all monthly metrics summaries
- Validate or update capacity baseline (used in next quarter's §4 Strategic Allocation)
- Identify structural patterns (e.g., "Ambiguity always spikes in Month 1")

---

## 8. Maintenance Rules

1. **Do not add a metric without a decision use-case.** Ask: "What would I do differently based on this metric?" If no answer — don't add it.
2. **Keep the engine lightweight.** The target overhead is <5 min/day and <15 min/week.
3. **Prefer trend over single-day noise.** One bad day tells you nothing. A 5-day pattern tells you to act.
4. **Update thresholds only with evidence.** If "< 70% completion rate" turns out to be too strict for your actual pattern, adjust — but document why.
5. **Metrics support judgment; they do not replace it.** A 68% completion rate with an emergency the previous week is fine. Context always wins.
6. **Review the engine itself quarterly.** If a metric is never reading anything useful, retire it.

---

**Last updated:** March 8, 2026 | **Version:** 1.0
