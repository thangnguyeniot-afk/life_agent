# AMBIGUITY GATE RULE — PHASE 2 P0.5

**Purpose:** Prevent vague/unclear tasks from entering the execution schedule. Clean input, not more process.

**Status:** System rule (effective immediately)  
**Scope:** All task intake (weekly planning, daily planning, ad-hoc scheduling)  
**Enforcement:** Behavioral (planning discipline), not tool-based

---

## CORE GATE: 3-QUESTION FILTER

Before ANY task enters the schedule, answer these three questions:

```
1. Can DONE be written clearly?
   → Artifact clearly named
   → Exit condition binary + verifiable
   → Next step explicit

2. Can the work be started immediately?
   → First action is ≤ 60 min AND concrete
   → OR blockers are identified + planned separately

3. If this task stalls, will I know why?
   → Exit condition is clear enough that failure = obvious
   → Clear vs unclear = verifiable
```

**Decision Rule:**
- **ALL THREE → YES:** Task may enter schedule ✅
- **ANY → NO:** Task may NOT enter schedule; convert to UNBLOCK TASK ❌

---

## UNBLOCK TASK DEFINITION

**What is an UNBLOCK TASK?**

A small, clarity-producing task whose only purpose is to remove ambiguity from another task.

**Characteristics:**
- Size: S or small-M only (≤ 90 min total)
- Output: Clarity, not implementation
- End state: Either clear DONE for next task, or explicit blocked status

**Examples:**

```markdown
VAGUE: "Improve database performance"
↓ CONVERT TO UNBLOCK TASK:
"Identify current bottleneck: profile queries on production dataset (30 min); 
document slow queries + suspect indices; write next-step options (improve, add index, redesign)"

VAGUE: "Research factory implementation patterns"
↓ CONVERT TO UNBLOCK TASK:
"Code review: find 2 existing factory patterns in codebase; document structure + trade-offs (45 min)"

VAGUE: "Handle test failures"
↓ CONVERT TO UNBLOCK TASK:
"Run test suite; capture failure output; categorize by type; list top 3 failures + root causes (20 min)"

VAGUE: "Continue working on adapter layer"
↓ CONVERT TO UNBLOCK TASK:
"Review Monday's closure notes; inspect current code state; identify where work stopped; 
write 3-step continuation plan (15 min)"
```

---

## BANNED VAGUE LANGUAGE

The following task names/descriptions must NOT enter the schedule:

- ❌ "improve X"
- ❌ "continue working on X"
- ❌ "research more"
- ❌ "handle X"
- ❌ "fix things / fix X"
- ❌ "check X"
- ❌ "polish X"
- ❌ "work on X"
- ❌ "do testing"
- ❌ "make progress on X"

**Exception:** These words are OK if they are accompanied by:
- Explicit artifact name (e.g., "improve performance on queries to test_db; target: query time <100ms measured by profiler")
- Explicit DONE state (e.g., "3 edge cases handled; all tests passing; zero regressions")
- Explicit next visible action (e.g., "first step: profile current query performance; identify bottleneck")

**Enforcement:** If task name contains banned language AND lacks explicit artifact/DONE/first step, it may NOT be scheduled. Convert to UNBLOCK TASK first.

---

## HIGH-AMBIGUITY RULE

**Definition:** A task is HIGH-AMBIGUITY if:
- Multiple unknowns exist (5+ open questions)
- Entry point is unclear
- Success criteria is subjective ("good enough" / "looks okay")
- Scope is elastic (could expand indefinitely)

**Gate:**
If a task is HIGH-AMBIGUITY:
- It must START with an UNBLOCK TASK (discover unknowns first)
- OR have an explicit first step that fits in ≤ 60 min

**Example:**

```
HIGH-AMBIGUITY TASK: "Factory feature implementation"
- Questions: What is factory? Where does it integrate? What's the API? 
  What are edge cases? How do we test it?
- Unknowns: 5+ open questions
- Entry point: Unclear
- Decision: CANNOT enter execution schedule yet

FIX → Schedule UNBLOCK TASK first:
"Factory Feature Research Sprint (60 min)
- What is factory pattern in this codebase?
- Where do factories integrate?
- What API is expected?
- Write entry-point candidates (2–3 options)
- Exit: Research note with scope + unknowns clarified"

THEN → After research complete, schedule implementation task
```

---

## MINIMAL TAGGING (NO NUMERIC SCORING)

Optional lightweight label for planning visibility:

```
Task Name | Status
-----------|--------
Task A | 🟢 Clear (ready to execute immediately)
Task B | 🟡 Needs Clarification (may enter schedule if unblock task done first)
Task C | 🔴 Blocked (cannot schedule; explicit blocker noted)
```

**That is the entire tagging system for PHASE 2. No numeric ambiguity score yet.**

---

## ENFORCEMENT POINTS

**Weekly Planning (WeekPlan creation):**
- [ ] Ambiguity gate applied to all anchors before acceptance
- [ ] High-ambiguity anchors have dependency unblock tasks scheduled
- [ ] No vague language in anchor names

**Daily Planning (Daily file creation):**
- [ ] Ambiguity gate applied to all blocks
- [ ] All blocks have explicit DONE criteria
- [ ] All blocks have explicit first step (≤ 60 min or clear continuation)

**Ad-hoc Scheduling (during week if new task arises):**
- [ ] Ambiguity gate applied before adding to daily plan
- [ ] If unclear: create UNBLOCK TASK instead
- [ ] Escalate if blocker identified

---

## VALIDATION CHECKLIST

After PHASE 2 implementation, audit one week of planning:

- [ ] Sample 5 planned tasks/anchors
- [ ] For each one, verify:
  - [ ] DONE criterion is explicit (not "good progress")
  - [ ] Artifact is nameable (not vague)
  - [ ] First action is concrete (≤ 60 min or clear blocker identified)
  - [ ] No banned vague language present
- [ ] Identify any vague tasks that slipped through
- [ ] Convert slipped tasks to UNBLOCK TASKS

**If ANY vague task passes gate → FAIL → revisit enforcement**

---

## PHASE 2 SUCCESS CRITERIA

✅ **PHASE 2 is successful when:**

1. Vague tasks stop entering the execution schedule
2. High-ambiguity work is pre-filtered to UNBLOCK TASKS
3. Planning becomes smaller but clearer
4. Fewer tasks stall during execution with "I don't know what to do next"
5. Re-entry notes are cleaner (know exactly where to start)

---

## RELATIONSHIP TO OTHER PHASES

| Phase | Rule | Relation to P0.5 |
|---|---|---|
| **P0.1 (DONE)** | Every task has artifact + exit + next step | P0.5 ensures DONE can be written before task enters schedule |
| **P0.4 (Closure)** | No cognitive load carries over | P0.5 ensures tasks aren't left half-understood |
| **P0.5 (Ambiguity)** | No vague tasks enter schedule | ← This phase |
| **P0.2 (Capacity)** | Max 3M daily | P0.5 ensures quality input before capacity is checked |

---

**Rule Published:** April 5, 2026  
**Effective:** Immediately for all new planning  
**Enforcement:** Planning discipline + peer review  
**Complexity:** Minimal (3-question gate + UNBLOCK TASK concept)

