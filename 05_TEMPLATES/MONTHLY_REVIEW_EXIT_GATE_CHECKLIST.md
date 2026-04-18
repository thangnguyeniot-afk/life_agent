# Monthly Review Exit Gate Checklist

**Purpose:** Verify boundary safety before Monthly Review is locked.

**When to use:** After Monthly Review content is written; before declaring review DONE.

**Process:** Check all items below. If ALL items pass → Review approved for lock. If 1–2 items fail → Fix targeted sections. If 3+ fail → Review has too many boundary leaks; escalate.

---

## ✅ Section 1: Finding Classification

- [ ] **All findings tagged** — Every substantive finding in §2) Output & Outcome, §3) System Change, §4–5) Life/Anti-Anchors is tagged [EXEC], [RULE], [PILOT], [ADVISORY], or [UNRESOLVED]
- [ ] **Tags visible** — Tags appear at or near the beginning of each finding (first 5 words if bullet format)
- [ ] **Consistent tagging** — Same finding type (e.g., "sleep quality pattern") is consistently tagged [ADVISORY] across all sections, not mixed as [EXEC] in one place and [ADVISORY] elsewhere

**FAIL:** Any finding without tag OR inconsistent tagging = cannot lock until corrected

---

## ✅ Section 2: System Change Clarity

- [ ] **System Change Review table complete** — Table includes all 7 columns: Change Name, Type, Mục tiêu, Kết quả, Control Layer, Gate, Quyết định
- [ ] **Type field populated** — Every row has Type = [RULE], [PILOT], [ADVISORY], or [UNRESOLVED]
- [ ] **Gate field populated** — Every row has Gate specified:
  - RULE rows: N/A or reference to decision
  - PILOT rows: Link to ADR + success criteria + re-eval date (e.g., "ADR-20260322 criteria #1–5; re-eval 2026-06-30")
  - ADVISORY rows: N/A (advisory doesn't promote without governance decision)
  - UNRESOLVED rows: Decision deadline or review checkpoint
- [ ] **No PILOT presented as permanent** — No PILOT row claims "integrated into system," "effective as permanent feature," or similar language; all PILOT rows state "pilot through [date]"

**FAIL:** Missing columns OR missing gate reference OR PILOT claiming permanence = cannot lock until corrected

---

## ✅ Section 3: Human Layer Boundary

- [ ] **Human Reflection is [ADVISORY]** — All human reflection findings are tagged [ADVISORY], never [EXEC] or [RULE]
- [ ] **Human Reflection findings are NOT in System Change Review table** — All human reflection observations appear ONLY in §3.5 (Human Advisory Signals), not in §3) System Change Review results
- [ ] **Human Reflection doesn't claim integration** — No phrase like "human layer added," "integrated," "system feature," "added to execution," or architectural language; only phrases like "optional pilot," "advisory signals," "reflection practice"
- [ ] **Human Reflection links to ADR** — §3.5 section OR any Human Reflection mention explicitly references ADR-20260322 and re-evaluation date (2026-06-30)
- [ ] **Human Reflection transformation visible** — If §3.5 exists and mentions capacity implications, shows: signal → capacity adjustment decision (not signal → direct planning assumption)

**FAIL:** Any violation of above = Human Layer boundary leak = cannot lock until corrected

---

## ✅ Section 4: Monthly Plan Intake Readiness

- [ ] **Intake Gate section exists** — §Intake Gate section is present before planning sections (§A)
- [ ] **Intake rules stated** — Section explicitly lists what CAN be extracted (EXEC/RULE/UNRESOLVED) vs CONDITIONAL (PILOT) vs CANNOT (ADVISORY)
- [ ] **ADVISORY transformation rule stated** — Section explicitly says ADVISORY findings must NOT be extracted as assumptions, but CAN inform capacity adjustments
- [ ] **No ADVISORY leaking into planning** — Review content does NOT read like planning instructions (e.g., "Do X because human reflection says Y"); all ADVISORY content is framed as input to discussion, not directive

**FAIL:** Missing intake gate OR missing rule clarity = Monthly Plan cannot apply gate correctly next month = cannot lock until corrected

---

## ✅ Section 5: Anti-Noise / Anti-Drift

- [ ] **No speculative narrative** — No phrases like "maybe," "possibly," "probably," "seems like," "could be," "should be"; all findings are based on observed facts or explicit decision
- [ ] **No unapproved proposals** — No pilot experiments or new system changes appear that weren't listed in an ADR or decision log entry (do not present new proposals as findings)
- [ ] **No "recommended actions" bypass gate** — No suggestions that should have been decisions (e.g., "next month we should try X"); all directional content goes through §6 Focus Adjustment or §Plan Intake Gate, not mixed into findings
- [ ] **Anti-Drift check clean** — No findings appear that should have been escalated to Decision Log (e.g., major blockers, unresolved dependencies should be tagged [UNRESOLVED], not left ambiguous)

**FAIL:** Speculative language OR unapproved pilots OR hidden recommendations = cannot lock until corrected

---

## Gate Decision Matrix

| Boxes Passed | Status | Action |
|---|---|---|
| **All 5 sections** (12/12 items) | ✅ PASS | Approve review for lock |
| **4–5 sections** (10–11 items) | ⚠️ FIXABLE | Make targeted edits (estimate <15 min); recheck and lock |
| **≤3 sections** (≤9 items) | 🔴 MAJOR | Block review lock; escalate to system audit (too many boundary leaks) |

---

## How to Use This Checklist

**Step 1:** After Monthly Review content is written, print this checklist.

**Step 2:** For each item, verify against the review:
- **PASS:** Check the box ✓
- **FAIL:** Note which section fails; flag for correction

**Step 3:** Count total passed boxes.
- All 12 passed → Lock review immediately
- 10–11 passed → Fix flagged items; recheck before lock
- ≤9 passed → Escalate; do not lock until re-audited

**Step 4:** Before April Planning, apply Monthly Plan Intake Gate checklist to verify plan extraction rules.

---

## Archive

This checklist is used monthly (every month-end review). Store in `05_TEMPLATES/` (canonical process checklist).

Reference in:
- TEMPLATE_Month_Final.md (§0 DoD)
- MONTHLY_REVIEW_PROCESS_GOVERNANCE.md
- March/April/May review instructions
