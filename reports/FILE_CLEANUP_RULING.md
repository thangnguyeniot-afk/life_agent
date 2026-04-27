# File Cleanup Ruling Report

**Repository:** `d:\Life_agent` (Life Agent — Personal Operating System)  
**Ruling Date:** 2026-04-27  
**Ruling Authority:** Claude (AUDIT/PLANNING mode — no files modified)  
**Basis:** FILE_CLEANUP_AUDIT.md + local file reads (no external access)  
**Input Audit:** reports/FILE_CLEANUP_AUDIT.md

---

## 1. Executive Ruling

### Can cleanup proceed?

**YES — partially. Cleanup is safe in phases.**

| Cleanup Area | Status | Blocker |
|---|---|---|
| Phase 4 (delete empty dir + pycache) | ✅ Safe to proceed immediately | None |
| Phase 1 (navigation/link fixes in INDEX) | ✅ Safe to proceed immediately | None |
| Phase 2 (promote AMBIGUITY_GATE to OS) | ✅ Safe to proceed — clear target identified | Requires writing to TASK_INTAKE_AND_ADMISSION.md |
| Phase 3a (archive Phase 1/2 audit files) | ✅ Safe after archive structure created | Need 99_ARCHIVE/ to exist |
| Phase 3b (archive Phase 3 audit files) | 🔴 BLOCKED | Phase 3 observation runs until ~2026-05-01 |
| Phase 3c (move W11/W12 hardening docs) | ✅ Safe after archive structure created | None |
| Phase 3d (migrate cold daily files to 06_MONTHS/) | ✅ Safe — per INDEX §11 rule | None |
| Weekly plan archival (W09–W13) | 🟡 Blocked by missing archive policy | User must approve archive path first |

### What should not be touched yet

1. **`07_REVIEWS/00_SYSTEM/PHASE_3_*.md`** and **`CAPACITY_SIGNAL_AUDIT`** — Phase 3 is in observation window (April 7 – ~May 1, 2026). Not complete. These files are still active references.
2. **`07_REVIEWS/00_SYSTEM/PATCH_AUDIT_MATRIX_MARCH_HUMAN_LAYER.md`** — PILOT items (P0.2 Energy-Aware Scheduling, P0.3 Capacity Limit) may still be in pilot. Absorption status unverified.
3. **Any `03_PLANNING/03_WEEK/W09–W13/` weekly files** — until archive path is approved.
4. **`AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md`** — until its content is promoted to `TASK_INTAKE_AND_ADMISSION.md`.

---

## 2. Recommended Archive Policy

### Recommended Archive Root: `99_ARCHIVE/`

**Rationale:**
- The repo uses numbered top-level directories (`00_README/` through `08_PROJECT_CONTEXT/`).
- `08_PROJECT_CONTEXT/` occupies the `08_` slot.
- `99_ARCHIVE/` sorts naturally to the end in any directory listing, visually signaling "cold storage" without disrupting the primary 00–08 sequence.
- Avoids renumbering existing folders.
- Naming convention matches repo style (two-digit prefix + underscore + name).

**Proposed Structure:**

```
99_ARCHIVE/
  01_WEEKLY/
    W09/               ← completed week plan/execution pairs
    W10/
    W11/
    W12/
    W13/
  02_SYSTEM_REVIEWS/   ← completed system audit files from 07_REVIEWS/00_SYSTEM/
  03_PROCESS_LOGS/     ← implementation reports, generation summaries, integration change logs
  04_MONTHLY/          ← completed monthly plans (not reviews — those stay in 07_REVIEWS/)
```

**Naming Convention for Archived Files:**
- Files keep their original names (no renaming).
- Subdirectory structure preserves original path context where useful.
  - Example: `99_ARCHIVE/01_WEEKLY/W09/2026-W09_WeekPlan.md`
- Do NOT rename files on archive — original names contain dating and identity.

**Archive Index:**
- Required. Create `99_ARCHIVE/README.md` on first use listing what is archived and why.
- Not a complex index — just a timestamped log of what was moved and on what date.

**What goes where:**

| Content Type | Archive Destination |
|---|---|
| Completed week plans/executions (W09–W13) | `99_ARCHIVE/01_WEEKLY/Wxx/` |
| Historical system audit files | `99_ARCHIVE/02_SYSTEM_REVIEWS/` |
| Integration change logs (W11_DRIFT, W13_GENERATION_SUMMARY) | `99_ARCHIVE/03_PROCESS_LOGS/` |
| Implementation reports (WEEKLY_vs_DAILY) | `99_ARCHIVE/03_PROCESS_LOGS/` |
| Completed monthly plans (2026-03_March_Planning.md) | `99_ARCHIVE/04_MONTHLY/` |
| Cold daily files (W10–W13 still in 04_DAY/) | `06_MONTHS/` (existing path) — NOT 99_ARCHIVE |

**Note on cold daily files:** The existing `06_MONTHS/` path already handles daily file archival per INDEX §11. Daily files should continue flowing to `06_MONTHS/`, not to `99_ARCHIVE/`.

---

## 3. Ruling on Apr 3–5 System Audit Phase Files

### Context

- **Phase 1 (P0.1 DONE + P0.4 Closure):** ✅ ACTIVE. Patches applied to `TEMPLATE_Daily.md`. Validated.
- **Phase 2 (P0.5 Ambiguity Gate):** ✅ ACTIVE. Rule published April 5. Currently enforced as AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md.
- **Phase 3 (Capacity Hard Limit):** 🔴 OBSERVATION PERIOD. Observation runs April 7 – ~May 1. Not deployed. Decision deferred pending 4-week evidence collection.

