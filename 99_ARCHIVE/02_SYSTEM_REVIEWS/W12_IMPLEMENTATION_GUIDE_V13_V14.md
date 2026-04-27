# W12 Hardening: Implementation Guide for V13 + V14

**Purpose:** Step-by-step instructions for integrating new weekend overflow validation checks into CAPACITY_ENGINE and GENERATE_WEEKPLAN

---

## File 1: CAPACITY_ENGINE.md

### Change 1: Add V13 + V14 to Validation Checks Table (§6)

**Location:** Section 6, after V12 row in validation checks table

**Current Content (V12 row):**
```
| Weekend usage decision | V12 | All five weekend slots explicitly declared per R11... | [failure condition] |
```

**Add TWO new rows after V12:**

```
| Weekend effort realism | V13 | Weekend-allocated work has M-level task breakdown; each task fits in declared slot capacity; spillover path exists (other weekend slot or deferral) | Weekend scope cannot be decomposed into realistic focus-blocks; OR declared slot hours insufficient for identified scope +10% spillover scenario; OR spillover has no named path (implicit overflow) |
| Personal capacity ceiling | V14 | Total personal execution (net weekday evening + weekend day hours) ≤ 18h/week (sustainable); if >18h, assumption documented; trend analysis shows personal load not increasing >2h × 3 consecutive weeks | Personal execution >20h/week (unsustainable); OR personal load trending upward >2h/week for 3+ weeks without escalation |
```

### Change 2: Add V13 Validation Logic (new section after V12 description)

**Location:** Section 6, after the V12 validation description prose

**Add:**

```markdown
### V13 — Weekend Effort Realism Check

**Purpose:** Ensure declared weekend hours can realistically accommodate project scope without silent spillover or artificial compression.

**Validation Steps:**

1. **Task Decomposition**
   - For each project allocated to weekend (TYPE B or TYPE C):
     - List all M-sized missions or execution phases assigned to Sat daytime and Sun afternoon
     - For each mission, state effort (hours) and focus type (architectural, implementation, specification, etc.)
   - Check: Does sum of listed tasks ≈ declared slot hours? (within ±1h margin)
   - Failure: Scope cannot be accounted for in declared slots ("8h declared but only 5h of identified work")

2. **Slot Fit Analysis**
   - Saturday daytime (5–6h available):
     - Can hold ≤1 deep M-block (3–4h execution + setup/breaks) with margin
     - Can hold 2 small independent tasks (1.5–2h each)
     - Overfull if: single 4h+ mission + another 3h+ mission = back-to-back execution (unrealistic)
   - Sunday afternoon (3–4h available, after morning review):
     - Can hold ≤1 M-block (2–3h execution given post-weekend fatigue)
     - Large second tasks should use Sat daytime, not Sun
   - Failure: Declared Sat 8h with scope list showing 2×4h tasks (impossible to execute start-to-finish Sat without spillover)

3. **Spillover Scenario (Assume +10–15% Overrun)**
   - If project work exceeds declared slot by 10% (realistic overrun margin):
     - ✓ Path exists: spillover fits in other weekend slot (Sat→Sun or vice versa)
     - ✓ Path exists: spillover fits in declared weekday evening block with identified capacity
     - ✓ Path exists: spillover deferred to next week with explicit decision + impact noted
     - ✗ Failure: "Spillover will just happen" (implicit absorption, no named path)

**When Applied:**
- After V12 (slot declaration) validates slots are named
- After V6 (goal-allocation match) validates effort estimates
- Before accepting weekend mode and slot allocation

**Output:**
- PASS: Weekend hours fully decomposed; spillover path exists or not needed (safe margin exists)
- WARN: Declared hours moderately exceed identified scope (+20–30%); proceed if cleanup/buffer explicitly named
- FAIL: Scope cannot be decomposed into realistic blocks; OR spillover has no path; scope reduction required

**Example PASS:**
```
Sat daytime 5h: RobotOS tests
  - M1: Write test scaffold (1h)
  - M2: Implement 3 memory-mgmt tests (3h)
  - M3: Code review + merge setup (45 min)
  Total: 4h 45 min ✓ (fits within 5h margin)
  Spillover (+10%): 5h 15 min → fits within Sat if setup compresses; no Sun spillover needed

