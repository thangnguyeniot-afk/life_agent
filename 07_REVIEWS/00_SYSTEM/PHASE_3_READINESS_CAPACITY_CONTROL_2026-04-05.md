# PHASE 3 READINESS — Capacity Control (Prep Only, No Deployment)

**Date:** April 5, 2026  
**Status:** PREPARATION — No hard limits deployed yet  
**Timeline:** 2–4 weeks observation → ~May 1 readiness decision  
**Deployment Status:** 🔴 BLOCKED (pending evidence collection)

---

## CONTEXT

PHASE 1 (DONE) and PHASE 2 (Ambiguity Gate) are now active.

System is running stably with:
- Explicit DONE criteria on all tasks
- Closure discipline (no cognitive load spillover)
- Ambiguity gate preventing vague tasks from entering schedule
- Month-End Intelligence Transfer providing forward-looking context

**Next logical step:** PHASE 3 (Capacity Hard Limit) would add numeric capacity controls.

**Why not deploy now?** 
- Need real operating data to calibrate limits correctly
- Premature hard limits will either be too loose (ineffective) or too tight (counterproductive)
- Current system generates sufficient signals; need 2–4 weeks to interpret them

**This document:** Define what PHASE 3 solves, what evidence we need, and when we'll know we're ready.

---

## A. WHAT PHASE 3 IS TRYING TO SOLVE

### Problem 1: Overload Days (Silent Failure)

**Current symptom:** Some days feel overloaded, but the feeling isn't formalized. Operator pushes through. No clear trigger for "this day is too much."

**What PHASE 3 addresses:**
- Formalize what "overload" means numerically
- Create a visible boundary (e.g., "max 3M tasks" or "max 2 high-ambiguity items")
- Stop attempting days that exceed boundary before they happen (not after)

**Current state:** Manual operator awareness → reactive ("I'm overloaded now")  
**PHASE 3 goal:** Formalized boundary → proactive ("this plan would overload; adjust scope")

---

### Problem 2: Unrealistic Planning

**Current symptom:** Weekly plan sometimes stretches capacity. March showed: plan assumed 70% Zephyr + 30% personal, actual was more like 60/15/15 with 10% to system work. The mismatch happened because of hidden assumptions.

**What PHASE 3 addresses:**
- Use real capacity data to set planning conservative defaults
- Make planning capacity assumptions explicit in WeekPlan (not implicit)
- Catch overcommit at planning time (not execution time)

**Current state:** Planning by feel + operator experience  
**PHASE 3 goal:** Planning by measured capacity + explicit allocation logic

---

### Problem 3: Hidden Load Inflation

**Current symptom:** Evening work load silently creeps up. Without measurement, doesn't become visible until energy crashes.

**What PHASE 3 addresses:**
- Surface evening load trending
- Create a "heavy evening" warning if pattern gets out of bounds
- Prevent silent accumulation with visible tracking

**Current state:** Pattern observed monthly in retrospective  
**PHASE 3 goal:** Pattern visible weekly (interventable)

---

### Problem 4: Ambiguity Stacking

**Current symptom:** Days with multiple high-ambiguity items feel different from days with same task count but all clear tasks. No distinction.

**What PHASE 3 addresses:**
- Measure whether ambiguity consumes capacity separately from task count
- Set rules like "max 1 high-ambiguity item per day" or similar
- Prevent days where operator gets confused by too many unknowns

**Current state:** Ambiguity prevented at gate; unknown if multiple ambiguities can coexist  
**PHASE 3 goal:** Ambiguity load measured and potentially controlled

---

## B. WHAT EVIDENCE WE NEED BEFORE ROLLOUT

### Evidence Set 1: Real Capacity Data (By Mid-April)

**What we need:**
- 2 full weeks of execution (April 7–20)
- Daily records showing: blocks completed, tasks done, evening work reality, energy level
- Weekly summaries showing: planned vs. actual, blockers, capacity trend

**How to collect:**
- Business as usual (use existing Daily / Weekly templates)
- Tally at week-end: "On average, how many meaningful tasks per day?"
- Tally at week-end: "How many days felt realistically paced vs. overloaded?"

**Questions to answer:**
- What is the average task-completion rate per day? (e.g., 3–5 tasks, or 1–2 blocks)
- What is the distribution? (do all days have similar load, or does it vary a lot?)
- When does a day feel overloaded? (operator observation)

---

### Evidence Set 2: Overload Pattern Recognition (By Late April)

**What we need:**
- Examples of "normal days" (operator felt good pace)
- Examples of "overloaded days" (operator felt too much)
- Root cause breakdown: What caused overload? (task count? ambiguity? time pressure? energy level?)

**How to collect:**
- At end of each week, operator flags 1–2 "good pace" days and 1–2 "overloaded" days
- Note what was different (e.g., "overloaded day had 5 tasks + 2 high-ambiguity items + 3 interruptions")
- Aggregate pattern

**Questions to answer:**
- Is overload driven more by task count, ambiguity, or time of day?
- Are weekdays meaningfully different from weekends?
- What's the earliest-warning signal of oncoming overload? (e.g., energy drop, or too many ambiguities at start of day?)

