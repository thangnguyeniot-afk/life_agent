# Life Anchors & Anti-Anchors Schema Audit: 2026-04-03

**Audit scope:** Evaluating compliance of Life Anchors (§4) and Anti-Anchors (§5) sections in March Review against:
- Governance finding classification schema [EXEC/ADVISORY/RULE/UNRESOLVED]
- Monthly Review Exit Gate requirements
- Monthly Plan Intake Gate requirements
- Human Layer boundary rules (ADR-20260322)

**Audit date:** 2026-04-03  
**Status:** Comprehensive audit (findings only, no auto-fixes)

---

## Executive Verdict

### Current Status: 🔴 RED (Boundary safety issues detected; NOT safe to extract to April planning as-is)

**Is it safe to use as-is?**
- ❌ NO. Two major boundary leaks detected in Life Anchors section
- ⚠️ MEDIUM RISK. Anti-Anchors section has classification clarity gaps, but operational status is generally sound

### Critical Verdict Summary

| Section | Classification Issues | Binding Risk | Intake Safety | Boundary Safety | Status |
|---|---|---|---|---|---|
| **Life Anchors** | Missing tags; advisory signals written as hard rules | 🔴 HIGH | ❌ NOT SAFE | 🔴 CRITICAL LEAK | 🔴 RED |
| **Anti-Anchors** | Unclear distinction between SOLVED/MITIGATED; missing rule owner links | 🟡 MEDIUM | ⚠️ CONDITIONAL | 🟡 MEDIUM | 🟡 YELLOW |

### Top 5 Governance Gaps

1. **Recovery (Sleep) anchor:** Written as [ADVISORY] signal but elevated to hard operational rule ("Non-negotiable 23:00 bedtime") without transformation
2. **Connection anchor:** [ADVISORY] signal but presented as directive action ("Restore weekly check-in") without intake-gate transform
3. **Movement, House Basics, Eat Properly anchors:** Labeled "assumed" but classified as "stable" = [UNRESOLVED] not clearly tagged
4. **Anti-Anchors classification:** Distinction between SOLVED (mechanism in place, confirmed) vs MITIGATED (mechanism in place, pattern still present) not explicit
5. **Missing transformation narrative:** Advisory signals being extracted to April planning without "testing validity Q2; will re-confirm May" caveats

**Impact if extracted to April planning as-is:**
- 🔴 Exit Gate will FAIL (§3.5 Human Layer Boundary check)
- 🔴 Intake Gate will FAIL (transformations missing)
- 🔴 Advisory signals treated as binding facts → boundary breach

---

## Life Anchors Audit

### Current Life Anchors Table (March Review §4)

| Anchor | Xu hướng | Assessment | April Action |
|---|---|---|---|
| Movement | ➖ | No data (March reflection just started; assumed normal) | Track in April. Establish baseline. |
| House Basics | ➖ | Stable (normal patterns assumed from lifestyle data) | Continue; no adjustment needed |
| Eat Properly | ➖ | Stable (assumed normal; no reflection data) | Continue; add daily tracking in April |
| Recovery | ⬆️ | Positive trend. Sleep quality identified as #1 energy lever; discipline improving (23:30→23:00 bedtime trend) | Protect hard in April. Non-negotiable 23:00 bedtime. |
| Connection | ⬇️ | Negative trend. Month is human-sparse (system design = solitary work; no team sync; minimal interaction) | Critical for April. Restore weekly 30–60 min team check-in. Prevent isolation drift. |

### Detailed Anchor-by-Anchor Audit

