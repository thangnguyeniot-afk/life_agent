# Weekend Effort Decomposition Template

**Purpose:** Validate that declared weekend capacity (Saturday daytime / Sunday afternoon) is grounded in concrete, realistic M-level tasks. This template feeds directly into CAPACITY_ENGINE V13 (Weekend Effort Realism) validation.

**When to Use:** During GENERATE_WEEKPLAN Step 6 (Assess Capacity and Effort Balance), for any project with planned weekend allocation.

**Output:** Completed decomposition embedded in WeekPlan § Capacity & Constraints, read by CAPACITY_ENGINE for V13 validation.

---

## Instructions

### 1. Identify Weekend Allocation Scope
- Which projects have weekend execution planned? (list by name + type)
- Which weekend slots are being used? (Sat daytime, Sun afternoon, or both?)
- What hours are declared for each slot per project?

**Example:**
- RobotOS: Saturday daytime 2h, Sunday afternoon 0h (not needed this week)
- Signee: Saturday daytime 0h (office work), Sunday afternoon 1.5h (async coordination)

### 2. For Each Weekend Slot With Allocation, Decompose Tasks

Use the sub-template below. Repeat for each {PROJECT} × {SLOT} combination.

---

## Sub-Template: Single Slot Decomposition

```
## {PROJECT} — {SLOT}

**Declared Hours:** {X}h
**Actual Task Breakdown:** (list each M-level task with effort)

| Task | Effort | DONE Condition | Notes |
|------|--------|---|---|
| M-task 1: [task name] | {Y}h | [binary completion] | [constraints, dependencies] |
| M-task 2: [task name] | {Z}h | [binary completion] | [constraints, dependencies] |
| ... | | | |
| **Total** | **{Y+Z}h** | — | |

**Math Check:**
- Declared hours: {X}h
- Task total: {Y+Z}h
- Fit? ✅ {Y+Z} ≤ {X} (surplus = {X-(Y+Z)}h) OR ❌ {Y+Z} > {X} (OVERFLOW = {(Y+Z)-X}h)
- Assessment: [PASS / WARN / FAIL]

**Spillover Scenario (if +10% scope inflation):**
- Current total: {Y+Z}h × 1.1 = {(Y+Z)*1.1}h
- Buffer available in slot: {X-(Y+Z)}h
- Fits? ✅ (spillover absorbed) / ⚠️ (partial spillover) / ❌ (full overflow)
- Spillover destination if overflow: [name other slot or weekday evening block, with path]
- Rationale: [why this path is realistic]

**V13 Assessment:** PASS / WARN / FAIL
```

---

## Complete Example (RobotOS, Saturday Daytime)

```
## RobotOS — Saturday Daytime

**Declared Hours:** 2h
**Actual Task Breakdown:**

| Task | Effort | DONE Condition | Notes |
|------|--------|---|---|
| M5: Team onboarding + Q&A | 1.25h | Repo access verified; team members acknowledge architecture doc clarity | async questions may arrive Sun; Q&A async |
| M6: Architecture synthesis (quick pass) | 0.75h | Rough notes → architecture_framework.md outline; no deep review needed | builds on weekday work; captures context while fresh |
| **Total** | **2h** | — | |

**Math Check:**
- Declared: 2h
- Task total: 2h
- Fit? ✅ 2h ≤ 2h (surplus = 0h)
- Assessment: PASS

**Spillover Scenario (if +10% scope inflation):**
- Current total: 2h × 1.1 = 2.2h
- Buffer available in slot: 0h
- Fits? ❌ (full overflow = 0.2h)
- Spillover destination if overflow: Sunday afternoon M6 synthesis continuation (0.25h allocated there already; could absorb 0.2h)
- Rationale: M6 synthesis is interruptible; if overflow occurs, defer fine detail to Sun afternoon; coarse framework captured on Sat

**V13 Assessment:** PASS (with Sun afternoon spillover buffer documented)
```

---

## Complete Example (Signee, Sunday Afternoon)

```
## Signee — Sunday Afternoon

**Declared Hours:** 1.5h
**Actual Task Breakdown:**

| Task | Effort | DONE Condition | Notes |
|------|--------|---|---|
| M7: Async coordination review + response | 0.75h | Slack threads reviewed; responses sent; team context captured in decision log | builds on weekday evening context |
| M8: Monthly context update + next-week prep | 0.75h | Monthly plan updated with team feedback; next week entry points identified | only if weekday entries are complete |
| **Total** | **1.5h** | — | |

**Math Check:**
- Declared: 1.5h
- Task total: 1.5h
- Fit? ✅ 1.5h ≤ 1.5h (surplus = 0h)
- Assessment: PASS

**Spillover Scenario (if +10% scope inflation):**
- Current total: 1.5h × 1.1 = 1.65h
- Buffer available in slot: 0h
- Fits? ❌ (full overflow = 0.15h)
- Spillover destination if overflow: Monday evening (already has 2h Signee evening block; context review can begin then)
- Rationale: Async coordination is flexible; if overflow, defer detailed response to Mon evening; quick skim still happens Sun

**V13 Assessment:** PASS (with Mon evening flex documented)
```

---

## Anti-Patterns to Avoid

### ❌ Vague Task Description
- BAD: "RobotOS work" (1h)
- GOOD: "M5: Architecture diagram refinement — update component dependencies, PR review" (1h)

### ❌ No DONE Condition
- BAD: "Work on documentation"
- GOOD: "Architecture doc outline merged to docs/ branch; CI passing"

