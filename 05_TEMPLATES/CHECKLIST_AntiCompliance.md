# Anti-Fake Compliance Validation Checklist

---

## Purpose

This checklist prevents the system from accepting plans, anchors, or execution records that are **procedurally complete but semantically empty**.

Fake compliance is the risk that:
- Fields are filled (required metadata: ✓ Linked Weekly Goal, ✓ First Strike, ✓ Exit Condition)
- But content is generic, vague, or generated without thought
- System appears to function when it is actually brittle

Example of fake compliance:
- Anchor: "Zephyr — Continue work on test infrastructure for ongoing development"
  - ✓ Has Linked Weekly Goal (present, checkable field)
  - ✓ Has First Strike ("Start by reviewing") 
  - ✓ Has Exit Condition ("Work is done when it's done")
  - ✗ But all three fields use generic language
  - Result: Procedurally valid. Semantically empty. → FAKE COMPLIANCE

This checklist tests whether content is GENUINELY SPECIFIC or merely procedurally present.

---

## When to Run This Checklist

Run this checklist:

1. **Before finalizing any WeekPlan:** Test if Weekly Goals pass specificity test.
2. **Before finalizing any Weekly Execution file:** Test if execution anchors have real (not generic) metadata.
3. **At daily closeout (INTEGRATE_DAILY):** Test if daily anchors executed with real Exit Conditions, not vague "mostly done" states.
4. **At week closeout (WEEK_CLOSEOUT):** Test if weekly execution demonstrates real execution vs. procedural theater.
5. **During monthly context updates (UPDATE_PROJECT_CONTEXT):** Test if context carries real insight vs. abstract bullet points.

---

## Anti-Fake Compliance Validation Tests

### Test Block 1: Metadata Field Specificity

For each anchor or goal being validated, ask the following questions for each required field:

#### Test 1.1 — Linked Weekly Goal Field

**Question:** Does the Linked Weekly Goal field reference a SPECIFIC goal from the WeekPlan, or a generic category?

- ✗ Fake: "Serves office hours work"
- ✗ Fake: "Serves Zephyr goal"
- ✓ Real: "Serves Goal 2: Zephyr Testing Infrastructure — Merge 3 RAM-load tests to develop"

**Validation rule:** The Linked Weekly Goal must:
- Reference the exact goal name from WeekPlan §2 (not paraphrase it)
- Include the goal's artifact or deliverable (what will be delivered)
- Pass the "third-party reading test": could someone unfamiliar with the week understand which goal this anchor serves?

**If field fails test → REJECT and rewrite goal reference until specific.**

---

#### Test 1.2 — First Strike Field

**Question:** Does the First Strike describe the EXACT first action, or a vague starting mode?

- ✗ Fake: "Get started with the work"
- ✗ Fake: "Review and begin"
- ✗ Fake: "Start the project"
- ✓ Real: "Open test file from W10 branch; check test requirements in comments; confirm environment is ready"

**Validation rule:** First Strike must:
- Name the SPECIFIC file, tool, or document to open/access first
- State the actual first action (not "start" or "begin")
- Include context needed to avoid false restarts (e.g., "from W10 branch", not just "open test file")
- Be concrete enough that someone with zero context could execute it

**Third-party test:** Could a Copilot agent, copy-pasted this field, execute the exact first step without asking clarifying questions?

**If field fails test → REJECT and rewrite until step-by-step specific.**

---

#### Test 1.3 — Exit Condition Field

**Question:** Does the Exit Condition describe an OBSERVABLE END STATE, or vague satisfaction?

- ✗ Fake: "Testing is complete"
- ✗ Fake: "Work is done"
- ✗ Fake: "Looks good"
- ✗ Fake: "Good progress"
- ✗ Fake: "Ready for next phase"
- ✓ Real: "3 tests passing locally; CI suite passes; PR submitted to develop; review checklist checked"

**Validation rule:** Exit Condition must:
- Define a BINARY state (it is either true or false; no gray area)
- Include observable markers (file state, CI status, artifact existence, etc.)
- Avoid subjective language (good, ready, looks okay)
- List specific artifacts or states that prove completion
- Include HOW completion is verified (automated test? file existence? review approval?)

**Third-party test:** Could someone verify this exit state objectively, without judgment? Answer yes/no?

**If field fails test → REJECT and rewrite until binary and observable.**

**If field fails test → REJECT and rewrite until binary and observable.**

### Test Block 3: Readability and Clarity Validation

This test ensures that generated artifacts are **scan-friendly and quickly understandable**, not dense walls-of-text that obscure meaning.