| Anchor | Current Wording Role | Correct Type | Evidence Quality | Stability Classification | Intake Safety | Binding Risk | Planning Use | Boundary Risk | Status |
|---|---|---|---|---|---|---|---|---|---|
| **Movement** | "assumed normal; no data" | [UNRESOLVED] | ❌ Zero data (March reflection "just started"; no actual measurement) | Assumed (not stable; not emerging; no evidence) | ✅ Safe (monitoring-only; no planning extraction) | 🟡 MEDIUM (risks over-stability claim) | "Track in April" = future decision, correct | 🟡 MEDIUM (assumes normalcy without data) | 🟡 YELLOW |
| **House Basics** | "stable; normal patterns assumed" | [UNRESOLVED] | ❌ Zero data ("assumed from lifestyle data"; no March measurement) | Assumed + Claimed Stable (false confidence) | ✅ Safe (monitoring-only) | 🟡 MEDIUM (hides uncertainty) | "Continue; no adjustment" = future action, ok | 🟡 MEDIUM (assumed without data) | 🟡 YELLOW |
| **Eat Properly** | "stable; no reflection data" | [UNRESOLVED] | ❌ Zero data (explicitly no reflection; "assumed normal") | Assumed (stated explicitly "no data") | ✅ Safe (future tracking action) | 🟡 MEDIUM (stated as fact without evidence) | "Continue; add tracking" = future action, correct | 🟡 MEDIUM (assumed without data) | 🟡 YELLOW |
| **Recovery (Sleep)** | "positive trend; #1 energy lever; discipline improving" | [ADVISORY] | ⚠️ Limited ("March reflection just started; 23:30→23:00 bedtime trend" = 1 month pattern) | Emerging (observed but limited period) | ❌ NOT SAFE (extracted as hard rule without tag/transform) | 🔴 **CRITICAL** (written as binding: "Non-negotiable 23:00 bedtime") | **Being extracted to "Non-negotiable 23:00 bedtime"** (§6 April Non-Negotiables) | 🔴 **CRITICAL LEAK** (advisory presented as bound execution directive) | 🔴 **RED** |
| **Connection** | "negative trend; solitary work; needs team sync" | [ADVISORY] | ⚠️ Limited ("March had zero recorded team sync" = 1 month pattern; subjective "human-sparse") | Emerging (observed but limited scope) | ❌ NOT SAFE (extracted as action directive without tag/transform) | 🔴 **CRITICAL** (written as binding directive: "Restore weekly check-in...Prevent isolation drift") | **Being extracted to "Weekly team check-in (30–60 min)"** (§6 April Non-Negotiables) | 🔴 **CRITICAL LEAK** (advisory being used as operational decision rule) | 🔴 **RED** |

### Key Audit Findings: Life Anchors

**Finding 1: Recovery anchor is [ADVISORY] but elevated to binding execution rule**

Current wording (March Review §4):
```
Recovery: Positive trend. Sleep quality identified as #1 energy lever; 
discipline improving (23:30→23:00 bedtime trend)
April Action: Protect hard in April. Non-negotiable 23:00 bedtime.
```

Current wording (§6 April Non-Negotiables):
```
1. Sleep: 23:00 bedtime hard stop. This is the energy regulator. 
   Everything else scales off sleep quality.
```

**Classification issues:**
- Sleep pattern is from "March Reflection (Human Layer) Insights" = optional Human Reflection template
- Per ADR-20260322, Human Reflection outputs are [ADVISORY] (non-binding input to capacity discussion)
- Evidence: "sleep-quality correlation is PRIMARY driver (7h+ → high energy; 5–6h → mid-week fatigue)" = one month observation
- Current wording presents it as hard operational constraint: "hard stop", "Everything else scales off"

**Intake safety problem:**
- ❌ Not tagged [ADVISORY]
- ❌ NOT transformed: proper format would be "Capacity model: protecting 23:00 bedtime (informed by March sleep-energy observation; testing validity Q2; will re-confirm May)"
- ✅ Current format reads like [RULE] or [EXEC], not [ADVISORY]

**Boundary risk:**
- 🔴 CRITICAL: Advisory signals from Human Reflection layer are bleeding into execution control ("hard stop", "non-negotiable")
- This violates ADR-20260322 §Explicit Non-Goals: "Using reflected emotion as veto for delivery commitments" (this is close to that)

**Patch required:** Rewrite as capacity hypothesis with re-confirmation note, tag as [ADVISORY]

---

**Finding 2: Connection anchor is [ADVISORY] but used as binding operational directive**

Current wording (March Review §4):
```
Connection: Negative trend. Month is human-sparse (system design = solitary work; 
no team sync; minimal interaction)
April Action: Critical for April. Restore weekly 30–60 min team check-in. 
Prevent isolation drift.
```

Current wording (§6 April Non-Negotiables):
```
3. Weekly team check-in (30–60 min). Prevent March isolation. 
   System design work is solitary; execution needs connection.
```

**Classification issues:**
- Connection pattern is subjective observation from operator ("human-sparse", "solitary", "isolation drift")
- Evidence: "March had zero recorded team sync" = observed pattern (true), but drawn from Human Reflection (optional)
- This is [ADVISORY] signal, not [EXEC] fact

**Intake safety problem:**
- ❌ Not tagged [ADVISORY]
- ❌ NOT transformed: extracted as action directive without alternate scenario or re-confirmation note
- ✅ Current format reads like [RULE]

**Boundary risk:**
- 🔴 CRITICAL: Subjective well-being signal (connection need) is being used as binding scheduling rule ("weekly check-in")
- This is close to ADR-20260322 violation: "Using subjective emotion to override scope/scheduling"

**Patch required:** Rewrite as capacity input with contingency, tag as [ADVISORY], add re-confirmation note

---