### Ruling Table

| File | Absorbed? | Live Content Remaining? | Recommended Action | Reason | Risk if Removed Early |
|---|---|---|---|---|---|
| `LIFE_AGENT_FULL_SYSTEM_AUDIT_2026-04-03.md` | Partial — findings absorbed into patches; root audit doc serves as permanent record | NO (findings implemented) | **KEEP PERMANENT** in `07_REVIEWS/00_SYSTEM/` | Root audit anchor. The 5 top findings, production-readiness verdict, and audit scope are not duplicated elsewhere. This is the "why did we run this whole thing" record. | Lose provenance of entire Apr 3–5 patch cycle |
| `AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md` | NO — unique rule content NOT present in `TASK_INTAKE_AND_ADMISSION.md` | YES — 3-question filter, UNBLOCK TASK definition + examples, BANNED VAGUE LANGUAGE list, MINIMAL TAGGING (🟢🟡🔴) are ALL absent from canonical OS | **PROMOTE → then archive original** | Active system rule stored in review folder. Must promote content to `01_OS/TASK_INTAKE_AND_ADMISSION.md` before this file can be archived. | Loss of live operational rule if archived before promotion |
| `ANCHOR_AND_ANTIANCHOR_SCHEMA_AUDIT_2026-04-03.md` | YES — schema changes absorbed into OS templates/weekly execution | NO | **ARCHIVE** → `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Historical schema audit. Changes were implemented in Phase 1. No live rules remain here. | Low — duplicate of absorbed content |
| `CAPACITY_SIGNAL_AUDIT_2026-04-05.md` | NO — this is an ACTIVE reference for Phase 3 evidence collection | YES — Phase 3 observation criteria and signal catalogue are referenced during the April 7–May 1 window | **KEEP ACTIVE** until Phase 3 decision (~May 1) | Evidence collection framework for ongoing Phase 3 observation. Cannot archive while observation is live. | Loss of Phase 3 observation framework mid-window |
| `DESIGN_VALIDATION_INTELLIGENCE_TRANSFER_2026-04-05.md` | YES — intelligence transfer design validated and absorbed | NO | **ARCHIVE** → `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Design validation trace. Findings absorbed into templates/procedures. Historical. | Low |
| `HUMAN_LAYER_FORENSIC_ANALYSIS_MARCH_EXTENSION_2026-04-03.md` | PARTIAL — source for PATCH_AUDIT_MATRIX; need to verify PILOT items before archiving | Possibly — PILOT items (P0.2, P0.3) may not be fully resolved | **HOLD** until PATCH_AUDIT_MATRIX PILOT status is confirmed | Source document for PROMOTE/PILOT/HOLD decisions. If PILOT items are still active, forensic context is still needed. | Medium — may lose rationale for active pilots |
| `MONTHLY_REVIEW_PROCESS_AUDIT_AND_PATCH_2026-04-03.md` | YES — monthly review process improvements absorbed into MONTHLY_REVIEW_PROCESS_GOVERNANCE.md | NO | **ARCHIVE** → `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Phase 1 scope audit, complete. | Low |
| `MONTH_END_CONTEXT_TRANSFER_AUDIT_2026-04-05.md` | YES — context transfer design absorbed into templates | NO | **ARCHIVE** → `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Historical design audit for intelligence transfer. | Low |
| `PATCH_AUDIT_MATRIX_MARCH_HUMAN_LAYER.md` | PARTIAL — PROMOTE items (P0.1, P0.4) implemented; PILOT items (P0.2, P0.3) status unknown | YES — PILOT status unverified | **HOLD** — do not archive until PILOT item status is confirmed | Governance decision matrix. PILOT items (capacity rule, energy scheduling) are in scope for Phase 3 observation. Removing now risks losing governance rationale for still-active pilots. | High — governance decisions for active pilots lost |
| `PHASE_1_VALIDATION_P0_PATCHES_2026-04-05.md` | YES — validation complete; patches confirmed in TEMPLATE_Daily.md | NO | **ARCHIVE** → `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Phase 1 closed. Validation trace is historical. | Low |
| `PHASE_2_SUMMARY_2026-04-05.md` | YES — summary of Phase 2 implementation; rule itself lives in AMBIGUITY_GATE_RULE | NO (summary only) | **ARCHIVE** after AMBIGUITY_GATE is promoted → `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Historical summary. Wait for AMBIGUITY_GATE promotion first to avoid confusion. | Low, but ordering matters |
| `PHASE_2_VALIDATION_P0_PATCHES_2026-04-05.md` | YES — validates P0.5 implementation; historical | NO | **ARCHIVE** after AMBIGUITY_GATE is promoted → `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Same timing dependency as PHASE_2_SUMMARY. | Low |
| `PHASE_3_PREPARATION_SUMMARY_2026-04-05.md` | NO — Phase 3 not deployed yet | YES — active preparation doc for ongoing observation (April 7 – ~May 1) | **KEEP ACTIVE** until Phase 3 decision | Phase 3 observation is running now. This doc defines the deployment criteria. Cannot archive until decision is made. | High — lose Phase 3 deployment criteria mid-observation |
| `PHASE_3_READINESS_CAPACITY_CONTROL_2026-04-05.md` | NO — Phase 3 not deployed | YES — defines what evidence is needed and when to deploy | **KEEP ACTIVE** until Phase 3 decision | Companion to PHASE_3_PREPARATION_SUMMARY. Still the active reference. | High — same as above |
| `SYSTEM_AUDIT_P0_PATCHES_2026-04-05.md` | YES — pre-implementation audit; findings drove the patches that are now applied | NO active rules; baseline state documentation | **ARCHIVE** → `99_ARCHIVE/02_SYSTEM_REVIEWS/` — but after Phase 3 decision | Useful baseline ("before" state for P0 patches). No live rules. Can archive once Phase 3 observation closes (not blocking, but keep nearby for context during observation). | Low; prefer to wait until May 1 |
| `SYSTEM_CHANGE_REVIEW_SCHEMA_AUDIT_2026-04-03.md` | YES — schema change process absorbed into weekly template change procedures | NO | **ARCHIVE** → `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Historical schema review. | Low |

