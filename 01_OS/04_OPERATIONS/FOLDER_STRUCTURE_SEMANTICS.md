# LIFE_AGENT Folder Structure Semantics — WEEKLY vs DAILY

> **Type:** Maintenance Reference  
> **Layer:** OS / Structure  
> **Purpose:** Define folder placement as part of artifact semantics; ensure planning and execution layers remain separate and scalable  
> **Mandatory for:** All file generation (weekly, daily, and related)  
> **Last updated:** 2026-03-21  

---

## Core Principle

**Folder placement encodes artifact meaning and operational context.** It is not merely storage convenience.

The life_agent planning system separates **planning layer** (weekly) from **execution layer** (daily) using folder structure. This separation ensures:
- Clear navigation: can immediately see which artifacts are planning vs execution
- Scalability: as weeks accumulate, each layer remains uncluttered
- Reduced error risk: rules about "where files go" prevent misgeneration
- Semantic clarity: folder path itself tells you the artifact type and week

---

## Folder Architecture

### 03_PLANNING (Root Planning Directory)

```
03_PLANNING/
├── 02_MONTH/
│   └── 2026-03_March.md    ← Monthly strategic planning
│
├── 03_WEEK/                ← PLANNING LAYER (by week)
│   ├── W09/
│   │   ├── 2026-W09_WeekPlan.md
│   │   └── 2026-W09_Execution.md
│   ├── W10/
│   │   ├── 2026-W10_WeekPlan.md
│   │   └── 2026-W10_Execution.md
│   └── W11/
│       ├── 2026-W11_WeekPlan.md
│       └── 2026-W11_Execution.md
│
└── 04_DAY/                 ← EXECUTION LAYER (by week)
    ├── W09/
    │   ├── 2026-03-09_Daily.md
    │   ├── 2026-03-10_Daily.md
    │   └── ...
    ├── W10/
    │   ├── 2026-03-16_Daily.md
    │   ├── 2026-03-17_Daily.md
    │   └── ...
    └── W11/
        ├── 2026-03-16_Daily.md
        ├── 2026-03-17_Daily.md
        └── ...
```

### Why This Structure?

**Before (Mixed):**
```
03_PLANNING/03_WEEK/
├── 2026-W09_WeekPlan.md
├── 2026-W10_WeekPlan.md
├── 2026-W10_Execution.md
├── 2026-W11_WeekPlan.md
├── 2026-W11_Execution.md
├── 2026-03-09_Daily.md         ← Misplaced: mixed layer
├── 2026-03-10_Daily.md         ← Misplaced: mixed layer
└── ... (15+ daily files, hard to scan)
```

**After (Separated):**
```
03_PLANNING/03_WEEK/
├── W09/2026-W09_WeekPlan.md
├── W09/2026-W09_Execution.md
├── W10/2026-W10_WeekPlan.md
├── W10/2026-W10_Execution.md
├── W11/2026-W11_WeekPlan.md
├── W11/2026-W11_Execution.md

03_PLANNING/04_DAY/
├── W09/2026-03-09_Daily.md
├── W09/2026-03-10_Daily.md
├── W10/2026-03-16_Daily.md
├── W10/2026-03-17_Daily.md
```

**Benefits of "After":**
- Parent folder immediately signals artifact type: `03_WEEK/` = planning, `04_DAY/` = execution
- Week subfolder groups related artifacts by operational week
- Easy to locate all planning for W11: look in `03_WEEK/W11/`
- Easy to locate all execution for W11: look in `04_DAY/W11/`
- Scales gracefully: adding W12, W13, W14... just creates new subfolders; parent folders stay uncluttered

---

## Naming Rules (CRITICAL)

### Weekly Files

**Rule:** Full identifier names with explicit week notation.

**Format:**
- `2026-Wxx_WeekPlan.md` (where xx = 09, 10, 11, etc.)
- `2026-Wxx_Execution.md`

**Valid:**
- `2026-W09_WeekPlan.md` ✓
- `2026-W11_Execution.md` ✓

**Invalid:**
- `WeekPlan.md` ✗ (no week identifier)
- `W11_WeekPlan.md` ✗ (missing year)
- `2026-W11-Plan.md` ✗ (wrong verb; must be "Plan" or "Execution")

### Daily Files

**Rule:** Date-based names with explicit date notation. No week identifier in filename (week is encoded in folder path).

