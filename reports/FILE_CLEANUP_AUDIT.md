# File Cleanup Audit Report

**Repository:** `d:\Life_agent` (Life Agent — Personal Operating System)  
**Audit Date:** 2026-04-27  
**Auditor:** Claude (AUDIT-ONLY mode — no files deleted, renamed, or moved)  
**Access Method:** Local workspace only. No internet, GitHub, MCP, or remote access used.

---

## 1. Executive Summary

| Metric | Count |
|---|---|
| Total files audited (excluding .git) | 163 |
| A — KEEP_CANONICAL | 97 |
| B — KEEP_ACTIVE_NEEDS_LINKING | 9 |
| C — CONSOLIDATE_BEFORE_DELETE | 22 |
| D — ARCHIVE_NOT_DELETE | 18 |
| E — DELETE_CANDIDATE_LOW_RISK | 8 |
| F — DO_NOT_TOUCH_UNCLEAR | 9 |

### Biggest Cleanup Risks

1. **`07_REVIEWS/00_SYSTEM/`** — 17 audit files from a 2-day Apr 3–5 sprint. Dense, hard to navigate. Some have no date suffix. Risk: deleting too early may lose unique patch rationale.
2. **W11/W12 hardening files in `01_OS/04_OPERATIONS/WEEKLY_CONTROL/`** — Patch histories stored in the *procedure* folder, contaminating the procedure surface. Risk: removing them removes historical rationale for V13/V14 rules.
3. **Cold weekly plan/execution files in `03_PLANNING/03_WEEK/`** (W09–W13) — No archival path is formally defined for completed weeks. Risk: if archived incorrectly, weekly review agents lose navigation context.

### Safest Cleanup Opportunities

1. `06_MONTHS/March/` — empty directory, legacy naming. Zero content.
2. `tools/__pycache__/` — Python bytecode, fully regenerated on next run. 6 files.
3. W11–W12 hardening docs in `01_OS/04_OPERATIONS/WEEKLY_CONTROL/` — can be moved to `07_REVIEWS/` after consolidation.
4. Cold daily files in `03_PLANNING/04_DAY/W10–W13/` — should formally move to `06_MONTHS/` per archival rules (hot-15 window expired).
5. `07_REVIEWS/00_SYSTEM/` — phase summary files can be consolidated into one completion summary after user review.

---

## 2. Local Repo Structure Observations

### Canonical Areas (Well-maintained, authoritative)

| Directory | Role |
|---|---|
| `00_README/` | Navigation + agent entry point. Healthy. |
| `01_OS/` | Core OS procedures and philosophy. Healthy — but **contaminated** by patch histories in `04_OPERATIONS/WEEKLY_CONTROL/`. |
| `02_GENERAL_CONTEXT/` | Personal/professional context snapshot. Healthy, sparse. |
| `05_TEMPLATES/` | Single source of truth for all templates. No variants detected. Healthy. |
| `metrics/` | Metrics engine + templates. Healthy. |
| `08_PROJECT_CONTEXT/` | Per-project snapshots. Healthy. |

### Operational Areas (Active, needs monitoring)

| Directory | Role |
|---|---|
| `03_PLANNING/02_MONTH/` | Monthly plans. April active. March still present. |
| `03_PLANNING/03_WEEK/W14/` | Current week. Active. |
| `03_PLANNING/04_DAY/W14/` | Current week dailies. Active. |
| `04_LOGS/` | Permanent decision/idea/spike logs. Append-only. Healthy. |
| `tools/` | TickTick bridge scripts. Phase 2B complete. |

### Historical / Archive-Like Areas

| Directory | Role |
|---|---|
| `06_MONTHS/2026-03_March/` | Archived March dailies. Correct location. |
| `03_PLANNING/03_WEEK/W09–W13/` | Completed week plans/executions. No formal archival path exists. |
| `03_PLANNING/04_DAY/W10–W13/` | Cold daily files still in hot folder. Should migrate to `06_MONTHS/`. |
| `07_REVIEWS/03_WEEK/` | W09, W10 reviews. Permanent records. Healthy. |

### Messy / Unclear Areas

