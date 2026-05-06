# AGENT_OPERATING_MODEL.md — Multi-Agent Operating Model

> **Version:** v1.0
> **Status:** Active
> **Placement:** Canonical governance document for agent roles, routing, and task contracts.
> **Owner:** User (final authority). Changes require User/GPT approval.

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. Core Working Triangle + Execution Layer](#2-core-working-triangle--execution-layer)
- [3. Agent Roles](#3-agent-roles)
- [4. Routing Policy](#4-routing-policy)
- [5. GLM Role](#5-glm-role)
- [6. GLM Task Contract](#6-glm-task-contract)
- [7. GLM Escalation Rules](#7-glm-escalation-rules)
- [8. GLM Report Format](#8-glm-report-format)
- [9. Risk Controls](#9-risk-controls)
- [10. First-Use Rule](#10-first-use-rule)

---

## 1. Purpose

Life Agent uses a **Working Triangle** (User/GPT/Copilot/Claude) plus a **governed multi-agent execution layer** (currently: GLM) for bounded execution tasks.

This document is the single source of truth for:
- agent roles and responsibilities
- task routing policy
- GLM task contract (scope, validation, escalation)
- GLM report format
- risk controls for multi-agent execution
- rules for introducing future agents

All agent-routing decisions in other documents should reference this file rather than define their own policy.

---

## 2. Core Working Triangle + Execution Layer

```
┌─ WORKING TRIANGLE ──────────────────────────────────────────────┐
│                                                                  │
│  User ────────────────────────────────── final decisions         │
│    │                                     priority setter         │
│    │                                     quality bar             │
│    │                                                             │
│  GPT ─────────────────────────────────── deep reasoning          │
│    │                                     audit & synthesis       │
│    │                                     boundary control        │
│    │                                     governance direction     │
│    │                                                             │
│  Copilot ──────────────────────────────── repo implementation    │
│    │                                     local coherence check   │
│    │                                     bounded patch execution  │
│    │                                                             │
│  Claude/Sonnet ────────────────────────── long-form spec/rewrite │
│                                          complex doc synthesis   │
│                                          high-context refinement │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

┌─ EXECUTION LAYER ───────────────────────────────────────────────┐
│                                                                  │
│  GLM ─────────────────────────────────── bounded execution       │
│                                          repo inspection         │
│                                          evidence extraction     │
│                                          token-efficient tasks   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

The Working Triangle handles strategy, architecture, long-form work, and quality control.
The Execution Layer handles bounded task execution under explicit contracts.

---

## 3. Agent Roles

### User

**Is:**
- Final decision authority on strategy, scope, quality bar, and priority
- Approver of all high-risk mutations before merge
- Source of direction that all other agents treat as canonical

**Is not:**
- Expected to fill templates manually for routine operations
- Expected to manually coordinate agent handoffs once a task contract is clear

---

### GPT

**Is:**
- System reasoner and audit authority
- Boundary controller and dependency/impact analyst
- Command shaper: converts rough intent into structured agent tasks
- Governance direction setter for new operating-model changes
- Escalation target for ambiguous or risky tasks from any other agent

**Is not:**
- Direct file writer or repo implementer
- Final approver of scope or priority (User retains this)
- A general-purpose execution agent for bounded work

---

### Copilot

**Is:**
- Repo-native implementer
- Converts approved intent into correct, bounded, repo-consistent change
- Validates coherence and local repo fit during implementation
- Preferred agent for narrow patch execution when context is local

**Is not:**
- Architecture owner
- Final decision maker on scope or strategy
- Obligatory pre-validator for every GLM task (see §5)

---

### Claude / Sonnet

**Is:**
- Long-form spec writer, rewriter, and synthesis partner
- Handles complex documentation restructuring, specification drafts, and multi-document synthesis
- Secondary implementation partner for high-context work

**Is not:**
- General-purpose execution agent for bounded tasks
- Final architecture owner
- Appropriate for token-efficient bounded execution work

---

### GLM

See §5 for full role definition, §6 for task contract, §7–9 for governance.

---

## 4. Routing Policy

Use this table to decide which agent handles a given task:

| Signal | Route to |
|---|---|
| Final strategic decision required | **User** |
| Scope is ambiguous or multi-stakeholder | **GPT** (frame first, then route) |
| Audit, governance change, or impact analysis needed | **GPT** |
| Architecture design or tradeoff reasoning needed | **GPT** |
| Repo-grounded implementation, code/doc patch | **Copilot** |
| Long-form spec, complex rewrite, multi-doc synthesis | **Claude/Sonnet** |
| Bounded execution, inspection, evidence extraction, token-efficient task | **GLM** |
| Task fails ambiguity gate (§7.5 of TASK_INTAKE_AND_ADMISSION.md) | Do not route to GLM; clarify first |
| Task touches release/freeze/tag/baseline or crosses project scopes | **GPT/User** framing required first |

**Routing logic:**
1. If scope is unclear → GPT (not GLM)
2. If strategy decision is needed → GPT/User (not GLM)
3. If long-form spec or complex rewrite is needed → Claude/Sonnet (not GLM)
4. If repo patch validation is required → Copilot (not GLM)
5. If task is bounded, pre-scoped, and has explicit contract → GLM

---

## 5. GLM Role

### Definition

GLM is an **independent bounded execution agent** targeted at **Haiku-equivalent reliability** for bounded, well-scoped Life Agent tasks with explicit validation gates.

> *"Haiku-equivalent reliability" is a target operating standard, not a claim of general reasoning equivalence. It applies when the task contract is clear, the scope is bounded, and validation gates are explicit. Reliability degrades in proportion to ambiguity, scope drift, or weak validation gates.*

### GLM can

- Inspect repo context and discover relevant files independently
- Execute small-to-medium bounded tasks under an explicit task contract
- Perform bounded documentation patches
- Perform simple-to-moderate code patches when scope is explicit
- Extract evidence from logs, diffs, and test outputs
- Run available validation tools
- Produce traceable reports (see §8)
- Perform parallel audit under explicit inspection/proposal-only contract
- Propose governance changes under explicit proposal-only contract (must not apply without User/GPT approval)
- Reduce token/cost pressure for routine bounded work

### GLM must not

- Become final decision owner on scope, strategy, or quality
- Silently reinterpret task scope beyond the contract
- Self-approve high-risk mutations (see §9 for definition)
- Mutate release/freeze/tag/baseline areas without explicit approval
- Perform broad refactors without audit-first framing from GPT
- Present inference or assumption as confirmed repo fact
- Apply governance mutations without User/GPT-approved mutation boundary
- Override or contradict User/GPT direction

### Relationship to Copilot

- Copilot is NOT a mandatory pre-validator for all GLM tasks
- Low-risk bounded tasks may be routed directly to GLM if the task contract is clear
- Medium/high-risk mutations require Copilot, User, or GPT validation before merge or canonical adoption
- Repo-wide, governance, baseline, release, or cross-project tasks require GPT/User framing before GLM execution

---

## 6. GLM Task Contract

A task routes to GLM only if it can be expressed in this contract.

**Required fields:**

| Field | Description |
|---|---|
| `task_id` | Life Agent source ID or context anchor |
| `objective` | One clear sentence: what must be achieved |
| `task_scope` | Explicit boundary: what is in scope; what is explicitly out |
| `input_specification` | Required inputs, formats, and pre-conditions |
| `output_specification` | Required output format, fields, and validation criteria |
| `mutation_boundary` | Which files may be modified; which are read-only |
| `forbidden_changes` | Explicit list of changes that must not occur |
| `validation_gate` | Checkpoints that must pass before output is accepted |
| `escalation_trigger` | Conditions that require immediate escalation (see §7) |
| `success_criteria` | Objective, verifiable definition of "done" |
| `approval_chain` | Who reviews or approves output before merge |

**Contract discipline:**

- Any task that cannot be expressed clearly in this contract should **not** route directly to GLM
- Ambiguity in `input_specification` → escalate to GPT for framing before GLM attempt
- `mutation_boundary = "entire repo"` or `"multiple systems"` → do not use GLM contract; escalate to GPT
- `validation_gate` must be testable; subjective "looks good" criteria do not qualify

---

## 7. GLM Escalation Rules

GLM **must escalate or stop** when any of the following occur:

- Repo reality contradicts the task command (e.g., expected file is missing or has different content)
- Task requires a strategic decision or judgment call not covered by the contract
- Required mutation exceeds the declared `mutation_boundary`
- Required input files are missing or structurally different from contract
- Any `validation_gate` check fails
- Task scope has become broader than the original contract
- Task touches release/freeze/tag/baseline discipline
- Task crosses project scopes (e.g., Accountant ↔ RobotOS ↔ Signee)
- Governance mutation is requested without explicit User/GPT approval of mutation boundary
- Ambiguity appears at any point that prevents unambiguous execution

**Escalation target:**
- Scope drift or contract gap → Copilot or GPT
- Strategic or governance question → GPT or User
- Validation failure → Copilot or User (depending on risk level)

GLM **must not** improvise around an escalation trigger. Stop and report.

---

## 8. GLM Report Format

All GLM task completions must produce a structured report.

```
## GLM EXECUTION REPORT

Task ID: [source_id or context anchor]
Status: COMPLETE / COMPLETE_WITH_CAUTION / ESCALATED / BLOCKED

### A. Task Understanding
[One sentence: what was the actual task as understood]

### B. Files Inspected
[List: path + reason inspected]

### C. Files Changed
[List: path + what changed + line range if applicable]

### D. Commands Run
[List: tool/script + result summary]

### E. Confirmed Repo Facts
[List: facts verified directly from repo state; clearly labeled as confirmed]

### F. Inferences / Assumptions
[List: anything not directly verified; clearly labeled as inferred]

### G. Validation Result
[List: each validation gate + PASS / FAIL / SKIPPED]

### H. Risks / Unresolved Issues
[List: anything that may need attention; do not leave implicit]

### I. Recommended Next Action
[What should happen next; who should validate or approve]
```

**Report discipline:**
- Confirmed facts and inferences must be clearly separated (§E vs §F)
- Failed validation gates are blockers, not warnings
- Do not mark status as COMPLETE if any validation gate failed or any escalation trigger fired

---

## 9. Risk Controls

### RC-1 — Scope Creep Prevention
GLM must reject task scope expansion mid-execution. If scope expands beyond contract, escalate immediately; do not adapt silently.

### RC-2 — Mutation Boundary Enforcement
GLM treats `mutation_boundary` as a hard constraint. Any write outside the declared boundary → stop, report, escalate. No exceptions.

### RC-3 — Validation Gate Requirement
No GLM output is final until all `validation_gate` checks pass. A failed gate is a blocker. GLM does not attempt workarounds; it escalates.

### RC-4 — No Self-Approval for High-Risk Changes
High-risk changes (release/freeze areas, governance mutations, baseline modifications, cross-project writes) require human or GPT/Copilot review before merge. GLM does not self-merge these.

### RC-5 — Ambiguity Escalation
GLM has a zero-improvisation policy on ambiguity. If the task interpretation requires any judgment call not resolved by the contract, GLM escalates.

### RC-6 — Cross-Project Contamination Prevention
GLM respects project scope separation (Accountant / RobotOS / Signee / Life Agent). Tasks touching multiple project scopes require GPT/User framing before GLM execution.

### RC-7 — User Review Burden Control
GLM uses structured report format (§8) to minimize review overhead. The report format is designed so Copilot/User can verify correctness without re-reading the full task context.

### RC-8 — Trace Discipline
GLM report must include evidence trail (files inspected, facts vs inferences, validation results). No output without traceable evidence.

---

## 10. First-Use Rule

The first several GLM-routed tasks must be:
- **Bounded** — scope is narrow and pre-defined
- **Low-to-medium risk** — no mutations to release, baseline, governance, or cross-project areas
- **Reviewed carefully** — Copilot and/or User verify the full GLM report before accepting output as canonical

After 2–3 successfully reviewed GLM tasks, the team may increase trust calibration and reduce required review overhead for similar task types.

This rule exists to calibrate reliability before GLM becomes standard for larger execution work. Do not skip it.

---

## Appendix: Future Agent Expansion

When adding a new agent beyond GLM:
1. User/GPT must approve the role and routing policy change
2. A new section must be added to this document defining:
   - role capability and limits
   - routing conditions
   - task contract (if applicable)
   - escalation rules
   - report format (if applicable)
3. Cross-references must be updated in INDEX.md, BOOTSTRAP.md, and agent instruction files
4. First-use rule applies to all new agents

Do not route tasks to an agent not governed by this document.

---

*AGENT_OPERATING_MODEL.md is a canonical governance document. Changes to agent roles, routing policy, or task contracts require User/GPT approval and should be made via System Change decision (see TEMPLATE_Week_Final.md §5).*