**Finding 3: Movement, House Basics, Eat Properly are [UNRESOLVED] but written as "stable"**

Current wording shows these as "➖ / Stable (assumed)" but:
- Movement: "No data (March reflection just started; assumed normal)"
- House Basics: "Stable (normal patterns assumed from lifestyle data)"
- Eat Properly: "Stable (assumed normal; no reflection data)"

**Classification issues:**
- All three have NO March data (just assumptions)
- Per governance schema, this is [UNRESOLVED]: "Open question / Pending Decision; not ready for commitment"
- Wording as "stable" creates false confidence

**Intake safety:**
- ✅ These are NOT being extracted to April planning (correctly)
- ⚠️ But wording hides the actual status: should be "track data; currently assumed to be stable pending confirmation"

**Boundary risk:**
- 🟡 MEDIUM: "Assumed" status is hidden by "Stable" label; could lead to silent assumptions in planning

**Patch required:** Retag as [UNRESOLVED], clarify "assumed steady pending data collection" rather than "stable"

---

### Life Anchors Schema Compliance

**Against governance schema:**
- ❌ No [TYPE] tags present
- ❌ No [STABILITY] classification (assumed/emerging/stable/confirmed) explicitly marked
- ❌ No intake transformation rules for [ADVISORY] signals
- ✅ Section correctly isolated from System Change Review

**What needs to pass Exit Gate §3 (Human Layer Boundary):**
- ✅ Human Reflection findings are in separate section (§4 is technically NOT mixed with System Change)
- ❌ FAIL: Recovery + Connection are [ADVISORY] but not tagged; not transformed; read as binding
- ❌ FAIL: No ADR-20260322 reference in section (should note pilot + re-eval criteria)

---

## Anti-Anchors Audit

### Current Anti-Anchors Section (March Review §5)

Four anti-anchors with current operational classification:

1. **Evening Capacity Overestimate**: "MITIGATED but not solved"
2. **Restart Friction**: "SOLVED"
3. **Intake Quality / Task Ambiguity**: "SOLVED"
4. **Three-Project Load Fatigue**: "MITIGATED by design"

### Detailed Anti-Anchor-by-Anti-Anchor Audit

| Anti-Anchor | Current Wording Role | Correct Type | Operational Status | Evidence Quality | Intake Safety | Guardrail Owner | Duplicate Rule Risk | Boundary Risk | Status |
|---|---|---|---|---|---|---|---|---|---|
| **Evening Capacity Overestimate** | "Mitigated but not solved; requires ongoing conservative planning" | [UNRESOLVED] | Mitigated (pattern exists; conservative planning mitigates impact) | ⚠️ Limited ("W09 only"; "insufficient data"; consistent with historical pattern) | ⚠️ CONDITIONAL ("Conservative evening allocation (1×S / 1×M)" = transforms pattern into planning constraint; ok but needs tag) | Capacity Planning (conservative default) | 🟡 MEDIUM (pattern tracked separately from Evening Capacity rule) | ✅ LOW (just planning input, not rule override) | 🟡 YELLOW |
| **Restart Friction** | "SOLVED (closure + re-entry package discipline works)" | [RULE] | Solved (mechanism confirmed; pattern prevented) | ✅ Strong ("W09 daily files show explicit closure notes + re-entry packages; no observed friction") | ✅ SAFE (mechanism is rule in Daily template; not extracting pattern as assumption) | Re-entry Package Rule (Daily closure discipline) | ✅ NO (already owns rule: "Re-entry package discipline maintained" in OS) | ✅ LOW (rule-owned mechanism) | ✅ GREEN |
| **Intake Quality / Task Ambiguity** | "SOLVED (semantic quality gates prevent entry)" | [RULE] | Solved (mechanism confirmed; pattern prevented) | ✅ Strong ("W09 daily files show semantic clarity; exit conditions binary") | ✅ SAFE (mechanism is rule; not extracting as assumption) | Semantic Quality Gates Rule (Daily template DoD) | ✅ NO (already owns: "Semantic Quality Gates" in OS) | ✅ LOW (rule-owned mechanism) | ✅ GREEN |
| **Three-Project Load Fatigue** | "MITIGATED by design (Daily Scope Rule prevents manifestation); requires monitoring" | [RULE] (with monitoring note) | Mitigated (mechanism prevents manifestation; pattern still present so needs monitoring) | ⚠️ LIMITED ("W09 validation only"; "preliminary"; needs more data to confirm sustainability) | ⚠️ CONDITIONAL (Daily Scope Rule is RULE; but sustainability is [UNRESOLVED] - needs quarterly re-eval) | Daily Project Scope Rule (max 2 anchors) | ❌ RISK (has own "Three-project viability" tracking; could duplicate scope rule) | 🟡 MEDIUM (rule prevents manifestation but sustainability is unconfirmed) | 🟡 YELLOW |