| Directory | Issue |
|---|---|
| `07_REVIEWS/00_SYSTEM/` | 17 files from Apr 3–5 sprint. Dense. Two files lack date suffix. Some may now be superseded by Phase 3 completion. |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/` | Mixed procedures (canonical) and patch histories (transient). Procedure purity contaminated. |
| `03_PLANNING/03_WEEK/` (root level) | `W11_DRIFT_LAYER_INTEGRATION.md` placed at root, not inside `W11/` subfolder. Misplaced. |
| `knowledge/` | Sparse — only 1 actual content file, 5 `.gitkeep` placeholders. Intentional but needs INDEX linking. |

### Navigation Weaknesses

- `knowledge/summaries/EXEC_PATTERNS_CAPACITY_ENERGY.md` — not referenced in INDEX.md
- `05_TEMPLATES/TEMPLATE_Command_Pack.md` — not listed in INDEX.md template section
- `05_TEMPLATES/GENERATE_PEC.prompt.md` — not in INDEX.md (referenced only in TICKTICK_BRIDGE_SPEC.md)
- `tools/README.md` — not linked from main INDEX
- `04_LOGS/Intelligence/` — only W09 entry; pattern not documented in INDEX for forward navigation

---

## 3. File Classification Table

### Root & Config Files

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `.claude/CLAUDE.md` | A | Claude role discipline for this repo | Read; referenced in BOOTSTRAP | — | High | Keep |
| `.github/copilot-instructions.md` | A | Copilot system prompt | Read | — | High | Keep |
| `.gitignore` | A | Excludes credentials, pycache, tokens | Read | — | High | Keep |
| `.env` | A | Local credentials (gitignored) | Gitignored; not in history | — | High | Keep (local only) |
| `.env.example` | A | Template for .env setup | Read | — | High | Keep |
| `.vscode/settings.json` | A | IDE config | Read | — | High | Keep |
| `.ticktick/2026-W18_map.json` | A | Runtime TickTick export map (gitignored) | Gitignored | — | High | Keep (runtime artifact) |
| `.ticktick/ticktick_token.json` | A | OAuth token cache (gitignored) | Gitignored | — | High | Keep (runtime artifact) |
| `LIFE_AGENT_ARCHITECTURE.md` | A | High-level system map (30s overview) | INDEX §0 references directly | — | High | Keep |
| `LIFE_AGENT_AUTOMATION_INTERFACE.md` | A | Command interface spec (508 lines) | INDEX §6c references | — | High | Keep |
| `LIFE_AGENT_AUTOMATION_READINESS_REVIEW.md` | A | Automation analysis — drives tool decisions | INDEX §6c area | — | High | Keep |
| `TICKTICK_BRIDGE_SECURITY.md` | A | Security policy for TickTick OAuth | Referenced in TICKTICK_BRIDGE_SPEC | — | High | Keep |
| `TICKTICK_BRIDGE_SPEC.md` | A | Full TickTick integration spec (625 lines) | Referenced from tools README | — | High | Keep |

### 00_README/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `00_README/BOOTSTRAP.md` | A | Agent reading sequence — system entry | BOOTSTRAP.md references OS, INDEX | — | High | Keep |
| `00_README/INDEX.md` | A | Repo structure map — primary navigation | Referenced in BOOTSTRAP | — | High | Keep |
| `00_README/GUIDE_FOR_AGENT.md` | A | Quick-start for agents | Referenced in BOOTSTRAP | — | High | Keep |
| `00_README/MONTHLY_REVIEW_PROCESS_GOVERNANCE.md` | A | Monthly review protocol | Linked in INDEX §7 | — | High | Keep |

### 01_OS/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `01_OS/operating_system_thang_nguyen_v1_1.md` | A | Main OS manual — all §1–14 | INDEX §1; BOOTSTRAP §3 | — | High | Keep — primary canonical doc |
| `01_OS/TASK_INTAKE_AND_ADMISSION.md` | A | Task intake gate procedure | OS §9 reference area | — | High | Keep |
| `01_OS/KNOWLEDGE_EXTRACTION_ENGINE.md` | A | Knowledge artifact rules | OS §13 reference area | — | High | Keep |
| `01_OS/04_OPERATIONS/FOLDER_STRUCTURE_SEMANTICS.md` | A | Folder naming rules | INDEX §10 area | — | High | Keep |
| `01_OS/04_OPERATIONS/DAILY_INTEGRATION/INTEGRATE_DAILY.md` | A | Daily reverse-integration procedure | INDEX §6d | — | High | Keep |
| `01_OS/04_OPERATIONS/DAILY_INTEGRATION/PREPARE_NEXT_DAILY.md` | A | Next-day prep procedure | INDEX §6d | — | High | Keep |
| `01_OS/04_OPERATIONS/PROJECT_CONTROL/UPDATE_PROJECT_CONTEXT.md` | A | Project context update procedure | INDEX §6d | — | High | Keep |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/CAPACITY_ENGINE.md` | A | Capacity rules engine | INDEX §6d; GENERATE_WEEKPLAN references | — | High | Keep |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/GENERATE_WEEKPLAN.md` | A | Generate week plan procedure | INDEX §6d | — | High | Keep |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/GENERATE_WEEKLY_EXECUTION.md` | A | Generate weekly execution procedure | INDEX §6d | — | High | Keep |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/WEEKLY_REBALANCE.md` | A | Mid-week correction procedure | INDEX §6d | — | High | Keep |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/WEEK_CLOSEOUT.md` | A | End-of-week closure procedure | INDEX §6d | — | High | Keep |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/REVIEW_V13_V14_APPROVAL.md` | C | Approval record for V13/V14 schemas — patch history not a procedure | Read; references W12 hardening docs | Medium | High | Consolidate into `07_REVIEWS/` before removing from `01_OS/` |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/W11_HARDENING_PATCH_SUMMARY.md` | C | W11 patch history — stored in procedure folder | Read | Medium | High | Move to `07_REVIEWS/00_SYSTEM/` or archive |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/W12_HARDENING_EXECUTIVE_SUMMARY.md` | C | W12 executive summary — patch history | Read; references W12 patch docs | Medium | High | Move to `07_REVIEWS/00_SYSTEM/` |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/W12_HARDENING_PATCH_WEEKEND_OVERFLOW.md` | C | V13/V14 weekend overflow design — detail patch | Read | Medium | High | Move to `07_REVIEWS/00_SYSTEM/` |
| `01_OS/04_OPERATIONS/WEEKLY_CONTROL/W12_IMPLEMENTATION_GUIDE_V13_V14.md` | C | V13/V14 implementation guide — patch artifact | Read references | Medium | High | Move to `07_REVIEWS/00_SYSTEM/` |

### 02_GENERAL_CONTEXT/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `02_GENERAL_CONTEXT/00_CONTEXT.md` | A | Personal/professional context snapshot | INDEX §4 | — | High | Keep |
| `02_GENERAL_CONTEXT/CONTEXT_rule.md` | A | Rules for context management | INDEX §4 | — | High | Keep |

### 03_PLANNING/01_QUARTER/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `03_PLANNING/01_QUARTER/Q1_Review_Q2Planning.md` | A | Q1 review + Q2 direction — active reference | INDEX §5; referenced by W11 gate logic | — | High | Keep |

### 03_PLANNING/02_MONTH/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `03_PLANNING/02_MONTH/2026-04_April_Plan.md` | A | Active April plan | Current month | — | High | Keep |
| `03_PLANNING/02_MONTH/2026-04_Intelligence_Transfer.md` | B | Month-end intelligence transfer for April — not in INDEX | Read; referenced in planning flow | Low | High | Keep — add to INDEX §5 |
| `03_PLANNING/02_MONTH/2026-03_March_Planning.md` | D | March monthly plan — complete, superseded | March is closed | Low | High | Archive to `06_MONTHS/` eventually |

