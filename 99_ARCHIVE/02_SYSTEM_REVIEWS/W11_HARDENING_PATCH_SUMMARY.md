# W11 Hardening Patch Summary

**Date:** March 21, 2026  
**Scope:** Surgical patches to generator + W11 instance (NOT full rewrite)  
**Status:** ✅ COMPLETE

---

## Patches Applied

### A. AMBIGUITY RULE PATCH

**Problem:** System was artificially compressing all mission ambiguity to ≤2, creating fake clarity.

**Fix (Generator):**
- Replaced "all missions Ambiguity ≤2" with honest scoring: 0–5 range
- 0–2: standard execution (any energy day)
- 3: moderate uncertainty, allowed ONLY on high-energy days (Tue) + must have explicit escalation note
- ≥4: SPIKE (not execution); requires decomposition or sandbox
- 5: not schedulable

**Effect (W11):**
- M1 dline: scored 2 (honest, not forced down)
- M2 dline: scored 3 (integration unknowns real; placed Tue only)
- RobotOS M2 evening: scored 2–3 (synthesis uncertain; acceptable as secondary evening work)

**Realism Impact:** Tue now explicitly carries 2 Ambiguity 3+ anchors (dline office + RobotOS eve); this is REAL and visible, not cosmetically hidden.

---

### B. SIZE RULE PATCH

**Problem:** System was forcing all work into M-sizes, hiding L-work or incorrectly labeling it.

**Fix (Generator):**
- Replaced "L missions decomposed to M-phases only" with nuanced rule:
  - Prefer M (default execution unit)
  - XS/S allowed for setup, verify, review, unblock, carry-over closeout
  - L allowed ONLY if: has internal checkpoint + produces stop-safe intermediate artifact + max 4h session (then MUST pause/verify)
  - XL forbidden

**Effect (W11):**
- M1, M2, M3, M4 all remain M-sized (realistic, not forced)
- No fake L→M relabeling detected

**Realism Impact:** Prevents hidden scope bloat (cosmetic M-labeling of actual L-work).

---

### C. START ANCHOR + FALLBACK PATCH

**Problem:** Start steps created motion, but didn't encode what to do if primary dependency blocked within first 15 minutes.

**Fix (Generator):**
- Added new mandatory column: "If blocked in first 15p (fallback)"
- Fallback must be OPERATIONAL, not abstract
- Fallback must produce useful artifact (even if pivot/rework)

**Fix (W11 Examples):**
- Mon M1: "If architecture foggy after 15 min, escalate Mon 11:00 (not EOD); switch to spike findings review"
- Tue M2: "If env unstable, capture blocker notes + switch to log analysis; escalate evening (don't stall)"
- Wed M2→M3: "If dline incomplete Wed 12:00, escalate + use PM for finishing; defer M3 to Thu rework"

**Realism Impact:** Fallbacks are now tight to start logic, not vague catch-alls. Each day knows exactly what to do in first 15 min if primary doesn't work.

---

### D. ARTIFACT STOP-SAFETY PATCH

**Problem:** Artifacts were named concretely, but stop conditions didn't include "minimum usable completeness" (safe-to-stop state).

**Fix (Generator):**
- Every stop condition now includes: "minimum usable state"
- Examples (NOW REQUIRED): 
  - Doc exists with headings + blocker section + next-step note (even if outline/draft)
  - Test file contains scaffold + first failing case + TODO markers
  - Checklist exists with at least categories + 3 findings

**Fix (W11 Examples):**
- M1 stop condition: "dline doc readable (even if incomplete) + scenarios mapped + 3 unknown blockers recorded"
- M2 stop condition: "dline scaffolds exist + at least running (pass/fail tracked) + existing tests passing; PR visible (even if tests still red)"

**Realism Impact:** Can pause and hand-off without re-reading; minimum artifact exists to be useful.

---

### E. REALISM QA GATE (NEW)

**Problem:** Old QA gates were operational but didn't catch cosmetically-neat-but-unrealistic scores.

**Fix (Generator):**
- Added NEW mandatory gate: REALISM QA (becomes Gate 5; Language QA becomes Gate 6)
- Realism QA validates:
  1. No single day exceeds realistic human capacity (~7h office, ~2h evening max)
  2. Ambiguity not stacked carelessly (consecutive high-ambiguity days)
  3. Evening blocks actually conservative (work type, not just label M)
  4. Contingent tasks have realistic unblock conditions (not >50% failure risk treated as 100% likely)
  5. Fallbacks fit available time (not requiring rescope to execute)
  6. Total load aligns with practical ability (<40h/week objective)
  - **FAIL rule:** If scores are cosmetically neat (all Ambiguity 2, perfect daily balance, all contingent 100% likely), file is gaming system

**Fix (W11 Validation):**
- ✅ Max office day: Wed 6–7h (realistic)
- ⚠️ Ambiguity stacking Tue: authentic tension (dline committed priority uses best energy; RobotOS secondary evening)
- ✅ Evening conservative: 1×M max; Ambiguity ≤2 except Tue synthesis
- ✅ Thu contingent realistic: explicit CONDITIONAL on Wed; rework path named
- ⚠️ Load tight but achievable: 31h total (within 40h); if Thu fails, 22h still committed

**Realism Impact:** Week now passes uncomfortable realism check, not just neat checkbox compliance.

---

### F. DAILY INHERITANCE PATCH + OVERRIDE RULES