### Summary Ruling: Apr 3–5 Files

- **KEEP PERMANENT (never archive):** 1 file — `LIFE_AGENT_FULL_SYSTEM_AUDIT_2026-04-03.md`
- **KEEP ACTIVE (observe until ~May 1):** 4 files — `CAPACITY_SIGNAL_AUDIT`, `PHASE_3_PREPARATION_SUMMARY`, `PHASE_3_READINESS_CAPACITY_CONTROL`, `PATCH_AUDIT_MATRIX`
- **HOLD (pending PILOT status):** 1 file — `HUMAN_LAYER_FORENSIC_ANALYSIS`
- **PROMOTE THEN ARCHIVE:** 1 file — `AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md`
- **ARCHIVE (safe now):** 6 files — `ANCHOR_AND_ANTIANCHOR`, `DESIGN_VALIDATION`, `MONTHLY_REVIEW_PROCESS_AUDIT`, `MONTH_END_CONTEXT_TRANSFER`, `PHASE_1_VALIDATION`, `SYSTEM_CHANGE_REVIEW_SCHEMA`
- **ARCHIVE (after AMBIGUITY_GATE promoted):** 2 files — `PHASE_2_SUMMARY`, `PHASE_2_VALIDATION`
- **ARCHIVE (after Phase 3 decision, ~May 1):** 2 files — `SYSTEM_AUDIT_P0_PATCHES`, then `CAPACITY_SIGNAL_AUDIT` + `PHASE_3_*` (if Phase 3 resolved)

---

## 4. Ruling on AMBIGUITY_GATE_RULE

### Verdict: PROMOTE to `01_OS/TASK_INTAKE_AND_ADMISSION.md`

**Evidence:**
- `TASK_INTAKE_AND_ADMISSION.md` §7 Rule 2 states: "If ambiguity ≥ 4, task may NOT be scheduled for direct execution." This partially overlaps with AMBIGUITY_GATE_RULE but does NOT contain the gate's operational specifics.
- `AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md` contains the following content NOT present anywhere in TASK_INTAKE_AND_ADMISSION.md:
  1. **3-Question Filter** — the core gate questions ("Can DONE be written? Can work start immediately? If it stalls, will I know why?")
  2. **UNBLOCK TASK definition** — concept + characteristics (size S/small-M, output = clarity, time ≤ 90 min) + 4 worked examples
  3. **BANNED VAGUE LANGUAGE list** — 10 banned phrases ("improve X", "continue working on X", "research more", etc.) + the exception rule
  4. **HIGH-AMBIGUITY RULE** — 4 conditions that trigger "high ambiguity" classification
  5. **MINIMAL TAGGING system** — the 🟢🟡🔴 label system for planning visibility (not the scoring system)
  6. **ENFORCEMENT POINTS checklist** — weekly planning / daily planning / ad-hoc scheduling check items
  7. **RELATIONSHIP TO OTHER PHASES** — explicit P0.1/P0.4/P0.5/P0.2 relationship table

**Target canonical file:** `01_OS/TASK_INTAKE_AND_ADMISSION.md`

**Exact target section:**  
The 3-Question Filter, BANNED VAGUE LANGUAGE, UNBLOCK TASK definition, and HIGH-AMBIGUITY RULE belong in a **new §7.5** ("Ambiguity Gate — Pre-Admission Filter") inserted between §7 (Hard Admission Rules) and §8 (Project-Aware Defaults). This placement is coherent because §7 already defines Rules 1–6, and §7.5 explicitly formalizes the ambiguity gate that Rule 2 references.

The MINIMAL TAGGING system (🟢🟡🔴) and ENFORCEMENT POINTS checklist belong in a **new §10.5** ("Task Status Labeling") inserted after §10 (Admission Checklist).

The PHASE RELATIONSHIPS table can be noted in a short trace annotation near §7 Rule 2, or preserved only in the archived AMBIGUITY_GATE_RULE file.

**Content to extract (verbatim, not summarized):**
- §7.5 — Full 3-Question Filter block (3 questions + decision rule)
- §7.5 — Full UNBLOCK TASK definition (characteristics + 4 examples)
- §7.5 — Full BANNED VAGUE LANGUAGE list (10 items + exception rule)
- §7.5 — HIGH-AMBIGUITY RULE (4 conditions + gate rule + example)
- §10.5 — MINIMAL TAGGING system (🟢/🟡/🔴 labels)
- §10.5 — ENFORCEMENT POINTS checklist (3 enforcement contexts)

**What to do with the original file after absorption:**
- Add a note at top: `> This rule has been absorbed into 01_OS/TASK_INTAKE_AND_ADMISSION.md §7.5 as of [date]. This file is the original publication record.`
- Then archive to `99_ARCHIVE/02_SYSTEM_REVIEWS/`
- Do NOT delete — preserves publication date, phase relationship table, and VALIDATION CHECKLIST which are useful historical context