### Key Audit Findings: Anti-Anchors

**Finding 1: Evening Capacity Overestimate is correctly [UNRESOLVED] but needs explicit intake-safety note**

Current wording:
```
Evening Capacity Overestimate
- Pattern: Historically plan evening as "2×M or 3×S" but live-time reality 
  is usually "1×M or 2×S"
- March evidence: Limited (W09 only); plan showed 1.5–2h + 0.5h spillover; 
  reality was ~1.5h firm + 0.5h optional
- Appeared: 1 week (insufficient data)
- For April: Conservative evening allocation (1×S on weak nights, 1×M on high-energy nights)
```

**Status assessment:**
- ✅ Correctly identified as pattern with insufficient data (1 week only)
- ✅ Correctly classified as "mitigated but not solved" (conservative planning mitigates, pattern continues)
- ⚠️ Evidence note says "insufficient data" but pattern is being used in April capacity planning

**Classification issues:**
- Type: [UNRESOLVED] (needs 2+ months data; unclear if sustainable)
- Governance schema example: "Evening capacity pattern: needs 2nd month of data; unclear if sustainable at 1–2 hours (will evaluate May)"

**Intake safety:**
- ✅ Extraction is safe: "Conservative planning" is a CAPACITY modeling choice, not binding prediction
- ⚠️ But should note: [UNRESOLVED] finding informing planning hypothesis (ok per governance)
- ✅ April planning correctly uses it: "Plan 1×M or 2×S default; 2×M only 2–3 days/week maximum"

**Boundary risk:**
- ✅ LOW (not being used as execution override; just capacity planning)

**Patch required:** Tag as [UNRESOLVED]; note "testing hypothesis Q2; will re-confirm May"

---

**Finding 2: Three-Project Load Fatigue has mitigation rule but sustainability is [UNRESOLVED]**

Current wording:
```
Three-Project Load Fatigue
- Pattern: Rotating between 3+ projects generates decision fatigue, context cost, hidden stress
- March evidence: Early-month tension real; Daily Scope Rule *prevented pattern from manifestation*; 
  mid-month calm noted
- For April: Keep Daily Scope Rule (permanent). Max 2 anchors/day stays non-negotiable. 
  This rule is life-support for multi-project sanity.
```

Current wording (§6 April Non-Negotiables):
```
2. Daily Scope Rule enforced. Max 2 anchors/day. No exceptions.
```

**Status assessment:**
- ✅ Rule is in place: Daily Project Scope Rule (max 2 anchors)
- ✅ Mechanism prevents pattern manifestation (confirmed in W09)
- ⚠️ Sustainability is still question: "preliminary; needs more data"

**Classification issues:**
- Rule status: [RULE] (Daily Scope Rule is approved system change, already in System Change Review)
- Pattern sustainability status: [UNRESOLVED] ("Can we sustain 3-project portfolio long-term?" decision checkpoint: May review)

**Governance concern:**
- Rule is correct and safe to extract
- But underlying question "is 3-project sustainable?" remains [UNRESOLVED]
- Should be tracked separately: not "Three-project model now safe" but "Three-project model requires monitoring"

**Intake safety:**
- ✅ SAFE to extract: Daily Scope Rule is a [RULE]
- ✅ SAFE to apply as non-negotiable: mechanism works (W09 confirmed)
- ⚠️ But sustainability question should remain flagged for May review

**Boundary risk:**
- ✅ MEDIUM (rule itself is safe; but underlying dependency question needs tracking)

**Patch required:** Separate the findings:
- [RULE]: Daily Scope Rule mitigates 3-project fatigue by design
- [UNRESOLVED]: Sustainability of 3-project portfolio; re-eval May (checkpoint: cumulative fatigue patterns)

---

**Finding 3: Restart Friction and Task Ambiguity are correctly [SOLVED]**

Both anti-anchors have:
- ✅ Strong evidence ("W09 confirmed")
- ✅ Mechanism in place (rule or discipline)
- ✅ Pattern prevented (not just mitigated)
- ✅ Safe to mark as "no longer needs monitoring as pattern" (mechanism owns it)

**Current status: GREEN** ✅

---

### Anti-Anchors Schema Compliance

**Against governance schema:**
- ⚠️ No explicit [TYPE] tags ([RULE]/[UNRESOLVED])
- ⚠️ No distinction between SOLVED (pattern prevented) vs MITIGATED (pattern reduced but present)
- ⚠️ "Owner" mechanism not always explicit (which rule owns each anti-anchor)
- ✅ Monitoring-vs-closed status mostly clear