#### Test 3.1 — Paragraph Length and Idea Density

**Question:** Do paragraphs exceed 3–4 lines? Do single paragraphs mix multiple distinct ideas?

- ✗ Fake: "The Goal is to improve RobotOS architecture by clarifying the adapter boundary and conducting team onboarding. This will require reviewing existing code, meeting with the team to resolve dependencies, and documenting the architecture decision before implementation begins. The expected output is a clear design document that defines the adapter boundary, and team members will be onboarded and ready to implement."
- ✓ Real (split into bullets):
  - **Deliverable:** Clear RobotOS adapter boundary definition
  - **Tasks:** Review existing code → meet team on dependencies → document architecture decision
  - **Team output:** All team members understand architecture; ready to implement

**Validation rule:** 
- Each paragraph must convey ONE primary idea (not 2–3 bundled together)
- If explaining capacity + allocation + constraint in same paragraph → split into separate labeled blocks
- If page feels like a wall-of-text when scanning, it fails this test

**If field fails test → Reformat using bullets, labeled sub-sections, or compact tables until scan-friendly.**

#### Test 3.2 — Numeric and Structural Content Formatting

**Question:** Are numbers, hours, allocations, slot declarations, and rules formatted as prose or as structured blocks?

- ✗ Fake (prose): "The team has allocated 3 hours for RobotOS Slot 1 on Saturday daytime, with an additional 0 hours for Sunday afternoon unless a critical issue requires overflow, in which case up to 2 hours could be used for spillover management."
- ✓ Real (structured):
  - **Slot 1 (Sat daytime):** 3h RobotOS
  - **Slot 4 (Sun afternoon):** 0h (no spillover this week)
  - **Overflow rule:** If critical issue detected Thursday → escalate by EOD, don't auto-spillover

**Validation rule:**
- All hour allocations must be listed as bullets or table rows, not buried in prose
- All slot declarations must use explicit format: **Slot #:** designation + value
- All rules must be stated as separate bullet items, not mixed into narrative
- Comparisons (e.g., "Pool A vs Pool B") must use side-by-side bullets or table rows

**If field fails test → Extract all numbers and rules into bullets/table format. Rewrite surrounding prose to be navigation-minimal.**

#### Test 3.3 — Synthesis Paragraph Density

**Question:** Does the artifact contain dense summary paragraphs that should be broken into scannable pieces?

- ✗ Fake: "This week represents a balance between deep architectural work and team coordination, with the primary focus on delivering the adapter boundary definition while maintaining responsive communication with team members who are waiting for design clarity. The capacity is tight because of ongoing Zephyr office commitments, so weekend work is necessary to create space for meaningful RobotOS progress without sacrificing day-job quality."
- ✓ Real (bullets):
  - **Primary focus:** Deliver RobotOS adapter boundary definition
  - **Supporting work:** Team coordination + design clarity meetings
  - **Constraint:** Zephyr office commitments limit weekday evening capacity
  - **Solution:** Use weekend Slot 1 (Sat daytime) for deep architectural work

**Validation rule:**
- Any synthesis paragraph > 2 sentences should be split into 3–4 labeled bullets
- Complex reasoning (trade-offs, decision logic) must use separate labeled lines, not embedded clauses
- Causal chains ("because X, therefore Y") work better as bullet chains than prose

**If field fails test → Break synthesis into labeled bullets. Preserve all logic; improve readability.**

---

#### Test 1.4 — Carry-over Rule Field (if present)

**Question:** Does the Carry-over Rule specify EXACTLY what carries over and how, or is it vague?

- ✗ Fake: "Continue if not done"
- ✗ Fake: "Finish next day if needed"
- ✓ Real: "If test merge blocked after 60 min (by review delay) → defer to Wed 8:00–8:10 Quick re-entry: check review status → resume merge if approved"

**Validation rule:** Carry-over Rule must:
- State the CONDITION that triggers carry-over (not "if not done" but "if blocked by X" or "if time exceeded after Y min")
- Name the exact artifact state that carries (e.g., "test file with 2/3 tests passing")
- Specify re-entry mode (Quick / Analytical / Fragile)
- Name the receiving day/time
- State the exact re-entry first action

**If field fails test → REJECT and rewrite until carry-over path is unambiguous.**

---

### Test Block 2: Content Depth Validation

#### Test 2.1 — Generic Language Detector

For each field in the anchor/goal being validated, run the **Generic Language Scan:**

Read through all text in the Linked Weekly Goal, First Strike, Exit Condition, and any Supporting Text fields.

