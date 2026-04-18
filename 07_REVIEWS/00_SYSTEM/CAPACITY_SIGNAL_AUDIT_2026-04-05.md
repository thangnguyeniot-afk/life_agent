# CAPACITY SIGNAL AUDIT — What's Already Being Captured

**Date:** April 5, 2026  
**Scope:** What is already visible in Daily, Weekly, and Monthly review structures  
**Purpose:** Foundation for PHASE 3 readiness planning

---

## ALREADY CAPTURED — High Quality Data

### Daily Level

✅ **Energy level** (Low/Normal/High)  
- Template field: Context § Energy level  
- Frequency: Every execution day  
- Quality: Manual observation (operator-reported)

✅ **Anchor count** (how many projects today)  
- Template field: Daily Project Scope Rule § "max 2 active projects"  
- Frequency: Every day (violates rule if >2); violations noted in Signals  
- Quality: Structural count (observable fact)

✅ **Evening work reality** (actual capacity vs. plan)  
- Template field: Evening block completion  
- Frequency: Every day with evening work  
- Quality: Artifact-based (completed or not)

✅ **Work completion** (started vs. finished)  
- Template field: Shutdown § DoD checkboxes  
- Frequency: Daily  
- Quality: High (explicit closure or spillover notation)

✅ **Daily signals** (what went wrong/right)  
- Template field: Signals section  
- Frequency: Daily  
- Quality: Operator judgment (free text)

✅ **Re-entry clarity** (is next-step obvious?)  
- Template field: Shutdown/unfinished work section  
- Frequency: When work doesn't complete  
- Quality: High (explicit re-entry package required)

---

### Weekly Level

✅ **Planned vs. Actual outcome movement**  
- Template field: Weekly Review § 4 (Planned vs Actual)  
- Frequency: Every week  
- Quality: High (measured against weekly outcomes, not task count)

✅ **Unplanned work absorbed** (%)  
- Template field: Weekly Review § 8 Capacity Review  
- Frequency: Every week  
- Quality: Operator estimate  
- Data available: Week 09–12 March shows ~10% KTLO absorbed consistently

✅ **Context switches** (significant ones)  
- Template field: Weekly Review § 8 Capacity Review  
- Frequency: Every week  
- Quality: Operator judgment (high/moderate/low)

✅ **Energy trend** (week pattern)  
- Template field: Weekly Review § 8 Capacity Review  
- Frequency: Every week  
- Options: Low overall / Stable / Peaked early / Peaked mid-week / Inconsistent

✅ **Main source of drag** (capacity killer)  
- Template field: Weekly Review § 8 Capacity Review  
- Frequency: Every week  
- Quality: Free-text analysis

✅ **Week classification** (Stable/Noisy/Blocked/Recovery/etc.)  
- Template field: Weekly Review § 2  
- Frequency: Every week  
- Quality: Operator judgment tag

✅ **Blocker/Risk/Signal logs**  
- Template field: Weekly Review § 7  
- Frequency: As they arise  
- Quality: Structured list

---

### Monthly Level

✅ **Capacity reality measurement**  
- Template field: Monthly Review § 2.1 Drift Check (Portfolio Balance)  
- Data from March: "3–4 blocks sustained; 5 blocks viable 2–3x/week"  
- Quality: Aggregated over full month from weekly data

✅ **Evening capacity pattern**  
- Template field: Monthly Review § 5 Anti-Anchors  
- Data from March: Pattern = "1.5–2h realistic; 2.5h risky"  
- Quality: Monthly pattern identification

✅ **Repeated friction patterns**  
- Template field: Monthly Review § 5 Anti-Anchors  
- Examples from March: Evening overcommit, restart friction (solved), task ambiguity (prevented)  
- Quality: Pattern trend over month

✅ **Carry-over work validation**  
- Template field: Monthly Review § 2.1 Drift Check  
- Data: "No carry-over debt; re-entry packages clear"  
- Quality: Binary (debt present or absent)

✅ **Human advisory signals** (optional Q2 pilot)  
- Template field: Monthly Review § 3.5  
- Data: "Sleep 7h+ = high energy; 5–6h = fade"  
- Quality: Correlation pattern (not causal)

---

## ALREADY CAPTURED — Medium Quality Data