**What needs for Intake Gate compliance:**
- ✅ Evening Capacity: Currently safe (just planning input); should tag as [UNRESOLVED]
- ✅ Restart Friction: Safe (mechanism in place); mark as [RULE]
- ✅ Task Ambiguity: Safe (mechanism in place); mark as [RULE]
- ⚠️ Three-Project Load: Safe but needs split (rule vs sustainability question)

---

## Schema Gap Analysis

### Missing Fields in Life Anchors Section

| Field | Required By | Impact | Examples |
|---|---|---|---|
| **[TYPE] tag** | Exit Gate §3.5; Intake Gate | Cannot verify if anchor is EXEC/ADVISORY/RULE/UNRESOLVED | Recovery should be tagged [ADVISORY]; Movement should be tagged [UNRESOLVED] |
| **Stability field** | Governance schema | Cannot distinguish assumed vs. emerging vs. stable | Movement/House Basics/Eat Properly = [UNRESOLVED] assumed; Recovery/Connection = [ADVISORY] emerging |
| **Intake transformation note** | Intake Gate rule | Cannot verify ADVISORY→hypothesis transform applied | Recovery: should note "testing hypothesis; will re-confirm May" |
| **Re-eval checkpoint** | Governance schema | No date for pending decisions | Recovery/Connection should link to "monthly re-confirm" pattern |
| **Alternate scenario** | Governance schema | ADVISORY signals without "what if this signal breaks?" cannot be planned around | Recovery: "If sleep-energy correlation breaks → adjust capacity model" |

### Missing Fields in Anti-Anchors Section

| Field | Required By | Impact | Examples |
|---|---|---|---|
| **[TYPE] tag** | Exit Gate; Intake Gate | Cannot verify if anti-anchor is RULE/UNRESOLVED/EXEC | Evening Capacity = [UNRESOLVED]; Restart Friction = [RULE] |
| **Operational status (explicit)** | Governance schema | Distinction between prevented/mitigated/solved is blurry | Three-Project Load needs: "[RULE] prevents manifestation" + "[UNRESOLVED] sustainability TBD" |
| **Owner mechanism** | Anti-SPOF rule | Cannot verify which rule owns each anti-anchor | Restart Friction → owned by "Re-entry Package discipline"; Evening Capacity → owned by "Capacity Planning" |
| **Re-eval checkpoint** | Governance schema | No dates for UNRESOLVED anti-anchors | Evening Capacity: "re-eval May"; Three-Project Sustainability: "re-eval June" |

---

## Governance Risk Analysis

### Highest-Risk Findings

**Risk 1: Recovery anchor bleeding advisory into execution control (🔴 CRITICAL)**

**Scenario:**
- March observation: "sleep-energy correlation is PRIMARY driver"
- Current wording: "This is the energy regulator. Everything else scales off sleep quality."
- Current use: "Non-negotiable 23:00 bedtime" in April Non-Negotiables (§6)
- April execution: If delivery deadline arises, this hard constraint could become contentious

**Boundary violation:**
- ❌ Violates ADR-20260322 §Explicit Non-Goals: "Using reflected emotion as veto for delivery commitments"
- ❌ Not properly transformed per Intake Gate rule: ADVISORY must become hypothesis ("testing validity Q2; will re-confirm May")

**Fix required:** P0 (must fix before April planning locks)

---

**Risk 2: Connection anchor presented as binding scheduling rule (🔴 CRITICAL)**

**Scenario:**
- March observation: "Month is human-sparse; March had zero recorded team sync"
- Current wording: "Critical for April. Restore weekly check-in. Prevent isolation drift."
- Current use: In April Non-Negotiables (§6) as schedule commitment
- April execution: If workload increases, this "critical" item may create tension with delivery priorities

**Boundary violation:**
- ❌ Violates ADR-20260322 spirit: subjective well-being signal used as binding scheduling constraint
- ❌ Not transformed per Intake Gate: should be "testing hypothesis that weekly connection improves outcomes"

**Fix required:** P0 (must fix before April planning locks)

---

**Risk 3: Three-Project sustainability question unclear (🟡 MEDIUM)**

**Scenario:**
- Current finding: "Three-project model viable... Daily Scope Rule prevents fatigue"
- But also: "W09 only; preliminary" and "needs quarterly re-eval"
- April extraction: "Three-project portfolio is viable" (implicit assumption)
- June re-eval question: Did we actually validate sustainability, or did we just avoid the pattern?

**Governance concern:**
- ⚠️ Pattern not [EXEC]-confirmed; just [RULE]-mitigated
- ⚠️ Sustainability question [UNRESOLVED] but written as resolved
- ⚠️ May result in silent assumption ("model is working") vs. active re-eval ("model needs confirmation")

