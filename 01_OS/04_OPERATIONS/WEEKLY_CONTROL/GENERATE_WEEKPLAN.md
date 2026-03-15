# GENERATE_WEEKPLAN

## Purpose

Generate the weekly planning artifact (`W##_WeekPlan.md`) that translates current month context, project states, and previous-week carry-over into a coherent, executable weekly plan.

The WeekPlan is the **planning baseline** for the weekly cycle. It defines:
- Weekly goals (what must be delivered this week)
- Mission structure and priorities (how work is organized)
- Anchor hypothesis (how daily execution will be framed and tracked)
- Capacity constraints and scope expectations
- Definition of Done (completion criteria apply week-wide)

The WeekPlan is generated **before** Weekly Execution and serves as the reference for all daily execution decisions. It is NOT a detailed daily schedule; it is a strategic frame within which daily planning inherits consistency.

---

## When to Run

**Timing Triggers:**
1. **End of previous week** — after WEEK_CLOSEOUT completes (the previous week is fully closed and carry-over is identified)
2. **Weekly planning boundary** — as the first formal step of the new weekly cycle
3. **Before GENERATE_WEEKLY_EXECUTION** — must have a valid WeekPlan before generating the weekly execution file
4. **Before daily file generation** — must have a WeekPlan before creating the first Daily file for the new week

**Frequency:** Once per week (typically Sunday evening or Monday early morning, depending on cycle boundary).

**Skip Condition:** Do NOT re-run GENERATE_WEEKPLAN mid-week unless WEEKLY_REBALANCE explicitly triggers a replanning. If weekly execution begins to drift, run WEEKLY_REBALANCE first; only escalate to full replanning if the escalation path explicitly requires it.

---

## Prerequisites

All of the following must be complete before running GENERATE_WEEKPLAN:

