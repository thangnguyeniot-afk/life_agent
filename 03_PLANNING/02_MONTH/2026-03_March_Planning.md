# 2026-03 — Monthly Planning & Review (Agent-Ready)

> **Month:** 2026-03 (March)  
> **Total time:** 45–60 phút  
> **Vai trò:** Đánh giá xu hướng + điều chỉnh cấp chiến thuật (không phải tổng hợp tuần, quản lý task, hay nghiên cứu sâu).  
> **Nguyên tắc:** Nhìn **xu hướng**, đánh giá **hệ**, không đánh giá bản thân. Thu hẹp/tinh chỉnh hệ thống, **không mở rộng thêm phức tạp**.

---

# A) Monthly Planning (đầu tháng) — 25–35 phút

## 1) Định hướng tháng này (5 phút)
- **Theme (1 câu):** Freeze scope + chạy được basic flow lặp lại; mọi thứ còn lại là "nice-to-have".
- **North Star (ưu tiên tuyệt đối):** Đến 31/03, Signee có demo scope v1 rõ ràng + board chạy basic flow ổn định có log/runbook.
- **Stop doing (1–3 mục):**
  1) Không mở thêm "feature mới" khi scope chưa freeze (bất kỳ dự án nào).
  2) Không nhảy giữa 3–4 việc khó trong ngày (chặn "priority distortion").
  3) Không làm XL trực tiếp — task nào >2h phải tách phase.

## 2) Core Outcomes của tháng (tối đa 3) — 10 phút
> Outcome = đo được (không phải to-do).  
> Mỗi outcome phải có Artifact để không trôi.

### 🗺 Outcome ↔ Project map
| # | Outcome | Project | Deadline |
|---|---|---|---|
| O1 | Signee Demo Scope Freeze v1 | **Signee** | 2026-03-14 |
| O2 | Board bringup + RobotOS Middleware & STM32F4 | **RobotOS** | 2026-03-28 |
| O3 | Frontend skeleton + 1 flow tối thiểu | **Signee** | 2026-03-31 |

---

1) **Outcome #1 — Signee Demo Scope Freeze v1 (internal sign-off)**
   - **Project:** Signee
   - **Impact:** Chặn scope creep + làm nền cho demo tháng 4
   - **Metric / DoD:**
     - Có feature list MUST + OUT-OF-SCOPE list + acceptance (demo criteria) cho từng feature.
     - Đọc lại sau 10 phút vẫn hiểu "demo gồm gì / không gồm gì / đo bằng gì". (DONE = dừng lại không mất ngữ cảnh)
   - **Deadline:** 2026-03-14
   - **Owner:** You
   - **Artifact (bắt buộc):** `RFC_Signee_DemoScope_v1.md` + `CHECKLIST_Signee_DemaCriteria.md`

2) **Outcome #2 — Board basic flow ổn định + RobotOS Middleware & STM32F4 bringup**
   - **Project:** RobotOS
   - **Impact:** Unblock v0.1 Alpha (deadline 2026-04-30) — không bringup xong tháng 3 = trễ v0.1
   - **Metric / DoD:**
     - Cả 2 board (board cũ + board mới) chạy được basic flow lặp lại ≥3 lần (cùng điều kiện)
     - Có log: lỗi / nguyên nhân / cách fix / điều kiện chạy lại
     - Có "runbook 1 trang" để setup và chạy lại nhanh
     - Có định nghĩa test case + quality gate rõ ràng (cho dev test tuần 4)
     - RobotOS: Zephyr workspace setup xong (west init/update, build OK trên STM32F4)
     - RobotOS: Middleware core skeleton khởi động (pub/sub interface + memory pool ở mức compile & link)
     - RobotOS: STM32F4 bringup tối thiểu (build + flash + hello world chạy được)
   - **Deadline:** 2026-03-28
   - **Owner:** You
   - **Artifact (bắt buộc):** `LOG_Board_Bringup_Mar.md` + `RUNBOOK_Board_BasicFlow_1page.md` + `LOG_RobotOS_Bringup_Mar.md`