⚠️ **Task ambiguity surface** (from Ambiguity Gate usage)  
- Where captured: Weekly planning (gate applied), Daily planning (gate applied)  
- Frequency: Every task entering schedule since PHASE 2  
- Quality: Gate prevents vague tasks; not all get explicitly tagged as "resolved" or "high-ambiguity"
- What exists: Knowledge that gate was applied; what's missing: count of how many tasks needed UNBLOCK TASKS

⚠️ **Task count per day** (number of completed tasks)  
- Where captured: Daily Shutdown (lists what was done)  
- Frequency: Daily  
- Quality: Implicit (artifacts listed, not aggregated as count)
- What exists: Individual day records; what's missing: weekly/monthly aggregation of task count

⚠️ **Deep work block actual time** (did blocks go 90 min as planned?)  
- Where captured: Daily file signals, not templated  
- Frequency: When blocks run short/long, operator notes it  
- Quality: Manual observation (not standardized)

⚠️ **System change adoption** (when new rules deployed, did they stick?)  
- Where captured: Monthly Review § 3 System Change Review  
- Data from March: Daily Scope Rule implemented; lived experience became clear by W09  
- Quality: Retrospective observation (not predictive)

---

## MISSING OR INVISIBLE — What PHASE 3 Will Need

❌ **Daily overload boundary** (at what point is a day "overloaded"?)  
- Currently: Operator knows it when it happens; no numeric trigger  
- Formalized: Unknown (S/M/L task mix? Time? Ambiguity load? Energy used?)
- Evidence needed: Examples of "normal days" vs. "overloaded days" to identify boundary

❌ **Task unit consistency** (what is "1 task"? S/M/L definitions)  
- Currently: Mixed (some counted as "block", some as "task", some as "component")  
- Formalized: Not yet  
- Evidence needed: Working backward from real execution data to define meaningful units

❌ **Ambiguity as load** (does high-ambiguity work consume capacity differently?)  
- Currently: Assumed (high ambiguity = harder), not measured  
- Formalized: Not yet  
- Evidence needed: Do 3 clear tasks have same impact as 1 high-ambiguity task?

❌ **Weekday vs. weekend capacity** (are they meaningfully different?)  
- Currently: Assumed different (weekday = Zephyr + evening, weekend = personal)  
- Formalized: Not yet  
- Evidence needed: Do weekday blocks feel different from weekend blocks? Load distribution?

❌ **Evening fatigue coupling** (does evening work on day N affect capacity on day N+1?)  
- Currently: Observed anecdotally (spillover happens; energy fade happens)  
- Formalized: Not yet  
- Evidence needed: Which patterns of evening work cause next-day energy drop?

❌ **When capacity fails** (is it at planning time or execution time?)  
- Currently: Both observed (plan too aggressive; execution hits surprise)  
- Formalized: Split not clear  
- Evidence needed: Breakdown of failure modes (planning vs. execution)

❌ **Recovery time** (how long does capacity bounce back after overload?)  
- Currently: Not tracked  
- Formalized: Not yet  
- Evidence needed: Pattern of recovery days after hard weeks

---

## SUMMARY: CAPACITY SIGNAL COVERAGE

| Category | Available Now | Quality | Gap for PHASE 3 |
|---|---|---|---|
| **Block count / day** | ✅ YES | High | No |
| **Energy pattern** | ✅ YES | High | No |
| **Evening capacity reality** | ✅ YES | High | No |
| **Unplanned work % / week** | ✅ YES | Medium | Scale to daily |
| **Work completion rate** | ✅ YES | High | Quantify as tasks/day |
| **Friction patterns** | ✅ YES | Medium | Define severity threshold |
| **Overload boundary** | ❌ NO | N/A | **PHASE 3 must identify** |
| **Task unit definition** | ⚠️ PARTIAL | Low | **PHASE 3 must define** |
| **Ambiguity impact** | ⚠️ PARTIAL | Low | **PHASE 3 must measure** |
| **Weekday/weekend split** | ⚠️ PARTIAL | Low | **PHASE 3 must analyze** |
| **Fatigue coupling** | ❌ NO | N/A | **PHASE 3 must track** |
| **Failure mode breakdown** | ⚠️ PARTIAL | Low | **PHASE 3 must categorize** |

---

## RECOMMENDATION

**Current capacity data is sufficient to begin 2-week observation period** with minimal additions.

No template changes needed immediately. Instead:
- Operators continue existing daily/weekly/monthly review practices
- Observation phase collects real data against existing templates
- After 2–4 weeks, re-audit what additional tracking is needed for PHASE 3 design

