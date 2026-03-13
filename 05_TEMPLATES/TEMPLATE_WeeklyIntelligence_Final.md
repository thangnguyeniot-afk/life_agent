# TEMPLATE_WeeklyIntelligence_Final.md — Weekly Intelligence Layer (Agent-Ready)

> **Function:** Cross-week pattern detection and system health assessment.
> **Input:** Weekly Review files (primary source).  
> **Output:** Management intelligence → planning adjustments.
> **Cadence:** Every 2 weeks, monthly, or at phase boundaries (not every week).
> **Separation:** WeekPlan = commitment. WeeklyReview = judgment. WeeklyIntelligence = pattern.

---

## Table of Contents

- [1. Intelligence Window](#1-intelligence-window)
- [2. Executive Signal](#2-executive-signal)
- [3. Capacity Trend](#3-capacity-trend)
- [4. Focus Distribution / Drift](#4-focus-distribution--drift)
- [5. Artifact Production Pattern](#5-artifact-production-pattern)
- [6. Repeating Blockers / Structural Friction](#6-repeating-blockers--structural-friction)
- [7. Question Resolution Pattern](#7-question-resolution-pattern)
- [8. System Stability Assessment](#8-system-stability-assessment)
- [9. Management Implications](#9-management-implications)
- [10. Recommended Control Rules](#10-recommended-control-rules)
- [11. Links / Trace](#11-links--trace)

---

## 1. Intelligence Window

**Weeks covered:** YYYY-Www → YYYY-Www *(example: 2026-W09 → 2026-W12)*

**Analysis date:** YYYY-MM-DD

**Source reviews:** Total count: ___ reviews analyzed

**Reviews included:**
- `07_REVIEWS/03_WEEK/YYYY-Www_Review.md`
- (repeat as needed)

**Why this window:**
(1–2 sentences: what prompted the analysis? phase boundary? capacity concern? pattern emerging?)

**Confidence level:** 
- [ ] High (≥4 weeks)
- [ ] Medium (2–3 weeks)
- [ ] Low (1 week) ← note: single-week data provides seed not trend

---

## 2. Executive Signal

> Operating summary in 4 lines or less.

**System state:** (one word: Stable / Noisy / Blocked / Drifting / Improving / Overloaded / Brittle)

**Main trend:** (1 sentence — what's changing week-to-week?)

**Biggest risk:** (1 sentence — what could destabilize the next phase?)

**Best positive signal:** (1 sentence — what's getting better?)

---

## 3. Capacity Trend

> Planned vs actual across the window. Judge the pattern, not raw numbers.

| Week | Planned Capacity | Actual Blocks | Over / Under | Notes |
|---|---|---|---|---|
| YYYY-Www | ~14–16 (Full) | … | … | … |

**Trend interpretation:** 
- Pattern: (e.g., "consistently full", "declining", "spiky", "recovering")
- Unplanned work absorption: (e.g., "steady ~10%", "spiked 30% W11")
- Energy stability: (improving / consistent / declining / volatile)

**Forecast for next window:**
- Expected capacity: Full / Reduced / Limited ← based on system trajectory
- Why: (what evidence supports this?)

---

## 4. Focus Distribution / Drift

> Which projects dominated? Is operating model being respected? Is any stream starved?

**Primary project rhythm (weekday dominant):**
- Intended: (from month/phase plan)
- Actual: (from weekly reviews)
- Alignment: On model / Drifting / Misaligned

**Secondary project pattern (weekday + weekend variable):**
- Signee / RobotOS tendency
- Weekend execution: (used / unused / unpredictable)
- Comment: (is secondary anchor truly ~30-40% or is it overflowing?)

**Project completion / momentum:**
- Which projects produced artifacts regularly?
- Which projects are mostly discussion?
- Is any project in backlog creep (expanding without closure)?

**Drift assessment:**
- [ ] Focus stayed aligned with operating model
- [ ] Minor drift (1–2 projects), correctable
- [ ] Major drift (project allocations need reset)

---

## 5. Artifact Production Pattern

> Done = DoD + Artifact + Trace. Track production discipline across weeks.

| Project / Stream | Artifact Types | Consistency | Notes |
|---|---|---|---|
| Signee | DRAFT / NOTE / ADR / … | High / Medium / Low / Missing | … |
| RobotOS | DRAFT / NOTE / SPIKE / … | High / Medium / Low / Missing | … |
| Zephyr | PLAN / SNAPSHOT / … | High / Medium / Low / Missing | … |

**Trace quality trend:**
- Artifact location discipline: (improving / stable / degrading)
- Evidence linkage (artifact → daily file → review): (strong / weak / inconsistent)
- Untraced work (discussions with no artifact): (minimal / moderate / high)

**Missing artifact flags:**
- Which work types lack trace? (example: "RobotOS architecture spike unconfirmed")
- Impact: (low impact on next phase / critical for scope freeze / blocks integration)

---

## 6. Repeating Blockers / Structural Friction

> Separate operational friction from system design friction.

### Operational (repeating issues)
> Meeting conflicts, env breaks, toolchain friction, dependency blockage.

- Blocker: … | Frequency: (recurring pattern?) | Mitigation: …
- Blocker: … | Frequency: … | Mitigation: …

### Structural (system design issues)
> Planning overload, anchor misuse, embedding prevention, third-project leakage, trace gaps.

- Issue: … | Impact: (capacity / clarity / focus?) | Root: … | Fix: …
- Issue: … | Impact: … | Root: … | Fix: …

### Escalations (critical blockers for next phase)
- Escalation: … | Must be addressed: (yes / should be / optional)

---

## 7. Question Resolution Pattern

> Spike weeks accumulate questions. Track whether they resolve or multiply.

**Total questions captured (across window):** ___ questions

**Resolution status:**
| Status | Count | Examples |
|---|---|---|
| Resolved / Answered | … | … |
| Carried forward appropriate | … | … |
| Carried forward 2+ weeks | … | … |
| Not yet investigated | … | … |

**Question type distribution:**
- Scope: ___ (trend: clarifying / multiplying / resolved)
- Architecture: ___ (trend: …)
- Integration: ___ (trend: …)
- Hardware: ___ (trend: …)
- Other: ___ (trend: …)

**Interpretation:**
- Is the spike/clarification process working? (questions → answers → closure)
- Or are questions accumulating without closure mechanism?
- What should the next phase do with open questions? (spike deeper / defer / accept ambiguity?)

---

## 8. System Stability Assessment

> Overall judgment on operating environment.

**Stability rating:** 
- [ ] More stable (improving confidence in execution)
- [ ] Stable (consistent operating pattern)
- [ ] Noisy but improving (disruptions reducing)
- [ ] Noisy and persistent (unresolved friction)
- [ ] Overloaded (capacity consistently exceeded)
- [ ] Brittle (single disruption breaks iteration)
- [ ] Drifting (focus or rules not holding)

**Why this rating:**
- Evidenced by: (capacity trend / artifact production / blocker frequency / energy pattern)
- Key indicator: (which signal matters most?)

**What must be protected:**
- Operating rules that are working: (e.g., "max 2 anchors/day is holding")
- Practices that should not change: (e.g., "monday verification pass")
- Guard rails that need strengthening: (e.g., "weekend review cadence")

**System hardening needed:**
- Process tightening: (e.g., "daily DoD closure is now mandatory")
- Capacity rebalancing: (e.g., "reduce planned capacity 10% next month")
- Rules addition / reinforcement: (e.g., "escalate unresolved questions by midweek")

---

## 9. Management Implications

> Translate intelligence into next-phase decisions.

**Keep (what's working):**
- …

**Change (what needs adjustment):**
- …

**Tighten (what needs stricter discipline):**
- …

**Stop doing (what's not valuable):**
- …

**Watch closely (emerging risk or opportunity):**
- …

**For next phase planning:**
- Capacity assumption: (Full / Reduced / Limited – based on this window's evidence)
- Project emphasis: (which project needs priority / protection?)
- System changes: (what rules / structure need modification?)
- Confidence in plan: (how much confidence in committing to W14+ plans?)

---

## 10. Recommended Control Rules

> Specific operating rules extracted from this window. Should directly influence next WeekPlan or phase plan.

| Rule | Rationale | Enforcement |
|---|---|---|
| Max 2 anchors/day | … | Weekly review audit |
| [New/adjusted rule] | … | … |
| [New/adjusted rule] | … | … |

**Priority rules (must enforce next window):**
- Rule: … | Why: (capacity / clarity / focus?)
- Rule: … | Why: …

**Optional tuning (experiment if feasible):**
- Adjustment: … | Expected benefit: … | Acceptance test: …

---

## 11. Links / Trace

> Auditability: which reviews fed this analysis?

**Weekly Reviews analyzed:**
- `07_REVIEWS/03_WEEK/YYYY-Www_Review.md` — [brief context if notable]
- (repeat as needed)

**Related week plans (if comparison needed):**
- `03_PLANNING/03_WEEK/YYYY-Www_WeekPlan.md`
- (repeat as needed)

**Previous intelligence (if exists):**
- `04_LOGS/Intelligence/YYYY-Www_Intelligence.md`

**Next milestone consuming this intelligence:**
- Month review: `07_REVIEWS/02_MONTH/YYYY-MM_Review.md` (when created)
- Phase review: [link if applicable]
- Quarter review: `07_REVIEWS/01_QUARTER/YYYY-Qq_Review.md` (when created)

---

*Weekly Intelligence transforms review history into management intelligence. It is evidence-grounded, pattern-oriented, and designed to inform system and planning decisions.*
