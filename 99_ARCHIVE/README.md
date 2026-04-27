# 99_ARCHIVE — Cold Storage

This folder holds files that are complete, historical, and no longer actively referenced — but are preserved because they contain design rationale, phase decisions, execution traces, or prompt conventions that may be needed for future reference or audit.

**This is not deletion.** Files here are cold, not gone.

---

## Policy

- **Filenames are preserved.** Do not rename files on archive. Original names carry dating and identity.
- **Original path context is noted.** The archive index below records where each file came from.
- **Do not archive files that still contain live rules.** Live rules must be promoted into canonical OS docs first (see `01_OS/` and `TASK_INTAKE_AND_ADMISSION.md`).
- **Do not archive Phase 3 observation files** until Phase 3 (Capacity Hard Limit) observation is explicitly closed (~2026-05-01 or later). Current Phase 3 files remain in `07_REVIEWS/00_SYSTEM/`.
- **Weekly W09–W13 archive policy is not yet approved.** Do not archive completed weekly files until the archive policy is confirmed.

---

## Folder Structure

```
99_ARCHIVE/
  01_WEEKLY/          — completed week plan and execution file pairs (W09–W13 and earlier)
  02_SYSTEM_REVIEWS/  — historical system audit, phase validation, and patch review files
  03_PROCESS_LOGS/    — implementation reports, generation summaries, integration change logs
  04_MONTHLY/         — completed monthly plan files (not reviews; those stay in 07_REVIEWS/)
```

---

## Archive Index

Files are logged here when moved. Format:

| Date Moved | Original Path | Destination | Reason |
|---|---|---|---|
| 2026-04-27 | `07_REVIEWS/00_SYSTEM/ANCHOR_AND_ANTIANCHOR_SCHEMA_AUDIT_2026-04-03.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Phase 1 schema audit complete; findings absorbed into OS templates and weekly execution |
| 2026-04-27 | `07_REVIEWS/00_SYSTEM/DESIGN_VALIDATION_INTELLIGENCE_TRANSFER_2026-04-05.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Phase 2 design validation complete; intelligence transfer design absorbed into templates |
| 2026-04-27 | `07_REVIEWS/00_SYSTEM/MONTHLY_REVIEW_PROCESS_AUDIT_AND_PATCH_2026-04-03.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Phase 1 monthly review audit complete; findings absorbed into MONTHLY_REVIEW_PROCESS_GOVERNANCE.md |
| 2026-04-27 | `07_REVIEWS/00_SYSTEM/MONTH_END_CONTEXT_TRANSFER_AUDIT_2026-04-05.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Phase 2 context transfer audit complete; design absorbed into templates |
| 2026-04-27 | `07_REVIEWS/00_SYSTEM/PHASE_1_VALIDATION_P0_PATCHES_2026-04-05.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Phase 1 validation complete; P0.1 (DONE) and P0.4 (Closure) patches confirmed applied to TEMPLATE_Daily.md |
| 2026-04-27 | `07_REVIEWS/00_SYSTEM/SYSTEM_CHANGE_REVIEW_SCHEMA_AUDIT_2026-04-03.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Phase 1 system change review schema audit complete; absorbed into OS procedures |
| 2026-04-27 | `07_REVIEWS/00_SYSTEM/PHASE_2_SUMMARY_2026-04-05.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Phase 2 summary archived after AMBIGUITY_GATE rule promoted to TASK_INTAKE_AND_ADMISSION.md §7.5/§10.5 |
| 2026-04-27 | `07_REVIEWS/00_SYSTEM/PHASE_2_VALIDATION_P0_PATCHES_2026-04-05.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Phase 2 validation complete; P0.5 (Ambiguity Gate) now canonical in TASK_INTAKE_AND_ADMISSION.md |
| 2026-04-27 | `07_REVIEWS/00_SYSTEM/AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Live rule content promoted to TASK_INTAKE_AND_ADMISSION.md §7.5 and §10.5; original Phase 2 publication record preserved here |
| 2026-04-27 | `01_OS/04_OPERATIONS/WEEKLY_CONTROL/W11_HARDENING_PATCH_SUMMARY.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Patch-history document; W11 hardening rules absorbed into GENERATE_WEEKLY_EXECUTION.md |
| 2026-04-27 | `01_OS/04_OPERATIONS/WEEKLY_CONTROL/W12_HARDENING_EXECUTIVE_SUMMARY.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Patch-history document; V13/V14 rules absorbed into CAPACITY_ENGINE.md |
| 2026-04-27 | `01_OS/04_OPERATIONS/WEEKLY_CONTROL/W12_HARDENING_PATCH_WEEKEND_OVERFLOW.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Patch-history document; V13 weekend effort realism rule absorbed into CAPACITY_ENGINE.md §6.1 |
| 2026-04-27 | `01_OS/04_OPERATIONS/WEEKLY_CONTROL/W12_IMPLEMENTATION_GUIDE_V13_V14.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | Patch-history document; V13/V14 implementation guidance absorbed into CAPACITY_ENGINE.md |
| 2026-04-27 | `01_OS/04_OPERATIONS/WEEKLY_CONTROL/REVIEW_V13_V14_APPROVAL.md` | `99_ARCHIVE/02_SYSTEM_REVIEWS/` | V13/V14 approval record; rules now live in CAPACITY_ENGINE.md; rationale preserved here |
| 2026-04-27 | `03_PLANNING/03_WEEK/W11_DRIFT_LAYER_INTEGRATION.md` | `99_ARCHIVE/03_PROCESS_LOGS/` | Integration change log; live drift layer rules absorbed into GENERATE_WEEKLY_EXECUTION.md §11.5; design rationale preserved here |
| 2026-04-27 | `04_LOGS/WEEKLY_vs_DAILY_PLACEMENT_RULE_IMPLEMENTATION_REPORT.md` | `99_ARCHIVE/03_PROCESS_LOGS/` | Implementation completion report; placement rules live in FOLDER_STRUCTURE_SEMANTICS.md, GENERATE_WEEKLY_EXECUTION.md Gate 9, and TEMPLATE_Daily.md |

---

## What Does NOT Go Here

| Content Type | Correct Location |
|---|---|
| Daily files (cold) | `06_MONTHS/YYYY-MM_MonthName/` (per INDEX §11) |
| Weekly/monthly reviews (permanent) | `07_REVIEWS/` |
| Permanent logs (Decision/Idea/Spike) | `04_LOGS/` |
| Active OS procedures | `01_OS/` |
| Active templates | `05_TEMPLATES/` |
| Active planning (current month/week) | `03_PLANNING/` |
| Project context snapshots | `08_PROJECT_CONTEXT/` |
| Live rules not yet promoted | Must promote first, then archive |

---

*Archive policy established: 2026-04-27. See `reports/FILE_CLEANUP_RULING.md` for full rationale.*