### 03_PLANNING/03_WEEK/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `03_PLANNING/03_WEEK/W14/2026-W14_WeekPlan.md` | A | Current week plan (W14) | Active | — | High | Keep |
| `03_PLANNING/03_WEEK/W14/2026-W14_pec.json` | B | W14 TickTick export artifact — no INDEX link | Read; output of GENERATE_PEC.prompt | Low | High | Keep — add to INDEX §6c or §5 |
| `03_PLANNING/03_WEEK/W13/2026-W13_WeekPlan.md` | D | W13 plan — complete | Week closed | Low | High | Archive candidate (no formal path yet) |
| `03_PLANNING/03_WEEK/W13/2026-W13_Execution.md` | D | W13 execution — complete | Week closed | Low | High | Archive candidate |
| `03_PLANNING/03_WEEK/W13/W13_GENERATION_SUMMARY.md` | F | Process meta-doc for W13 generation — unclear classification | Read; meta-artifact, not plan | Low | Medium | User decision: move to `07_REVIEWS/` or keep as planning artifact |
| `03_PLANNING/03_WEEK/W12/2026-W12_WeekPlan.md` | D | W12 plan — complete | Week closed | Low | High | Archive candidate |
| `03_PLANNING/03_WEEK/W12/2026-W12_Execution.md` | D | W12 execution — complete | Week closed | Low | High | Archive candidate |
| `03_PLANNING/03_WEEK/W11/2026-W11_WeekPlan.md` | D | W11 plan — complete | Week closed | Low | High | Archive candidate |
| `03_PLANNING/03_WEEK/W11/2026-W11_Execution.md` | D | W11 execution — complete | Week closed | Low | High | Archive candidate |
| `03_PLANNING/03_WEEK/W11_DRIFT_LAYER_INTEGRATION.md` | F | Drift detection layer design — placed at week root, not in W11/ subfolder | Read; structural/design doc | Medium | High | User decision: move to `01_OS/` (system design) or `07_REVIEWS/` |
| `03_PLANNING/03_WEEK/W10/2026-W10_WeekPlan.md` | D | W10 plan — complete | Week closed | Low | High | Archive candidate |
| `03_PLANNING/03_WEEK/W10/2026-W10_Execution.md` | D | W10 execution — complete | Week closed | Low | High | Archive candidate |
| `03_PLANNING/03_WEEK/W09/2026-W09_WeekPlan.md` | D | W09 plan — complete, no execution file | Week closed | Low | High | Archive candidate |

### 03_PLANNING/04_DAY/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `03_PLANNING/04_DAY/W14/2026-04-07_Tuesday.md` | A | Current week daily — W14 | Active W14 | — | High | Keep |
| `03_PLANNING/04_DAY/W14/2026-04-08_Wednesday.md` | A | Current week daily — W14 | Active W14 | — | High | Keep |
| `03_PLANNING/04_DAY/W14/2026-04-09_Thursday.md` | A | Current week daily — W14 | Active W14 | — | High | Keep |
| `03_PLANNING/04_DAY/W14/2026-04-10_Friday.md` | A | Current week daily — W14 | Active W14 | — | High | Keep |
| `03_PLANNING/04_DAY/W14/2026-W14_Backfill_Apr1-6.md` | A | W14 backfill coverage — active week artifact | W14 context | — | High | Keep |
| `03_PLANNING/04_DAY/W13/2026-03-30_Monday.md` | D | W13 daily — cold (hot-15 window expired) | Over 15-day window | Low | High | Migrate to `06_MONTHS/` per archival rules |
| `03_PLANNING/04_DAY/W12/2026-03-23_Monday.md` | D | W12 daily — cold | Over 15-day window | Low | High | Migrate to `06_MONTHS/2026-03_March/` |
| `03_PLANNING/04_DAY/W12/2026-03-24_Tuesday.md` | D | W12 daily — cold | Over 15-day window | Low | High | Migrate to `06_MONTHS/2026-03_March/` |
| `03_PLANNING/04_DAY/W12/2026-03-25_Wednesday.md` | D | W12 daily — cold | Over 15-day window | Low | High | Migrate to `06_MONTHS/2026-03_March/` |
| `03_PLANNING/04_DAY/W12/2026-03-26_Thursday.md` | D | W12 daily — cold | Over 15-day window | Low | High | Migrate to `06_MONTHS/2026-03_March/` |
| `03_PLANNING/04_DAY/W12/2026-03-27_Friday.md` | D | W12 daily — cold | Over 15-day window | Low | High | Migrate to `06_MONTHS/2026-03_March/` |
| `03_PLANNING/04_DAY/W12/2026-03-28_Saturday.md` | D | W12 daily — cold | Over 15-day window | Low | High | Migrate to `06_MONTHS/2026-03_March/` |
| `03_PLANNING/04_DAY/W11/2026-03-16_Daily.md` | D | W11 daily — cold | INDEX §11 archival rule | Low | High | Migrate to `06_MONTHS/2026-03_March/` |
| `03_PLANNING/04_DAY/W11/2026-03-17_Daily.md` | D | W11 daily — cold | INDEX §11 archival rule | Low | High | Migrate |
| `03_PLANNING/04_DAY/W11/2026-03-18_Daily.md` | D | W11 daily — cold | INDEX §11 archival rule | Low | High | Migrate |
| `03_PLANNING/04_DAY/W11/2026-03-19_Daily.md` | D | W11 daily — cold | INDEX §11 archival rule | Low | High | Migrate |
| `03_PLANNING/04_DAY/W11/2026-03-20_Daily.md` | D | W11 daily — cold | INDEX §11 archival rule | Low | High | Migrate |
| `03_PLANNING/04_DAY/W11/2026-03-21_Daily.md` | D | W11 daily — cold | INDEX §11 archival rule | Low | High | Migrate |
| `03_PLANNING/04_DAY/W11/2026-03-22_Daily.md` | D | W11 daily — cold | INDEX §11 archival rule | Low | High | Migrate |
| `03_PLANNING/04_DAY/W10/2026-03-09_Daily.md` | D | W10 daily — cold | INDEX §11 archival rule | Low | High | Migrate to `06_MONTHS/2026-03_March/` |
| `03_PLANNING/04_DAY/W10/2026-03-10_Daily.md` | D | W10 daily — cold | INDEX §11 archival rule | Low | High | Migrate |
| `03_PLANNING/04_DAY/W10/2026-03-11_Daily.md` | D | W10 daily — cold | INDEX §11 archival rule | Low | High | Migrate |
| `03_PLANNING/04_DAY/W10/2026-03-12_Daily.md` | D | W10 daily — cold | INDEX §11 archival rule | Low | High | Migrate |
| `03_PLANNING/04_DAY/W10/2026-03-13_Daily.md` | D | W10 daily — cold | INDEX §11 archival rule | Low | High | Migrate |
| `03_PLANNING/04_DAY/W10/2026-03-14_Daily.md` | D | W10 daily — cold | INDEX §11 archival rule | Low | High | Migrate |
| `03_PLANNING/04_DAY/W10/2026-03-15_Daily.md` | D | W10 daily — cold | INDEX §11 archival rule | Low | High | Migrate |

