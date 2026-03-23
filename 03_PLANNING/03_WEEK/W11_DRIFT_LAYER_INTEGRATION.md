# Drift Detection Layer Integration Summary

**Phase:** Phase 4 (Drift Detection Layer Design & Integration)  
**Date:** 2026-03-21 (post-phase 3 hardening)  
**Scope:** Added operational drift detection to GENERATE_WEEKLY_EXECUTION.md + 2026-W11_Execution.md  
**Status:** ✅ Complete — Ready for live daily execution tracking  

---

## 1. What is the Drift Detection Layer?

**Problem:** The hardened 7-layer system was strong structurally but behaved as a planning/control document only. It couldn't detect when execution diverged from plan **during the week** — only post-mortem at Sunday review.

**Solution:** An operational layer that sits alongside existing structure and answers three questions **in real time (daily):**
1. Is execution on-track? (GREEN)
2. Is execution slipping but recoverable? (YELLOW)
3. Is critical path threatened? (ORANGE/RED)

**Design Principle:** Lightweight (5-minute daily check), not bureaucratic. Operational signals, not aspirational scoring.

---

## 2. Six Categories of Drift (Definitions)

| Drift Type | Definition | Observable Signal | Example |
|---|---|---|---|
| **Schedule Drift** | Planned anchor not started in intended window OR extends beyond plan | Did it start on time? | Mon M1 not started by 8:30 |
| **Dependency Drift** | Upstream anchor slipped; downstream no longer valid/blocked | Is upstream artifact at expected completion? | Tue M2 blocked because Mon M1 architecture still unclear |
| **Artifact Drift** | Time spent but visible artifact not produced | Artifact exists? | 4 hours on M2, but no PR draft = artifact drift |
| **Clarity Drift** | Repeated motion on same anchor without reducing ambiguity | Did ambiguity reduce? Or stayed same/increased? | Touched M2 twice, ambiguity still 3/5 →clarity drift |
| **Load Drift** | Contingent work absorbed into committed (week becomes overloaded invisibly) | Is contingent pre-executing before prerequisite? | Thu RAM already started before Wed dline complete |
| **Attention Drift** | Time diverted into uncontrolled research, side work, hidden third scope | Protected scope preserved? | Office time consumed by unplanned Zephyr support |

---

## 3. Drift Signals (7-Signal Schema)

Every major daily anchor defines these signals (checked EOD, ~5 min):

| Signal | Question | Observable? | Y/N/Increased |
|---|---|---|---|
| **Started on time?** | Did anchor begin in intended window? | YES (timestamp check) | Y/N |
| **Blocker in first 15p?** | Did fallback trigger? | YES (fallback used or not) | Y/N |
| **Artifact produced?** | Does visible output exist? | YES (file, PR, log, note) | Y/N |
| **Ambiguity reduced?** | Are unknowns smaller than morning? | SOMETIMES (compare morning → EOD) | Yes/No/Increased |
| **Fallback used?** | Did primary path fail? | YES (binary: used or not) | Y/N |
| **Protected scope preserved?** | Critical items still on track? | YES (hard-gate days only) | Y/N |
| **Contingent held?** | Not absorbed into committed? | YES (on dependent days) | Y/N |

**Collection:** Once per day EOD for each primary anchor. Optional midday check if blocker suspected.

---

## 4. Drift States & Triggers (GREEN/YELLOW/ORANGE/RED)

| State | Count of Signals Off | Hard Gate Threat? | Allowed Action | Forbidden Action |
|---|---|---|---|---|
| **GREEN** | 0–1 off | NO | Continue execution as planned | Relax vigilance; skip checks |
| **YELLOW** | 2 signals off | NO | Use fallback; adjust daily plan; flag EOD | Ignore signal; hide issue |
| **ORANGE** | 3+ signals off | YES ⚠️ | De-escalate work; protect hard gate; escalate to Agent 1 | Continue business-as-usual; ignore threat |
| **RED** | Hard gate failed OR week intent broken | CRITICAL | Full replan required; trigger WEEKLY_REBALANCE | Continue executing old plan |

---

## 5. Response Rules (Prescribed Actions Per Drift Type)

**If Schedule Drift (not started on time):**
- Midday: Assess why (blocker vs priority shift)
- Within 2h: Switch fallback if blocker; escalate if priority shift
- Log: Reason + fallback activated (Y/N)