---

### Evidence Set 3: Ambiguity Gate Effectiveness (By Early May)

**What we need:**
- Count of how many tasks needed UNBLOCK TASKS (ambiguity gate converted them)
- Did tasks that passed the gate execute cleanly?
- Did UNBLOCK TASKS actually resolve ambiguity?

**How to collect:**
- Weekly planning: Count "gate-flagged → UNBLOCK TASK conversions"
- Weekly wrap-up: Note any vague tasks that still slipped through despite gate
- Monthly review: Aggregate pattern

**Questions to answer:**
- Is the ambiguity gate working? (preventing vague task entry? yes/no)
- Does high ambiguity + clear task count have measurable impact on execution? (do days with 2 clear tasks + 1 high-ambiguity item feel different from days with 3 clear tasks?)

---

### Evidence Set 4: Fatigue & Recovery Signals (By Early May)

**What we need:**
- Pattern of energy level (daily notes: Low/Normal/High)
- Connection between evening workload and next-day energy
- Recovery rate after heavy weeks

**How to collect:**
- Daily: Log energy level (already done in Current Energy Context)
- Weekly: Note if evening work on day N caused energy drop on day N+1
- Monthly: Any patterns between week load and next week energy?

**Questions to answer:**
- Does evening work on busy days noticeably reduce next-day energy?
- How long does capacity recovery take after an overloaded day/week?
- Is there a sustainable evening work level? (e.g., "1×S ok, 1×M ok, but both together ruins next day")

---

### Evidence Set 5: Failure Mode Breakdown (By Early May)

**What we need:**
- When execution stalls or tasks incomplete, categorize the reason
- Is it planning (unrealistic plan)? or execution (unexpected blocker)?
- Is it fatigue? Ambiguity? External interruption?

**How to collect:**
- Weekly Review § 9 "What Worked/What Didn't" — when noting failures, briefly categorize reason
- Monthly Review — aggregate failure patterns

**Questions to answer:**
- Which failure modes are most common? (planning too aggressive? execution hits unknown? energy crash?)
- Could PHASE 3 hard limits have prevented the failure?

---

## C. OBSERVATION PLAN (April 5 – May 5)

### Week 1 (April 7–13): Baseline Collection
- Operators run normal weeks using existing templates
- At week-end: tally capacity data (blocks, tasks, evening work)
- At week-end: flag 1–2 "good" and 1–2 "overloaded" days

### Week 2 (April 14–20): Pattern Confirmation
- Continue normal operation
- Track ambiguity gate usage (how many UNBLOCK TASKS created?)
- At week-end: aggregate; compare to week 1

### Week 3 (April 21–27): Fatigue Tracking
- Normal operation
- Pay attention to energy level + evening work correlation
- At week-end: note recovery rate after hard days

### Week 4 (April 28–May 4): Failure Mode Audit
- Normal operation
- When tasks don't complete or days feel off, briefly capture why
- At week-end: categorize failure modes

### Checkpoint (May 1–5): Analysis & Readiness Decision
- Aggregate all four weeks of evidence
- Answer the five "Questions to Answer" above
- Decide: Ready for PHASE 3? Or need more data?

---

## D. QUESTIONS PHASE 3 MUST ANSWER (Before Rollout)

### Design Question 1: What is the correct overload boundary?

**Current hypothesis:** 3M-sized tasks is a reasonable max per day  
**To test:** Is 3M accurate? Should it be 2M + 2S? Or 4M only on high-energy days?  
**Data needed:** Evidence Set 1 (real task completion) + Evidence Set 2 (overload markers)

---

### Design Question 2: Does ambiguity count separately from task count?

**Current hypothesis:** Yes, probably (intuitive: high-ambiguity work feels harder)  
**To test:** Do days with 2 clear tasks + 1 high-ambiguity feel same as days with 3 clear tasks?  
**Data needed:** Evidence Set 3 (ambiguity gate usage) + Evidence Set 2 (subjective overload rating)

**If YES:** PHASE 3 needs rule like "max 1 high-ambiguity item + 2 clear items"  
**If NO:** Task count is the only metric; ambiguity is pre-filtered by gate

---

### Design Question 3: Are weekdays and weekends meaningfully different?

**Current hypothesis:** Yes (weekday = Zephyr time only, constrained; weekend = flexible)  
**To test:** Do weekend days support higher capacity than weekday evenings?  
**Data needed:** Evidence Set 1 (weekday vs. weekend completion rates)

---

### Design Question 4: Is evening load fatigue-coupled to next day?

**Current hypothesis:** Yes (evening work on day N affects day N+1 energy)  
**To test:** When evening load is high, does next day feel noticeably different?  
**Data needed:** Evidence Set 4 (energy tracking + evening work patterns)