**Trace note to preserve:**
The original file has a RELATIONSHIP TO OTHER PHASES table linking P0.1/P0.4/P0.5/P0.2. This table should be preserved either in the archived file or as a comment in TASK_INTAKE_AND_ADMISSION.md §7.5 intro.

---

## 5. Ruling on Knowledge Placeholder Folders

| Folder | Current State | Intended Role | Recommended Action | Reason |
|---|---|---|---|---|
| `knowledge/adr/` | `.gitkeep` only; actual ADRs live in `04_LOGS/ADR/` | Intended as ADR location per `knowledge/` taxonomy, but OS §13 routes ADRs to `04_LOGS/ADR/` | **REMOVE `.gitkeep` and collapse directory** | Creates navigation ambiguity. Two ADR locations will confuse agents. `04_LOGS/ADR/` is the established, referenced location. Removing `knowledge/adr/` eliminates false destination. |
| `knowledge/design/` | `.gitkeep` only; no content exists anywhere else for design docs | OS §13 identifies design documents (interface sketches, architecture notes) as a knowledge artifact type; no alternative location exists | **KEEP — add `README.md`** explaining role | Design documents (output of architecture tasks) belong here per OS §13. No conflict with other locations. The empty state is correct — no design docs yet, not a duplication problem. Add README.md with: what goes here, what format, when to use. |
| `knowledge/research/` | `.gitkeep` only; research spikes go to `04_LOGS/Spike_Log.md` | OS §13 mentions research notes; `Spike_Log.md` captures spike outcomes, not raw research notes | **KEEP — add `README.md`** distinguishing from Spike_Log | `Spike_Log.md` records completed spike outcomes. `knowledge/research/` is for persistent research notes (not tied to a specific week). Distinct roles. Add README.md clarifying: "Research notes go here (not spike outcomes — those go to 04_LOGS/Spike_Log.md)." |
| `knowledge/summaries/` | Has content: `EXEC_PATTERNS_CAPACITY_ENERGY.md` | Reusable pattern summaries | **KEEP as-is** — add to INDEX §6 | Working correctly. Only missing: INDEX reference. |

**Action blocked requiring user decision:**
- The `knowledge/adr/` removal is low-risk (no content) but constitutes a directory collapse. User should approve.

---

## 6. Ruling on `W11_DRIFT_LAYER_INTEGRATION.md`

**Current classification in Audit:** F (DO_NOT_TOUCH_UNCLEAR)

**Ruling: Reclassify to D (ARCHIVE_NOT_DELETE) → move to `99_ARCHIVE/03_PROCESS_LOGS/`**

### Evidence of Absorption

`GENERATE_WEEKLY_EXECUTION.md` Table of Contents (line 26, confirmed by read):
```
- [11.5. Drift Detection Layer: Design & Integration](#115-drift-detection-layer-design--integration)
```

The drift detection layer WAS integrated into `GENERATE_WEEKLY_EXECUTION.md` at §11.5 (confirmed in the integration doc itself, §7, which documents the exact lines added). The live rules (6 drift categories, 7-signal schema, GREEN/YELLOW/ORANGE/RED states, response rules, daily inheritance protocol) all live in §11.5 of the generator.

### What this file IS

`W11_DRIFT_LAYER_INTEGRATION.md` is an **integration change log**, not a live procedure. It documents:
- What was added to which generator section (§12: "Files Modified — Clean Audit" table)
- The design rationale for why drift detection was needed (§1, §11)
- Gaming resistance analysis (§11: "What This Protects Against")
- Pre-execution validation checklist (§13)
- Success criteria (§14)

The live procedural content is in GENERATE_WEEKLY_EXECUTION.md. This file is the "why and how we built it" record.

### Why immediate deletion is NOT safe

The gaming resistance analysis (§11) and design rationale (§1) are NOT duplicated in GENERATE_WEEKLY_EXECUTION.md §11.5. They explain why the system was designed this way, which future agents/reviewers need to understand if they question the 5-minute check protocol or the GREEN/YELLOW/ORANGE thresholds.

### Misplacement issue

File is at `03_PLANNING/03_WEEK/W11_DRIFT_LAYER_INTEGRATION.md` (week root level), not inside `03_PLANNING/03_WEEK/W11/`. This misplacement makes it appear to be part of the week's planning artifacts, which it is not. Moving it to archive corrects the misplacement without any content loss.

### Recommendation

1. Move to `99_ARCHIVE/03_PROCESS_LOGS/W11_DRIFT_LAYER_INTEGRATION.md`
2. Add archive note at top of file on move: `> Integration change log. Drift layer is live in GENERATE_WEEKLY_EXECUTION.md §11.5.`
3. Do not delete.

---

## 7. Revised Cleanup Categories

Based on this ruling, several files are reclassified:

### Category A — KEEP_CANONICAL

**Additions from D:**
- `07_REVIEWS/00_SYSTEM/PHASE_3_PREPARATION_SUMMARY_2026-04-05.md` (Phase 3 observation active)
- `07_REVIEWS/00_SYSTEM/PHASE_3_READINESS_CAPACITY_CONTROL_2026-04-05.md` (Phase 3 observation active)
- `07_REVIEWS/00_SYSTEM/CAPACITY_SIGNAL_AUDIT_2026-04-05.md` (Phase 3 observation evidence)

**Net change:** +3

### New Category — PROMOTE (subset of previous A/F)

- `07_REVIEWS/00_SYSTEM/AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md` — must be promoted to `TASK_INTAKE_AND_ADMISSION.md` before any archival action

**Net:** 1 file in PROMOTE queue (previously miscounted as A but with a flag)