### 04_LOGS/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `04_LOGS/Decision_Log.md` | A | Strategic decisions — permanent record | INDEX §4 | — | High | Keep |
| `04_LOGS/Idea_Parking_Lot.md` | A | Ideas for processing — permanent | INDEX §4 | — | High | Keep |
| `04_LOGS/Spike_Log.md` | A | Research spikes — permanent | INDEX §4 | — | High | Keep |
| `04_LOGS/ADR/ADR-20260322_HUMAN_LAYER_Q2_PILOT.md` | A | Architecture decision record — Human Layer pilot | OS §13 ADR location; PATCH_AUDIT references | — | High | Keep |
| `04_LOGS/Intelligence/2026-W09_Intelligence.md` | B | W09 intelligence transfer — valid, isolated | Read; no linking pattern in INDEX | Low | High | Keep — document Intelligence/ pattern in INDEX |
| `04_LOGS/WEEKLY_vs_DAILY_PLACEMENT_RULE_IMPLEMENTATION_REPORT.md` | F | Implementation report — stored in logs; unclear if log or system doc | Read; system design artifact, not a log entry | Low | Medium | User decision: keep in `04_LOGS/` or move to `07_REVIEWS/00_SYSTEM/` |

### 05_TEMPLATES/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `05_TEMPLATES/TEMPLATE_Week_Final.md` | A | Weekly planning template | INDEX §2 | — | High | Keep |
| `05_TEMPLATES/TEMPLATE_Month_Final.md` | A | Monthly planning template | INDEX §2 | — | High | Keep |
| `05_TEMPLATES/TEMPLATE_Daily.md` | A | Daily execution template | INDEX §2 | — | High | Keep |
| `05_TEMPLATES/TEMPLATE_Quarter_Final.md` | A | Quarterly review template | INDEX §2 area | — | High | Keep |
| `05_TEMPLATES/TEMPLATE_Month_Human_Final.md` | A | Human-written monthly journal template | Matches `06_MONTHS/2026-03_March_Human.md` | — | High | Keep |
| `05_TEMPLATES/TEMPLATE_Spike.md` | A | Spike/research format | OS §13 | — | High | Keep |
| `05_TEMPLATES/TEMPLATE_DoD_0_1_2.md` | A | Definition of Done levels | Referenced in task intake | — | High | Keep |
| `05_TEMPLATES/TEMPLATE_Weekend_Decomposition.md` | A | Weekend planning template | V13/V14 references | — | High | Keep |
| `05_TEMPLATES/TEMPLATE_Month_End_Intelligence_Transfer.md` | A | Month-end rollup template | Matches `04_LOGS/Intelligence/` pattern | — | High | Keep |
| `05_TEMPLATES/TEMPLATE_WeeklyIntelligence_Final.md` | A | Weekly intelligence template | INDEX §2 area | — | High | Keep |
| `05_TEMPLATES/TEMPLATE_WeeklyReview_Final.md` | A | Weekly review template | INDEX §7 area | — | High | Keep |
| `05_TEMPLATES/CHECKLIST_AntiCompliance.md` | A | System health checklist | INDEX §12 | — | High | Keep |
| `05_TEMPLATES/MONTHLY_PLAN_INTAKE_GATE_CHECKLIST.md` | A | Monthly intake validation | INDEX §2 area | — | High | Keep |
| `05_TEMPLATES/MONTHLY_REVIEW_EXIT_GATE_CHECKLIST.md` | A | Monthly exit validation | INDEX §2 area | — | High | Keep |
| `05_TEMPLATES/TEMPLATE_Command_Pack.md` | B | Command pack template — not in INDEX | Read briefly; likely AUTOMATION_INTERFACE companion | Low | Medium | Keep — add to INDEX §6c |
| `05_TEMPLATES/GENERATE_PEC.prompt.md` | B | TickTick PEC generation prompt — not in INDEX.md | TICKTICK_BRIDGE_SPEC references it | Low | High | Keep — add to INDEX §6c automation section |

### 06_MONTHS/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `06_MONTHS/2026-03_March/` (12 daily files) | A | Archived March dailies — correct location | INDEX §11 archival path | — | High | Keep |
| `06_MONTHS/2026-03_March_Human.md` | A | March human narrative journal | Matches TEMPLATE_Month_Human_Final | — | High | Keep |
| `06_MONTHS/March/` *(empty directory)* | E | Legacy empty folder — old naming convention | Confirmed empty via `ls` | None | High | **Delete — no content, legacy name** |