### ❌ Cosmetic Allocation (Capacity Math Without Scope)
- BAD: Declare 2h on Saturday → Task list adds to 1.2h → "remainder is buffer" (no real work planned)
- GOOD: Declare 2h on Saturday → Task list adds to 2h exactly → Real scope tied to hours; buffer only if explicitly needed for contingency

### ❌ Impossible Scope
- BAD: 1.5h slot → 3 separate tasks (M-level synthesis, testing, review) → Obviously doesn't fit
- GOOD: 1.5h slot → 1–2 tasks maximum (M-level scope decomposition, each with realistic effort)

### ❌ Invisible Spillover
- BAD: Tasks list 2.5h but declared slot is 2h; no spillover path documented
- GOOD: Tasks list 2h; declared slot is 2h; if +10% overflow, documented path exists (Sun afternoon or named weekday evening)

### ❌ Forgetting the +10% Stress Test
- BAD: Decomposition detailed but no "what if work takes 10% longer" scenario
- GOOD: Each decomposition includes spillover scenario and realistic destination if slot overflows

---

## Integration Into WeekPlan

Once completed, embed this decomposition in the WeekPlan file under:

**§ Capacity & Constraints**

Create a sub-section: **Weekend Effort Decomposition (V13 Validation)**

Include:
1. **Summary table:** List all weekday slots with declared project hours (one row per project × slot combo)
2. **Detailed breakdown:** (For each entry in the table) Paste the completed sub-template above
3. **V13 Result:** PASS / WARN / FAIL (aggregate across all slots)

**Example summary table (goes first in decomposition section):**

| Weekend Slot | Project | Declared Hours | Task Count | Math Check | Spillover Path | V13 Status |
|---|---|---|---|---|---|---|
| Sat daytime | RobotOS | 2h | 2 tasks | ✅ 2h total | Sun afternoon (0.2h buffer) | PASS |
| Sun afternoon | Signee | 1.5h | 2 tasks | ✅ 1.5h total | Mon evening (flex) | PASS |
| Sat daytime | Zephyr | — | — | N/A (office project) | N/A | N/A |
| Sun afternoon | Zephyr | — | — | N/A (office project) | N/A | N/A |

---

## Validation Gate

**Before finalizing WeekPlan, confirm:**

- [ ] All weekend slots are accounted for (5 slots documented per R11)
- [ ] Every slot WITH allocation has a completed decomposition sub-template
- [ ] Every task in every decomposition has:
  - [ ] Concrete M-level name (not generic)
  - [ ] Realistic effort estimate (hours)
  - [ ] Binary DONE condition
  - [ ] Spillover scenario (+10% stress test)
- [ ] Math checks all PASS or have documented WARN (no unexplained FAIL)
- [ ] All spillover destinations are named and realistic
- [ ] Aggregate V13 assessment (PASS / WARN / FAIL) is recorded
- [ ] Decomposition is embedded in the WeekPlan file (not separate document)

---

## Common Mistakes & Remedies

| Mistake | Red Flag | Remedy |
|---|---|---|
| Tasks are too vague | "Work on X" appears in ANY task name | Rewrite to include specific component/artifact: "M5: [filename/component] + [what changes]" |
| Declared hours don't equal task sum | Math check shows ≠ | Either reduce tasks to fit slot, or increase declared hours (with capacity model validation), or move tasks to different slot |
| No spillover scenario | Decomposition has no "+10%" section | Add scenario; name concrete destination (other slot or named evening block); show math proving it fits OR document escalation if it doesn't |
| Spillover destination is vague | "Use remaining time" or "defer if needed" | Name the ACTUAL alternative: "Sun afternoon 0.5h buffer", "Mon evening 1h Signee block", or "escalate to month" |
| Mixing office & personal projects | Sat job used for Zephyr (TYPE A) | Zephyr is office-locked; cannot use personal weekend slots. Verify Pool A (office hours) capacity is satisfied Mon–Fri; personal weekend slots are Pool B only |
| Weekend is cosmetic | Tasks total 1.5h but slot is 2h; no real work defined for the 0.5h | Explicitly name the 0.5h purpose: "0.5h buffer for knowledge capture" or reduce declared slot to 1.5h |

---

## FAQ

**Q: What's the difference between "declared hours" and "task total"?**
A: Declared hours = how many hours the weekly plan commits to working on this project+slot. Task total = how long listed M-tasks actually take. They should match (or be very close). If task total < declared: either add tasks or reduce declared hours. If task total > declared: add hours or defer tasks.

**Q: Do all weekend projects need decomposition?**
A: Only those with declared weekend allocation. If RobotOS has 0h on Saturday and 0h on Sunday, no decomposition needed for RobotOS. But the fact that Saturday has 0h must be stated (per R11 slot-level declaration).

**Q: Can I use this template mid-week?**
A: Yes. If a STRONG context signal arrives mid-week and triggers WEEKLY_REBALANCE (Adaptive Mode), re-run the decomposition for affected weekend slots to validate new allocation still passes V13. Check Invariant 6 (replan budget + cooldown) before re-running.

**Q: What does "M-level" mean?**
A: M = Medium block (~1–2h work unit). Tasks should be single-session doable, not multi-day. Avoid task lists (sub-tasks of a sub-task); stay at the synthesis/review/coordination level. See CAPACITY_ENGINE for examples.

**Q: If spillover exceeds the named destination, what happens?**
A: If spillover scenario shows "+10% overflow cannot fit anywhere → escalate to month context." Document this in WeekPlan and don't overcommit the slot initially. Start with conservative task allocation; treat buffer as actual margin, not hidden work.

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-03-29 | Initial template; tied to CAPACITY_ENGINE V13 validation framework |