### Category C — CONSOLIDATE_BEFORE_DELETE

**Removals from C (moved to appropriate categories):**
- `PATCH_AUDIT_MATRIX_MARCH_HUMAN_LAYER.md` → moved to HOLD (D-BLOCKED)
- `SYSTEM_AUDIT_P0_PATCHES_2026-04-05.md` → moved to D (archive after Phase 3)

**Net change:** -2 from C → C now has ~20 files

### Category D — ARCHIVE_NOT_DELETE

**Additions:**
- `W11_DRIFT_LAYER_INTEGRATION.md` (from F)
- `PATCH_AUDIT_MATRIX_MARCH_HUMAN_LAYER.md` (from C, HOLD status)
- `SYSTEM_AUDIT_P0_PATCHES_2026-04-05.md` (from C)
- `HUMAN_LAYER_FORENSIC_ANALYSIS_MARCH_EXTENSION_2026-04-03.md` (HOLD sub-status)

**Removals:** PHASE_3_PREPARATION_SUMMARY, PHASE_3_READINESS, CAPACITY_SIGNAL_AUDIT → moved to A

**Net: D ≈ 19 files**

### Category E — DELETE_CANDIDATE_LOW_RISK

Unchanged: 8 files (`06_MONTHS/March/` empty dir + 6 pycache + `.ticktick/` note)

Actually `.ticktick/` files are gitignored runtime files — they were listed in the audit as A. E remains: 1 empty dir + 6 pycache = **7 content files** (the empty dir is a dir, not a file).

### Category F — DO_NOT_TOUCH_UNCLEAR

**Removals:**
- `W11_DRIFT_LAYER_INTEGRATION.md` → moved to D
- `AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md` → moved to PROMOTE

**Remaining F:**
- `04_LOGS/WEEKLY_vs_DAILY_PLACEMENT_RULE_IMPLEMENTATION_REPORT.md`
- `03_PLANNING/03_WEEK/W13/W13_GENERATION_SUMMARY.md`
- `knowledge/adr/.gitkeep` (ruling: remove, pending user approval)
- `knowledge/design/.gitkeep` (ruling: keep, add README)
- `knowledge/research/.gitkeep` (ruling: keep, add README)

**Net: F ≈ 5 files**

### Revised Count Summary

| Category | Original | Revised | Delta |
|---|---|---|---|
| A — KEEP_CANONICAL | 97 | 100 | +3 |
| PROMOTE (new) | — | 1 | +1 |
| B — KEEP_ACTIVE_NEEDS_LINKING | 9 | 9 | 0 |
| C — CONSOLIDATE_BEFORE_DELETE | 22 | 20 | -2 |
| D — ARCHIVE_NOT_DELETE | 18 | 19 | +1 |
| E — DELETE_CANDIDATE_LOW_RISK | 8 | 8 | 0 |
| F — DO_NOT_TOUCH_UNCLEAR | 9 | 5 | -4 |
| **Total** | **163** | **162** | (-1 due to ruling on empty dir reclassification) |

---

## 8. Safe Patch Plan

### Phase 1 — Navigation / Link Fixes Only

**Estimated files to edit:** `00_README/INDEX.md` (primary), possibly `03_PLANNING/02_MONTH/2026-04_April_Plan.md`

**Target edits:**

| Action | File | Section | Purpose | Risk |
|---|---|---|---|---|
| Add Intelligence/ folder reference | `00_README/INDEX.md` | §4 Context & Logs | `04_LOGS/Intelligence/` pattern not documented | None |
| Add knowledge/summaries reference | `00_README/INDEX.md` | §6 Knowledge System | `EXEC_PATTERNS_CAPACITY_ENERGY.md` invisible | None |
| Add TEMPLATE_Command_Pack.md | `00_README/INDEX.md` | §2 Canonical Templates | Missing from template listing | None |
| Add GENERATE_PEC.prompt.md | `00_README/INDEX.md` | §6c Automation Layer | Only referenced in TICKTICK_BRIDGE_SPEC | None |
| Add tools/README.md reference | `00_README/INDEX.md` | §6c Automation Layer | Tools folder undiscoverable from INDEX | None |
| Add Intelligence_Transfer cross-link | `03_PLANNING/02_MONTH/2026-04_April_Plan.md` | Header or references section | Intelligence transfer not linked from plan | Low |

**Pre-condition:** None. Safe to run immediately.  
**Approver:** User.  
**Actor:** Claude or Copilot.

---

### Phase 2 — Promote Live Rules Into Canonical OS Docs

**Single target:** `01_OS/TASK_INTAKE_AND_ADMISSION.md`  
**Source:** `07_REVIEWS/00_SYSTEM/AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md`

**Content extraction plan:**

| New Section | Location in TASK_INTAKE | Content to Copy | Source Lines |
|---|---|---|---|
| §7.5 — Ambiguity Gate Pre-Admission Filter | After §7 Rule 6 | 3-Question Filter + Decision Rule | AMBIGUITY_GATE §CORE GATE |
| §7.5 (continued) | Same | UNBLOCK TASK definition + characteristics + 4 examples | AMBIGUITY_GATE §UNBLOCK TASK |
| §7.5 (continued) | Same | BANNED VAGUE LANGUAGE list + exception rule | AMBIGUITY_GATE §BANNED VAGUE LANGUAGE |
| §7.5 (continued) | Same | HIGH-AMBIGUITY RULE (4 conditions + gate) | AMBIGUITY_GATE §HIGH-AMBIGUITY RULE |
| §10.5 — Task Status Labeling | After §10 Admission Checklist | MINIMAL TAGGING system (🟢🟡🔴) | AMBIGUITY_GATE §MINIMAL TAGGING |
| §10.5 (continued) | Same | ENFORCEMENT POINTS checklist | AMBIGUITY_GATE §ENFORCEMENT POINTS |