**If YES:** PHASE 3 needs lookahead rule (don't stack heavy evening + next heavy day)  
**If NO:** Evening load is independent; can be aggressive

---

### Design Question 5: Which failure modes could PHASE 3 prevent?

**Current hypothesis:** Planning overcommit (PHASE 3 catches at plan time) and ambiguity pile-up (high-ambiguity rule)  
**To test:** Audit real failures; categorize; see which would have been caught by hard limits  
**Data needed:** Evidence Set 5 (failure mode breakdown)

---

## E. ROLLOUT TRIGGER CRITERIA

PHASE 3 is ready to deploy only if ALL criteria are met:

- [ ] 2–4 weeks of stable capacity data collected (Evidence Set 1 available)
- [ ] Overload patterns identified with 3+ examples of each type (Evidence Set 2 available)
- [ ] Ambiguity gate effectiveness confirmed: vague tasks prevented, UNBLOCK Tasks effective (Evidence Set 3 available)
- [ ] Energy/fatigue correlation understood (Evidence Set 4 available, even if inconclusive)
- [ ] Failure modes analyzed; clear which could be prevented by hard limits (Evidence Set 5 available)
- [ ] Numeric thresholds can be proposed (e.g., "3M is sustainable" or "1 high-ambiguity per day")
- [ ] No contradictions between hypothesis and data (if data suggests different thresholds, adjust hypothesis)
- [ ] System is stable (PHASE 1 & 2 working; new rules won't be added during PHASE 3 rollout)

**If ANY criterion is not met:** Continue observation; propose more targeted data collection; defer PHASE 3 to next cycle.

---

## F. FUTURE DESIGN INPUTS (To Be Decided During PHASE 3 Design, Not Now)

The following decisions WILL be made during PHASE 3 formal design phase (after evidence collection), not now:

- ❓ **Task unit definition:** S/M/L or another system?
- ❓ **Daily load cap logic:** "Max 3M" or "Max 1M + 2S + 1 high-ambiguity"?
- ❓ **Weekday vs. weekend rules:** Different caps? Different ambiguity rules?
- ❓ **Evening capacity coupling:** Lookahead rule needed? If so, how aggressive?
- ❓ **Fatigue recovery rule:** After overload, mandatory light day? Or just tracking?
- ❓ **Integration with Ambiguity Gate:** Should Ambiguity Gate + Capacity Control rules be unified?
- ❓ **Enforcement timing:** At planning time? Execution time? Both?
- ❓ **Breathing room:** Should PHASE 3 cap be 85% of measured max capacity (to allow for unknowns)?

**All of these will be answered by the evidence, not by assumption.**

---

## G. WHAT PHASE 3 WILL NOT DO (Clear Boundaries)

❌ **Will NOT:** Replace operator judgment  
→ Operator still owns "is this a high-ambiguity task?" or "did I overcommit?"  
→ Hard limits are guardrails, not autopilot

❌ **Will NOT:** Change the existing gates (Review Exit, Plan Intake, Ambiguity)  
→ Those stay as-is  
→ PHASE 3 adds a new capacity check, doesn't modify existing ones

❌ **Will NOT:** Force a specific task unit system until evidence suggests one  
→ Current system (blocks, tasks, anchors) works; PHASE 3 just adds sizing

❌ **Will NOT:** Add complexity if simpler rule works  
→ If "max 3M" prevents overload, use that; don't invent scoring systems

---

## H. CHECKPOINT PLAN (Timeline)

| Date | Action | Decision |
|---|---|---|
| **Apr 5** | Prep complete (this document) | PHASE 3 ready for observation prep |
| **Apr 13** | Week 1 checkpoint | Continue observation; data collecting normally |
| **Apr 20** | Week 2 checkpoint | Continue observation; patterns emerging? |
| **Apr 27** | Week 3 checkpoint | Continue observation; any surprises? |
| **May 1–5** | Final evidence review | **READY/NOT READY decision** |
| **If READY:** May 6+ | Formal PHASE 3 design | Use evidence to build rules |
| **If NOT READY:** May + | Extended observation | Identify what's still missing |

---

## I. SUMMARY: WHAT THIS PREP ACCOMPLISHES

✅ **Defines the problem:** PHASE 3 solves overload/unrealistic planning/ambiguity piling/fatigue (not vague problems)

✅ **Specifies evidence needed:** 5 specific evidence sets that answer capacity questions

✅ **Prevents premature deployment:** Clear "no" criteria; won't deploy until evidence says "yes"

✅ **Makes rollout repeatable:** Future PHASE 3 deployments can use same evidence framework

✅ **Keeps current system stable:** No changes to Daily/Weekly/Monthly; just observation

✅ **Defines future work:** Clear inputs for formal PHASE 3 design (after evidence arrives)

---

## NEXT STEPS

1. **April 5–6:** Share this readiness document with operators
2. **April 7:** Begin normal execution; collect data using existing templates
3. **Weekly:** At week-end, capture "overload vs. normal" observations
4. **May 1:** Review evidence; decide PHASE 3 readiness
5. **If ready:** Begin formal PHASE 3 design using data
6. **If not ready:** Identify additional evidence needed; extend collection

---

**Preparation Status:** ✅ COMPLETE  
**Deployment Status:** 🔴 BLOCKED (waiting for evidence)  
**Next Review:** May 1, 2026 (readiness checkpoint)

