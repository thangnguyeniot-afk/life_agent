# LIFE_AGENT Automation Interface

> **Purpose:** Define how the human interacts with LIFE_AGENT through compact commands.
> This is the canonical spec for command-based operation. Update when commands stabilize or change.

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. Design Principles](#2-design-principles)
- [3. Team Role Model](#3-team-role-model)
- [4. Command Model](#4-command-model)
- [5. Core Command Set](#5-core-command-set)
- [6. Input Schemas](#6-input-schemas)
- [7. Output Contracts](#7-output-contracts)
- [8. Automation Boundaries](#8-automation-boundaries)
- [9. First Implementation Roadmap](#9-first-implementation-roadmap)
- [10. Maintenance Rules](#10-maintenance-rules)

---

## 1. Purpose

This file defines how the human owner of LIFE_AGENT interacts with the system through minimal-input commands.

The goal is to replace the current model — where the human manually fills templates and coordinates between files — with a lighter model where:

- The human provides a short command and a few key fields.
- Agent 2 (Copilot + MCP) reads the repo, generates the structured output, and writes the files.
- Agent 1 (ChatGPT) handles reasoning, framing, and interpretation when needed.
- The human only confirms direction or approves decisions.

This is not full automation. It is **decision-supported, command-driven operation** — the human stays in control of direction; the agents handle structure.

---

## 2. Design Principles

1. **Minimum human input.** The human should provide only what cannot be inferred. If the repo already has the answer, the agent reads it.

2. **Maximum structured output.** Every command produces a concrete file, entry, or structured list. No output should be free-form narrative without a schema.

3. **Decision support over blind automation.** Where judgment is required (scope, strategy, priority), the agent presents options. The human confirms. The agent then writes.

4. **Automation serves the OS.** If a flow adds overhead without reducing manual effort, it does not belong in the command set.

5. **Keep commands compact and repeatable.** A command should be usable from a single message. No multi-step rituals.

6. **Human confirms direction; agents handle structure.** Strategic decisions (what to prioritize, what to drop) are always human. Structural decisions (how to format, where to write, which template to use) are always agent.

7. **Read before writing.** Agent 2 must always read the current repo state before creating or updating any file. Never act on assumed state.

8. **Prefer reversible actions.** All file creation is additive. No deletion without explicit instruction.

---

## 3. Team Role Model

### Human

**Responsibilities:**
- Provides final direction on strategy, scope, and priorities
- Confirms or adjusts agent-generated output before it becomes canonical
- Sends commands with minimal structured input
- Approves decisions on carry-forwards, scope tradeoffs, context changes
- Escalates pattern-level concerns (sustained drift, project direction change)

**Does NOT do:**
- Fill templates manually for routine cadence operations
- Manually roll up daily → weekly → monthly metrics
- Search the repo for context before starting a planning session

---

### Agent 1 — ChatGPT

**Responsibilities:**
- Reasoning, triage, and framing for non-trivial questions
- Decision support: "here are 2–3 options with tradeoffs"
- Interpretation of ambiguous signals from weekly/monthly reviews
- Translation of raw human input into structured task/outcome proposals
- Intermediate step between human intent and Agent 2 file writes

**Does NOT do:**
- Direct file writes or repo modifications
- Final decisions on scope or priority
- Replacement of human judgment on strategic direction

**When to use:** Before sending a complex `plan week`, `close month`, or `drift check` command — if the human has rough notes or ambiguity about direction, Agent 1 helps clarify before Agent 2 acts.

---

### Agent 2 — Copilot + MCP

**Responsibilities:**
- Reading the full repo state before any operation
- Instantiating templates with correct fields filled
- Creating and updating plan instances, metrics files, logs, and artifact stubs
- Computing structurally inferrable data (completion rate, carry-over list, signal flags)
- Maintaining naming convention and folder placement

**Does NOT do:**
- Interpret ambiguous signals without presenting options
- Make scope or priority decisions
- Change strategic content in quarter/month plans without explicit instruction
- Guess when input is missing — asks for the minimum needed field

---

## 4. Command Model

### How Commands Work

```
Human sends:
  [command]
  [minimal structured input — 2–5 fields at most]

Agent 2 process:
  1. Read LIFE_AGENT_ARCHITECTURE.md (orientation)
  2. Read relevant files for this command (see §6 for what each command reads)
  3. Generate output according to Output Contract (§7)
  4. Present output or write file
  5. If confirmation required: present first, then write on approval

Human responds:
  "ok" / "write it" / [override or addition]
```

### Confirmation Model

| Risk Level | When Applied | Example |
|---|---|---|
| No confirmation | Pure additive, no strategic content | `log decision`, `create spike` (append only) |
| Light confirmation | Agent presents summary before writing | `open day`, `update metrics` |
| Full confirmation | Involves scope or planning decisions | `plan week`, `plan month`, `close month` |

---

## 5. Core Command Set

| Command | Purpose | Minimal Input | Expected Output | Confirmation |
|---|---|---|---|---|
| `open day` | Instantiate today's daily plan | Top priority (1 sentence) | `YYYY-MM-DD_DailyPlan.md` created in `03_PLANNING/04_DAILY/` | Light |
| `close day` | Fill shutdown section + metrics capture | actual blocks / energy / artifact / main drift | Daily file shutdown + metrics section filled | Light |
| `plan week` | Create next week plan file | Week number, top priorities, known capacity constraints | `YYYY-Www_WeekPlan.md` created in `03_PLANNING/03_WEEK/` | Full |
| `close week` | Complete week review + metrics | Main wins, main drift, energy pattern, actual blocks | `WeeklyReview.md` + `WeeklyMetrics.md` created | Full |
| `plan month` | Create next month plan file | Month, theme, top 3 outcomes (1-line each) | `YYYY-MM_MonthPlan.md` created in `03_PLANNING/02_MONTH/` | Full |
| `close month` | Fill monthly review + metrics | 3 wins, 3 lessons, capacity truth, adjustment | Month plan Part B filled + monthly metrics created | Full |
| `update metrics` | Fill metrics from daily captures | Raw daily data or "compute from daily files" | Weekly or monthly metrics file updated | Light |
| `create spike` | Instantiate spike document | Topic/question, constraint, deadline | `SPIKE_YYYY-MM-DD_<topic>.md` created | Light |
| `log decision` | Append decision record | Decision, options, chosen, rationale | `Decision_Log.md` entry appended | None |
| `triage inbox` | Process idea parking lot | None (Agent reads lot) | Categorized list: Execute / Spike / Defer / Drop | Full (human decides fate) |
| `drift check` | Surface current execution drift | None (Agent reads recent plans + actuals) | Drift summary + 1–2 adjustment options | Full (human confirms action) |
| `prepare artifact` | Create knowledge artifact stub | Type (ADR/Research/Summary/Design), topic | Artifact file created in `knowledge/` | Light |

---

## 6. Input Schemas

Each command requires only the fields listed. All other fields are either read from the repo or inferred.

---

### `open day`

```
open day
priority: [1 sentence — most important outcome today]
energy: [Low / Normal / High — optional, default Normal]
```

*Agent reads:* current week plan, current month North Star, project contexts.

---

### `close day`

```
close day
actual blocks: [N] / [N planned]
energy: [Low / Normal / High]
artifact: [name or 1-line description, or "none"]
drift: [1-line: what went off-plan, or "none"]
```

*Agent writes:* shutdown section + metrics capture in today's daily file.

---

### `plan week`

```
plan week
week: [YYYY-Www]
priorities: [top 2–3 items, 1 line each]
capacity note: [anything unusual this week — optional]
fixed events: [meetings/blocks already locked — optional]
```

*Agent reads:* current month plan weekly intent, project contexts, previous week carry-overs.

---

### `close week`

```
close week
week: [YYYY-Www]
wins: [top 1–2 accomplishments]
drift: [main unplanned item or delay]
energy pattern: [typical — Low / Normal / High / Mixed]
actual blocks/day: [avg or Mon-Fri list]
```

*Agent reads:* week plan for this week, any daily files for the week.
*Agent writes:* weekly review file + weekly metrics instance.

---

### `plan month`

```
plan month
month: [YYYY-MM]
theme: [1 sentence]
outcomes:
  O1: [outcome, deadline]
  O2: [outcome, deadline]
  O3: [outcome, deadline — optional]
capacity note: [anything unusual — optional]
```

*Agent reads:* current quarter plan, project contexts, last month's closing notes.

---

### `close month`

```
close month
month: [YYYY-MM]
wins: [top 1–3]
lessons: [top 1–3]
capacity truth: [conservative blocks/day + spike blocks/day]
adjustment: [1–2 things for next month]
```

*Agent reads:* current month plan (Part A + metrics), weekly reviews for the month.

---

### `create spike`

```
create spike
topic: [clear question or unknown]
goal: [what you need to know]
constraints: [time, tech, scope]
deadline: [24h / 48h / 72h]
```

---

### `log decision`

```
log decision
decision: [what was decided]
options: [what was considered]
chosen: [what was selected]
owner: [who owns it]
next: [first action within 48h]
```

---

### `triage inbox`

```
triage inbox
```

*Agent reads:* `04_LOGS/Idea_Parking_Lot.md`. Returns categorized list. Human confirms fate of each item.

---

### `drift check`

```
drift check
```

*Agent reads:* current week plan, recent daily files (if any), current month plan progress. Returns drift summary + adjustment options. Human confirms before any changes are made.

---

## 7. Output Contracts

Each command must produce the outputs listed below. No extra files unless needed.

| Command | Primary Output | Secondary Output | Metrics Touch |
|---|---|---|---|
| `open day` | Daily plan file created | None | None |
| `close day` | Daily file shutdown section filled | Metrics Capture section filled | Daily entry |
| `plan week` | Week plan file created | Carry-over list from previous week | None |
| `close week` | Weekly review file created | Weekly metrics instance created | Weekly rollup |
| `plan month` | Month plan file created | Links to project context + quarter plan | None |
| `close month` | Month plan Part B filled | Monthly metrics instance created | Monthly rollup |
| `update metrics` | Weekly or monthly metrics file updated | Warning signals flagged | Weekly or monthly |
| `create spike` | Spike file created | None | None |
| `log decision` | Decision_Log.md entry appended | None | None |
| `triage inbox` | Categorized item list (not a file) | Proposed actions per item | None |
| `drift check` | Drift summary (not a file) | 1–2 adjustment options | None |
| `prepare artifact` | Knowledge artifact stub created | None | None |

---

## 8. Automation Boundaries

### Safe to Automate

- File creation from templates (daily plans, week plans, spike docs, review stubs)
- Structured data entry (metrics capture, decision log, artifact stubs)
- Aggregation from structured inputs (weekly completion rate, energy pattern, signal checklist)
- Carry-over extraction (unfinished items from week plan)
- Risk flag propagation (open risks from month plan to next month plan)
- Naming and folder placement (enforcing naming convention)

### Requires Human Confirmation Before Writing

- Week/month plan priorities and capacity allocation
- Monthly outcome selection and scope tradeoffs
- Any change to strategic content in quarter or month plans
- Warning signal interpretation beyond threshold comparison
- Drift check recommendations before adjusting plans

### Agent 1 Should Interpret First (Before Agent 2 Writes)

- Ambiguous drift signals (multiple possible root causes)
- Monthly executive summary narrative
- System change proposals from weekly review
- Priority conflicts between projects in week planning
- Quarterly capacity truth validation

### Never Automate

- Strategic objective selection for new quarters
- Scope tradeoffs affecting delivery commitments
- Project direction changes or phase transitions
- Final decision on dropping a committed deliverable
- Context file updates without confirmed external data

---

## 9. First Implementation Roadmap

### Phase 1 — Daily Habit (Week 1–2)

**Target:** Establish `open day` → `close day` as the daily execution loop.

- Start each day with `open day [priority]`.
- End each day with `close day [3 fields]`.
- No other commands required.
- Goal: Generate real daily data for metrics.

**Success signal:** Daily plan files exist for 5+ consecutive days. Metrics Capture sections filled.

---

### Phase 2 — Weekly Rhythm (Week 2–4)

**Target:** Add `plan week` and `close week` around the daily loop.

- Monday: `plan week` to create week plan file.
- Friday or Sunday: `close week` to generate review + metrics.
- Daily loop continues as in Phase 1.

**Success signal:** Weekly review + weekly metrics exist for 2+ consecutive weeks. Completion rate is being tracked.

---

### Phase 3 — Decision Hygiene (Ongoing from Week 2)

**Target:** Use `create spike` and `log decision` whenever decisions arise.

- When encountering an ambiguous question → `create spike`.
- When making a meaningful choice → `log decision`.
- These are one-off, not cadence-based.

**Success signal:** Decision_Log.md has entries. Spike docs exist for resolved unknowns.

---

### Phase 4 — Monthly Closure (End of Month 1)

**Target:** Use `close month` and `plan month` at each month boundary.

- Last day of month: `close month` to fill Part B + create monthly metrics.
- First day of new month: `plan month` to align new month with quarter.

**Success signal:** Month plan has a completed Part B. Monthly metrics instance exists.

---

### Phase 5 — Drift and Triage (After Phase 2 Stabilizes)

**Target:** Use `drift check` and `triage inbox` periodically.

- Use `drift check` when something feels off mid-week.
- Use `triage inbox` monthly to clear the Idea Parking Lot.

---

## 10. Maintenance Rules

1. **Do not add a command without a repeated use-case.** If a flow doesn't happen at least 2x/month, it doesn't need a command.

2. **Keep input schemas at ≤5 fields.** If a command needs more than 5 fields, it's probably two commands.

3. **Avoid duplicate command semantics.** If two commands do the same thing in slightly different contexts, merge them or clarify the trigger condition.

4. **Prefer reuse of existing templates.** Every command should produce output that matches a canonical template. Do not invent output formats.

5. **Protect human attention first.** If a command requires the human to spend more time filling input than they save from not doing it manually, retire the command.

6. **Review command set quarterly.** At each quarter boundary, check: are all commands being used? Are any causing friction? Retire or simplify.

7. **Command pack (TEMPLATE_Command_Pack.md) is the user-facing layer.** Keep this spec focused on contract definitions. The command pack is the daily-use artifact.

---

**Last updated:** March 8, 2026 | **Version:** 1.0