**Post-promotion action on source file:**
- Add header note to `AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md`:
  `> Absorbed into 01_OS/TASK_INTAKE_AND_ADMISSION.md §7.5 on [date]. This file is the original publication record (Phase 2 rule, April 5, 2026).`
- Then queue for archive after Phase 2 validation completes.

**Pre-condition:** Phase 1 must be complete (INDEX links updated so agents can find TASK_INTAKE more easily).  
**Approver:** User + GPT review (this touches a canonical OS spec — rule 2 of §7 exists and must mesh with new §7.5).  
**Actor:** Claude (long-form content integration, boundary-aware).

---

### Phase 3 — Create Archive Structure + Archive Historical Files

**Step 1: Create `99_ARCHIVE/` with subfolders and README**

```
99_ARCHIVE/
  README.md              ← archive index (what was moved, when, why)
  01_WEEKLY/             ← completed week plan/execution pairs
  02_SYSTEM_REVIEWS/     ← historical system audit/review files
  03_PROCESS_LOGS/       ← change logs, generation summaries, implementation reports
  04_MONTHLY/            ← completed monthly plans
```

**Step 2: Archive `07_REVIEWS/00_SYSTEM/` historical phase files (safe now)**

Move to `99_ARCHIVE/02_SYSTEM_REVIEWS/`:
1. `ANCHOR_AND_ANTIANCHOR_SCHEMA_AUDIT_2026-04-03.md`
2. `DESIGN_VALIDATION_INTELLIGENCE_TRANSFER_2026-04-05.md`
3. `MONTHLY_REVIEW_PROCESS_AUDIT_AND_PATCH_2026-04-03.md`
4. `MONTH_END_CONTEXT_TRANSFER_AUDIT_2026-04-05.md`
5. `PHASE_1_VALIDATION_P0_PATCHES_2026-04-05.md`
6. `SYSTEM_CHANGE_REVIEW_SCHEMA_AUDIT_2026-04-03.md`

Move to `99_ARCHIVE/02_SYSTEM_REVIEWS/` **after AMBIGUITY_GATE promotion:**
7. `PHASE_2_SUMMARY_2026-04-05.md`
8. `PHASE_2_VALIDATION_P0_PATCHES_2026-04-05.md`
9. `AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md` (after promotion + header note)

Move to `99_ARCHIVE/02_SYSTEM_REVIEWS/` **after Phase 3 observation (~May 1):**
10. `SYSTEM_AUDIT_P0_PATCHES_2026-04-05.md`
11. `CAPACITY_SIGNAL_AUDIT_2026-04-05.md`
12. `PHASE_3_PREPARATION_SUMMARY_2026-04-05.md`
13. `PHASE_3_READINESS_CAPACITY_CONTROL_2026-04-05.md`

**Step 3: Move W11/W12 hardening docs from `01_OS/04_OPERATIONS/WEEKLY_CONTROL/`**

Move to `99_ARCHIVE/02_SYSTEM_REVIEWS/`:
- `W11_HARDENING_PATCH_SUMMARY.md`
- `W12_HARDENING_EXECUTIVE_SUMMARY.md`
- `W12_HARDENING_PATCH_WEEKEND_OVERFLOW.md`
- `W12_IMPLEMENTATION_GUIDE_V13_V14.md`
- `REVIEW_V13_V14_APPROVAL.md`

**Step 4: Archive process logs and integration change docs**

Move to `99_ARCHIVE/03_PROCESS_LOGS/`:
- `03_PLANNING/03_WEEK/W11_DRIFT_LAYER_INTEGRATION.md` (confirmed absorbed)
- `04_LOGS/WEEKLY_vs_DAILY_PLACEMENT_RULE_IMPLEMENTATION_REPORT.md` (pending user ruling — safe if user confirms no current reference)

Move to `99_ARCHIVE/03_PROCESS_LOGS/` (after W13 archived):
- `03_PLANNING/03_WEEK/W13/W13_GENERATION_SUMMARY.md`

**Step 5: Migrate cold daily files to `06_MONTHS/`** (per INDEX §11 existing rule)

Move `03_PLANNING/04_DAY/W10–W13/` files:
- W10 dailies (7 files: 2026-03-09 through 2026-03-15) → `06_MONTHS/2026-03_March/`
- W11 dailies (7 files: 2026-03-16 through 2026-03-22) → `06_MONTHS/2026-03_March/`
- W12 dailies (6 files: 2026-03-23 through 2026-03-28) → `06_MONTHS/2026-03_March/`
- W13 daily (1 file: 2026-03-30) → create `06_MONTHS/2026-04_April/` + move there

**Step 6: Archive completed monthly plan**

Move `03_PLANNING/02_MONTH/2026-03_March_Planning.md` → `99_ARCHIVE/04_MONTHLY/`

**Step 7: Archive knowledge placeholder cleanup**

- Remove `knowledge/adr/.gitkeep` (and directory) — **pending user approval**
- Add `knowledge/design/README.md` explaining what goes there (interface sketches, architecture notes per OS §13)
- Add `knowledge/research/README.md` explaining distinction from `04_LOGS/Spike_Log.md`

**Archive index requirement:** Update `99_ARCHIVE/README.md` with each move.