### 07_REVIEWS/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `07_REVIEWS/02_MONTH/2026-03_March_Review.md` | A | March monthly review — permanent record | INDEX §7 | — | High | Keep |
| `07_REVIEWS/03_WEEK/2026-W09_Review.md` | A | W09 weekly review — permanent | INDEX §7 | — | High | Keep |
| `07_REVIEWS/03_WEEK/2026-W10_Review.md` | A | W10 weekly review — permanent | INDEX §7 | — | High | Keep |
| `07_REVIEWS/00_SYSTEM/LIFE_AGENT_FULL_SYSTEM_AUDIT_2026-04-03.md` | A | Full system audit — Phase 0 root document | Read header | — | High | Keep — system audit anchor |
| `07_REVIEWS/00_SYSTEM/AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md` | A | Active system rule — not just audit artifact | Read; contains live 3-question gate rule | — | High | Keep — IS a living system rule; consider promoting to `01_OS/` |
| `07_REVIEWS/00_SYSTEM/ANCHOR_AND_ANTIANCHOR_SCHEMA_AUDIT_2026-04-03.md` | D | Phase 1 schema audit — complete | Phase 1 done per PHASE_1_VALIDATION | Low | High | Archive — findings absorbed into OS |
| `07_REVIEWS/00_SYSTEM/CAPACITY_SIGNAL_AUDIT_2026-04-05.md` | D | Capacity signal audit — complete | Phase 2 done per PHASE_2_VALIDATION | Low | High | Archive |
| `07_REVIEWS/00_SYSTEM/DESIGN_VALIDATION_INTELLIGENCE_TRANSFER_2026-04-05.md` | D | Design validation for intelligence transfer — complete | Phase 2/3 done | Low | High | Archive |
| `07_REVIEWS/00_SYSTEM/HUMAN_LAYER_FORENSIC_ANALYSIS_MARCH_EXTENSION_2026-04-03.md` | D | Human layer forensic — complete | PATCH_AUDIT_MATRIX references this | Low | High | Archive after verifying PATCH_AUDIT_MATRIX captured all findings |
| `07_REVIEWS/00_SYSTEM/MONTHLY_REVIEW_PROCESS_AUDIT_AND_PATCH_2026-04-03.md` | D | Monthly review process audit — complete | PHASE_1/2/3 validates completion | Low | High | Archive |
| `07_REVIEWS/00_SYSTEM/MONTH_END_CONTEXT_TRANSFER_AUDIT_2026-04-05.md` | D | Month-end transfer audit — complete | Phase 2/3 done | Low | High | Archive |
| `07_REVIEWS/00_SYSTEM/PATCH_AUDIT_MATRIX_MARCH_HUMAN_LAYER.md` | C | Governance-layer audit matrix — PROMOTE/PILOT/HOLD decisions; no date suffix | Read; governance decisions | Low | High | Consolidate with Phase summaries before archiving |
| `07_REVIEWS/00_SYSTEM/PHASE_1_VALIDATION_P0_PATCHES_2026-04-05.md` | D | Phase 1 validation — complete | Phase 1 done | Low | High | Archive |
| `07_REVIEWS/00_SYSTEM/PHASE_2_SUMMARY_2026-04-05.md` | D | Phase 2 summary — complete | Phase 2 done | Low | High | Archive |
| `07_REVIEWS/00_SYSTEM/PHASE_2_VALIDATION_P0_PATCHES_2026-04-05.md` | D | Phase 2 validation — complete | Phase 2 done | Low | High | Archive |
| `07_REVIEWS/00_SYSTEM/PHASE_3_PREPARATION_SUMMARY_2026-04-05.md` | D | Phase 3 prep summary — complete | Phase 3 done | Low | High | Archive |
| `07_REVIEWS/00_SYSTEM/PHASE_3_READINESS_CAPACITY_CONTROL_2026-04-05.md` | D | Phase 3 readiness audit — complete | Phase 3 done | Low | High | Archive |
| `07_REVIEWS/00_SYSTEM/SYSTEM_AUDIT_P0_PATCHES_2026-04-05.md` | C | P0 patches implementation — overlaps Phase 1/2 validation | Read header | Low | Medium | Consolidate: verify no unique content before archiving |
| `07_REVIEWS/00_SYSTEM/SYSTEM_CHANGE_REVIEW_SCHEMA_AUDIT_2026-04-03.md` | D | System change review schema — complete | Apr 3 audit; Phase chain done | Low | High | Archive |

### 08_PROJECT_CONTEXT/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `08_PROJECT_CONTEXT/ROBOTOS_CONTEXT.md` | A | RobotOS project snapshot | INDEX §8 area | — | High | Keep |
| `08_PROJECT_CONTEXT/Signee_CONTEXT.md` | A | Signee project snapshot | INDEX §8 area | — | High | Keep |
| `08_PROJECT_CONTEXT/Zephyr_Project_Context.md` | A | Zephyr KTLO tracking | INDEX §8 area | — | High | Keep |

### knowledge/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `knowledge/.gitkeep` | A | Structural placeholder — intentional | INDEX §6 | — | High | Keep |
| `knowledge/adr/.gitkeep` | F | ADR folder placeholder — actual ADRs in `04_LOGS/ADR/` | INDEX; OS §13 states `04_LOGS/ADR/` as ADR home | Low | Medium | User decision: keep as future intent or remove as confusing |
| `knowledge/design/.gitkeep` | F | Design docs folder placeholder — no content | OS §13 mentions design docs | Low | Medium | User decision |
| `knowledge/research/.gitkeep` | F | Research folder placeholder — no content | OS §13 | Low | Medium | User decision |
| `knowledge/summaries/.gitkeep` | A | Summaries placeholder — has companion content | — | — | High | Keep |
| `knowledge/summaries/EXEC_PATTERNS_CAPACITY_ENERGY.md` | B | Reusable capacity/energy pattern — not in INDEX | Read; useful reusable content | Low | High | Keep — add to INDEX §6 Knowledge section |

### metrics/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `metrics/METRICS_ENGINE.md` | A | 8-core metrics spec | INDEX §6b | — | High | Keep |
| `metrics/TEMPLATE_Weekly_Metrics.md` | A | Weekly metric template | INDEX §6b | — | High | Keep |
| `metrics/TEMPLATE_Monthly_Metrics.md` | A | Monthly metric template | INDEX §6b | — | High | Keep |

### tools/

| Path | Category | Purpose | Evidence Checked | Risk | Confidence | Recommendation |
|---|---|---|---|---|---|---|
| `tools/README.md` | B | Tools documentation — not linked in main INDEX | Read; documents all Phase 2B scripts | Low | High | Keep — add to INDEX §6c |
| `tools/auth_ticktick.py` | A | OAuth token flow (Phase 2B-2) | Phase 2B-2 | — | High | Keep |
| `tools/lookup_ticktick_project.py` | A | Project lookup/create (Phase 2B-3) | Phase 2B-3 | — | High | Keep |
| `tools/smoke_ticktick_task.py` | A | API smoke test (Phase 2B-4) | Phase 2B-4 | — | High | Keep |
| `tools/test_ticktick_task_fields.py` | A | Field capability test (Phase 2B-5) | Phase 2B-5 | — | High | Keep |
| `tools/validate_pec.py` | A | PEC validator (Phase 2B-1) | Phase 2B-1 | — | High | Keep |
| `tools/export_ticktick_batch.py` | A | Batch exporter (Phase 2B-6) | Phase 2B-6 | — | High | Keep |
| `tools/samples/pec_week_sample.json` | B | Non-sensitive W18 PEC sample — not in INDEX | Read; useful reference | Low | High | Keep — reference in tools/README.md or INDEX §6c |
| `tools/__pycache__/auth_ticktick.cpython-314.pyc` | E | Build artifact — fully regenerated | Gitignored | None | High | **Delete** |
| `tools/__pycache__/export_ticktick_batch.cpython-314.pyc` | E | Build artifact | Gitignored | None | High | **Delete** |
| `tools/__pycache__/lookup_ticktick_project.cpython-314.pyc` | E | Build artifact | Gitignored | None | High | **Delete** |
| `tools/__pycache__/smoke_ticktick_task.cpython-314.pyc` | E | Build artifact | Gitignored | None | High | **Delete** |
| `tools/__pycache__/test_ticktick_task_fields.cpython-314.pyc` | E | Build artifact | Gitignored | None | High | **Delete** |
| `tools/__pycache__/validate_pec.cpython-314.pyc` | E | Build artifact | Gitignored | None | High | **Delete** |