**Fix required:** P1 (should clarify before May re-eval)

---

**Risk 4: Evening Capacity pattern insufficient for planning (🟡 MEDIUM)**

**Scenario:**
- Current data: W09 only (1 week)
- Governance rule: [UNRESOLVED] needs 2+ data points before [EXEC]
- April planning: Using pattern as "conservative default" (1×M / 2×S)
- May review: Will we have enough data to classify as [EXEC], or still [UNRESOLVED]?

**Governance concern:**
- ⚠️ Pattern is being used in planning correctly (conservative hypothesis)
- ✅ But "insufficient data" status should remain visible
- ✅ Should link to May review checkpoint

**Fix required:** P1 (should clarify re-eval checkpoint)

---

### Boundary Safety Matrix

| Finding | Leakage Type | Current Risk | Patch Needed | Priority |
|---|---|---|---|---|
| **Recovery (Sleep)** | Advisory→Execution (binding rule) | 🔴 CRITICAL | Tag + transform | P0 |
| **Connection** | Advisory→Scheduling (binding constraint) | 🔴 CRITICAL | Tag + transform | P0 |
| **Movement/House/Eat** | Unresolved→Stable (false confidence) | 🟡 HIGH | Retag + clarify assumed | P1 |
| **Three-Project Sustainability** | Mitigated→Resolved (silent assumption) | 🟡 MEDIUM | Split findings; clarify [UNRESOLVED] | P1 |
| **Evening Capacity** | Limited data→Planning input | 🟡 MEDIUM | Link to re-eval checkpoint | P1 |

---

## Fix Readiness Assessment

### Can it be patched lightly? Or requires major restructure?

**Current situation:** Life Anchors section has strong semantic content (good trend identification, correct insights) but CRITICAL boundary safety issues. Anti-Anchors section has operational clarity gaps but no critical leaks.

**Fix complexity: LOW-MEDIUM (schema annotations + wording sharpness; no content rewrite)**

### Patch Level Analysis

#### Patch Level P0 (Must fix before April 30; blocking Exit/Intake gate)

**Item 1: Add [TYPE] tags to all Life Anchors**
```
Movement: [UNRESOLVED]
House Basics: [UNRESOLVED]
Eat Properly: [UNRESOLVED]
Recovery: [ADVISORY]
Connection: [ADVISORY]
```
Effort: 2 min · Result: Classifiable

**Item 2: Rewrite Recovery anchor with transformation + re-confirm note**
Current: "Protect hard in April. Non-negotiable 23:00 bedtime."
New: "Capacity model: protecting 23:00 bedtime (informed by March sleep-energy observation [ADVISORY]; testing validity Q2; will re-confirm May). Hypothesis: 7h+ sleep enables high energy; <6h correlates with fatigue."
Effort: 5 min · Result: Boundary-safe; governance-compliant

**Item 3: Rewrite Connection anchor with transformation + re-confirm note**
Current: "Critical for April. Restore weekly team check-in. Prevent isolation drift."
New: "Capacity model: testing weekly connection hypothesis (March observation: solitary system design creates isolation risk [ADVISORY]; hypothesis: weekly 30–60 min sync prevents drift; will validate Q2; may become optional if pattern breaks). Alternate scenario: if connection improves morale significantly, consider making permanent."
Effort: 5 min · Result: Boundary-safe; governance-compliant

**Item 4: Add intake transformation rule in section header (for clarity)**
Add at start of §4): "Note: Life Anchors may inform capacity planning but are not deterministic. ADVISORY signals must be re-confirmed monthly; do not assume persistence."
Effort: 3 min · Result: Auditable

**Total P0 effort:** ~15 min · Result: Exit Gate + Intake Gate pass

---

#### Patch Level P1 (Should fix in next 1–2 weeks; improves governance clarity)

**Item 1: Clarify Movement/House Basics/Eat Properly as [UNRESOLVED] assumed**
Current: "Stable (assumed normal; no reflection data)"
New: "Monitoring — assumed stable pending data (no March measurement). Will establish baseline in April."
Effort: 5 min per item · Result: Clarity

**Item 2: Split Three-Project Load findings**
Add separate tracking:
- [RULE] Finding: "Daily Scope Rule prevents 3-project fatigue manifestation (W09 confirmed)"
- [UNRESOLVED] Question: "Sustainability of 3-project portfolio long-term unclear; requires quarterly re-eval (checkpoint: June end-of-Q2 review)"
Effort: 10 min · Result: Prevents silent assumption