**Pre-condition:** `99_ARCHIVE/` directory structure must exist first.  
**Approver:** User for each sub-step. Do not batch moves without per-step approval.  
**Actor:** Copilot (file moves are mechanical; Claude for README writing).

---

### Phase 4 — Delete Generated / Temp / Empty Files

**Safe to delete immediately with user approval:**

| Target | Type | Reason |
|---|---|---|
| `06_MONTHS/March/` | Empty directory | Legacy naming; no content; real data in `2026-03_March/` |
| `tools/__pycache__/auth_ticktick.cpython-314.pyc` | Python bytecode | Gitignored; regenerates automatically |
| `tools/__pycache__/export_ticktick_batch.cpython-314.pyc` | Python bytecode | Same |
| `tools/__pycache__/lookup_ticktick_project.cpython-314.pyc` | Python bytecode | Same |
| `tools/__pycache__/smoke_ticktick_task.cpython-314.pyc` | Python bytecode | Same |
| `tools/__pycache__/test_ticktick_task_fields.cpython-314.pyc` | Python bytecode | Same |
| `tools/__pycache__/validate_pec.cpython-314.pyc` | Python bytecode | Same |

**Pre-delete reference check:** None required — empty directory and gitignored bytecode confirmed via local read.  
**Approver:** User.  
**Actor:** Any.

---

### Phase 5 — Re-Run Local Reference Audit

After Phases 1–4 complete, verify:

| Check | Command/Method | What Must Be True |
|---|---|---|
| INDEX references intact | Search for broken `[text](path)` links in `00_README/INDEX.md` | No path references to moved/deleted files |
| BOOTSTRAP intact | Read `00_README/BOOTSTRAP.md` | All referenced files still exist at referenced paths |
| 01_OS procedures intact | Grep for W11/W12 hardening file names in `01_OS/` | No remaining references to moved files |
| GENERATE_WEEKLY_EXECUTION intact | Read §11.5 TOC entry | Still present; not accidentally removed |
| TASK_INTAKE_AND_ADMISSION updated | Read §7.5 | New section present; content matches AMBIGUITY_GATE extraction |
| 99_ARCHIVE README complete | Read `99_ARCHIVE/README.md` | All archived files listed with date and reason |
| knowledge/ structure clean | List `knowledge/` | No `adr/` folder; `design/` and `research/` have README.md |
| 06_MONTHS/ complete | List `06_MONTHS/` | W10–W13 cold dailies present; no W10–W13 remaining in `04_DAY/` |

**Actor:** Claude (audit); user verifies final state.

---

## 9. Do-Not-Touch List

Files and folders that must NOT be modified, moved, or deleted in the next cleanup patch, even if they appear redundant or cold:

| File / Folder | Reason |
|---|---|
| `07_REVIEWS/00_SYSTEM/PHASE_3_PREPARATION_SUMMARY_2026-04-05.md` | Phase 3 observation active until ~May 1. Active reference. |
| `07_REVIEWS/00_SYSTEM/PHASE_3_READINESS_CAPACITY_CONTROL_2026-04-05.md` | Same. Contains deployment criteria for Phase 3. |
| `07_REVIEWS/00_SYSTEM/CAPACITY_SIGNAL_AUDIT_2026-04-05.md` | Active evidence reference for Phase 3 observation window. |
| `07_REVIEWS/00_SYSTEM/PATCH_AUDIT_MATRIX_MARCH_HUMAN_LAYER.md` | PILOT items (P0.2, P0.3) status unconfirmed. Governance decisions must stay accessible. |
| `07_REVIEWS/00_SYSTEM/HUMAN_LAYER_FORENSIC_ANALYSIS_MARCH_EXTENSION_2026-04-03.md` | Source for PATCH_AUDIT_MATRIX. Hold until PILOT status confirmed. |
| `07_REVIEWS/00_SYSTEM/LIFE_AGENT_FULL_SYSTEM_AUDIT_2026-04-03.md` | Permanent record. Never archive. |
| `07_REVIEWS/00_SYSTEM/AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md` | Do not archive — must promote first. |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/CAPACITY_ENGINE.md` | Core engine. Do not touch — hardening docs next to it will move but this stays. |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/GENERATE_WEEKLY_EXECUTION.md` | §11.5 drift layer lives here. Do not touch during cleanup. |
| `03_PLANNING/03_WEEK/W14/` (all) | Current week. Do not archive or touch. |
| `03_PLANNING/04_DAY/W14/` (all) | Current week. Do not archive or touch. |
| `03_PLANNING/02_MONTH/2026-04_April_Plan.md` | Active month. |
| `03_PLANNING/02_MONTH/2026-04_Intelligence_Transfer.md` | Active intelligence transfer in progress. |
| `04_LOGS/Decision_Log.md`, `Idea_Parking_Lot.md`, `Spike_Log.md` | Permanent append-only logs. Never archive. |
| `04_LOGS/ADR/ADR-20260322_HUMAN_LAYER_Q2_PILOT.md` | Active ADR; Q2 pilot in progress. |
| `05_TEMPLATES/` (all) | Single source of truth. Do not touch during cleanup. |
| `08_PROJECT_CONTEXT/` (all) | Project snapshots. Do not touch during cleanup. |
| `tools/` (all .py files) | Active TickTick bridge. Do not touch. |
| `knowledge/summaries/EXEC_PATTERNS_CAPACITY_ENERGY.md` | Active content. Only needs INDEX link added. |

---

## 10. User Decisions Needed

### Decision 1: Approve `99_ARCHIVE/` as archive root