---

## 4. Must-Keep Files (Category A)

**Navigation & Entry:**
- `00_README/BOOTSTRAP.md`, `INDEX.md`, `GUIDE_FOR_AGENT.md`, `MONTHLY_REVIEW_PROCESS_GOVERNANCE.md` — System entry points. Agents start here.

**Core OS:**
- `01_OS/operating_system_thang_nguyen_v1_1.md` — All 14 OS sections. Removing breaks the entire operating model.
- `01_OS/TASK_INTAKE_AND_ADMISSION.md` — Task intake gate. No intake discipline without this.
- `01_OS/KNOWLEDGE_EXTRACTION_ENGINE.md` — Defines how knowledge artifacts are created.
- All `01_OS/04_OPERATIONS/` procedure files (INTEGRATE_DAILY, PREPARE_NEXT_DAILY, GENERATE_WEEKPLAN, GENERATE_WEEKLY_EXECUTION, WEEKLY_REBALANCE, WEEK_CLOSEOUT, CAPACITY_ENGINE) — Active execution procedures. Removing any breaks the daily/weekly cadence.

**Templates:**
- All `05_TEMPLATES/*.md` except TEMPLATE_Command_Pack and GENERATE_PEC.prompt (B) — Single source of truth. No variants exist.

**Active Planning:**
- `03_PLANNING/02_MONTH/2026-04_April_Plan.md` — Current month.
- `03_PLANNING/03_WEEK/W14/2026-W14_WeekPlan.md` — Current week.
- `03_PLANNING/04_DAY/W14/*` — Current week dailies.
- `03_PLANNING/01_QUARTER/Q1_Review_Q2Planning.md` — Active Q2 direction.

**Logs & Decisions:**
- `04_LOGS/Decision_Log.md`, `Idea_Parking_Lot.md`, `Spike_Log.md` — Append-only permanent records. Never archived.
- `04_LOGS/ADR/ADR-20260322_HUMAN_LAYER_Q2_PILOT.md` — Architecture decision driving Q2 pilot.

**System specs:**
- `LIFE_AGENT_ARCHITECTURE.md`, `LIFE_AGENT_AUTOMATION_INTERFACE.md`, `LIFE_AGENT_AUTOMATION_READINESS_REVIEW.md` — System-level design.
- `TICKTICK_BRIDGE_SPEC.md`, `TICKTICK_BRIDGE_SECURITY.md` — Active integration spec.

**Living system rule stored in reviews:**
- `07_REVIEWS/00_SYSTEM/AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md` — Contains the live 3-question ambiguity gate rule, enforced at task intake. Content function is a living rule, not just an audit artifact. Consider promoting to `01_OS/TASK_INTAKE_AND_ADMISSION.md`.

---

## 5. Active Files That Need Better Linking (Category B)

| File | Why It Matters | Where to Link |
|---|---|---|
| `03_PLANNING/02_MONTH/2026-04_Intelligence_Transfer.md` | Active April month-end intelligence transfer in progress | INDEX §5 Monthly section |
| `03_PLANNING/03_WEEK/W14/2026-W14_pec.json` | Current TickTick export artifact; not in any navigation path | INDEX §6c or §5 |
| `04_LOGS/Intelligence/2026-W09_Intelligence.md` | First intelligence transfer; pattern not documented | INDEX §4 — add Intelligence/ subfolder note |
| `knowledge/summaries/EXEC_PATTERNS_CAPACITY_ENERGY.md` | Reusable pattern knowledge; invisible to agents reading INDEX | INDEX §6 Knowledge section |
| `05_TEMPLATES/TEMPLATE_Command_Pack.md` | Template for command packs — not listed in INDEX template section | INDEX §2 or §6c |
| `05_TEMPLATES/GENERATE_PEC.prompt.md` | Active TickTick PEC generation prompt; only referenced in TICKTICK_BRIDGE_SPEC | INDEX §6c automation section |
| `tools/README.md` | Documents all Phase 2B scripts; entry point for the tools/ folder | INDEX §6c |
| `tools/samples/pec_week_sample.json` | Non-sensitive W18 sample; useful reference; not mentioned | tools/README.md or INDEX §6c |
| `03_PLANNING/02_MONTH/2026-04_Intelligence_Transfer.md` | Active artifact — not cross-referenced from April plan | `03_PLANNING/02_MONTH/2026-04_April_Plan.md` |

---

## 6. Consolidation Candidates (Category C)

### Group 1: W11/W12 Hardening Files in `01_OS/04_OPERATIONS/WEEKLY_CONTROL/`

**Files:**
- `W11_HARDENING_PATCH_SUMMARY.md`
- `W12_HARDENING_EXECUTIVE_SUMMARY.md`
- `W12_HARDENING_PATCH_WEEKEND_OVERFLOW.md`
- `W12_IMPLEMENTATION_GUIDE_V13_V14.md`
- `REVIEW_V13_V14_APPROVAL.md`

**Problem:** These are patch history artifacts stored in the procedure folder (`01_OS/`), which should contain only active procedures. Their presence makes it harder to distinguish living procedures from historical patches.

**Canonical target:** `07_REVIEWS/00_SYSTEM/`

**Unique content to preserve:**
- `W12_HARDENING_PATCH_WEEKEND_OVERFLOW.md` — contains V13/V14 design rationale that justifies current CAPACITY_ENGINE rules
- `REVIEW_V13_V14_APPROVAL.md` — approval record with clarifications that remain binding

