# Signee – Project Context

> **Dùng để import vào AI agent.**  
> Cập nhật file này mỗi đầu sprint hoặc khi có thay đổi lớn.  
> **Last updated:** 2026-03-29 (W12 final: M3 polish blocked, team test reports dependency documented)

---

## Table of Contents

- [1️⃣ Project Identity](#1%EF%B8%8F%E2%83%A3-project-identity)
- [2️⃣ Current State](#2%EF%B8%8F%E2%83%A3-current-state)
- [3️⃣ Resource Model](#3%EF%B8%8F%E2%83%A3-resource-model)
- [4️⃣ Risk Snapshot](#4%EF%B8%8F%E2%83%A3-risk-snapshot)
- [🔎 Tài liệu liên quan](#-tài-liệu-liên-quan)

---

| **Mục tiêu gần nhất** | Alpha release – Android capture/QR hoạt động + PWA auth/connect flow |
| **Phase** | Build (Sprint 1 – Foundation) |

**Mô tả ngắn:**  
Hệ thống thử quần áo ảo gồm 3 thành phần chính:
- **Android Mirror App** – Capture ảnh user, hiển thị kết quả AI trên màn hình gương
- **PWA (Mobile Web)** – User scan QR, chọn trang phục, trigger fitting, xem gallery
- **Cloud Backend** – REST API + WebSocket Relay + AI Fitting Service

---

## 2️⃣ Current State

| Field | Value |
|---|---|
| **% hoàn thành** | ~18% (Docs 100% ✅ · Android scaffold 15% · PWA 0% · CI/CD 10% · Backend external · M3 polish 100% ✅ W11, extended polish ⏸️ blocked) |
| **Sprint hiện tại** | Sprint 1 – Foundation (W12 M3 extended polish ⏸️ blocked awaiting team test reports; W13 continue when reports available)

### Trạng thái theo thành phần

| Component | Status | Ghi chú |
|---|---|---|
| **Docs / Planning** | ✅ Done | Sprint 0 hoàn thành (Dec 2024 – Jan 2025); W11 complete |
| **M3 Polish (Baseline)** | ✅ Complete (W11) | W11 M3 polish done ✅ (baseline quality); all acceptance criteria met |
| **M3 Extended Polish** | ⏸️ BLOCKED (W12) | Waiting for team test report submission; cannot proceed with quality refinement until reports uploaded; defer to W13 when available |
| **Android App** | 🔄 In progress (scaffold) | Hilt DI ✅, Room DB ✅, Retrofit ✅, 3 Activities (Mirror/QR/Splash) shell with TODO – logic pending |
| **PWA** | ❌ Not started | Directory empty – no code; Sprint 2 dependency |
| **Cloud Backend** | <!-- TODO --> | <!-- TODO --> |
| **AI Fitting Service** | <!-- TODO --> | <!-- TODO --> |
| **CI/CD Pipeline** | ⚠️ Not implemented | Docs & plan complete ✅; GitHub Actions / Firebase setup pending |

### 3 Milestone tiếp theo

| # | Milestone | Target date | Owner |
|---|---|---|---|
| 1 | Android core: Camera capture + QR display + WebSocket client | <!-- TODO: target date --> | Android Dev |
| 2 | PWA scaffold + Auth flow + QR connect (Sprint 2) | <!-- TODO: target date --> | PWA Dev |
| 3 | End-to-end fitting flow Beta demo: PWA ↔ WebSocket ↔ Android ↔ AI | <!-- TODO: target date --> | Full team |

### Blockers

- **M3 Extended Polish (W12)** ⏸️ **BLOCKED** – Waiting for team test reports; cannot proceed with quality refinement until reports uploaded; **Action:** Resume W13 when team reports available
- **PWA chưa bắt đầu** – directory rỗng, chưa assign dev, blocking toàn bộ Sprint 3
- **CI/CD chưa có pipeline thực tế** – GitHub Actions chưa được setup dù docs đã viết xong (tasks 4.1–4.6 còn ⏳)
- **Android activities chỉ là shell** – MirrorActivity, QRCodeActivity đều là `// TODO`, chưa có camera/WebSocket logic
- **Mock server chưa chạy** – task 3.2 ⏳, block integration testing local

---

## 3️⃣ Resource Model

| Role | Người | Phụ trách |
|---|---|---|
| **Bạn (PM / Tech Lead)** | <!-- TODO: tên --> | Architecture decisions, documentation, review |
| **Android Dev** | <!-- TODO: tên --> | Android Mirror App |
| **PWA Dev** | <!-- TODO: tên --> | PWA (Mobile Web App) |
| **Backend / DevOps** | <!-- TODO: tên --> | Cloud API, WebSocket, CI/CD |
| **QA** | <!-- TODO: tên --> | Testing, bug tracking |

### Weekly load dự kiến

| Week | Focus block | Ai làm |
|---|---|---|
| <!-- TODO: e.g. "W1 (Feb 24)" --> | <!-- TODO: e.g. "PWA init + Auth flow" --> | <!-- TODO --> |
| <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |
| <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |

---

## 4️⃣ Risk Snapshot

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 1 | **PWA chưa bắt đầu** – nếu không có dev sớm, Beta deadline bị trượt | 🔴 High | 🔴 High | Assign PWA dev ngay, dùng Vite + React scaffold để rút ngắn setup |
| 2 | <!-- TODO: e.g. "AI service latency > 10s ảnh hưởng UX" --> | <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |

### Scope freeze status

- **Scope đã freeze?** <!-- TODO: Yes / No / Partial -->
- **Features confirmed cho MVP:**
  - ✅ QR scan → Connect to Mirror
  - ✅ Garment browsing & selection
  - ✅ AI virtual try-on (generate fitting)
  - ✅ Gallery view (Save / Share / Mirror display)
  - ✅ Mix & Match (swap top/bottom)
  - ⏳ Purchase flow → **Deferred to future version**
  - ⏳ Cloud gallery sync → **Deferred to future version**

---

## 📎 Tài liệu liên quan

| Tài liệu | Link |
|---|---|
| Project Overview | `overall/PROJECT_OVERVIEW.md` |
| User Flow | `docs/user-flow/USER_FLOW.md` |
| API Specs | `docs/core/API_SPECS.md` |
| Architecture | `docs/core/ARCHITECTURE.md` |
| Release Plan | `docs/setup-deployment/RELEASES.md` |
| Sprint History | `docs/sprints/` |

---

# 2026 Signee Year-End Outlook — SECC / Gương thần / Locator Pipeline

> **Added:** 2026-05-05 (W18)
> **Type:** Strategic horizon context — NOT W18 execution tasks.
> **Purpose:** Record user-provided May→June→year-end signals to inform future planning, SECC contract analysis, resource allocation, delegation boundaries, and year-end forecast.
> **Scope boundary:** Do not convert any item in this section into immediate weekly tasks without explicit TASK_INTAKE admission (§7.5).

---

## 1. Purpose

This section records strategic horizon context for the Signee project covering May 2026 through year-end. It is **not** an execution task list and must not be treated as W18 or W19 execution scope.

It is intended to inform:
- May/June planning decisions
- SECC contract analysis (scope, cost, risk)
- Resource forecast and allocation
- Delegation boundaries (Anh Khương scope)
- Year-end project risk and product commitment

No item in this section should be scheduled into a weekly PEC or TickTick sync without passing through TASK_INTAKE §7.5 admission.

---

## 2. Confirmed / User-Provided Signals

Signals captured 2026-05-05 (W18). Confidence = user-stated unless otherwise noted.

| Signal | Current Understanding | Timing | Confidence |
|---|---|---|---|
| Gương thần June demo | Demo of "magic mirror" product needed in June | June 2026 | High — user stated |
| Basic features sufficient for demo | Full production scope not required; demo = basic feature set | June 2026 | High — user stated |
| SECC District 7 contract | A contract is needed in June for SECC District 7 deployment | June 2026 | High — user stated |
| Contract side decided by partner | User does not control contract-side details; partner decides | June 2026 | High — user stated |
| Kickoff late June / early July | Project expected to kick off late June or early July | Late Jun / Early Jul 2026 | Medium — timing conditional on contract |
| 12 Signee devices | SECC scope includes 12 Signee devices | SECC deployment | High — user stated |
| Locator guest frontend paid webapp | Locator frontend for guests needs paid clip/photo webapp | H2 2026 | Medium — product model stated |
| Locator model = screen + mobile webapp | Similar to current Signee: physical screen + mobile PWA hybrid | H2 2026 | High — user stated |
| RBB missing digital signing | RBB platform lacks digital signing capability | Current gap | High — user stated |
| RBB digital signing → delegate Anh Khương | RBB digital-signing work should not be absorbed by user | To assign | High — user stated |
| Business advertising needs booking mechanism | Ad scenarios require a booking flow | H2 2026 | High — user stated |
| Booking mechanism → delegate Anh Khương | Advertising booking mechanism should be delegated | To assign | High — user stated |
| Mirror dangerous/prohibited-content research | Exceptional/dangerous/prohibited-content scenarios need research | June 2026 | High — user stated; NOT W18 work |

---

## 3. Timeline View

### May 2026

- Keep Signee light; do not start heavy production.
- Focus on: cost/accounting clarity, contract analysis inputs, business/company process.
- W18 Signee scope: customer meeting (scope clarification) + cost accounting only.
- Do not schedule implementation tasks.
- Prepare analysis inputs for SECC contract review (see §5).

### June 2026

- **Gương thần demo** — basic feature set; target demo-ready state.
- **SECC contract analysis** — full scope analysis against §5 inputs.
- **SECC contract preparation/closure** — if partner side is ready.
- **Mirror dangerous/prohibited-content research** — must happen in June before product commitment.
- **Locator paid clip/photo webapp scope** — clarify commercial and technical model.
- **12-device deployment assumptions** — validate hardware/software/support model.

### Late June / July 2026

- Potential kickoff window.
- Convert contract/scope into implementation plan **only after** commercial clarity (contract signed, payment terms clear, scope locked).
- Do not assume kickoff until contract, payment, and scope are confirmed.

### H2 2026 / Year-End

- Potential SECC rollout and device operations.
- Potential paid media/webapp product line (clip/photo).
- Potential device operations/support burden (12 devices deployed).
- Need forecast for: staffing, cost, maintenance/support, technical risk.

---

## 4. Workstream Breakdown

| Workstream | Description | Owner / Boundary | Timing | Notes |
|---|---|---|---|---|
| Gương thần demo | Basic feature demo for SECC/customer | User (scope decision); team (implementation) | June 2026 | Demo scope = basic features; do not inflate |
| SECC contract analysis | Analyse SECC contract terms, scope, cost, risk | User owns framing + decision | June 2026 | See §5 for required analysis inputs |
| 12 Signee device deployment | Hardware/software/support model for 12 devices | User owns scope/cost decision; team implements | Late Jun / Jul+ | Do not start implementation before contract |
| Locator guest frontend paid webapp | Paid clip/photo flow for guest locator frontend | User owns product model; dev implements | H2 2026 | Commercial/privacy obligations to clarify first |
| RBB digital signing | Fill RBB platform digital-signing gap | **Delegate to Anh Khương** | To assign | User must not absorb this work |
| Business advertising booking mechanism | Booking flow for advertising scenarios | **Delegate to Anh Khương** | To assign | User owns decision; Anh Khương implements |
| Mirror safety / content research | Research dangerous/prohibited/exceptional content scenarios | User directs; research output | June 2026 | Required before any product commitment on mirror |

**Delegation rule:** User owns contract/cost/scope analysis and decision framing. User must not absorb RBB digital signing or advertising booking mechanism implementation.

---

## 5. Contract / Cost Analysis Inputs

SECC contract analysis must include at minimum:

- Device count: 12 Signee devices
- Hardware/device cost (unit + total)
- Installation and setup cost
- Ongoing maintenance and support cost
- Software/webapp scope (what is delivered, what is excluded)
- Paid clip/photo webapp flow (included or separate contract?)
- Payment and transaction handling (who owns the payment stack?)
- Data, media, and storage requirements
- Privacy and content responsibility (who is liable for user content?)
- SLA and support expectations (response time, uptime guarantees)
- Partner/customer responsibilities
- Advance payment and milestone payment structure
- Warranty, repair, and device replacement terms
- Margin and risk buffer

---

## 6. Product / Architecture Implications

- **Locator frontend model** resembles current Signee: physical screen + mobile webapp hybrid. Implementation playbook is likely reusable; confirm scope overlap.
- **Paid clip/photo webapp** may create payment processing, media storage, and privacy/content obligations. These must be scoped and costed before product commitment.
- **RBB digital signing gap** belongs to the RBB platform. This is a separate workstream delegated to Anh Khương; do not treat it as Signee core work.
- **Booking mechanism** for advertising scenarios is a separate workstream delegated to Anh Khương. User owns the decision to include/exclude; Anh Khương owns implementation.
- **Mirror safety scenarios** (dangerous, prohibited, exceptional content) require June research before any product or policy commitment. Do not make content commitments without this research.

---

## 7. Risks / Unknowns

| Risk / Unknown | Impact | Next Clarification |
|---|---|---|
| Contract side decided by partner | User has limited leverage on contract terms; scope may drift | Clarify what user can negotiate vs. must accept |
| Scope not locked | Delivery commitment premature; may overcommit | Lock scope before any implementation estimate |
| Payment / advance not confirmed | Cash flow risk; do not start work before payment clarity | Confirm advance payment model in June |
| Kickoff timing uncertain | Planning instability; W19/W20 may need re-anchor | Track: contract signed = kickoff trigger |
| 12-device deployment assumptions | Hardware/logistics/support burden unknown | Validate with partner before contract close |
| Media / payment / privacy obligations | Paid clip/photo creates non-trivial compliance surface | Legal/privacy review before product launch |
| Content abuse / dangerous-scenario risk | Mirror product may face misuse; requires safety policy | June research output required before commitment |
| Delegation dependency on Anh Khương | RBB + booking work stalls if delegation is not formalized | Confirm delegation timeline in June planning |
| User capacity risk | Too much absorbed = Phase 3 regression + RobotOS slip | Enforce delegation boundary strictly |

---

## 8. Planning Implications

- **W18:** Do not inject this as heavy execution. W18 Signee scope = customer meeting + cost accounting only (already in PEC).
- **May:** Remains RobotOS-heavy. Signee in May = contract/cost/scope clarity only. No production tasks.
- **June planning** must include: Gương thần demo, SECC contract analysis, mirror safety research, locator webapp scope clarification.
- **W18/W19** should only carry lightweight Signee prep if explicitly admitted through TASK_INTAKE §7.5 admission gate.
- **Future weekly plans** must not schedule Signee implementation tasks until scope, payment, and contract are clear.
- **Delegation** (RBB digital signing, booking mechanism) should be formalized in June planning, not deferred indefinitely.
- **Cross-project restructure decisions** (user bottleneck reduction, delegation map, compensation, business setup): `04_LOGS/Decision_Memo_2026-05_Life_Agent_Restructure.md`. Signee-specific signals remain in this file (§2026 Year-End Outlook).

---

## 9. Open Questions

- What basic features are required for the Gương thần June demo? (Feature list needed before June sprint planning)
- What exactly is included in the SECC contract scope? (Software only? Hardware? Support? Media?)
- Who owns contract drafting and approval on the partner side?
- What is the commercial model for the paid clip/photo webapp? (Per-use? Subscription? One-time?)
- What is the expected deployment and support model for 12 devices? (On-site? Remote? Who handles failures?)
- What must be delegated to Anh Khương and by when? (RBB digital signing + advertising booking — needs timeline)
- What content/safety scenarios must be blocked, moderated, or flagged on the mirror?