**Mark as FAKE if ANY of these patterns appear:**

- Weak verbs (without direct object): "work", "do", "proceed", "handle", "manage", "execute"
- Vague process language: "improve", "optimize", "refactor", "enhance", "polish", "iterate"
- Temporal hedging: "continue", "keep going", "move forward", "progress"
- Abstract containers: "stuff", "things", "work", "effort", "tasks"
- Subjective satisfaction: "good", "well", "properly", "adequately", "reasonable"
- Missing specificity: "the infrastructure", "the system", "the setup" (which? what specific component?)

**Example FAKE (generic language scan):**

> "Zephyr — Improve the test infrastructure by optimizing test suite execution. First Strike: Get started on refactoring the test framework. Exit Condition: Better performance achieved."

Detected patterns:
- "Improve" ← weak verb (vague improvement)
- "test infrastructure" ← article ("the") → not specific
- "optimizing" ← vague process
- "Get started on" ← empty first action
- "refactoring" ← vague; which part?
- "Better performance" ← subjective (what is "better"?)

**VERDICT: FAKE COMPLIANCE**

---

**Example REAL (passes generic language scan):**

> "Zephyr — Merge 3 RAM-load tests to develop branch. First Strike: Open test_memory.c from W10 branch; review inline comment listing remaining test assertions; confirm environment setup complete. Exit Condition: All 3 tests passing in CI; PR submitted; develop branch merge confirmed."

Detected patterns:
- 0 weak verbs (specific action: "Merge", "submit")
- 0 vague process language
- Specific file names (test_memory.c)
- Specific artifact states (CI passing, PR submitted, merge confirmed)
- Observable verification (CI report, PR status)

**VERDICT: REAL COMPLIANCE**

---

#### Test 2.2 — Artifact Naming Test

**Question:** Can you list the specific files, documents, or components that should exist when this anchor completes?

For the anchor being validated:

1. Read Linked Weekly Goal + First Strike + Exit Condition
2. Ask: "What artifact(s) should exist if this work is done?"
3. Write them down as a list:
   - File name: _________________
   - File name: _________________
   - Observable state: _________________ (e.g., "CI passing", "PR merged")

**FAKE COMPLIANCE TEST:** If you cannot complete this list, or if you write generic descriptors like "code", "tests", "documentation" without naming the specific file → FAKE COMPLIANCE

**Examples:**

✗ FAKE: Anchor "Improve the test infrastructure" → Artifact list: "Better infrastructure" (not a real artifact)

✓ REAL: Anchor "Merge RAM-load tests to develop" → Artifact list: 
   - File: test_memory.c (merged to develop)
   - Artifact: PR#123 merged
   - State: CI passing

---

#### Test 2.3 — Third-Party Executability Test

**Question:** If you handed this anchor to a third party (or Copilot, or a colleague unfamiliar with the project), could they execute the First Strike and reach the Exit Condition without asking clarifying questions?

**Procedure:**

1. Copy the First Strike exactly as written
2. Give it to someone (real or simulated) with ZERO project context
3. Ask: "Can you do this without asking questions?"

- If their answer is "I need clarification on [X]" → FAKE COMPLIANCE (First Strike is not independent)
- If their answer is "I can start, but unclear what I'm aiming for" → FAKE COMPLIANCE (Exit Condition is vague)
- If their answer is "I can do this; here is what I will produce" → REAL COMPLIANCE (sufficient specificity)

**Example FAKE (third-party test):**

Anchor: "Zephyr — Work on test infrastructure"
First Strike: "Begin improving the test system"

Third-party response: "I need clarification:
- Which test system? (unit? integration? end-to-end?)
- What tool am I using? (Jest? pytest? custom?)
- What file do I open?
- What is 'improve'?
- How do I know when I'm done?"

**VERDICT: FAKE COMPLIANCE (too vague for independent execution)**

---

**Example REAL (third-party test):**

Anchor: "Zephyr — Merge 3 RAM-load tests to develop"
First Strike: "Open test_memory.c from W10 branch; review inline test requirement comments; verify test runner is available"

Third-party response: "I can do this:
1. Clone/checkout W10 branch
2. Open test_memory.c
3. Read the comments describing the 3 tests
4. Check test runner setup
5. Then I would write the tests and merge per the Exit Condition"

**VERDICT: REAL COMPLIANCE (sufficient for independent start)**

---

### Test Block 3: Integration and Context Consistency

#### Test 3.1 — Goal Traceability Chain

**Question:** Can you trace the connection Goal → WeekPlan → WeekPlan section?