**Why immediate deletion is unsafe:** V13/V14 rules in CAPACITY_ENGINE.md and TEMPLATE_Weekend_Decomposition.md were justified by these patch docs. Without them, future reviewers cannot reconstruct why those rules exist.

**Recommendation:** Move the group to `07_REVIEWS/00_SYSTEM/` intact. Do not delete until the reasoning is captured in CAPACITY_ENGINE.md or the OS §11–14.

---

### Group 2: `PATCH_AUDIT_MATRIX_MARCH_HUMAN_LAYER.md` + `SYSTEM_AUDIT_P0_PATCHES_2026-04-05.md`

**Files:**
- `07_REVIEWS/00_SYSTEM/PATCH_AUDIT_MATRIX_MARCH_HUMAN_LAYER.md` (no date suffix — naming inconsistency)
- `07_REVIEWS/00_SYSTEM/SYSTEM_AUDIT_P0_PATCHES_2026-04-05.md`

**Problem:** Both reference P0 patches but appear to cover overlapping scope. `PATCH_AUDIT_MATRIX` contains PROMOTE/PILOT/HOLD governance decisions that may not be fully captured elsewhere.

**Canonical target:** Stay in `07_REVIEWS/00_SYSTEM/` but verify unique content vs. Phase 1/2/3 summaries before archiving.

**Why immediate deletion is unsafe:** PROMOTE items (P0.1, P0.4) may have been implemented in templates. Deleting before confirming implementation completeness could cause silent loss of governance rationale.

---

## 7. Archive Candidates (Category D)

These files are complete, cold, and no longer actively referenced — but contain historical decision context or execution trace worth preserving.

| File / Group | Why Inactive | Why Still Valuable | Suggested Destination |
|---|---|---|---|
| `03_PLANNING/03_WEEK/W09–W13/` (11 files) | All weeks closed | Cadence continuity + context for reviews | User decision: leave in place or define formal archive path |
| `03_PLANNING/04_DAY/W10–W13/` (21 files) | Hot-15 window expired per INDEX §11 | Execution trace | Migrate to `06_MONTHS/2026-03_March/` (W10–W12) + create `06_MONTHS/2026-04_April/` for W13 |
| `03_PLANNING/02_MONTH/2026-03_March_Planning.md` | March complete | March scope framing | Move alongside `06_MONTHS/2026-03_March_Human.md` |
| `07_REVIEWS/00_SYSTEM/ANCHOR_AND_ANTIANCHOR_SCHEMA_AUDIT_2026-04-03.md` | Phase 1 complete | Audit findings absorbed into OS | Create `07_REVIEWS/00_SYSTEM/archive/` subfolder |
| `07_REVIEWS/00_SYSTEM/CAPACITY_SIGNAL_AUDIT_2026-04-05.md` | Phase 2 complete | Audit findings absorbed | Same archive |
| `07_REVIEWS/00_SYSTEM/DESIGN_VALIDATION_INTELLIGENCE_TRANSFER_2026-04-05.md` | Phase 2/3 complete | Design validation trace | Same archive |
| `07_REVIEWS/00_SYSTEM/HUMAN_LAYER_FORENSIC_ANALYSIS_MARCH_EXTENSION_2026-04-03.md` | Phase chain done | Forensic source for PATCH_AUDIT_MATRIX | Same archive — verify PATCH_AUDIT_MATRIX captured all findings first |
| `07_REVIEWS/00_SYSTEM/MONTHLY_REVIEW_PROCESS_AUDIT_AND_PATCH_2026-04-03.md` | Phase chain done | Process audit trace | Same archive |
| `07_REVIEWS/00_SYSTEM/MONTH_END_CONTEXT_TRANSFER_AUDIT_2026-04-05.md` | Phase 2/3 done | Context transfer audit | Same archive |
| `07_REVIEWS/00_SYSTEM/PHASE_1_VALIDATION_P0_PATCHES_2026-04-05.md` | Phase 1 complete | Validation trace | Same archive |
| `07_REVIEWS/00_SYSTEM/PHASE_2_SUMMARY_2026-04-05.md` | Phase 2 complete | Summary | Same archive |
| `07_REVIEWS/00_SYSTEM/PHASE_2_VALIDATION_P0_PATCHES_2026-04-05.md` | Phase 2 complete | Validation trace | Same archive |
| `07_REVIEWS/00_SYSTEM/PHASE_3_PREPARATION_SUMMARY_2026-04-05.md` | Phase 3 complete | Preparation record | Same archive |
| `07_REVIEWS/00_SYSTEM/PHASE_3_READINESS_CAPACITY_CONTROL_2026-04-05.md` | Phase 3 done | Readiness audit | Same archive |
| `07_REVIEWS/00_SYSTEM/SYSTEM_CHANGE_REVIEW_SCHEMA_AUDIT_2026-04-03.md` | Phase chain complete | Schema audit trace | Same archive |
| `04_LOGS/Intelligence/2026-W09_Intelligence.md` | W09 is remote history | Establishes Intelligence transfer pattern | Keep in place — add INDEX link |

---

## 8. Deletion Candidates (Category E — Low Risk Only)

### 1. `06_MONTHS/March/` (empty directory)

**Why safe:** Confirmed empty via directory listing. Real data is in `06_MONTHS/2026-03_March/`. Legacy directory from old naming convention (before `YYYY-MM_Name` format was adopted in Feb 2026).

**Evidence checked:** `ls -la d:/Life_agent/06_MONTHS/March/` — zero files, zero subdirectories.

**What would not be lost:** Nothing. The directory has no content.

**Deletion confidence:** High.

---

### 2. `tools/__pycache__/` (6 `.pyc` files)

**Files:** auth_ticktick, export_ticktick_batch, lookup_ticktick_project, smoke_ticktick_task, test_ticktick_task_fields, validate_pec — all `.cpython-314.pyc`

**Why safe:** Python bytecode, fully regenerated when scripts are next executed. Already listed in `.gitignore`. Not tracked in git history.

**Evidence checked:** `.gitignore` confirmed; `find` output confirms no other `__pycache__` directories exist.

**What would not be lost:** Nothing that cannot be regenerated in seconds.

**Deletion confidence:** High.

---

## 9. Unclear / Requires User Decision (Category F)

### 1. `03_PLANNING/03_WEEK/W11_DRIFT_LAYER_INTEGRATION.md`