3) **Outcome #3 — Frontend started (1 app skeleton + 1 flow tối thiểu)**
   - **Project:** Signee
   - **Impact:** Mở đường cho demo flow tháng 4; ADR kiến trúc tránh rewrite sau
   - **Metric / DoD:**
     - Có skeleton chạy được (routing/navigation baseline)
     - Có 1 flow end-to-end tối thiểu (mock data ok)
     - Có 1 ADR chốt quyết định kiến trúc UI
   - **Deadline:** 2026-03-31
   - **Owner:** You
   - **Artifact (bắt buộc):** `ADR_UI_Architecture.md` + commit(s) + link repo

## 3) Capacity & Rhythm (để không overload) — 5–10 phút
- **WIP max (cá nhân):** 2–3 việc lớn / tuần
- **Capacity budget (%):**
  - Signee (dominant): 35%
  - RobotOS (middleware + bringup): 30%
  - Zephyr KTLO (work-world): 15%
  - Buffer (đứt mạch, fix, emergency ≤48h): 20%
- **Deep blocks/day:** 2 blocks (90')
- **Office hours (techlead):** slot 1 (Tue/Thu 16:00–16:30) ; slot 2 (Sat 10:00–10:30) *(có thể đổi theo thực tế)*

## 4) Weekly Intent (4 tuần) — 5–10 phút
> Mỗi tuần 1 "intent" rõ ràng để giảm mơ hồ và tránh scope phình.

- **Week 1 (2026-W09): Setup + Framing**
  - Big: draft demo scope v0 + test board (board mới)
  - Small: tạo LOG + checklist bring-up; RobotOS west init/update + STM32F4 hello world
  - KTLO focus: dọn 1–2 nợ nhỏ (không mở việc mới)

- **Week 2 (2026-W10): Freeze v1 + First loop**
  - Big: Signee demo scope freeze v1 (internal sign-off)
  - Small: run basic flow lần 2–3, ghi rõ điều kiện; giao board + assign việc cho các anh em; RobotOS scope freeze v1
  - KTLO focus: giữ nhịp "ít nhưng đúng"

- **Week 3 (2026-W11): Stabilize + QA strategy**
  - Big: board stabilize top 3 blockers → runbook 1 trang; define quality gate + test cases + test methodology cho dev (tuần 4)
  - Small: RobotOS Middleware core skeleton (pub/sub + memory pool compile & link OK)
  - KTLO focus: không để "chuyển ngữ cảnh" phá nhịp

- **Week 4 (2026-W12): All apps running + April readiness**
  - Big: chốt Outcome #2 (board runbook + RobotOS bringup log); see all apps running (board + Frontend + RobotOS); gom artifact + link
  - Small: Frontend test bằng PWA (OK on mobile); RobotOS STM32F4 bringup xác nhận lần cuối; 2–4 contracts I/O
  - KTLO focus: đóng debt, không mở scope

## 5) Risk / Assumption / Decisions (P0) — 5 phút
### Top risks (3)
1) Scope creep (demo scope không "ký" được → kéo dài sang tháng 4)
2) Board instability (basic flow không lặp lại được → tốn tuần 3–4)
3) Priority distortion (emergency xen vào làm vỡ deep blocks, trôi artifact)

### Assumptions
- Board/hardware đã sẵn sàng để test thực tế trong tháng 3.
- Demo scope có thể đóng băng nội bộ (ít nhất mức "v1") mà không cần chờ hoàn hảo.
- RobotOS tháng 3: scope freeze v1 + bắt đầu Middleware core skeleton + STM32F4 bringup tối thiểu (không mở thêm module ngoài pub/sub + memory pool).

### Decisions needed (24/48/72h)
- [ ] Decision: "Basic flow" định nghĩa chính thức là gì? | Deadline: 2026-03-02 | Owner: You
- [ ] Decision: Signee demo MUST list (top 10) chốt v0 | Deadline: 2026-03-03 | Owner: You
- [ ] Decision: UI architecture choice (routing/state strategy) cho skeleton | Deadline: 2026-03-10 | Owner: You