**Procedure:**

1. Note the Linked Weekly Goal in the anchor
2. Look up that exact goal in WeekPlan §2 (Weekly Goals section)
3. Confirm: Is the goal listed there VERBATIM (or close enough to trace)?
4. If YES → pass. If NO → FAKE COMPLIANCE (broken traceability)

**Example FAIL:**

Anchor lists: "Serves Goal 2: Infrastructure Tests"
WeekPlan §2 lists: (Goal 1, Goal 2: Zephyr Testing Framework, Goal 3, ...)

The anchor and WeekPlan don't match → broken traceability → REJECT

---

#### Test 3.2 — Capacity Alignment Check

**Question:** When summed with other anchors for the same pool/day, does this anchor create realistic load?

**Procedure:**

1. Identification the pool (Office Pool A vs. Personal Pool B)
2. Identify the day this anchor executes
3. List all other anchors executing the same day in the same pool
4. Sum estimated time for all anchors
5. Compare against expected capacity for that day

Example:
- Pool A, Thursday
- Anchor 1: "Zephyr tests" (60 min estimated)
- Anchor 2: "Zephyr review" (45 min estimated)
- Anchor 3: "Zephyr merge" (30 min estimated)
- Total: 135 min = ~2.25 hours
- Expected Thu office capacity: ~7 hours
- Alignment: OK (leave 5 hours for other work)

If anchors sum to >6.5 hours in office hours (leaving only 30 min for unexpected work, rest hours, etc.) → OVERLOAD → escalate.

---

#### Test 3.3 — Artifact Output Format Realism Check

**Question:** Does the Exit Condition's artifact state match realistic engineering practice?

**Procedure:**

For each artifact named in the Exit Condition, ask:

- Is this a typical deliverable in the project? (if unsure, ask team lead)
- If "PR merged" is the exit: Is CI required before merge? Is review required?
- If "document written" is the exit: Is there a template or standard format expected?
- If "test passing" is the exit: Does this imply review of the test? Or just binary pass?

**Example FAKE:** Exit Condition: "Code is perfect and everyone likes it"
- "Perfect" is subjective, not realistic engineering metric
- "Everyone likes it" is social judgment, not technical artifact
- VERDICT: FAKE COMPLIANCE

**Example REAL:** Exit Condition: "3 tests passing in CI; code review checklist complete; PR merged to develop"
- CI passing is objective (pass/fail)
- Review checklist is explicit (concrete step list)
- Merged state is verifiable (git log)
- VERDICT: REAL COMPLIANCE

---

### Test Block 4: Seasonal Reality Validation

#### Test 4.1 — Load Reality Check

**Question:** Given week type (early/mid/late month), does anchor load match realistic energy?

**Procedure:**

1. Determine week phase (early/mid/late month)
2. If late month: Do anchors assume fresh energy, or reflect potential fatigue?
3. If early month: Do anchors build ramp-up energy gradually?
4. If mid-month: Are anchors at peak capacity without burning out?

**Example FAKE:** Late-month Thursday, anchor: "Refactor entire test infrastructure" (L-sized work, 4+ hours)
- Late-month Thu usually has lower energy
- L-sized anchor conflicts with realistic capacity
- VERDICT: FAKE COMPLIANCE (over-ambitious for actual energy)

**Example REAL:** Late-month Thursday, anchor: "Review test merge results; document changes; prepare hand-off notes" (M-sized work, 1.5 hours)
- Reflects realistic late-week energy
- Work is closure/documentation, not new construction
- VERDICT: REAL COMPLIANCE

---

#### Test 4.2 — Carry-over Saturation Check

**Question:** Is carry-over load realistic for the week type, or are anchors hiding overload?

**Procedure:**

1. Count carry-over items from previous week
2. Estimate time for each
3. Sum carry-over time across the week
4. Check against expected capacity: Should not exceed 10% of weekly capacity for Pool A, 15% for Pool B

**Example FAKE:**
- Pool A weekly capacity: ~36 hours
- Carry-over: 4 items @ 2h each = 8 hours
- Carry-over ÷ Total Capacity = 8/36 = ~22%
- Exceeds 10% threshold → OVERLOAD HIDDEN → FAKE COMPLIANCE

**Example REAL:**
- Pool A weekly capacity: ~36 hours
- Carry-over: 2 items @ 1h each = 2 hours
- Carry-over ÷ Total Capacity = 2/36 = ~5.5%
- Within 10% threshold → realistic → REAL COMPLIANCE

---