**Format:**
- `YYYY-MM-DD_Daily.md` (e.g., `2026-03-16_Daily.md`)

**Valid:**
- `2026-03-16_Daily.md` ✓
- `2026-03-17_Daily.md` ✓

**Invalid:**
- `2026-03-16.md` ✗ (missing "_Daily" suffix)
- `03-16_Daily.md` ✗ (year required for clarity)
- `Daily_2026-03-16.md` ✗ (wrong order)
- `2026-W11-03-16_Daily.md` ✗ (redundant; week already in folder path)

### Why Explicit Full Names?

1. **Unambiguous at a glance:** Anyone can immediately identify which week and which day without reading folder context
2. **Search-friendly:** Grep/search operations work correctly across the entire workspace
3. **Portable:** If a file is emailed or copied elsewhere, the name still contains full context
4. **Historical clarity:** Years from now, all artifacts stay identifiable without needing to know the folder layout

---

## Placement Rules

### Weekly Files

**MUST be within:** `03_PLANNING/03_WEEK/Wxx/`  
**MUST NOT be:** Directly under `03_PLANNING/03_WEEK/` or under `03_PLANNING/04_DAY/`

**Auto-create rule:** If `Wxx` subfolder does not exist, **automatically create it**. Do NOT fail with "folder not found" error; do NOT ask for permission. Just create the folder.

**Example:**
- ✓ `03_PLANNING/03_WEEK/W11/2026-W11_WeekPlan.md`
- ✓ `03_PLANNING/03_WEEK/W11/2026-W11_Execution.md`
- ✗ `03_PLANNING/03_WEEK/2026-W11_WeekPlan.md` (missing Wxx subfolder)
- ✗ `03_PLANNING/04_DAY/2026-W11_Execution.md` (wrong parent folder)

### Daily Files

**MUST be within:** `03_PLANNING/04_DAY/Wxx/`  
**MUST NOT be:** Under `03_PLANNING/03_WEEK/` or directly under `03_PLANNING/04_DAY/`

**Auto-create rule:** If `04_DAY/Wxx` subfolder does not exist, **automatically create it**. Do NOT fail or ask.

**Week determination rule:** The date YYYY-MM-DD determines which Wxx folder the file goes into:
- Dates 03-09 through 03-15 → W10
- Dates 03-16 through 03-22 → W11
- Dates 03-23 through 03-29 → W12
- (And so on; use standard calendar week boundaries)

**Example:**
- ✓ `03_PLANNING/04_DAY/W11/2026-03-16_Daily.md` (opens W11: 03-16 is correct week)
- ✓ `03_PLANNING/04_DAY/W10/2026-03-10_Daily.md` (opens W10: 03-10 is correct week)
- ✗ `03_PLANNING/03_WEEK/2026-03-16_Daily.md` (wrong parent folder; mixes daily into weekly)
- ✗ `03_PLANNING/04_DAY/2026-03-16_Daily.md` (missing week subfolder)
- ✗ `03_PLANNING/04_DAY/W11/2026-03-10_Daily.md` (date belongs to W10, not W11; inconsistency)

---

## Enforcement & Generation Rules

### For GENERATE_WEEKLY_EXECUTION

When generating a Weekly Execution file for Wxx:
1. Create folder `03_PLANNING/03_WEEK/Wxx/` if it doesn't exist
2. Write the file to `03_PLANNING/03_WEEK/Wxx/2026-Wxx_Execution.md`
3. Before finalizing, verify the path using Artifact Placement QA (Gate 9)
4. Do NOT write weekly files to root `03_PLANNING/03_WEEK/` directory
5. Do NOT write daily files to `03_WEEK/` folder

### For Daily File Generation (GENERATE_DAILY, future procedure)

When generating a Daily file for date YYYY-MM-DD in week Wxx:
1. Determine the correct Wxx from the date (using calendar week boundaries)
2. Create folder `03_PLANNING/04_DAY/Wxx/` if it doesn't exist
3. Write the file to `03_PLANNING/04_DAY/Wxx/YYYY-MM-DD_Daily.md`
4. Before finalizing, verify the path using Artifact Placement QA (Gate 9)
5. Do NOT write daily files to `03_WEEK/` folder
6. Do NOT write weekly files to `04_DAY/` folder

### For Error Detection