**Item 3: Add Evening Capacity re-eval checkpoint**
Add to Anti-Anchor note: "Re-eval checkpoint: May review with 4 weeks data; decision: if pattern repeats 4/4 weeks → may promote to [EXEC]; if breaks → update model"
Effort: 5 min · Result: Governance-tracked

**Item 4: Add ADR-20260322 reference note in Life Anchors section header**
Note: "Life Anchors capturing well-being signals per ADR-20260322 Human Layer Q2 pilot. Signals are advisory-only per ADR governance rules."
Effort: 3 min · Result: Auditable

**Total P1 effort:** ~30 min · Result: Complete governance documentation

---

#### Patch Level P2 (Nice to have; cleanup + documentation)

**Item 1:** Create example transformation in template
**Item 2:** Build Life Anchor → Capacity Hypothesis mapping guide

---

## Specific Wording Changes Required (P0)

### Recovery Anchor Patch

**Current (March Review §4):**
```
Recovery | ⬆️ | Positive trend. Sleep quality identified as #1 energy lever; 
discipline improving (23:30→23:00 bedtime trend) | Protect hard in April. 
Non-negotiable 23:00 bedtime.
```

**Current (§6 April Non-Negotiables):**
```
1. Sleep: 23:00 bedtime hard stop. This is the energy regulator. 
   Everything else scales off sleep quality.
```

**After P0 Patch:**
```
Recovery | ⬆️ | [ADVISORY] Emerging pattern: Sleep quality identified as #1 energy lever 
(7h+ → high energy; 5–6h → mid-week fatigue). March data: discipline improving 
(23:30→23:00 bedtime trend). **Re-confirm monthly.** | 
Capacity hypothesis: Protecting 23:00 bedtime (testing validity Q2; will re-confirm May).

```

Also in §6:
```
1. Sleep: Protect target 23:00 bedtime (capacity model — testing hypothesis based on 
   March sleep-energy observation; will validate Q2; may adjust if pattern breaks). 
   This improves measured energy levels; enable by protecting core sleep hours.
```

---

### Connection Anchor Patch

**Current (March Review §4):**
```
Connection | ⬇️ | Negative trend. Month is human-sparse (system design = solitary 
work; no team sync; minimal interaction) | Critical for April. Restore weekly 
30–60 min team check-in. Prevent isolation drift.
```

**Current (§6 April Non-Negotiables):**
```
3. Weekly team check-in (30–60 min). Prevent March isolation. System design 
   work is solitary; execution needs connection.
```

**After P0 Patch:**
```
Connection | ⬇️ | [ADVISORY] Emerging pattern: March isolation risk detected 
(no team sync recorded; solitary system work). Observation: operator reported 
reduced connection needs monitoring. **Re-confirm monthly.** | 
Capacity hypothesis: Testing weekly connection hypothesis (April: weekly 30–60 min 
sync; monitoring effect on morale + isolation perception; will re-confirm May). 
If pattern breaks, may become optional.
```

Also in §6:
```
3. Weekly team check-in (30–60 min). Testing hypothesis: weekly connection reduces 
   isolation risk (based on March pattern; monitoring effectiveness Q2; may adjust 
   if pattern changes). Not a hard commitment; adaptive based on monthly re-eval.
```

---

## Compliance Checklist (After P0 Patch)

**Exit Gate §3 (Human Layer Boundary) will check:**
- [ ] All human reflection findings tagged [ADVISORY]
- [ ] All [ADVISORY] findings in separate section (not mixed with System Change)
- [ ] All [ADVISORY] findings DO NOT read as binding rules
- [ ] ADR-20260322 referenced in section (re-eval criteria visible)

**After P0 patch:** ✅ PASS (Recovery + Connection rewritten; advisory transformation visible)

---

**Intake Gate § (Source verification) will check:**
- [ ] Each plan decision traces back to review finding with tag
- [ ] ADVISORY findings are transformed (not extracted as assumptions)
- [ ] Alternate scenario or re-confirmation note visible

**After P0 patch:** ✅ PASS (Recovery + Connection have transformation narrative + re-confirm note)

---

## Audit Summary

### 1. Overall Assessment

**Life Anchors:**
- 🔴 RED: 2 critical boundary leaks (Recovery, Connection written as hard rules, not advisory)
- 🟡 YELLOW: 3 unclear (Movement, House, Eat classifi as "stable" but actually "assumed")
- Governance impact: Exit Gate WILL FAIL; Intake Gate WILL FAIL without patch

**Anti-Anchors:**
- 🟡 YELLOW: Classification clarity gaps; but operational status sound
- ✅ Mostly safe to extract (Evening escalated correctly; Three-Project tracked; others ruled correctly)
- Governance impact: Minor cleanup needed; not gate-blocking but should formalize