Sun afternoon 2h: Signee spec review
  - M1: Review testing spec draft (1h)
  - M2: Feedback consolidation (45 min)
  Total: 1h 45 min ✓ (fits within 2h margin)
  Spillover (+10%): 1h 55 min → fits without spillover
```

**Example FAIL:**
```
Sat daytime 6h: RobotOS architecture + testing
  - M1: Architecture review + refactor (4h)
  - M2: Write tests (4h)
  Total: 8h ✗ (exceeds Sat capacity; cannot execute back-to-back)
  Spillover scenario: requires Sun afternoon 2h minimum
  → Remediation: Decompose into Sat 4h (architecture only) + Sun 3h (testing); OR defer testing to W13
```

---

### Change 3: Add V14 Validation Logic

**Location:** Section 6, after the V13 description prose

**Add:**

```markdown
### V14 — Personal Capacity Ceiling Check

**Purpose:** Ensure total personal execution (weekday evening + weekend daytime) remains within sustainable human capacity and does not exhibit unsustainable trending.

**Validation Steps:**

1. **Personal Capacity Calculation**
   - Start with gross weekday evening: 10h/week (2h × 5 evenings, 19:30–21:30 Mon–Fri)
   - Subtract structural deductions (from this week's anchor):
     - Thu = S-only energy dip (typically 0–1h available)
     - Fri = closure or S-only (typically 0–1h available)
     - Result: net weekday evening capacity (typically 5–8h/week realistically executable)
   - Add weekend daytime:
     - Sat daytime: declared hours (full execution capacity)
     - Sun morning: ~2–3h (review/overhead, NOT execution capacity; separate)
     - Sun afternoon: declared hours (if used; 0h if not planned)
   - Total personal execution: [net evening] + [Sat] + [Sun afternoon] = X h/week

2. **Sustainability Bands**
   - **11–18h/week:** PASS — normal sustainable range
   - **18–20h/week:** WARN — stretched week; requires explicit decision + assumption documentation; if pattern continues 3+ weeks, escalate
   - **>20h/week:** FAIL — unsustainable; scope reduction required OR explicit strategic decision to accept sprint (must escalate to month context)

3. **Trend Analysis (Multi-Week Pattern)**
   - Compare this week's personal execution (X h) to:
     - W-1 personal execution
     - W-2 personal execution
     - W-3 personal execution
   - Calculate trend:
     - Flat (Δ <1h): no trend concern ✓
     - Mild increase (Δ 1–2h/week): monitor ⚠️
     - Steep increase (Δ >2h/week × 3 consecutive weeks): escalate ❌
   - Example trend escalation:
     - W09: 12h personal
     - W10: 14h personal (Δ +2h)
     - W11: 16h personal (Δ +2h)
     - W12: 18h personal (Δ +2h)
     - Pattern detected: 3-week continuous increase → escalate to month; decide if sustainable or requires rebalancing

**When Applied:**
- After V13 (weekend effort realism) confirms weekend hours are decomposable
- After V9 (capacity sum) validates total allocation
- Before finalizing capacity model

**Output:**
- PASS: Personal execution 11–18h/week; trend flat or mild (Δ <2h/week); sustainable
- WARN: Personal execution 18–20h/week (stretched) → requires assumption documentation + escalation if trend continues; OR personal load trending Δ +2h × 2–3 weeks → monitor for unsustainability
- FAIL: Personal execution >20h/week (unsustainable sprint) → must escalate to month context for decision; OR personal load trending Δ +2h × 3+ consecutive weeks without escalation → requires intervention

**Example PASS:**
```
W12 personal capacity calculation:
  - Net weekday evening: 6h (Thu S-only −1h, Fri closure −1h from 10h gross)
  - Sat daytime: 5h declared + planned
  - Sun afternoon: 3h declared + planned
  - Total: 6 + 5 + 3 = 14h personal ✓ (within 11–18h normal)
  
Trend check (past 3 weeks):
  - W09: 12h
  - W10: 13h (Δ +1h)
  - W11: 14h (Δ +1h)
  - W12: 14h (Δ 0h)
  Trend: flat & sustainable ✓

Status: PASS
```

**Example WARN:**
```
W12 personal capacity calculation:
  - Net weekday evening: 8h (Thu full evening + Fri full evening used; no structural deductions)
  - Sat daytime: 6h declared + planned
  - Sun afternoon: 4h declared + planned
  - Total: 8 + 6 + 4 = 18h personal ⚠️ (at stretched threshold)
  
Trend check (past 3 weeks):
  - W09: 12h
  - W10: 15h (Δ +3h)
  - W11: 17h (Δ +2h)
  - W12: 18h (Δ +1h)
  Trend: 3-week continuous increase ❌

Status: WARN — Stretched week + concerning trend
  
Required action:
  - Document assumption: "Q1 deliverable deadline requires sustained high effort; month context escalation made (see Month file §[n])"
  - Decision: Continue with 18h this week OR reduce scope to 15h
  - Trend intervention: If W13 also >16h, escalate to month for rebalancing
```

**Example FAIL:**
```
W12 personal capacity calculation:
  - Net weekday evening: 8h (full use of evenings)
  - Sat daytime: 7h declared + planned
  - Sun afternoon: 5h declared + planned
  - Sun evening: 2h opened (normally OFF) to close scope
  - Total: 8 + 7 + 5 + 2 = 22h personal ✗ (unsustainable sprint)

Status: FAIL — Unsustainable personal execution
  
Required action:
  - Scope reduction mandatory (reduce to <18h or ideally <15h)
  - OR explicit decision to accept sprint: escalate to month context + document recovery plan for W13+
  - If escalating: month must approve + allocate recovery time
```

---

### Change 4: Update Output Contract (§7)

**Location:** Section 7 — Output Contract — Validation Status Table

**Current table last row (V11):**
```
| Pool isolation | V11 | PASS / FAIL | |
```

**Add two new rows after V11:**

```
| Weekend effort realism | V13 | PASS / WARN / FAIL | |
| Personal capacity ceiling | V14 | PASS / WARN / FAIL | |
```

---

## File 2: GENERATE_WEEKPLAN.md

### Change 1: Update Step 6 — Assess Capacity and Effort Balance

**Location:** Section Step 6, subsection **Key rules** after V12 description

**Current text (around line 810–815):**
```
   - If any V-check is **FAIL**: resolve before proceeding (see CAPACITY_ENGINE §8 — Decision Logic)
   - If any V-check is **WARN**: document the assumption and proceed with caution
```

**Add after above:**

```
   - **NEW (V13, V14):** After running capacity engine:
     - V13 (Weekend effort realism): If WARN, verify decomposition documented; If FAIL, reduce scope or defer weekend allocation
     - V14 (Personal capacity ceiling): If WARN, document assumption + check trend (escalate if 3-week pattern); If FAIL, escalate scope-reduction decision to month context
```

### Change 2: Update Step 6 Actions (Detail subprocess)

**Location:** Section Step 6, subsection **Actions**

**Current action 4:**
```
4. Review engine output:
   - If any V-check is **FAIL**: resolve before proceeding...
```

**Expand to include:**

```
4. Review engine output:
   - If any V-check is **FAIL**: resolve before proceeding
   - If V13 (weekend effort realism) is WARN: verify task breakdown documented; proceed with buffer assumption if spillover path exists
   - If V13 is FAIL: resolve via scope reduction or weekend reallocation
   - If V14 (personal capacity ceiling) is WARN: document why week is stretched (deadline, project phase, etc.); check if trend is 3-week pattern (escalate if yes)
   - If V14 is FAIL: escalate to month context; cannot proceed without scope reduction or strategic decision
```

### Change 3: Add Decomposition Requirement to Step 6

**Location:** Section Step 6, add new sub-step before "Run CAPACITY_ENGINE"

**Add:**

```
   2.5. **Prepare Weekend Effort Decomposition (NEW)**
   - For any project with planned weekend allocation (Sat daytime or Sun afternoon):
     - List each mission/task to be executed on each weekend day
     - State effort hours per task (should total ≈ declared slot hours)
     - Identify spillover scenario (if work +10%, where does it go?)
     - Feed this into CAPACITY_ENGINE as input for V13 validation
```

### Change 4: Update Capacity Summary embed instructions (Step 6)

**Location:** Section Step 6, action 5 (Embed engine output)

**Current:**
```
5. Embed the engine's Capacity Summary block in the WeekPlan `## Capacity & Constraints` section
```

**Expand to:**

```
5. Embed the engine's Capacity Summary block in the WeekPlan `## Capacity & Constraints` section, including:
   - V13 validation result (weekend effort realism: PASS / WARN / FAIL)
   - V14 validation result (personal capacity ceiling: PASS / WARN / FAIL)
   - If V13 WARN: spillover path documented
   - If V14 WARN: assumption about why week is stretched; trend status (flat / increasing / escalation decision made)
   - If V13 or V14 FAIL: remediation action (scope reduction / deferral / escalation with reason)
```

### Change 5: Update Capacity Validation Checklist (Step 9 / Definition of Good WeekPlan)

**Location:** Section **Constraint Honoring** or section **Definition of Good WeekPlan**

**Add after existing capacity checks:**

```
- [ ] V13 (Weekend effort realism): Weekend-allocated work has documented task breakdown; each task fits in declared slot; spillover path exists or not needed
- [ ] V14 (Personal capacity ceiling): Total personal execution within sustainable band (11–18h/week normal; 18–20h = WARN with assumption documented; >20h = escalated); trend analysis completed
```

---

## File 3: NEW — TEMPLATE_WEEKEND_DECOMPOSITION.md

**Purpose:** Provide structure for planners to prepare weekend scope before running CAPACITY_ENGINE

**Create new file** at `OS/04_OPERATIONS/WEEKLY_CONTROL/TEMPLATE_WEEKEND_DECOMPOSITION.md`

**Content:**

```markdown
# Weekend Effort Decomposition Template

**Week:** W##  
**Date:** YYYY-MM-DD  
**Planner:** [Name]

---

## Purpose

Before running CAPACITY_ENGINE's V13 check, decompose all projects allocated to weekend into M-sized tasks. This template ensures:
- Weekend scope is realistic (can fit in declared slot hours)
- Spillover scenario is planned (if work exceeds declared hours, where does it go?)
- Allocation is driven by project needs, not load-balancing gamification

---

## Saturday Daytime

**Declared allocation:** [X hours]

| Project | Mission/Task | Effort (h) | Focus Type | Notes |
|---|---|---|---|---|
| RobotOS | [Task name] | [h] | [arch/impl/spec/review] | [Any dependencies or risk] |
| RobotOS | [Task name] | [h] | [arch/impl/spec/review] | [Any dependencies or risk] |
| Signee | [Task name] | [h] | [arch/impl/spec/review] | [Any dependencies or risk] |
| **TOTAL** | | **[sum]** | | |

**Feasibility Check:**
- Sum of tasks ≈ declared allocation? ✓ / ✗
- Can tasks fit in one daytime block (5–6h)? (no more than ~1 large task + 1 small, or 2 independent small tasks) ✓ / ✗
- Spillover (+10%): If work exceeds [X] h, where does [overrun] go? → [Specify: Sun afternoon, weekday evening, or defer to W##]

---

## Sunday Afternoon

**Declared allocation:** [Y hours] (or 0 if not planned)

| Project | Mission/Task | Effort (h) | Focus Type | Notes |
|---|---|---|---|---|
| RobotOS | [Task name] | [h] | [arch/impl/spec/review] | [Any dependencies or risk] |
| Signee | [Task name] | [h] | [arch/impl/spec/review] | [Any dependencies or risk] |
| **TOTAL** | | **[sum]** | | |

**Feasibility Check:**
- Sum of tasks ≈ declared allocation? ✓ / ✗
- Can tasks fit in one afternoon block (3–4h, post-weekend fatigue)? ✓ / ✗
- Spillover (+10%): If work exceeds [Y] h, where does [overrun] go? → [Specify: weekday evening or defer to W##]

---

## Personal Load Summary

| Component | Hours | Source |
|---|---|---|
| Net weekday evening (Mon–Fri after structural deductions) | [E] h | Derive from anchor table |
| Sat daytime | [X] h | Declared above |
| Sun afternoon | [Y] h | Declared above |
| Sun morning (overhead) | ~2–3 h | Structural |
| **Total personal execution** | **[E + X + Y]** h | |

**Sustainability Check:**
- Total in 11–18h range (normal)? ✓ / ⚠️ / ✗
- If >18h: assumption documented? ✓ / ✗
- Trend (compare to past 3 weeks): flat / +1h / +2h+ ? → escalate if +2h/week × 3 weeks

---

## Spillover Resolution Matrix

| If Scenario | Then | Escalation? |
|---|---|---|
| Sat work exceeds [X] by >10% | Move overflow to [slot] | No (if slot exists) |
| Sun work exceeds [Y] by >10% | Move overflow to [slot] | No (if slot exists) |
| Both Sat and Sun at capacity + combined overflow | Defer [task] to W## | Yes (impacts month goal?) |
| Cannot fit decomposed tasks in declared slots | Reduce scope or reallocation | Yes (decision needed) |

---

## Approval Gate

- [ ] All weekend tasks decomposed and listed above
- [ ] Task drift check: are these tasks tracked in project contexts or goal list?
- [ ] Spillover path exists for each weekend day
- [ ] Personal load total calculated and within sustainable band
- [ ] Ready for CAPACITY_ENGINE V13/V14 validation

Ready for capacity model finalization: ✓ / ✗

---

**Attached to:** W##_WeekPlan.md (as reference in planning notes, not embedded in final plan)

```

---

## Summary of Changes

### CAPACITY_ENGINE.md

1. **Table §6:** Add V13 + V14 rows to Validation Checks table
2. **Section §6:** Add V13 validation logic (task decomposition, slot fit, spillover scenario)
3. **Section §6:** Add V14 validation logic (personal capacity calculation, sustainability bands, trend analysis)
4. **Table §7:** Add V13 + V14 rows to output Validation Status table

### GENERATE_WEEKPLAN.md

1. **Step 6:** Add V13/V14 execution guidance after V12
2. **Step 6 Actions:** Expand action 4 to include V13/V14 decision logic
3. **Step 6 Actions:** Add new sub-step 2.5 (weekend decomposition prep)
4. **Step 6 Actions:** Expand action 5 with V13/V14 embedding requirements
5. **Step 9 (Checklist):** Add V13 + V14 checks to Definition of Good WeekPlan

### New File

**TEMPLATE_WEEKEND_DECOMPOSITION.md** — Provides structure for weekend scope decomposition before capacity validation

---

## Estimated Implementation Time

- CAPACITY_ENGINE.md changes: ~30 min (add 2 validation checks + output rows)
- GENERATE_WEEKPLAN.md changes: ~20 min (expand step 6; add checklist items)
- Template creation: ~15 min
- **Total: ~1 hour for all edits**

---

## Testing / Validation

**Before committing:**

1. Run V13 + V14 logic manually on existing W11 capacity model
   - Does W11 pass V13? (decomposition check)
   - Does W11 pass V14? (personal load check)
   - Document results

2. Draft W12 capacity model with new checks active
   - Does W12 decomposition satisfy V13?
   - Does W12 personal load satisfy V14?
   - Are new columns/sections clear to planner?

3. Solicit feedback from first use (W12+)
   - Is V13 decomposition check practical or burdensome?
   - Is V14 trend detection useful?
   - Any refinement needed?

---

**Next Step:** Apply changes to CAPACITY_ENGINE.md and GENERATE_WEEKPLAN.md, test on W12 instance.

```