**Problem:** Daily inheritance was strong, but didn't handle upstream slip decisions explicitly.

**Fix (Generator):**
- Added new mandatory column: "Override Rule (if upstream dependency slips, what gets dropped/protected?)"
- For chains like Tue→Wed→Thu, added explicit decision logic: if upstream <50% done by checkpoint, escalate + defer dependent

**Fix (W11 Explicit Override Table):**

| Day | If Upstream Slips | Protect First | Drop First | Re-entry |
|---|---|---|---|---|
| **Tue** | Mon M1 incomplete | dline_send scaffold + tests | Edge cases | Analytical re-entry |
| **Wed** | Tue M2 <50% by 8:00 | Core dline paths, PR visibility | M3 RAM | Escalation decision |
| **Thu** | Wed PR not open | Thu morning decision | RAM expansion to W12 | Rework vs defer |

**Realism Impact:** Critical path is now explicit about what happens if Tue slips; no silent squeezing into Wed.

---

## What is Now Harder to Game

### 1. Ambiguity Score Cosmetics
**BEFORE:** All missions compressed to Ambiguity ≤2 → looked clean, hid complexity  
**NOW:** Ambiguity 3+ allowed but must be placed on high-energy slots + fallback named → complexity is visible

**What this means:** Week that has Ambiguity 3 on Tue now clearly shows that Tue is stretched, not just "standard execution day"

### 2. Size Compression
**BEFORE:** L-work could be relabeled M if wishful → hidden scope  
**NOW:** L allowed only with checkpoint + min-usable intermediate + max 4h boundary → can't hide big work

**What this means:** If a mission is actually L, it now shows as L with explicit pause points, not cosmetically listed as M

### 3. Fallback Vagueness
**BEFORE:** Fallbacks could be abstract ("adapt as needed", "escalate if blocked")  
**NOW:** Fallback must be operational and produce artifact (e.g., "switch to log capture + blocker note")

**What this means:** If primary path fails at start, team knows exactly what pivot work to execute, not fuzzy re-planning

### 4. Minimum Usable State Omission
**BEFORE:** Stop condition could be "all tests passing" (100% completion assumption)  
**NOW:** Stop condition must include "minimum usable" (artifact exists even 50% done; can hand-off mid-work)

**What this means:** Partial completion is now not a failure; safe-to-stop is explicit, preventing hidden spillover

### 5. Contingent / Committed Confusion
**BEFORE:** Contingent tasks could be listed alongside committed without distinction  
**NOW:** Must explicitly state: prerequisite + failure scenario + deferral condition

**What this means:** Thu RAM expansion cannot be silent; if Wed incomplete, Thu must rework (not expansion) or defer

### 6. Unrealistic Optimism (Realism QA Gate)
**BEFORE:** No catch for cosmetically perfect weeks (all Ambiguity 2, all contingent 100% likely, perfect load balance)  
**NOW:** Realism QA fails if scores are too neat → must acknowledge real constraints/risks

**What this means:** Good weeks now have visible tension (tight load, some uncertainty, realistic failure modes named)

### 7. Upstream Slip Silence
**BEFORE:** Daily file didn't know what to do if previous day incomplete  
**NOW:** Override rules explicit: if Tue 50% done by Wed 8:00, escalate + drop M3 (don't silently compress Wed)

**What this means:** Critical path is now transparent; if Tue slips, Wed has pre-decided override logic (escalate, not squeeze)

---

## Validation: W11 as First Hardened Instance

**Ambiguity Honesty:**
- M1 dline = 2 ✅ (realistic for architecture from spike)
- M2 dline = 3 ✅ (integration unknowns real; placed Tue only)
- RobotOS M2 eve = 2–3 ✅ (synthesis uncertain; acceptable secondary)

**Fallback Attachment:**
- Mon M1: escalate Mon 11:00 if blocked ✅
- Tue M2: switch to log capture + escalate evening ✅
- Wed M2→M3: deferral decision if <50% done ✅

**Minimum Usable States:**
- Artifacts include blocker sections + next-step notes ✅
- Stop conditions state "even if incomplete" where realistic ✅

**Override Rules:**
- Tue→Wed→Thu chain has explicit "if <50% done" escalation ✅
- What to protect vs drop named ✅

**Realism QA:**
- Capacity realistic (~7h office, ~2h eve max) ✅
- Ambiguity stacking uncomfortable but transparent ✅
- Contingent conditions realistic (Thu conditional on full Wed complete) ✅
- Load tight (31h) but achievable ✅

---

## System Hardening Status

**Old System (Pre-Patch):**
- ❌ Ambiguity artificially compressed
- ❌ Fallbacks vague or missing
- ❌ Stop conditions didn't include safestop states
- ❌ No realistic unhappiness check
- ❌ Upstream slip logic implicit

**Hardened System (Post-Patch):**
- ✅ Honest ambiguity scoring (0–5, with placement rules for ≥3)
- ✅ Operational fallbacks attached to start-step logic
- ✅ Minimum usable states explicit (safe-to-stop, hand-offable)
- ✅ Realism QA gate catches cosmetic neatness
- ✅ Upstream override rules explicit (if slip detected, execute THIS)

**W11 is first instance to be tested against this hardened system.**

If W11 executes as planned → system realism is validated  
If W11 has material slip (e.g., Tue M2 blocked) → override rules activate (don't squeeze Wed, escalate instead)