### 2. Binding-Risk Summary

| Finding | Current Status | Binding Risk | Patch Impact |
|---|---|---|---|
| Recovery (Sleep) | Hard rule ("non-negotiable") | 🔴 CRITICAL | → Transform to hypothesis |
| Connection | Directive ("restore"; "critical") | 🔴 CRITICAL | → Transform to hypothesis |
| Movement/House/Eat | Claimed "stable" | 🟡 HIGH | → Retag as [UNRESOLVED] assumed |
| Three-Project | Implicit satisfaction | 🟡 MEDIUM | → Split rule vs. open question |
| Evening Capacity | Correct as planning input | ✅ LOW | → Add re-eval checkpoint |

### 3. Highest-Risk Extraction to April Planning

If extracted to April plan **without P0 patch:**
1. ❌ April plan extracts Recovery as "Non-negotiable sleep constraint" (binding fact)
2. ❌ April plan extracts Connection as "Weekly check-in scheduling requirement" (binding rule)
3. ✅ April plan extracts Three-Project model as "validated" (actually: mitigated, not validated)
4. ✅ April plan extracts Evening as "conservative planning" (correct)

**Result:** Exit Gate + Intake Gate fail; boundary breach on advisory signals.

### 4. Safe to Use As-Is?

**Functionally:** ⚠️ CONDITIONAL. Sections have good insights; operational decisions mostly sound.

**For governance:** ❌ NO. Two critical boundary leaks make sections unsuitable for formal review lock.

**For April planning:** ❌ NO. Advisory signals need transformation before extraction.

**For monitoring:** ✅ SAFE. Internal tracking and monitoring directives are sound.

---

## Patch Recommendation Map

### P0 (MUST FIX before April 30 review locks)

| Item | Current | Fix | Effort | Reason |
|---|---|---|---|---|
| Recovery antenna tag + transform | Hard rule ("non-negotiable") | → [ADVISORY] + hypothesis + re-confirm note | 5 min | Exit/Intake gate blocker |
| Connection anchor tag + transform | Directive ("critical") | → [ADVISORY] + hypothesis + re-confirm note | 5 min | Exit/Intake gate blocker |
| Add type tags to all anchors | Not tagged | Add [EXEC/ADVISORY/RULE/UNRESOLVED] | 2 min | Exit gate requirement |
| Add intake transformation rule header note | Missing | Note: "ADVISORY must be re-confirmed monthly" | 3 min | Clarity |

**Total P0:** ~15 min. Result: Gate-compliant.

---

### P1 (Should do in next 1–2 weeks)

| Item | Current | Fix | Effort | Reason |
|---|---|---|---|---|
| Clarify Movement/House/Eat as [UNRESOLVED] assumed | "Stable" without data | "Monitoring — assumed pending data" | 15 min | Governance clarity |
| Split Three-Project findings | Mixed (rule + unsolved) | Separate [RULE] + [UNRESOLVED] tracking | 10 min | Prevents silent assumption |
| Add Evening Capacity re-eval checkpoint | Just monitoring | Add "May review checkpoint + promotion criteria" | 5 min | Governance tracking |
| Add ADR reference in section header | Missing | Link ADR-20260322 + re-eval date | 3 min | Auditability |

**Total P1:** ~35 min. Result: Complete governance documentation.

---

### P2 (Cleanup)

| Item | Effort |
|---|---|
| Create transformation example in template | 10 min |
| Build anchor→hypothesis mapping guide | 15 min |
| Document "re-confirm monthly" patterns | 10 min |

---

## Success Criteria for Govenance-Safe Sections

After P0 patch, sections should pass these checks:

**Exit Gate compliance:**
- [ ] All findings tagged [EXEC/ADVISORY/RULE/UNRESOLVED]
- [ ] No ADVISORY findings presented as binding rules
- [ ] ADR-20260322 reference visible in Life Anchors section
- [ ] No speculative language ("may", "might", "possibly") in [EXEC] findings

**Intake Gate compliance:**
- [ ] Each plan decision extracted from review traces to tagged finding
- [ ] ADVISORY findings show transformation (hypothesis + re-confirm note)
- [ ] Alternate scenario or contingency noted for ADVISORY→decision flow

**Boundary safety:**
- [ ] No advisory signals presented as hard execution rules
- [ ] No Human Layer signals used as veto for delivery commitments
- [ ] All [ADVISORY] can be re-confirmed/retracted month-to-month

---

**Audit completed:** 2026-04-03  
**Audit confidence level:** HIGH (comprehensive schema audit; all 2 sections reviewed)  
**Blocking issues:** 2 critical (Recovery + Connection boundary leaks)  
**Compliance: Ready for P0 patch**

