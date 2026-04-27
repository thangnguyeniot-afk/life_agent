# knowledge/design/

This folder holds persistent design documents for Life Agent projects and the operating system itself.

---

## What belongs here

- Interface sketches (component boundaries, data flow, API shape)
- Architecture notes (layer decisions, system boundary definitions)
- Design explorations that are not yet decisions but are worth keeping
- System structure notes that are stable enough to reference across weeks

---

## What does NOT belong here

| Artifact type | Correct location |
|---|---|
| Architecture Decision Records (binding decisions) | `04_LOGS/ADR/` |
| Weekly execution logs or daily plans | `03_PLANNING/` |
| Temporary scratch notes | Do not commit; discard after use |
| Spike outcomes and research findings | `04_LOGS/Spike_Log.md` or `knowledge/research/` |
| OS procedures and canonical rules | `01_OS/` |

---

## Promotion rule

If a design note here becomes a binding architectural decision, record or cross-reference it through:
- `04_LOGS/ADR/` for Architecture Decision Records
- The relevant OS section in `01_OS/operating_system_thang_nguyen_v1_1.md`
- The relevant operational procedure in `01_OS/04_OPERATIONS/`

Design notes here are not binding until promoted.