## 6) Reading budget (để agent đọc ít nhưng đúng)
- **INDEX:** `00_INDEX.md` (map vault + map repo bus)
- **00_CONTEXT:** `00_CONTEXT/Quarter_Hardening_Mar-May.md`
- **Snapshot (latest):** `SNAPSHOTS/2026-02_EndMonth.md`
- **Week plans:** `WEEK/2026-W09.md` … `2026-W12.md`
- **ADR liên quan:** `ADR_UI_Architecture.md`, `ADR_Signee_DemoCriteria.md` (nếu có)
- **Team tools (Jira/GitHub links):** *(điền link repo + board notes)*

---

# B) Monthly Review (cuối tháng) — 45–60 phút

## 0) DoD (Definition of Done) cho Monthly Review
Monthly Review được coi là **HOÀN THÀNH** khi:
- Có cái nhìn rõ ràng về **xu hướng tháng**
- Tất cả **System Change** trong tháng được đánh giá (giữ/điều chỉnh/rollback)
- Trọng tâm tháng tới được **thu gọn & rõ ràng** (1–2 điểm)
- Không mang cảm giác "phải làm nhiều hơn", mà là "làm đúng hơn"

---

## 1) Executive Summary of the Month (5 phút)
- **Tháng này nhìn chung thế nào? (1–3 câu):** …
- **Trạng thái tổng thể:** ⬆️ / ➖ / ⬇️
- **Cảm nhận chung về năng lượng & nhịp sống:** …
- **Một câu mô tả tháng:** …

---

## 2) Output & Outcome Review (10–15 phút)
> Nhìn output như **tín hiệu**, không quản lý delivery.

### 📦 Output đáng chú ý
- **Những output quan trọng đã hoàn thành:**
  - …
  - …
- **Output quan trọng chưa đạt / bị trì hoãn:**
  - …
  - …

### 🎯 Outcome thực tế
- **Điều gì thực sự tạo ra giá trị trong tháng này?**
  - …
- **Điều gì làm nhiều nhưng giá trị thấp?**
  - …

---

## 3) System Change Review (10–15 phút)
> Đánh giá các "System Change" đã triển khai trong tháng (thói quen/cơ chế/công cụ/quy tắc).

| System Change | Mục tiêu | Kết quả (Effective/Partial/Ineffective) | Quyết định (Giữ/Điều chỉnh/Rollback) |
|---|---|---|---|
| … | … | … | … |
| … | … | … | … |
| … | … | … | … |

**Rule (cứng):**
- Mỗi System Change **phải có kết luận** trong tháng.
- Không để System Change trôi sang tháng sau mà **không đánh giá**.

---

## 4) Life Anchors — Monthly Trend (5–10 phút)
> Đánh giá xu hướng duy trì cuộc sống trong cả tháng.

| Anchor | Xu hướng (⬆️/➖/⬇️) | Nhận định ngắn |
|---|---|---|
| Movement |  |  |
| House Basics |  |  |
| Eat Properly |  |  |
| Recovery |  |  |
| Connection |  |  |

---

## 5) Anti-Anchors — Monthly Pattern (5–10 phút)
> Nhận diện pattern phá hoại lặp lại trong tháng.

- **Anti-Anchor nào xuất hiện nhiều nhất?** …
- **Có hành vi nào trở thành "bình thường mới"?** …
- **Điều gì cần chặn sớm trong tháng tới?** …

---

## 6) Focus Adjustment for Next Month (10 phút)
> Tinh chỉnh trọng tâm, **không đặt mục tiêu tham vọng**.

### 🎯 Trọng tâm chính của tháng tới (1–2)
1) …
2) …

### ⛔ Điều cần giảm / bỏ / tránh
- …
- …

### 🛠 System Change dự kiến (nếu có)
- …

---

## 7) Context Compression (nếu tới chu kỳ 2–4 tuần / milestone)
- Snapshot created? (Yes/No): …
- Snapshot link: …

---

## Appendix (tuỳ chọn)
- PR/commit/doc quan trọng
- Links: ADR / Spec / Logs / Jira/GitHub
- …

---

## Note về Daily HOT 15 ngày (để khỏi nổ folder)
- Daily files chỉ giữ **15 ngày HOT**.  
- Lịch sử dài hạn nằm ở **Weekly/Monthly/Snapshots** và **Logs**.