## Anti-Fake Compliance Checklist Template

Use this template to validate any execution artifact (anchor, goal, weekly plan, daily file, execution summary).

```
## Anti-Fake Compliance Validation Report

**Artifact being validated:** [Anchor name / Goal name / Weekly Plan / etc.]
**Validated by:** [Name/Agent]
**Date:** [YYYY-MM-DD]
**Confidence:** [Low / Medium / High]

### Test Block 1: Metadata Specificity

- [ ] **Test 1.1 — Linked Weekly Goal:** Field references SPECIFIC goal from WeekPlan? YES / NO
  - If NO: List what is generic/vague: _______________
  
- [ ] **Test 1.2 — First Strike:** Describes EXACT first action with named file/tool? YES / NO
  - If NO: List missing specificity: _______________
  
- [ ] **Test 1.3 — Exit Condition:** Binary, observable, avoids subjective language? YES / NO
  - If NO: List subjective patterns: _______________
  
- [ ] **Test 1.4 — Carry-over Rule (if present):** Specifies trigger condition + re-entry path? YES / NO
  - If NO: List missing clarity: _______________

### Test Block 2: Content Depth

- [ ] **Test 2.1 — Generic Language Detector:** Free of weak verbs, vague process words, subjective satisfaction language? YES / NO
  - If NO: List detected patterns: _______________

- [ ] **Test 2.2 — Artifact Naming:** Can list 2+ specific files or observable states? YES / NO
  - Artifacts named: 
    - _______________
    - _______________
    - _______________

- [ ] **Test 2.3 — Third-Party Executability:** Could unfamiliar party execute First Strike and reach Exit Condition? YES / NO
  - If NO: List missing context: _______________

### Test Block 3: Integration Consistency

- [ ] **Test 3.1 — Goal Traceability:** Linked goal matches WeekPlan §2 goal name verbatim? YES / NO
  - If NO: Goal listed as: _______________ vs. WeekPlan: _______________

- [ ] **Test 3.2 — Capacity Alignment:** Anchor + others same day/pool stay within realistic load? YES / NO
  - If NO: Total estimated load: _______________ (exceeds threshold)

- [ ] **Test 3.3 — Artifact Output Format:** Expected artifacts match realistic project practice? YES / NO
  - If NO: Unrealistic expectation: _______________

### Test Block 4: Seasonal Reality

- [ ] **Test 4.1 — Load Reality for Week Phase:** Anchor load matches realistic energy for week type? YES / NO
  - If NO: Week type: _______________ vs. Anchor expectation: _______________

- [ ] **Test 4.2 — Carry-over Saturation:** Carry-over load ≤ 10–15% of weekly capacity? YES / NO
  - Carry-over load: _______________% (threshold: 10–15%)

### Overall Verdict

- **Total Passed:** ____ / 10 checks
- **Total Failed:** ____ / 10 checks

**Anti-Fake Compliance Status:**
- [ ] PASS — All checks green; artifact is REAL COMPLIANCE
- [ ] FAIL — 1+ checks failed; rewrite before executing
- [ ] CONDITIONAL — 1–2 checks borderline; proceed with caution + flag for post-execution review

**If FAIL or CONDITIONAL: Required revisions**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

**Notes / Escalations:**
_______________________________________________
_______________________________________________
```

---

## Escalation Path

If an artifact **FAILS** anti-fake compliance and you cannot specify the fix:

1. **Escalate to:** Agent 1 or Project Owner
2. **Provide:** This completed checklist + examples of what is generic
3. **Request:** Rewrite guidance or strategic decision (is this goal/anchor core to weekly success, or can it be deferred?)
4. **Decision:** Rewrite + re-validate before execution, OR defer to following week

**Do not execute artifacts that fail anti-fake compliance testing.**

---

## Summary

**Anti-fake compliance prevents:**
- ✗ Procedurally valid but semantically empty plans
- ✗ Fields filled with generic language that creates friction at execution time
- ✗ Hidden overload masked by vague anchor descriptions
- ✗ Broken traceability between daily, weekly, and monthly layers
- ✗ Artificial compliance that degrades into execution failure

**Run this checklist at:**
- Week planning finalization (GENERATE_WEEKPLAN)
- Weekly execution finalization (GENERATE_WEEKLY_EXECUTION)
- Daily execution closeout (INTEGRATE_DAILY)
- Month context updates (UPDATE_PROJECT_CONTEXT)
- Any point where you suspect procedural theater (filled fields, empty content)

**Result:** System remains high-signal. Execution anchors are real, specific, and independently executable.
