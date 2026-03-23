# Signee – Project Context

> **Dùng để import vào AI agent.**  
> Cập nhật file này mỗi đầu sprint hoặc khi có thay đổi lớn.  
> **Last updated:** 2026-03-22 (W12 planning, M3 status update)

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
| **% hoàn thành** | ~18% (Docs 100% ✅ · Android scaffold 15% · PWA 0% · CI/CD 10% · Backend external · M3 polish optional W12) |
| **Sprint hiện tại** | Sprint 1 – Foundation (W11 M3 polish complete; W12 optional extended polish if capacity)

### Trạng thái theo thành phần

| Component | Status | Ghi chú |
|---|---|---|
| **Docs / Planning** | ✅ Done | Sprint 0 hoàn thành (Dec 2024 – Jan 2025); W11 complete |
| **M3 Polish (Optional)** | ✅ Complete (W11) / ⏳ Enhanced polish if capacity (W12) | W11 M3 polish done; W12 optional extended polish defers if Zephyr/RobotOS consume capacity |
| **Android App** | 🔄 In progress (scaffold) | Hilt DI ✅, Room DB ✅, Retrofit ✅, 3 Activities (Mirror/QR/Splash) shell với TODO – chưa có logic |
| **PWA** | ❌ Not started | Directory hoàn toàn trống – chưa có code |
| **Cloud Backend** | <!-- TODO --> | <!-- TODO --> |
| **AI Fitting Service** | <!-- TODO --> | <!-- TODO --> |
| **CI/CD Pipeline** | ⚠️ Not implemented | Docs & plan xong ✅, nhưng GitHub Actions / Firebase chưa setup (tasks 4.1–4.6 còn ⏳) |

### 3 Milestone tiếp theo

| # | Milestone | Target date | Owner |
|---|---|---|---|
| 1 | Android core: Camera capture + QR display + WebSocket client | <!-- TODO: target date --> | Android Dev |
| 2 | PWA scaffold + Auth flow + QR connect (Sprint 2) | <!-- TODO: target date --> | PWA Dev |
| 3 | End-to-end fitting flow Beta demo: PWA ↔ WebSocket ↔ Android ↔ AI | <!-- TODO: target date --> | Full team |

### Blockers

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