**If Artifact Drift (time spent, no artifact):**
- Force stop anchor
- Create "Residue Note": what was done, what's blocking, what's next
- Log: Residue state as acceptable partial progress
- Status: YELLOW (partial) or ORANGE (if hard gate artifact missing)

**If Clarity Drift (ambiguity unchanged after 2 touches):**
- Stop execution immediately
- Convert to decision point: "What clarification is needed?"
- Escalate question (don't continue spinning)
- Status: YELLOW→ORANGE if Ambiguity ≥3

**If Dependency Drift (upstream slipped):**
- Check downstream validity vs upstream artifact state
- Contingent dependencies: prepare to drop downstream
- Independent dependencies: proceed, note drift
- Protected scope rule: protect hard gate first
- Status: YELLOW or ORANGE depending on hard-gate threat

**If Load Drift (contingent absorbed):**
- Audit daily hours: separate contingent from committed
- If contingent >30% of committed: ORANGE status
- Do NOT pre-execute contingent
- Status: ORANGE (force drop)

**If Hard Gate Day Threatened (Wed dline):**
1. **Tier 1 (Early):** Architecture unclear by Tue EOD → escalate
2. **Tier 2 (Hard):** PR not open by Wed noon → escalate (don't wait EOD)
3. **Tier 3 (Critical):** PR not open by Wed EOD → immediate escalation; W12 impact

---

## 6. Daily Integration (What Daily File Inherits)

**From Weekly file, each daily anchor inherits:**
- Primary artifact target (concrete)
- Expected drift signals to measure
- Fallback anchor if primary blocks
- Protected scope marking (if hard-gate day)
- Contingent status (if dependent on prior day)
- Override rule (if upstream cascade)

**Daily file checks (EOD, ~5 min):**
- All 7 signals measured and logged
- State assigned: GREEN/YELLOW/ORANGE/RED
- If state changed or is YELLOW/ORANGE: reason noted in Weekly Drift Log
- Hard-gate days: signals doubly verified

---

## 7. Implementation in GENERATE_WEEKLY_EXECUTION.md

**Changes Made:**

1. **§11.5 NEW SECTION: "Drift Detection Layer: Design & Integration"** (~500 lines)
   - Drift Definition (6 categories + observable criteria)
   - Drift Signals (7-signal schema per anchor)
   - Drift States (GREEN/YELLOW/ORANGE/RED with triggers)
   - Drift Responses (prescribed actions per drift type)
   - Daily Integration (what daily inherits + what to check)
   - Drift File Structure (template for weekly file structure)

2. **Gate 6 NEW: "Drift Detectability QA"** (adds to QA gates)
   - Validates: signals are measurable + fallbacks operational + hard gates protected + responses defined
   - Ensures: user can detect fake progress vs real movement
   - Checks: weekly overload visibility

3. **Renamed Prior Gate 6 → Gate 7:** "Language QA (No Narrative Bloat)"

4. **PHASE 11 NEW:** "Drift Detection Layer Integrated" (in 12-phase checklist)
   - Drift definition, signals, states, response rules, daily inheritance, hard gate protection, drift log
   - Checklist items for each requirement

5. **PHASE 12 (RENAMED):** "Seven Operational Layers Present" (was PHASE 11)

6. **Checklist Updated:** From "11-Phase" to "12-Phase" framework throughout

**Result:** Generator now supports and validates drift detection in all weekly files.

---

## 8. Implementation in 2026-W11_Execution.md

**New Section 11: "Execution Drift Detection Layer"** (~150 lines)

**Subsections:**

1. **Drift Signals Defined (Per Day)** — Table showing:
   - Day | Anchor | Hard Gate? | Status Signal | Artifact Signal | Ambiguity Signal | Protected Scope
   - All W11 anchors (Mon M1, Tue M2, Wed M2→M3, Thu M4, etc.) with specific signal expectations

2. **Drift Response Rules (Quick Reference for Daily Use)** — Action cards:
   - If started late → escalate same-day
   - If blocker in first 15p → switch fallback + check cascade
   - If no artifact → force stop + residue note
   - If ambiguity unchanged → stop execution, escalate Q&A
   - If contingent absorbed → drop
   - If Wed dline threatened → PROTECT (3-tier escalation logic)

3. **Weekly Drift Log (Track Daily)** — Empty tracking table with columns:
   - Day | Anchor | Signal | State | Action Taken | Notes | Carry-to-W12

4. **Hard Gate Protection Rules (Wed Dline)** — Explicit:
   - Protect first: dline logic + PR + tests
   - Drop first: Thu RAM expansion, evening polish, Signee polish
   - Never compromise: Wed hard gate is non-negotiable
   - Escalation: By Tue EOD if unclear; Wed noon if not on track; Wed 17:00 if failed

**Coverage:** All W11 critical paths (Mon→Wed hard gate + Thu contingent + evening/weekend independent work) explicitly mapped for drift tracking.

---

## 9. How to Use Daily (3-Minute Protocol)

**Every day EOD (takes ~5 min, not heavy):**

1. **Open Weekly Drift Log section** (from weekly execution file)
2. **For each primary anchor today:**
   - Check signal 1 (started on time?) → Y/N
   - Check signal 2 (blocker?) → Y/N
   - Check signal 3 (artifact exists?) → Y/N
   - Check signal 4 (ambiguity reduced?) → Yes/No/Increased
   - Check signal 5 (fallback used?) → Y/N
   - If hard gate day: check signal 6 (protected scope?) → Y/N
   - If dependent day: check signal 7 (contingent held?) → Y/N
3. **Count signals off** (0–1 off = GREEN; 2 off = YELLOW; 3+ off = ORANGE; hard gate failed = RED)
4. **Assign state**
5. **If YELLOW/ORANGE:** Note reason in Drift Log
6. **If ORANGE on hard-gate chain:** Escalate same-day (don't wait)
7. **Log complete.** (This replaces guessing; you now have objective data)

**Weekly Review (5 min at week-end):**
- Scan Drift Log for patterns (repeated blockers? ambiguity stacks? load creep?)
- Did override rules activate as expected?
- Lessons for next week's design

---

## 10. Integration Points (Where Drift Layer Connects)

| Integration Point | Connection |
|---|---|
| **Weekly Generator (§11.5)** | Drift layer is part of generator; new 12-phase checklist validates drift detectability |
| **Daily Inheritance Contract** | Daily files inherit drift signals + expected measurement points from weekly |
| **QA Gates (Gate 6)** | Drift Detectability QA ensures weekly file supports drift detection |
| **Hard-Gate Protection** | Wed dline (and other critical anchors) have explicit drift thresholds + escalation triggers |
| **Override Rules** | If upstream drifts, override logic kicks in (drop contingent, protect critical path, escalate) |
| **Weekly Rebalance (Mode C)** | If RED state reached (week intent broken), trigger WEEKLY_REBALANCE instead of continuing |
| **Dependency Chain (§5.5)** | Override table now references drift response rules (if upstream slips by 50%, activate override) |

---

## 11. What This Protects Against (Gaming Resistance)

**Before Drift Layer:** 
- Week plans looked good on paper, but execution diverged invisibly until Sunday review ("Oh, we found out Wed the architecture was wrong")
- No early warning system
- No prescribed response to blockers/delays (ad-hoc reactions)
- Hard gates could be squeezed without detection

**After Drift Layer:**
- Tue/Wed: operator and Agent 1 can see real-time divergence
- Signals are objective (started on time? binary) not subjective (working hard? ambiguous)
- Every drift type has a prescribed response (not guessing)
- Hard gates are protected by escalation thresholds (Wed noon check, not just EOD)
- Weekly Rebalance can be triggered early (not by Sunday surprise)

---

## 12. Files Modified (Clean Audit)

| File | Section | Change | Lines Added | Purpose |
|---|---|---|---|---|
| GENERATE_WEEKLY_EXECUTION.md | TOC | Added §11.5 reference | 1 | Navigation |
| GENERATE_WEEKLY_EXECUTION.md | §11.5 NEW | Full drift layer spec (definitions, signals, states, responses, integration) | ~500 | Operational specification |
| GENERATE_WEEKLY_EXECUTION.md | §14 Gates | Gate 6 NEW (Drift Detectability QA) | ~35 | Validation |
| GENERATE_WEEKLY_EXECUTION.md | §14 Gates | Gate 7 renamed (was Gate 6: Language QA) | 0 | Renumbering |
| GENERATE_WEEKLY_EXECUTION.md | §15 Checklist | PHASE 11 NEW (Drift Detection) + PHASE 12 renamed | ~10 | QA phase structure |
| GENERATE_WEEKLY_EXECUTION.md | §15 Checklist | "11-Phase" → "12-Phase" throughout | 5 | Consistency |
| 2026-W11_Execution.md | TOC | Added §11 reference | 1 | Navigation |
| 2026-W11_Execution.md | §11 NEW | Drift signals table + response rules + drift log + hard-gate protection | ~150 | Live example |
| 2026-W11_Execution.md | §10 Report | Phase count updated 11→12 | 2 | Consistency |
| NEW FILE | W11_DRIFT_LAYER_INTEGRATION.md | — | ~350 | This document |

**Total additions:** ~600 lines across generator + W11 example (generator is now ~1700 lines; W11 is now ~500 lines)

---

## 13. Pre-Execution Validation Checklist

Before using drift layer in live W11 execution:

- [ ] Drift signals for each major anchor are concrete (not vague)
- [ ] Fallback anchors are documented (not "adapt as needed")
- [ ] Hard-gate day (Wed) has explicit protect/drop rules
- [ ] Drift responses cover all 6 drift types
- [ ] Daily inheritance includes signal-checking points
- [ ] Drift Log table exists in weekly file (even if empty)
- [ ] Escalation thresholds are specific (not "if needed": by Tue EOD, by Wed noon, by Wed EOD)
- [ ] Operator understands 5-minute EOD signal protocol
- [ ] Agent 1 knows escalation triggers for hard-gate days

**If any fails:** Review §11.5 of generator or §11 of W11 example to fill gap before week starts.

---

## 14. Success Criteria (How to Know Drift Layer Is Working)

**Week executing well if:**
- ✅ Wed noon: operator can say "dline PR status: on track (GREEN) / at risk (YELLOW) / threatened (ORANGE)" objectively
- ✅ Tue EOD: any architectural uncertainty is logged + escalation decision made (not hidden until Wed)
- ✅ Thu: can distinguish "Thu contingent is clean (Wed done, Thu proceeds GREEN)" from "Thu contingent cancelled (Wed slipped, ORANGE)"
- ✅ Any YELLOW state has corresponding action logged (fallback used? escalated? reworked?)
- ✅ Wed hard gate: either opened by EOD (success) or RED state triggered (replan initiated) — no fuzzy middle

**If this feels like too much data:** It's not. You're replacing guessing ("hope Wed works out") with objective tracking ("Wed status is GREEN/YELLOW/ORANGE based on signals"). The 5-minute EOD check is faster than scrolling email trying to remember what happened.

---

## 15. Next Steps (Post-Integration)

1. **W11 Live Execution:** Use §11 Drift signals to track daily execution (Tue–Thu critical path)
2. **Execution Diary:** Record Drift Log entries EOD (becomes artifact for W11 review)
3. **Wed Noon Checkpoint:** Check hard-gate signals; if ORANGE, escalate immediately
4. **W12 Planning:** Use W11 Drift Log patterns to inform W12 generation (what blockers repeat? what signals predicted slips?)
5. **Generator Usage:** Future weeks use updated 12-phase generator with Drift QA built-in

---

## Summary

**Drift Detection Layer = control layer sitting on top of existing 7-layer + 5-gate system.**

- Defines 6 types of drift (observable + actionable)
- Uses 7-signal schema per daily anchor (concrete, not aspirational)
- Maps drift to response rules (prescribed actions per drift type)
- Integrates with daily inheritance (signals are checked daily, not post-hoc)
- Protects hard gates (Wed dline cannot be squeezed without escalation)
- Enables 3-minute daily check (not heavy bureaucracy)

**In W11:** Drift signals track Mon M1 → Tue M2 → Wed PR hard gate  + Thu contingent + evening/weekend independent work. Early warning system active by Tue/Wed.

**In generator:** New §11.5 + Gate 6 + PHASE 11 mean all future weekly files support drift detection; checklist validates detectability before file is ready.

---

**Phase 4 complete. Drift Detection Layer integrated and ready for live execution.**