### Week Closure
- Previous week (W##-1) is fully closed (WEEK_CLOSEOUT complete)
- Previous Weekly Execution file is finalized and archived
- Carry-over tasks have been extracted and documented (from WEEK_CLOSEOUT output)

### Month Context
- Month file (YYYY-MM_Month.md) exists and is current (updated within last 48 hours if active changes occurred)
- Month strategy and goals are documented
- Month phase (early/mid/late) is clear
- Month-level risks or escalations are documented

### Project States
- All project context files (ROBOTOS_CONTEXT.md, Signee_CONTEXT.md, Zephyr_Project_Context.md) are current
- Known blockers, dependencies, and risks are documented
- Project deliverables or milestones for this week are identified

### Capacity and Anchor History
- Anchor tracking file exists (daily anchor adherence history for past 3–4 weeks)
- Capacity reality for the coming week is known (vacation, external commitments, etc.)
- Previous anchor patterns are reviewed (what worked, what needs adjustment)

### Open Items
- All carry-over from previous week closeout is available
- Any mid-week rebalance notes (if W##-1 had rebalancing) are reviewed
- Decision log is current (if month-level or strategic decisions affect this week)

---

## Inputs

### Primary Inputs

1. **Month file** (`YYYY-MM_Month.md`)
   - Month strategy and direction
   - Monthly goals and milestones
   - Known month-level risks, constraints, scope changes
   - Phase assessment (early/mid/late)

2. **Previous Week Closeout** (output from WEEK_CLOSEOUT.md: previous W##-1)
   - Carry-over tasks (meaningful, executable)
   - Blocked or dependent items
   - Dropped or deferred items with rationale
   - System learnings and signal patterns from the previous week
   - Any escalations or decision points

3. **Previous Weekly Execution** (`W##-1_Execution.md`)
   - Actual execution pattern (how the previous week unfolded)
   - Anchor adherence data
   - Blocks and spillovers (for pattern analysis)
   - Drift and rebalance history (if rebalancing occurred)

4. **Project Context Files**
   - `ROBOTOS_CONTEXT.md` — current RobotOS project state, blockers, deliverables
   - `Signee_CONTEXT.md` — current Signee project state, blockers, deliverables
   - `Zephyr_Project_Context.md` — current Zephyr project state, blockers, deliverables
   - Any other active project context

5. **Anchor Tracking File** (maintained by daily operations)
   - Anchor adherence pattern (past 3–4 weeks)
   - Which anchor structures have been most reliable
   - Which re-entry patterns work best
   - Patterns in energy, timing, and block effectiveness

6. **Carry-over Task List** (extracted by WEEK_CLOSEOUT)
   - List of meaningful work items to carry forward
   - Executable next steps (exact entry points, not vague)
   - Blocked items (with named blockers and dependencies)
   - Priority relative to new weekly goals

---

## Outputs

### Primary Output

**File:** `OS/03_EXECUTION/WEEK/W##_WeekPlan.md`

A structured weekly plan document containing:

1. **Weekly Goals** (3–5 concrete deliverables or outcomes)
   - What must be delivered by week-end
   - How goals align with month strategy
   - Priority order (if multiple)

2. **Capacity and Constraints**
   - Maximum hours available (accounting for vacation, external commitments)
   - Constraint list (dependencies, blockers, third-party dependencies)
   - Scope freeze decision (is this week's scope fixed or flexible?)

3. **Mission Structure**
   - Primary mission (the main thread of work)
   - Secondary missions (supporting work)
   - Optional/stretch work (if capacity allows)
   - How missions relate to carry-over

4. **Anchor Hypothesis**
   - Proposed daily anchor structure (which anchors will frame each day)
   - Re-entry pattern (how to recover if a day is interrupted)
   - Block pattern (which blocks to use, when)
   - Rationale (why this structure is chosen for this week)

5. **Carry-over Integration**
   - Which carry-over items are scheduled into weekly goals
   - Which are parked pending blockers
   - Which are explicitly dropped (with reason)
   - Estimated effort budget for carry-over

6. **Definition of Done (DoD)**
   - What completion means for this week
   - Artifact requirements (PRs merged, demos done, reports written, etc.)
   - Quality criteria (code reviewed, tested, documented)

7. **Weekly Focus Summary**
   - 1–2 paragraph text summarizing the week's theme, priorities, and key decisions

### Secondary Outputs

- **Planning notes** (decision log entry documenting why this plan was chosen)
- **Risk register** (known blockers, third-party dependencies, decision points)
- **Rebalance trigger conditions** (if the week drifts to > X% off plan, trigger WEEKLY_REBALANCE)

---

## Source-of-Truth Hierarchy

The following hierarchy governs planning decisions when inputs conflict:

1. **Month Strategy** (top priority)
   - If a weekly plan does not align with month goals, resolve the conflict before proceeding
   - Month-level constraints always take precedence over weekly convenience

2. **Project States** (second priority)
   - Current project deliverables, blockers, and dependencies define what is possible this week
   - If a project has external dependencies or gate dates, those drive weekly scope

3. **Previous Week Closeout** (third priority)
   - Carry-over items and learnings from the previous week inform planning
   - Do not ignore carry-over; integrate it or explicitly reject it with documented reason

4. **Carry-over Work** (fourth priority)
   - Executable carry-over from previous week shapes weekly scope
   - Blocked carry-over may need to be parked or escalated

5. **Capacity Reality** (fifth priority)
   - Hours available, energy patterns, and anchor reliability determine what is achievable
   - Do not inflate scope beyond realistic capacity
   - Account for vacation, external meetings, known energy dips

6. **Anchor Pattern History** (sixth priority)
   - Past anchor structures and their adherence rates inform the weekly anchor hypothesis
   - Choose anchor patterns that have demonstrated reliability in recent weeks
   - Deviate only with explicit rationale (new project, seasonal change, etc.)

---

## Planning Logic

### Planning Principle

Weekly planning translates **strategic direction** (from month) and **execution reality** (from previous week) into a **coherent frame** that daily execution can inherit without repeated replanning.

A good plan is one that daily execution can follow without constant ad-hoc decisions. A bad plan is one that requires daily rewriting or that conflicts with operational reality.

### Wide-Band vs. Narrow-Band Planning

- **Wide-band:** 3–5 goals with flexible execution path (choose among methods)
- **Narrow-band:** 1–2 goals with specific execution path (only one way to deliver)

Wide-band planning is recommended for weeks with:
- Multiple projects running in parallel
- High uncertainty in blockers or dependencies
- Good anchor adherence history (can trust daily decisions)

Narrow-band planning is recommended for weeks with:
- Critical scope freeze (project gate dates)
- Complex blockers (hard dependencies on third parties)
- Poor anchor adherence history (need strict structure)

### Planning Flow (see §9 for detailed procedure)

1. **Read Month** — Understand strategic direction and constraints
2. **Read Previous Closure** — Identify carry-over and patterns
3. **Evaluate Projects** — Determine feasible scope for each project
4. **Reconcile Carry-over** — Decide what to integrate, park, or drop
5. **Determine Goals** — Synthesize month strategy + project state + carry-over into 3–5 weekly goals
6. **Assess Capacity** — Estimate effort for goals; check against available hours
7. **Design Anchor Structure** — Choose anchor hypothesis that fits goals and supports execution
8. **Define Constraints** — Document scope freeze, blockers, dependencies
9. **Write DoD** — Specify what completion means for each goal
10. **Write Plan** — Produce final WeekPlan file

---

## Anchor Hypothesis Generation

The weekly anchor hypothesis is the structural proposal for how daily execution will frame itself.

### Anchor Components

**Primary anchor** — The main work focus (usually one domain: RobotOS, Signee, Zephyr, or Synthesis)

**Secondary anchor** — Supporting work (second domain or cross-cutting work like reviews, documentation, testing)

**Optional anchor** — Stretch work (emergencies, exploratory work, or scope-dependent)

**Re-entry block** — How to recover if a day is interrupted (repeat the primary anchor, or shift to secondary)

**Deep block** — Uninterrupted focus time for complex work (when, how long, which domain)

### Anchor Hypothesis Rationale

The hypothesis must specify **why** this structure is chosen:

- "Primary anchor is RobotOS because the deadline is Friday"
- "Re-entry is secondary anchor because primary work is interruptible if needed"
- "Deep block is Wednesday-Friday because synthesis work requires unbroken focus"
- "Hypothesis shifts in Week 2 if RobotOS gate passes early"

### Anchor Pattern Adaptation

Review the previous 3–4 weeks of anchor adherence:
- If an anchor structure has >80% adherence, repeat it (it works)
- If an anchor structure has 50–80% adherence, modify edges (core is sound, details need adjustment)
- If an anchor structure has <50% adherence, redesign (it is not compatible with actual execution)

---

## Carry-over Integration

### Carry-over Scope Assessment

For each carry-over item from the previous week:

1. **Classify:** Is it meaningful (needed by month goals or projects)? Or is it nice-to-have?
2. **Estimate:** How much effort does it require?
3. **Schedule:** Can it fit into the weekly plan without displacing new goals?
4. **Blocker Check:** Is it blocked by external dependencies? If so, park it with escalation.

### Carry-over Integration Decision

- **Integrate:** Add carry-over to weekly goals if it aligns with month strategy and fits capacity
- **Park:** Document carry-over as "available if capacity allows" (secondary mission)
- **Escalate:** If carry-over is blocked or critical, mark it as escalation requiring decision
- **Drop:** If carry-over is no longer needed (project shipped, priorities changed), drop it and document why

### Carry-over Effort Budget

Allocate 10–20% of weekly capacity to absorb carry-over work. This allows:
- Ad-hoc bugs or urgent requests
- Blocked items that unblock mid-week
- Context-switching costs

Do not inflate carry-over into the primary capacity plan. Treat it as a cushion, not a guarantee.

---

## Constraints and Capacity Rules

### Hard Constraints

**Hard constraints must be honored; violating them breaks the plan:**

1. **Project Deadlines** — If RobotOS demo is Friday, all prep work must fit before Friday
2. **External Dependencies** — If Signee requires equipment from vendor, plan cannot proceed until equipment arrives
3. **Scope Freeze** — If month decision is "freeze scope at 3 goals," do not add a 4th without month-level decision
4. **Capacity Limits** — If total available hours are 40, do not plan 50 hours of work

### Soft Constraints

**Soft constraints are preferences; violate only with explicit rationale:**

1. **Anchor Pattern** — Prefer anchor structures with >80% historical adherence
2. **Energy Curves** — Account for afternoon dips or weekend energy changes
3. **Context-switching Costs** — Minimize rapid domain switching if possible
4. **Learning Transfer** — Sequence work to allow concepts learned early-week to apply later-week

### Capacity Calculation

**Available hours = (total work hours per week) - (vacation, meetings, external time) - (maintenance/admin)**

Example:
- Work week: 40 hours gross
- Vacation/meetings: 5 hours
- Admin, comms, email: 4 hours
- **Available for planned work: 31 hours**

Allocate planned work as:
- Primary goals: 60–70% (18–22 hours)
- Secondary missions: 15–20% (5–6 hours)
- Carry-over buffer: 10–15% (3–5 hours)
- Unplanned contingency: 5–10% (2–3 hours)

---

## Carry-over Handling

### Meaningful Carry-over

Carry-over is meaningful if it meets at least one of:
1. Blocks a project milestone or month goal
2. Unblocks other work downstream
3. Carries an established commitment from a previous week
4. Is explicitly called out in the month plan

Carry-over is NOT meaningful if:
1. It was a "nice-to-have" and is no longer relevant
2. A project decision has superseded it
3. It has been pending > 2 weeks with no progress (escalation needed instead)
4. It is vague ("finish RobotOS") instead of specific

### Carry-over Scheduling Rules

1. **Integrate before adding new work** — If a goal requires carry-over to complete, schedule the carry-over first
2. **Separate blocked from executable** — Do not mix work that can start with work that cannot
3. **Estimate conservatively** — If carry-over "probably takes 3 hours," plan for 4 hours (include context-switching)
4. **Set unblock triggers** — If carry-over is blocked, state explicitly what unblocks it and when to check

### Carry-over Deprecation

Carry-over older than 2 weeks without progress should trigger escalation:
- Is this truly high-priority? (if so, something is blocking it → escalate to unblock)
- Is this actually needed? (if not needed, drop it)
- Has the situation changed? (if so, replan the work)

Do not let stale carry-over accumulate in the plan. Either integrate it, escalate it, or drop it.

---

## Escalation Handling

### Escalation Triggers

Escalate to Month/Project context if any of the following cannot be resolved at the weekly level:

1. **Resource Deadlock** — A goal requires external resource that is unavailable
   - Escalation: Document the dependency; request allocation at month level
   
2. **Priority Conflict** — Two projects have conflicting requirements for the same week
   - Escalation: Raise to month strategy; request prioritization decision
   
3. **Scope Inflation** — Required work exceeds available capacity by >20%
   - Escalation: Raise to month; request scope reduction or week length extension
   
4. **Blocker Aging** — A carry-over item has been blocked > 2 weeks
   - Escalation: Raise to project; request unblock action
   
5. **Risk Materialization** — A known risk has happened; plan no longer feasible
   - Escalation: Raise to month/project; request replanning decision

### Escalation Documentation

When escalating, document:
- **What** — The specific constraint or conflict
- **Why** — Why it cannot be resolved at weekly level
- **Impact** — What happens if unresolved (goals slip, deliverables miss, etc.)
- **Options** — 2–3 possible resolutions (scope changes, date changes, resource changes)
- **Requested Decision** — What decision is needed to proceed

---

## Consistency Checks

Before finalizing the WeekPlan, verify all of the following:

### Goal Alignment
- [ ] Weekly goals explicitly reference how they serve month strategy
- [ ] Each goal has a clear definition of completion (not vague)
- [ ] Goals do not conflict with each other (no mutual blockers)
- [ ] Goals sum to achievable scope (capacity-rated, not inflated)

### Project Alignment
- [ ] Current project blockers are documented and have workarounds or escalations
- [ ] No project has missing dependencies without escalation
- [ ] Project deadlines (if any) are met by planned completion dates

### Carry-over Alignment
- [ ] All carry-over is either integrated, parked, or escalated (no orphaned items)
- [ ] Integrated carry-over has scheduled time (not hoped for)
- [ ] Blocked carry-over has explicit unblock trigger

### Anchor Alignment
- [ ] Proposed anchor structure has demonstrated >60% adherence in recent history
- [ ] Anchor structure supports the goal delivery sequence
- [ ] Re-entry pattern is clearly defined and tested in recent weeks
- [ ] Deep blocks (if any) are scheduled and protected

### Capacity Alignment
- [ ] Total planned work ≤ 70% of available hours (leaves 30% buffer)
- [ ] Carry-over effort is estimated conservatively (+15% for context-switching)
- [ ] Vacation, meetings, and external time are accounted for
- [ ] No single anchor is overloaded (>60% of its available time)

### Constraint Honoring
- [ ] Hard constraints are explicitly listed and cannot be violated
- [ ] Soft constraint deviations are documented with rationale
- [ ] Scope freeze (if any) is honored

### Escalation
- [ ] All unresolved blockers are escalated (not silently omitted)
- [ ] Escalation pathways are documented (who to ask, what decision is needed)

---

## Definition of Good WeekPlan

A **good WeekPlan** demonstrates all of the following:

1. **Coherent Direction** — The plan expresses a single strategic thread. Reading it does not leave confusion about priorities.

2. **Month Alignment** — Goals clearly serve month strategy; if a week is a re-plan, the rationale is documented.

3. **Honest Scope** — Work scope is achievable without heroic effort. If the plan requires exceeding available capacity, escalation is documented (not hidden).

4. **Clear Carry-over** — Carry-over items are integrated, parked, or escalated with explicit decisions (not left ambiguous).

5. **Realistic Anchor** — The proposed anchor structure has demonstrated reliability. If it is new, the rationale is explained and risk is acknowledged.

6. **Defined Completion** — Definition of Done is specific enough that daily execution can validate completion without re-reading the month file.

7. **Unambiguous Constraints** — Scope freeze, hard blockers, and external dependencies are listed. An outsider reading the plan could execute it.

8. **Execution Inheritance** — Daily planning can inherit anchor structure, mission framing, and DoD without needing to rewrite them daily.

9. **Risk Visibility** — Known risks, blockers, and decision points are documented. They are not surprises on Thursday.

10. **Traceable History** — The plan can explain why it was chosen (what month context, what carry-over, what project state led to this plan). Traceability supports later learning.

---

## Planning Procedure (10 Steps)

### Step 1 — Read Month Context

**Purpose:** Understand strategic direction and constraints that this week must serve.

**Actions:**
- Open the current month file (YYYY-MM_Month.md)
- Read the month strategy (§2: what this month is accomplishing)
- Identify month milestones or gate dates affecting this week
- Note any scope changes, rebalancing, or strategic shifts documented mid-month
- Extract: month direction (1–2 sentences), key milestones, constraints

**Output:** Month summary (3–5 bullet points of strategic constraints for the week)

---

### Step 2 — Read Previous Week Closeout

**Purpose:** Understand what carried forward and what lessons apply to this week.

**Actions:**
- Open the previous week's WEEK_CLOSEOUT output (W##-1_Closeout or completion notes within W##-1_Execution)
- Read the carry-over section (what tasks are meaningful and ready to continue)
- Read the learnings section (what worked, what needs adjustment in anchor/pacing)
- Note any signals or patterns documented (e.g., "Thu dip recurring," "re-entry block effective")
- Identify any escalations or decision points requiring month/project attention

**Output:** Carry-over list (10–15 potential items), learnings summary (3–5 patterns)

---

### Step 3 — Evaluate Project States

**Purpose:** Determine what each active project can deliver this week and what blockers exist.

**Actions:**
- Open each active project context file (ROBOTOS_CONTEXT.md, Signee_CONTEXT.md, Zephyr_Project_Context.md)
- For each project, identify:
  - Current deliverable or milestone this week (if any)
  - Known blockers or dependencies
  - Current status (on track, at risk, blocked, etc.)
  - Required effort (estimate from project deliverables)
- Note any third-party dependencies (external APIs, vendor deliverables, etc.)
- Document decision points or escalations needed at project level

**Output:** Project summary (1 section per project: deliverable, blockers, effort estimate)

---

### Step 4 — Identify and Classify Carry-over

**Purpose:** Decide which carry-over items to integrate into the plan.

**Actions:**
- List all carry-over items from Step 2
- For each item, classify:
  - **Meaningful?** (aligned with month/projects or should be dropped)
  - **Blocked?** (what would unblock it)
  - **Effort estimate** (hours; be conservative)
  - **Integration decision** (integrate into primary goal, park as secondary, or escalate)
- Total estimated effort for integrated carry-over
- Document rationale for any carry-over dropped or escalated

**Output:** Classified carry-over list (meaningful + blocked; total effort; integration decisions)

---

### Step 5 — Determine Weekly Goals

**Purpose:** Synthesize month strategy, project states, and carry-over into 3–5 concrete weekly goals.

**Actions:**
- Synthesize month strategy + project deliverables + carry-over into a coherent goal set
- Goals should be 3–5 in number (more than 5 is scope inflation)
- Each goal should:
  - Serve a clear month/project purpose (not random)
  - Be achievable in the week without heroic effort
  - Have a clear definition of completion (artifact or deliverable)
- Sequence goals (if there is a dependency, order them)
- Assign each goal to a project or domain (ownership clarity)

**Output:** Goal list (3–5 goals, each with owner and completion criteria)

---

### Step 6 — Assess Capacity and Effort Balance

**Purpose:** Verify that planned work fits available capacity.

**Actions:**
- Calculate available hours:
  - Total work hours per week (e.g., 40)
  - Subtract vacation, external meetings, maintenance (e.g., 9 hours)
  - Remaining capacity (e.g., 31 hours)
- Estimate effort for each goal (use project context + historical data)
- Add carry-over effort estimate
- Total effort vs. available capacity:
  - If total ≤ 70% of capacity (21 hours), plan is sustainable
  - If total 70–85% (21–26 hours), plan is tight but achievable
  - If total > 85% (>26 hours), scope must be reduced or escalated
- If scope inflation exists, decide: reduce a goal, escalate for capacity request, or replan to be realistic

**Output:** Capacity summary (available hours, planned hours, % utilization, contingency buffer)

---

### Step 7 — Create Weekly Anchor Hypothesis

**Purpose:** Design the daily anchor structure that will support the week's execution.

**Actions:**
- Review anchor pattern history (from anchor tracking file): which structures had >80% adherence in past 4 weeks?
- Propose the weekly anchor structure that:
  - Supports goal delivery sequence (primary anchor matches primary goal)
  - Has demonstrated reliability (historical adherence >60%)
  - Fits capacity (anchors are not overloaded)
  - Includes re-entry pattern (if a day is interrupted, what happens?)
  - Includes deep blocks (focused time for complex work)
- Document the anchor hypothesis with rationale:
  - "Primary: RobotOS tests (35% of time) — deadline is Friday"
  - "Secondary: Signee context (20% of time) — slower than tests, supports setup"
  - "Re-entry: fall back to secondary if morning blocked"
  - "Deep block: Wed–Fri afternoons for synthesis (uninterrupted focus)"
  - "Rationale: Past 4 weeks show RobotOS-heavy weeks have >85% adherence; re-entry to secondary works when interruptions occur"

**Output:** Anchor hypothesis (structure + rationale); re-entry pattern; deep blocks scheduled

---

### Step 8 — Define Constraints and Scope Freeze

**Purpose:** Specify what is fixed and what is flexible in the week.

**Actions:**
- Document hard constraints:
  - "RobotOS tests must merge by Fri (project gate date)"
  - "Signee equipment arrives Wed, project blocks until then"
  - "Vacation: Fri morning (4 hours unavailable)"
- Document soft constraints (preferences, not absolutes):
  - "Prefer RobotOS primary anchor (good adherence history)"
  - "Avoid rapid context-switching if possible"
- Specify scope freeze:
  - Is the goal list fixed? (if so, state "Scope freeze: no new goals mid-week; requests escalate to month")
  - Are deliverables negotiable? (if so, state which are flex)
  - Can carry-over be added? (if so, up to what effort limit?)

**Output:** Constraint list (hard + soft); scope freeze decision; redline boundaries

---

### Step 9 — Define Weekly Definition of Done (DoD)

**Purpose:** Specify what completion means for each goal (avoiding ambiguity at week-end).

**Actions:**
- For each goal, define completion criteria:
  - **Goal 1 (RobotOS tests):** "All tests merged to develop branch; CI passing; demo ready"
  - **Goal 2 (Signee context):** "Context + monthly plan + env setup doc complete and reviewed; team notified"
  - **Goal 3 (Carry-over synthesis):** "Pptx draft complete; feedback incorporated; ready for design review"
- Define shared DoD for all work:
  - Code: reviewed and merged (if applicable)
  - Docs: written and linked
  - Tests: passing
  - Artifacts: accessible and titled (not orphaned)
- Define week-level DoD:
  - All carry-over is either completed or explicitly reparked with reason
  - All escalations are documented with decision or workaround
  - All blockers are visible (not silent failures)

**Output:** Detailed DoD (per-goal + week-level criteria; specific artifacts required)

---

### Step 10 — Write WeekPlan File

**Purpose:** Produce the final `W##_WeekPlan.md` file that will serve as the execution baseline.

**Actions:**
- Create new file: `OS/03_EXECUTION/WEEK/W##_WeekPlan.md` (where ## is the week number)
- Populate sections:
  1. **Header:** Week identifier (W##), dates (Mon–Fri), phase (1st week of month, final week, etc.)
  2. **Strategic Context:** 2–3 sentence summary of month strategy and why this week matters
  3. **Weekly Goals:** 3–5 goals with owner, effort estimate, completion criteria
  4. **Capacity Summary:** Available hours, planned hours, % utilization, buffer
  5. **Anchor Hypothesis:** Daily anchor structure with rationale, re-entry pattern, deep blocks
  6. **Carry-over Integration:** List of carry-over items (integrated/parked/escalated), total effort
  7. **Constraints:** Hard constraints, soft constraints, scope freeze decision
  8. **Definition of Done:** Per-goal DoD + week-level DoD
  9. **Known Risks:** Blockers, dependencies, decision points
  10. **Focus Summary:** 2–3 paragraph narrative of the week's theme and key decisions
- Link to:
  - Month file (YYYY-MM_Month.md)
  - Previous week closure (W##-1_Execution, carry-over)
  - Project context files (ROBOTOS_CONTEXT.md, etc.)
  - Anchor tracking file (for reference during week)

**Output:** Finalized `W##_WeekPlan.md` file, ready for GENERATE_WEEKLY_EXECUTION to consume

---

## Consistency Checks Detailed

Before finalizing the WeekPlan, validate the following checklist:

### Plan Completeness
- [ ] All 3–5 goals are named and have owners
- [ ] Each goal has a clear definition of completion (not vague)
- [ ] Carry-over items are classified (integrated/parked/escalated)
- [ ] Anchor structure is named and has historical rationale
- [ ] Constraints are documented
- [ ] DoD is specific (not generic)
- [ ] Risks and blockers are listed

### Goal Validation
- [ ] Goals sum to month strategy (not contradicting)
- [ ] Goals fit available capacity (with 20–30% buffer)
- [ ] Goals do not conflict with each other
- [ ] Each goal has an owner (clarity on who executes)

### Carry-over Validation
- [ ] Integrated carry-over has time allocated (visible in effort estimate)
- [ ] Parked carry-over is explicitly marked secondary/optional
- [ ] Escalated carry-over has decision documented (waiting on month/project)
- [ ] No carry-over is left ambiguous (integrate, park, escalate, or drop — choose one)

### Anchor Validation
- [ ] Proposed anchor structure has >60% historical adherence
- [ ] Primary anchor matches primary goal (coherence)
- [ ] Re-entry pattern is clearly defined
- [ ] Deep blocks (if any) are scheduled and protected

### Capacity Validation
- [ ] Available hours calculated correctly (work hours minus vacation/admin)
- [ ] Planned work ≤ 70% of available (leave 30% buffer)
- [ ] Carry-over effort includes context-switching buffer (+15%)
- [ ] No single anchor overloaded (>60% of its available time)

### Constraint Validation
- [ ] Hard constraints listed (project deadlines, external dependencies, scope freeze)
- [ ] Soft constraints listed (preferences, not absolutes)
- [ ] Scope freeze decision is clear (what is fixed, what is flex)
- [ ] All constraints can be honored by the plan (not just stated, but achievable)

### Month Alignment
- [ ] Plan references month strategy (not generic)
- [ ] Plan explains how goals serve month milestones
- [ ] Any month-level decisions (scope changes, risk materializations) are incorporated

---

## Definition of Good WeekPlan (Validation Checklist)

Before considering the WeekPlan final, verify:

### Strategic Coherence
- [ ] Reading the plan, it is clear what this week is working toward
- [ ] Goals do not feel random; each serves a documented purpose
- [ ] Plan explains *why* this structure was chosen (not just what)

### Execution Readiness
- [ ] A team member could read this and execute without asking questions (self-contained)
- [ ] DoD is specific enough that completion is measurable, not subjective
- [ ] Anchor structure is clear (daily execution can inherit it as-is)

### Reality-Based Planning
- [ ] Effort estimates are conservative (not optimistic)
- [ ] Capacity calculation is honest (not inflated available hours)
- [ ] Carry-over is either integrated with time allocated or explicitly parked
- [ ] Blockers are documented (not hoped-for-to-disappear)

### Constraint Honoring
- [ ] Hard constraints are explicitly listed and plan respects them
- [ ] Soft constraint deviations (if any) are documented with rationale
- [ ] Scope freeze (if any) is honored

### Risk Visibility
- [ ] Blockers and dependencies are visible (not on a hidden escalation list)
- [ ] Escalations (if any) are documented (who to ask, what decision is needed)
- [ ] Decision points are marked (not assumed to resolve automatically)

### Traceable Reasoning
- [ ] Plan explains carry-over decisions (why integrated/parked/escalated)
- [ ] Plan explains anchor choice (why this structure, why not another)
- [ ] Plan explains scope (why 3 goals, why not 4, capacity analysis visible)

---

## Standard Checklist

Use this checklist before finalizing a WeekPlan:

### Pre-Planning (preparation before Steps 1–10)
- [ ] Previous week is closed (WEEK_CLOSEOUT complete)
- [ ] Month file is current (updated within 48 hours if active)
- [ ] Project context files are current (updated within 1 week)
- [ ] Anchor tracking file is accessible
- [ ] Carry-over from previous week is extracted and available

### During Planning (Steps 1–10)
- [ ] Month context read and summarized (2–3 strategic constraints identified)
- [ ] Previous week closure read for carry-over and learnings
- [ ] Project states evaluated (deliverables, blockers, effort identified)
- [ ] Carry-over classified (meaningful/blocked; integration decisions made)
- [ ] Goals synthesized (3–5 from month + projects + carry-over)
- [ ] Capacity assessed (effort vs. available hours; buffer confirmed)
- [ ] Anchor structure proposed (with historical rationale)
- [ ] Constraints and scope freeze documented
- [ ] DoD defined (per-goal and week-level)
- [ ] WeekPlan file written and populated

### Validation (consistency checks before finalizing)
- [ ] Goal alignment ✅ (goals serve month, fit capacity, no conflicts)
- [ ] Project alignment ✅ (blockers documented, no missing dependencies)
- [ ] Carry-over alignment ✅ (all items classified, integrated items scheduled)
- [ ] Anchor alignment ✅ (historical adherence >60%, supports goals)
- [ ] Capacity alignment ✅ (work ≤ 70% of available, buffer exists)
- [ ] Constraint honoring ✅ (hard constraints listed and achievable)
- [ ] Month alignment ✅ (goals serve month strategy)

### Post-Planning (after WeekPlan is written)
- [ ] WeekPlan file created at `OS/03_EXECUTION/WEEK/W##_WeekPlan.md`
- [ ] File links to month, previous week closure, project context
- [ ] File is readable by team (plain markdown, no hidden context)
- [ ] Anchor tracking file is linked for reference during the week
- [ ] Plan is ready for GENERATE_WEEKLY_EXECUTION to consume
- [ ] Planning notes (rationale, decisions made) are documented in Decision Log if significant

### Ready for Next Phase
- [ ] WeekPlan is finalized and committed to version control
- [ ] Next step: Run GENERATE_WEEKLY_EXECUTION to create the operational baseline
- [ ] Team is notified of new weekly plan (if collaboration is needed)

---

## Reusable Command Template

Use this template to generate a new WeekPlan. Replace placeholders with actual paths/values:

```
# GENERATE_WEEKPLAN Command Template

## Input Variables

MONTH_FILE = "<path/to/YYYY-MM_Month.md>"
# Example: 2026-03_March.md
# The current month context file containing strategy and milestones

PREVIOUS_WEEK_CLOSURE = "<path/to/W##-1_Execution.md or W##-1_Closeout notes>"
# Example: 2026-W09_Execution.md
# The closure output from the previous week (carry-over and learnings)

PROJECT_CONTEXT_ROBOTOS = "<path/to/ROBOTOS_CONTEXT.md>"
# Example: 08_PROJECT_CONTEXT/ROBOTOS_CONTEXT.md
# Current RobotOS project state, blockers, deliverables

PROJECT_CONTEXT_SIGNEE = "<path/to/Signee_CONTEXT.md>"
# Example: 08_PROJECT_CONTEXT/Signee_CONTEXT.md
# Current Signee project state, blockers, deliverables

PROJECT_CONTEXT_ZEPHYR = "<path/to/Zephyr_Project_Context.md>"
# Example: 08_PROJECT_CONTEXT/Zephyr_Project_Context.md
# Current Zephyr project state, blockers, deliverables

ANCHOR_TRACKING_FILE = "<path/to/anchor_tracking.md or history>"
# Example: 02_GENERAL_CONTEXT/anchor_tracking.md
# Historical anchor adherence data for past 3–4 weeks

AVAILABLE_CAPACITY = <hours per week>
# Example: 31
# Total work hours available after vacation, meetings, admin

NEW_WEEK_NAME = "W##"
# Example: W11
# Week number (integer or pattern); used in filename

NEW_WEEK_DATES = "YYYY-MM-DD to YYYY-MM-DD"
# Example: 2026-03-16 to 2026-03-22
# Mon–Sun dates for the new week

## Execution Steps

1. Read MONTH_FILE (strategic direction and constraints)
2. Read PREVIOUS_WEEK_CLOSURE (carry-over and learnings)
3. Read PROJECT_CONTEXT_* files (deliverables and blockers)
4. Calculate new AVAILABLE_CAPACITY (given vacation/meetings for this week)
5. Execute Steps 1–10 of the planning procedure (§9)
6. Produce output: $NEW_WEEK_NAME_WeekPlan.md

## Output File

File: OS/03_EXECUTION/WEEK/$NEW_WEEK_NAME_WeekPlan.md

Structure:
- Week header (dates, phase, context)
- Strategic context (month alignment, purpose)
- Weekly goals (3–5 concrete deliverables)
- Capacity summary (hours, utilization, buffer)
- Anchor hypothesis (daily structure + rationale)
- Carry-over integration (integrated/parked/escalated)
- Constraints (hard/soft, scope freeze)
- Definition of Done (per-goal and week-level)
- Known risks (blockers, dependencies, escalations)
- Focus summary (2–3 paragraph narrative)
- Links (month, previous closure, project context, anchor tracking)

## Example Usage

```
# Planning W11

MONTH_FILE = "06_MONTHS/2026-03_March.md"
PREVIOUS_WEEK_CLOSURE = "03_PLANNING/03_WEEK/2026-W10_Execution.md"
PROJECT_CONTEXT_ROBOTOS = "08_PROJECT_CONTEXT/ROBOTOS_CONTEXT.md"
PROJECT_CONTEXT_SIGNEE = "08_PROJECT_CONTEXT/Signee_CONTEXT.md"
PROJECT_CONTEXT_ZEPHYR = "08_PROJECT_CONTEXT/Zephyr_Project_Context.md"
ANCHOR_TRACKING_FILE = "02_GENERAL_CONTEXT/ANCHOR_TRACKING.md"
AVAILABLE_CAPACITY = 32  # Full week (no vacation)
NEW_WEEK_NAME = "W11"
NEW_WEEK_DATES = "2026-03-16 to 2026-03-22"

# Execute planning procedure with inputs above
# → Produces output: 03_PLANNING/03_WEEK/2026-W11_WeekPlan.md
```

---

## Integration with Other Procedures

### GENERATE_WEEKPLAN in the Weekly Cycle

GENERATE_WEEKPLAN is the **first step** of the weekly cycle. It produces the strategic baseline that all downstream procedures inherit:

**Operational Sequence:**

1. **GENERATE_WEEKPLAN** (this procedure) → Creates W##_WeekPlan.md
   - Inputs: Month file, previous closure, project states, carry-over, capacity
   - Outputs: WeekPlan (goals, anchor, DoD, constraints)

2. **GENERATE_WEEKLY_EXECUTION** (operational execution) → Creates W##_Execution.md
   - Inputs: W##_WeekPlan.md (baseline), daily execution evidence
   - Outputs: Weekly Execution (completion status, patterns, learnings)

3. **Daily Loop** (INTEGRATE_DAILY + PREPARE_NEXT_DAILY) → Runs each day
   - Inputs: Daily plans inherit anchor from WeekPlan
   - Outputs: Daily evidence for weekly execution

4. **WEEKLY_REBALANCE** (mid-week correction, if needed) → Optional trigger
   - Inputs: W##_WeekPlan.md, weekly execution evidence
   - Decision: If drift > Level 2, replans the remainder of the week
   - Outputs: Updated WeekPlan with rebalance note (does not rewrite history)

5. **WEEK_CLOSEOUT** (week-end closure) → Closes the week
   - Inputs: W##_Execution.md (completed), daily evidence
   - Outputs: Carry-over extraction, learnings summary, readiness for next plan

**Cross-References:**

- GENERATE_WEEKPLAN ↔ GENERATE_WEEKLY_EXECUTION: Plan is the baseline; Execution tracks how reality diverges
- GENERATE_WEEKPLAN ↔ WEEKLY_REBALANCE: Plan may be replanned mid-week if distortion exceeds threshold
- GENERATE_WEEKPLAN ↔ WEEK_CLOSEOUT: Plan's DoD is used to validate completion at week-end
- GENERATE_WEEKPLAN ↔ INTEGRATE_DAILY: Daily anchor structure is inherited from weekly plan
- GENERATE_WEEKPLAN → PREPARE_NEXT_DAILY: WeekPlan guides daily setup (anchor frame, goal focus)

### Relationship to GENERATE_WEEKLY_EXECUTION (Mode A)

**GENERATE_WEEKPLAN** produces the plan (strategic intent).

**GENERATE_WEEKLY_EXECUTION Mode A** consumes that plan and uses it as a template for weekly execution framing. Mode A is a lightweight operation that says:

- "This is our plan; let's execute it"
- Uses WeekPlan's goals, anchor, DoD as baseline
- Updates it as the week reveals reality

**GENERATE_WEEKLY_EXECUTION Mode B** is forensic reconstruction (used if the week ended and we're documenting what actually happened; less relevant to planning).

---

## Troubleshooting

### Problem: "I don't know what the month strategy is (Month file vague or out of date)"

**Diagnosis:** Month context is missing or unclear during GENERATE_WEEKPLAN.

**Resolution:**
1. Stop planning. Do not generate a WeekPlan without month context.
2. Return to month file and clarify (or ask for clarification):
   - What is the month trying to accomplish? (in 1–2 sentences)
   - Are there project milestones or gate dates this month? (explicit dates)
   - Are there scope changes since month start?
3. Update the month file if it is out of date.
4. Resume GENERATE_WEEKPLAN with cleared month context.

---

### Problem: "I have 10+ carry-over items from last week"

**Diagnosis:** Carry-over is accumulating (previous week had incomplete work, or carry-over was not filtered).

**Resolution:**
1. This is a signal that something is wrong. Stop and investigate:
   - Is carry-over meaningful, or is it stale work?
   - Did the previous week attempt too much scope?
   - Are blockers preventing carry-over completion?
2. Classify each carry-over item:
   - **Drop:** "No longer needed" (project changed, priority shifted) — OK to drop
   - **Escalate:** "Blocked 2+ weeks; needs external action" — escalate to unblock
   - **Integrate:** "Meaningful and achievable this week" — integrate
3. Integrate only 2–3 carry-over items into the new plan. The rest go to a "deferred" list.
4. If carry-over is accumulating across >2 weeks, escalate to month-level (is monthly workload realistic?).

---

### Problem: "Goals are vague ('finish RobotOS' or 'make progress')"

**Diagnosis:** Goals lack clarity on what completion looks like.

**Resolution:**
1. For each goal, ask: "How do I know this is done?"
   - If the answer is vague, re-specify the goal.
   - If the answer is clear, you have a good goal.
2. Rewrite goals using the pattern:
   - Bad: "Work on RobotOS"
   - Good: "Merge RobotOS test suite to develop branch; CI passing; demo ready for Friday gate"
3. Each goal should have a specific artifact or deliverable (not just effort).

---

### Problem: "Planned work exceeds available capacity (>85% utilization)"

**Diagnosis:** Scope inflation. Too many goals or inflated effort estimates.

**Resolution:**
1. Do not plan >70% of capacity (leave 30% buffer).
2. Choose: either reduce goals or extend capacity:
   - **Option A:** Drop a goal (which is most flexible or least important?)
   - **Option B:** Park a goal as secondary/optional (execute if capacity allows)
   - **Option C:** Request more capacity from month-level (vacation reduction, external time reduction)
   - **Option D:** Escalate overflow to next week (carry to W##+ 1)
3. Recalculate with reduced scope until work ≤ 70% of capacity.

---

### Problem: "Anchor structure I want doesn't match historical adherence"

**Diagnosis:** Proposing an anchor pattern with <60% historical adherence (risky).

**Resolution:**
1. Review anchor tracking file. Find anchors with >80% adherence in past 4 weeks.
2. If your desired anchor has <60% adherence, either:
   - **Option A:** Choose a more reliable anchor (modify the structure slightly)
   - **Option B:** Accept the risk (document explicitly: "Attempting new anchor pattern; high risk; will rebalance if <50% adherence observed mid-week")
   - **Option C:** Investigate why the anchor fails (is it a bad structure, or is it a capacity problem?); fix the root cause
3. Never propose an anchor without acknowledging its historical reliability (or lack thereof).

---

### Problem: "I don't have time to do full planning (Steps 1–10)"

**Diagnosis:** Planning is rushed or postponed.

**Resolution:**
1. Allocate 60–90 minutes for full GENERATE_WEEKPLAN (it is the foundation of the week).
2. If time is not available:
   - **Option A:** Schedule planning for a dedicated block (e.g., Sunday evening, 8–9:30 pm)
   - **Option B:** Use the reusable template (§11) as a shortcut (still requires inputs, but structure is provided)
   - **Option C:** Escalate: if no planning time exists, the month-level workload is overloaded (raise to month)
3. Never skip planning. A week without a plan drifts faster than a week with a rough plan.

---

### Problem: "Escalations to month/project-level don't get resolved"

**Diagnosis:** Escalation pathway is unclear or escalated items are not tracked.

**Resolution:**
1. When escalating, document explicitly:
   - What decision is needed (not vague)
   - Who should decide (month owner? project owner?)
   - When decision is needed by (day/time)
   - What happens if decision is not made (e.g., goal slips)
2. Track escalations in Decision Log (02_GENERAL_CONTEXT/Decision_Log.md).
3. Follow up before the escalation deadline (do not hope it is resolved; confirm).
4. If escalation is not resolved by the deadline, either:
   - Proceed with default assumption (documented in plan), or
   - Replan to work around the unresolved escalation

---

### Problem: "Plan is finalized, but something changes mid-week (unexpected blocker, new priority)"

**Diagnosis:** Mid-week change requires replan.

**Resolution:**
1. **If the change is minor** (one task slips, one carry-over unblocks):
   - Do NOT re-run GENERATE_WEEKPLAN.
   - Use INTEGRATE_DAILY to document the change in daily evidence.
   - Carry it forward to WEEK_CLOSEOUT.
2. **If the change is medium** (20–30% of scope affected):
   - Use WEEKLY_REBALANCE to adjust remaining week.
   - WEEKLY_REBALANCE does NOT rewrite history; it adjusts forward.
3. **If the change is major** (>30% of scope affected, month decision changed):
   - Consider re-running GENERATE_WEEKPLAN for the remainder of the week.
   - Document why replanning is necessary (rationale, trigger).
   - This is rare and should be escalated to month-level.

---

## Appendix A: Full Weekly Operational Sequence

**Complete 5-step cycle with cross-references:**

```
WEEK START
    ↓
1. GENERATE_WEEKPLAN (this procedure)
   Input: Month, previous closure, project states, carry-over, capacity
   Output: W##_WeekPlan.md (goals, anchor, DoD, constraints)
    ↓
2. GENERATE_WEEKLY_EXECUTION (Mode A: lightweight or Mode B: forensic)
   Input: W##_WeekPlan.md (baseline)
   Output: W##_Execution.md (operational state, updated as week progresses)
    ↓
3. Daily Loop (INTEGRATE_DAILY + PREPARE_NEXT_DAILY; repeat Mon–Fri)
   Input: Daily execution evidence
   Output: Updated W##_Execution.md with daily learnings, anchor adherence, blockers
    ↓
4. WEEKLY_REBALANCE (optional, triggered if drift > Level 2)
   Input: W##_WeekPlan.md, weekly execution evidence
   Decision: Does weekly scope need replanning?
   Output: Updated W##_WeekPlan.md (with rebalance note; does not rewrite history)
    ↓
5. WEEK_CLOSEOUT (end of week)
   Input: W##_Execution.md (completed), daily evidence, W##_WeekPlan.md (original)
   Output: Carry-over extraction, learnings, ready for next plan
    ↓
WEEK END → Next GENERATE_WEEKPLAN begins the next cycle
```

**Cross-Reference Map:**

- GENERATE_WEEKPLAN is read by:
  - GENERATE_WEEKLY_EXECUTION (uses plan as baseline)
  - INTEGRATE_DAILY (inherits anchor from plan)
  - PREPARE_NEXT_DAILY (inherits anchor from plan)
  - WEEKLY_REBALANCE (validates scope against plan)
  - WEEK_CLOSEOUT (validates completion against plan's DoD)

- GENERATE_WEEKPLAN reads from:
  - Month file (strategic direction)
  - Previous WEEK_CLOSEOUT output (carry-over, learnings)
  - Project context files (deliverables, blockers)
  - Anchor tracking file (historical adherence)

---

## Appendix B: Planning Decision Tree

Use this tree to navigate planning decisions:

```
START: Need to plan a new week

QUESTION 1: Is previous week closed?
  NO  → Close previous week first (run WEEK_CLOSEOUT)
  YES → Continue to QUESTION 2

QUESTION 2: Is month file current?
  NO  → Update month file with latest strategy/changes
  YES → Continue to QUESTION 3

QUESTION 3: Are project context files current?
  NO  → Update project files with latest blockers/deliverables
  YES → Continue to QUESTION 4

QUESTION 4: Carry-over from previous week — how much?
  >10 items → Carry-over is accumulating (signal of unfinished work)
              Classify: drop stale items, escalate blocked, integrate meaningful
  5–10 items → Normal; classify into integration tiers
  <5 items  → Low carry-over; integrate into plan

QUESTION 5: Month strategy — clear?
  Vague   → Clarify month first; do not proceed without clarity
  Clear   → Continue to QUESTION 6

QUESTION 6: Available capacity this week?
  <20 hours → Overloaded week; escalate for scope reduction
  20–30 hours → Normal; proceed with planning
  30+ hours  → High capacity; can be aggressive with scope

QUESTION 7: How many goals for the week?
  <3      → Too few; integrate more carry-over or projects
  3–5     → Ideal range
  >5      → Too many; scope inflation; reduce via parking or escalation

QUESTION 8: Anchor structure — historical adherence?
  >80%    → Reliable; use it
  60–80%  → Acceptable; use it; monitor
  <60%    → Risky; modify structure or accept high-risk rebalance trigger

QUESTION 9: Carry-over effort + new goals — fit in capacity?
  Work > 85% of capacity → Reduce scope or escalate
  Work 70–85%           → Tight but achievable; ensure buffer
  Work < 70%            → Comfortable; plan is sustainable

QUESTION 10: All constraints and DoD documented?
  NO  → Document before finalizing
  YES → Finalize WeekPlan file

OUTPUT: W##_WeekPlan.md ready for GENERATE_WEEKLY_EXECUTION
```

---

## Appendix C: Historical Pattern Examples (Template for Recording Learnings)

**Use this section to document patterns observed in planning across multiple weeks. Update as new patterns emerge.**

### Example Pattern 1: Thursday Dip
- **Observation:** Weeks with Thu-heavy workload show >20% drift from plan
- **Cause:** Energy and focus drop on Thu afternoon
- **Mitigation:** Schedule lighter work or deep blocks earlier (Wed-Fri morning)
- **Weeks Observed:** W08, W09, W10
- **Anchor Adjustment:** If primary anchor requires Thu execution, pair with light re-entry day Friday

### Example Pattern 2: Re-entry Reliability
- **Observation:** Re-entry to secondary anchor after interruption has >85% success rate
- **Cause:** Secondary anchor work is interruptible by nature (code review, async work)
- **Confidence:** High (empirical data across 10+ interruptions)
- **Application:** Use secondary anchor as re-entry pattern; primary anchor only for protected blocks

### Example Pattern 3: Carry-over Integration Failure
- **Observation:** Carry-over >4 items has <50% completion rate by week-end
- **Cause:** Carry-over is sequential (each item blocks the next); new work disrupts sequence
- **Mitigation:** Limit integrated carry-over to 2–3 items; park rest as "if capacity allows"
- **Weeks Observed:** W06, W07, W09
- **Application:** Cap carry-over integration at 2–3 items; be conservative with estimates

### Example Pattern 4: Project Transition Costs
- **Observation:** Switching projects mid-week costs ~1 hour context-switching overhead
- **Cause:** Anchor change requires re-studying project context, rebuilding mental model
- **Mitigation:** Sequence projects (RobotOS Mon–Wed, Signee Thu–Fri) rather than alternating
- **Weeks Observed:** W04, W05, W08
- **Application:** In anchor design, minimize project switching; batch by domain

---

## Version History

| Date | Version | Changes |
|---|---|---|
| 2026-03-15 | 1.0 | Initial canonical procedure: 10-step planning process, decision tree, troubleshooting, full integration with weekly operations stack |