**Options:**
- A. Create `99_ARCHIVE/` with the structure proposed (recommended)
- B. Use a different name (`08_ARCHIVE/` requires renaming `08_PROJECT_CONTEXT/` — not recommended)
- C. Keep historical files in-place with an archive subfolder inside existing directories

**Recommended default:** Option A — `99_ARCHIVE/`

**Consequence if deferred:** No historical files can be moved. Phases 3 and parts of Phase 2 are blocked.

---

### Decision 2: Confirm Phase 3 observation is ongoing

**Question:** Is the April 7 – May 1 observation window still active? Have you been collecting capacity signals as defined in `PHASE_3_READINESS_CAPACITY_CONTROL_2026-04-05.md`?

**Options:**
- A. Yes, observation is ongoing → keep Phase 3 files active until ~May 1
- B. Phase 3 was paused or cancelled → can archive Phase 3 files now
- C. Phase 3 completed early → archive Phase 3 files + define deployment

**Recommended default:** Option A (assume observation is ongoing per document).

**Consequence if deferred:** Phase 3 files remain in active area, which is correct. No urgency.

---

### Decision 3: Confirm PILOT status for P0.2 and P0.3

**Question:** Are capacity hard limit (P0.2) and energy-aware scheduling (P0.3) still in pilot, or were they abandoned/promoted?

**Context:** `PATCH_AUDIT_MATRIX_MARCH_HUMAN_LAYER.md` designates P0.2 and P0.3 as PILOT (test only, no template integration). Their status determines when PATCH_AUDIT_MATRIX and HUMAN_LAYER_FORENSIC can be archived.

**Options:**
- A. Still in pilot → keep both files on hold
- B. Abandoned → archive both files now
- C. Promoted to system rules → absorb into OS before archiving

**Recommended default:** Option A (treat as still in pilot per documentation).

**Consequence if deferred:** 2 files remain on HOLD, which is safe.

---

### Decision 4: Approve `knowledge/adr/` directory removal

**Question:** Remove `knowledge/adr/.gitkeep` and collapse the `knowledge/adr/` directory?

**Context:** ADRs are documented in `04_LOGS/ADR/` per OS §13. The `knowledge/adr/` placeholder creates a false navigation destination. No content is at risk — directory is empty.

**Options:**
- A. Yes, remove — ADRs live in `04_LOGS/ADR/` only
- B. Keep — intent is to eventually migrate ADRs to `knowledge/adr/` (future plan)
- C. Keep — no urgency; revisit later

**Recommended default:** Option A (remove confusion; keep OS §13 referencing `04_LOGS/ADR/`).

**Consequence if deferred:** Minor navigation confusion. Low urgency.

---

### Decision 5: Confirm archive policy for completed weekly plan/execution files (W09–W13)

**Question:** Should completed week plans and execution files be archived to `99_ARCHIVE/01_WEEKLY/` or remain in `03_PLANNING/03_WEEK/`?

**Context:** INDEX §11 defines archival only for **daily** files (hot 15-day window). No archival rule exists for weekly files. W09–W13 are cold and completed.

**Options:**
- A. Move to `99_ARCHIVE/01_WEEKLY/Wxx/` — clean separation of active vs historical
- B. Keep in `03_PLANNING/03_WEEK/` permanently — they are lightweight and navigation-accessible
- C. Add formal archival rule to INDEX §11 before moving anything

**Recommended default:** Option B for now, with Option C as next step. Weekly files are small. No urgency to move. Defining the rule first is safer.

**Consequence if deferred:** W09–W13 remain in `03_PLANNING/03_WEEK/`. No harm. INDEX §11 should be updated at next review cadence.

---

### Decision 6: Approve AMBIGUITY_GATE_RULE promotion to `TASK_INTAKE_AND_ADMISSION.md`

**Question:** Approve inserting §7.5 and §10.5 into `TASK_INTAKE_AND_ADMISSION.md` as described in §4 of this ruling?

**Context:** The content is a live system rule that currently exists only in a review folder. Promotion is low-risk (additive change to canonical OS doc) and eliminates the misclassification.

**Options:**
- A. Yes — proceed with promotion as described (recommended)
- B. Create a new file in `01_OS/` instead of adding to TASK_INTAKE
- C. Leave in review folder — live there permanently

**Recommended default:** Option A. The 3-question filter and UNBLOCK TASK concept are semantically adjacent to TASK_INTAKE_AND_ADMISSION §7 (Hard Admission Rules). They belong in the same spec.

**Consequence if deferred:** Rule remains stored in review folder, making it invisible to agents reading TASK_INTAKE_AND_ADMISSION as the admission authority.

---

## Summary: Decision Priority

| # | Decision | Urgency | Safe Default if Deferred |
|---|---|---|---|
| 1 | Approve `99_ARCHIVE/` as archive root | HIGH — blocks Phase 3 | Phase 3 stays blocked |
| 2 | Confirm Phase 3 observation status | MEDIUM — affects 4 files | Treat as ongoing |
| 3 | Confirm PILOT P0.2/P0.3 status | MEDIUM — affects 2 files | Treat as still in pilot |
| 4 | Approve `knowledge/adr/` removal | LOW | Keep placeholder |
| 5 | Confirm weekly file archive policy | LOW | Keep W09–W13 in place |
| 6 | Approve AMBIGUITY_GATE promotion | HIGH — enables Phase 2 | Rule stays in review folder |

---

*Report generated by Claude in AUDIT/PLANNING mode. No project files were modified, moved, or deleted. Only this report file was created at `reports/FILE_CLEANUP_RULING.md`. No online, GitHub, MCP, or remote access was used.*