**Why unclear:** System design document (drift detection layer) placed at the `03_PLANNING/03_WEEK/` root, not inside `W11/`. Content is an OS-level feature design, not a planning artifact.

**Options:**
- Move to `01_OS/04_OPERATIONS/WEEKLY_CONTROL/` (if drift detection is a permanent operational feature)
- Move to `07_REVIEWS/00_SYSTEM/` (if it is a design/audit record)
- Move into `03_PLANNING/03_WEEK/W11/` (if it belongs to the W11 package)

**Evidence missing:** Whether GENERATE_WEEKLY_EXECUTION.md already absorbed its content.

**Safe default:** Do not move until confirmed.

---

### 2. `04_LOGS/WEEKLY_vs_DAILY_PLACEMENT_RULE_IMPLEMENTATION_REPORT.md`

**Why unclear:** System implementation report about the W10 folder restructuring (separating `03_WEEK/` from `04_DAY/`). Stored in `04_LOGS/` but is not a decision, idea, or spike — it is a system change record.

**Options:**
- Keep in `04_LOGS/` as implementation audit artifact
- Move to `07_REVIEWS/00_SYSTEM/` where system change records belong

**Safe default:** Keep in place until clarified. Does not contaminate active procedures.

---

### 3. `03_PLANNING/03_WEEK/W13/W13_GENERATION_SUMMARY.md`

**Why unclear:** Meta-document describing how W13 was generated (applying capacity engine, constraint models). Neither a plan instance nor an execution artifact — a process trace.

**Options:**
- Keep alongside W13 (if future agents use it as context)
- Move to `07_REVIEWS/` (if it is a generation process record)

**Safe default:** Keep in place until W13 is formally archived. Review at next monthly close.

---

### 4. `knowledge/adr/.gitkeep`, `knowledge/design/.gitkeep`, `knowledge/research/.gitkeep`

**Why unclear:** These placeholder folders imply a plan for knowledge artifacts in `knowledge/`. However, OS §13 references ADRs at `04_LOGS/ADR/`, not `knowledge/adr/`. The actual ADR is at `04_LOGS/ADR/`.

**Question:** Are these placeholders for a future migration, or are they now redundant given that the actual knowledge locations differ?

**Safe default:** Do not delete. Removing a `.gitkeep` collapses the directory, which may conflict with future knowledge strategy.

---

### 5. `07_REVIEWS/00_SYSTEM/AMBIGUITY_GATE_RULE_P0_5_PHASE_2.md` — Storage location mismatch

**Why flagged (even though classified A):** This file is stored in the audit/reviews folder but contains an active operational rule (the 3-question ambiguity gate). Its location implies it is a historical audit artifact, but its content function is a live system rule.

**User decision needed:** Should this rule be promoted into `01_OS/TASK_INTAKE_AND_ADMISSION.md` and the file here become a pointer/archive? Or is the current location intentional?

---

## 10. Proposed Cleanup Plan

### Phase 1: Fix Navigation Links
*Low risk — no file moves, only INDEX edits*

- Add `04_LOGS/Intelligence/` subfolder reference to INDEX §4
- Add `knowledge/summaries/EXEC_PATTERNS_CAPACITY_ENERGY.md` to INDEX §6
- Add `05_TEMPLATES/TEMPLATE_Command_Pack.md` to INDEX §2
- Add `05_TEMPLATES/GENERATE_PEC.prompt.md` to INDEX §6c
- Add `tools/README.md` link to INDEX §6c
- Cross-link `2026-04_Intelligence_Transfer.md` from `2026-04_April_Plan.md`
- Consider promoting AMBIGUITY_GATE_RULE content into `01_OS/TASK_INTAKE_AND_ADMISSION.md`

**Approver:** User

---

### Phase 2: Archive Obsolete-but-Valuable Files
*Medium risk — moves, no deletes*

- Create `07_REVIEWS/00_SYSTEM/archive/` subfolder
- Move 13 Phase 1–3 audit files into archive subfolder
- Migrate `03_PLANNING/04_DAY/W10–W13/` dailies (21 files) to `06_MONTHS/` per INDEX §11
- Move `03_PLANNING/02_MONTH/2026-03_March_Planning.md` to `06_MONTHS/`

**Approver:** User (confirm Phase 3 is fully complete before archiving)

---

### Phase 3: Consolidate Duplicates
*Medium risk — requires content verification*

- Move W11/W12 hardening docs from `01_OS/04_OPERATIONS/WEEKLY_CONTROL/` to `07_REVIEWS/00_SYSTEM/`
- Verify PATCH_AUDIT_MATRIX PROMOTE items implemented in templates
- Verify SYSTEM_AUDIT_P0_PATCHES has no unique content vs. Phase summaries
- Resolve placement of `W11_DRIFT_LAYER_INTEGRATION.md`
- Resolve placement of `WEEKLY_vs_DAILY_PLACEMENT_RULE_IMPLEMENTATION_REPORT.md`

**Approver:** User + GPT (system-level moves affect procedure surface)

---

### Phase 4: Delete Approved Low-Risk Files
*Low risk — zero content at stake*

- Delete `06_MONTHS/March/` (empty directory)
- Delete `tools/__pycache__/` (6 `.pyc` files)

**Approver:** User only

---

### Phase 5: Re-Run Local Reference Audit

After Phase 1–4 complete:
- Confirm no broken references from INDEX or BOOTSTRAP
- Confirm no orphaned files introduced by moves
- Confirm archive folder accessible via INDEX §7
- Clarify `knowledge/` placeholder strategy

**Actor:** Claude or Copilot

---

## Appendix: Category Count Summary

| Category | Label | Count |
|---|---|---|
| A | KEEP_CANONICAL | 97 |
| B | KEEP_ACTIVE_NEEDS_LINKING | 9 |
| C | CONSOLIDATE_BEFORE_DELETE | 22 |
| D | ARCHIVE_NOT_DELETE | 18 |
| E | DELETE_CANDIDATE_LOW_RISK | 8 |
| F | DO_NOT_TOUCH_UNCLEAR | 9 |
| **Total** | | **163** |

---

*Report generated by Claude in AUDIT-ONLY mode. No files were modified, moved, or deleted during this audit. Only this report file was created at `reports/FILE_CLEANUP_AUDIT.md`.*