Periodically scan for misplaced files:

**Scan 1: Check for daily files in wrong location**
```bash
# Find any YYYY-MM-DD_Daily.md files under 03_WEEK/
find 03_PLANNING/03_WEEK/ -name "*_Daily.md"
# If any results → MISPLACED. Move to 04_DAY/Wxx/
```

**Scan 2: Check for weekly files in wrong location**
```bash
# Find any *_WeekPlan.md or *_Execution.md under 04_DAY/
find 03_PLANNING/04_DAY/ -name "*_WeekPlan.md"
find 03_PLANNING/04_DAY/ -name "*_Execution.md"
# If any results → MISPLACED. Move to 03_WEEK/Wxx/
```

**Scan 3: Check for weekly files without week subfolder**
```bash
# Find any 2026-Wxx_*.md files directly under 03_WEEK/ (not in subfolders)
ls 03_PLANNING/03_WEEK/*.md 2>/dev/null
# If any results → MISPLACED. Move to 03_WEEK/Wxx/
```

---

## Transition Rules

### If Files Are Currently Misplaced

1. **Identify all misplaced daily files:**
   - Any file matching `YYYY-MM-DD_Daily.md` under `03_PLANNING/03_WEEK/` is misplaced
   - Correct folder: `03_PLANNING/04_DAY/Wxx/` (where Wxx matches the date)

2. **Identify all misplaced weekly files:**
   - Any file matching `2026-Wxx_*.md` directly under `03_PLANNING/03_WEEK/` (not in subfolder) is misplaced
   - Correct folder: `03_PLANNING/03_WEEK/Wxx/`

3. **Move files to correct locations:**
   - Preserve filenames exactly (do NOT rename)
   - Create target folders as needed
   - Update any path references in other files (e.g., if README.md points to old path)

4. **Verify no content changes:**
   - File content MUST remain identical after move
   - Only path changes; content untouched

---

## FAQ

**Q: Why not just put all files in one folder with date prefixes?**

A: Prefix-only structure (e.g., `2026-W11_Execution.md` and `2026-03-16_Daily.md` in same folder) scales poorly as weeks accumulate. After 52 weeks, the folder contains 60+ files, and human navigation becomes difficult. Subfolder structure keeps each folder's file count manageable (~2 files per week for planning, ~7 per week for execution).

**Q: Can I rename a file to skip the week subfolder?**

A: No. Folder placement is part of the artifact semantic. Even if you rename the file, the content should still specify which week it belongs to (in the file header or metadata). The folder path provides the authoritative, easy-to-verify structure. Changing folder structure would require changes across multiple generation rules and documentation.

**Q: What if a daily file spans a week boundary (e.g., planning started Mon, continues Fri of next week)?**

A: Create separate daily files, one per calendar date. Do NOT create a multi-day daily file. Each file belongs to exactly one date and one week folder.

**Q: How do I quickly find all planning for a specific week?**

A: Navigate to `03_PLANNING/03_WEEK/Wxx/`. All planning files for week Wxx are there: both WeekPlan and Execution.

**Q: How do I quickly find all execution for a specific week?**

A: Navigate to `03_PLANNING/04_DAY/Wxx/`. All daily files for week Wxx are there (one file per day that has a daily plan).

---

## Related Documentation

- **GENERATE_WEEKLY_EXECUTION.md § Artifact Placement QA (Gate 9)** — Validation rules for weekly file placement
- **TEMPLATE_Daily.md § Placement rule** — Enforcement rule for daily file generation
- **LIFE_AGENT OS § Folder Architecture** — Broader folder structure of life_agent system

---

## Maintenance Checklist

- [ ] All weekly files are in `03_PLANNING/03_WEEK/Wxx/` subfolders
- [ ] All daily files are in `03_PLANNING/04_DAY/Wxx/` subfolders
- [ ] No daily files exist under `03_PLANNING/03_WEEK/` root
- [ ] No weekly files exist under `03_PLANNING/04_DAY/` root
- [ ] All filenames follow naming rules (full explicit names, not generic)
- [ ] All weekly file paths verified using Gate 9 before finalization
- [ ] All new week subfolders auto-created on first file generation (no manual folder creation needed from user)

---

**Last Review:** 2026-03-21  
**Next Review:** At end of Q2 2026 or if folder structure needs scaling beyond 52 weeks of data
