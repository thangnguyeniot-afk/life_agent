# 🧭 QUARTER REVIEW & PLANNING (FINAL -- Delivery + Capacity)

> **⚠ Lưu ý đặc biệt:** Quý này là quý phi tiêu chuẩn — bao gồm **3 tháng: tháng 3 · 4 · 5**. Tháng 6 sẽ được plan riêng sau khi kết thúc quý này. Mọi deadline, stage gate, và capacity plan trong tài liệu này chỉ có hiệu lực đến hết **31/5**.

------------------------------------------------------------------------

# I. QUARTER REVIEW

## 🔹 Artifact tồn tại

### Zephyr

-   DBUS2 testing document hoàn chỉnh\
-   Môi trường test gần hoàn thiện\
-   Framework phương pháp viết test rõ ràng

### Signee

-   Khung project hoàn chỉnh\
-   Thiết kế frontend 2 app\
-   Board đã nhận

### RobotOS

-   Nền tảng kiến thức hệ thống\
-   Hardware board hoàn chỉnh

------------------------------------------------------------------------

## 🔹 Biggest Bottleneck

> Quản lý năng lượng và tập trung chưa tốt.

------------------------------------------------------------------------

# II. STRATEGIC SPINE

## 🎯 Strategic Theme

Deliver Under Constraint & Expand Capacity Safely.

------------------------------------------------------------------------

## 🏗 Core Objectives

1.  Hoàn thành Signee Series A Demo trước 30/5.\
2.  Hoàn thành RobotOS Prototype chạy trên board trước 31/5.\
3.  Duy trì Zephyr release ổn định.\
4.  Nâng capacity từ 3--4 block → 5 block có kiểm soát.

------------------------------------------------------------------------

## ⚠ Risk To Avoid

1.  Song song đẩy full power Signee & RobotOS trước tháng 4.\
2.  Scope creep RobotOS.\
3.  Overload do tăng block quá nhanh.\
4.  Delegate không rõ ràng dẫn đến sửa lại toàn bộ.

------------------------------------------------------------------------

# III. PROJECT ALLOCATION

## 📅 Phase 1 (→ 30/4)

-   Signee --- Dominant\
-   RobotOS --- Structured Momentum\
-   Zephyr --- Maintenance

------------------------------------------------------------------------

## 📅 Phase 2 (Tháng 5) — Dual Core Delivery

-   Signee --- Co-Dominant (Demo stabilization + delivery 30/5)\
-   RobotOS --- Co-Dominant (Prototype sprint + delivery 31/5)\
-   Zephyr --- Stable

> Priority order nếu conflict: **Signee Demo > RobotOS Prototype > Zephyr.**
> Cả 2 deadline đều là 30–31/5 — không có slack để hoán đổi.

------------------------------------------------------------------------

## 📊 Effort Budget by Phase

> Portfolio rule cấp quý — dùng trong Weekly Review để đo lệch. Nếu lệch > 15% so với target → điều chỉnh phân bổ ngay, không chờ tháng sau.

| Project | Phase 1 (→ 30/4) | Phase 2 (Tháng 5) |
|---------|:----------------:|:-----------------:|
| Signee  | ~60%             | ~40%              |
| RobotOS | ~25%             | ~45%              |
| Zephyr  | ~15%             | ~15%              |

> ⚠ Phase 2 có 2 deliverable song song (Signee demo 30/5 + RobotOS prototype 31/5). Nếu conflict → Signee demo được ưu tiên (xem Emergency override tại 10.1).
>
> **Reconciliation rule — Emergency Override vs Effort Budget:** Emergency override (≤8h) là ngoại lệ có time-bound, không trigger "lệch >15%" rule trong thời gian override. Sau override, rebalance lại effort trong vòng 3 ngày tiếp theo. Nếu lệch kéo dài >3 ngày sau override → mới trigger điều chỉnh phân bổ.

------------------------------------------------------------------------

# IV. MONTHLY DIRECTION (SKELETON)

## 📅 Month 1 — Setup & Scope Freeze

-   Signee: test board + lock scope demo
-   RobotOS: freeze scope prototype + define interfaces
-   Anti-goal: không mở module mới

------------------------------------------------------------------------

## 📅 Month 2 — Delivery Signee

-   Signee: finish demo + stabilize (no new features after mid-month)
-   RobotOS: momentum + delegated docs/tests
-   Anti-goal: không mở rộng kiến trúc

------------------------------------------------------------------------

## 📅 Month 3 — Delivery RobotOS

-   RobotOS: prototype sprint + fix critical bugs
-   Signee: stabilization
-   Anti-goal: không thêm feature

------------------------------------------------------------------------

# V. STAGE GATES (Checkpoint theo Phase)

> Stage Gate là cột mốc điều hướng cứng: nếu Gate chưa pass → không mở scope mới, ưu tiên unblock gate đó trước. Gate ràng buộc plan tháng với nhau.

| Gate | Thời điểm | Điều kiện pass |
|------|-----------|----------------|
| **Gate A** | Cuối Month 1 (31/3) | Signee scope lock · RobotOS interface freeze |
| **Gate B** | Cuối Month 2 (30/4) | Signee feature freeze |
| **Gate C** | Cuối Month 3 (30/5) | Signee demo ready · Demo accepted by stakeholder |
| **Gate D** | Cuối Month 3 (31/5) | RobotOS prototype chạy trên board thật |

------------------------------------------------------------------------

# VI. CAPACITY EXPANSION LAYER

## 🎯 Capacity Objective

Cuối quý đạt:

-   4 block ổn định/ngày\
-   5 block 2--3 ngày/tuần\
-   Không crash năng lượng

------------------------------------------------------------------------

## 🔹 Phase A --- Calibration (2–3 tuần)

-   Giữ 3--4 block/ngày\
-   Tăng hiệu suất/block\
-   Giảm khởi động \< 10 phút\
-   Mỗi block có artifact rõ

------------------------------------------------------------------------

## 🔹 Phase B --- Controlled Overload (Tháng 4)

-   Tối đa 2 ngày/tuần 5 block\
-   Không 2 ngày 5 block liên tiếp\
-   Sau 5 block → ngày hôm sau ≤ 4 block\
-   Không tăng scope

------------------------------------------------------------------------

## 🔹 Phase C --- Dual Delivery Sprint (Tháng 5)

-   Mục tiêu kép: Signee demo-ready (30/5) + RobotOS prototype-ready (31/5)\
-   Cấu trúc block: Signee testing block ưu tiên • RobotOS sprint block điền vào thời gian còn lại\
-   Tối đa 3 ngày liên tiếp 5 block — sau đó recovery 2 ngày\
-   Ngủ ≥ 6h30\
-   Không tập nặng\
-   Nếu conflict → Signee ưu tiên, không bù sprint RobotOS bằng cách cắt recovery

------------------------------------------------------------------------

# VII. ENERGY PROTECTION RULES

-   Không tăng block và tăng scope cùng lúc\
-   Nếu mệt mức 4--5 trong 3 ngày liên tiếp → giảm về 3 block/ngày\
-   Không tập nặng trước milestone

------------------------------------------------------------------------

# VIII. DEFINITION OF DONE (Quarter Level — Coarse)

> 3–5 bullet đầu ra tối thiểu cho mỗi objective. Dùng để thống nhất tiêu chuẩn trước khi lập plan tháng/tuần. Chi tiết hóa tại Section X.

## ✅ Signee Demo Done
- [ ] Tất cả demo flows chạy end-to-end không lỗi trên môi trường staging
- [ ] Stakeholder xem demo và xác nhận bằng văn bản / email
- [ ] Không có P0/P1 bug open tại thời điểm demo
- [ ] Demo script + môi trường được document đủ để reproduce

## ✅ RobotOS Prototype Done
- [ ] Boot thành công trên target board
- [ ] Tất cả MUST interface nhận lệnh và phản hồi đúng
- [ ] Chạy ổn định ≥ N phút liên tục (N xác định trong Spike)
- [ ] Happy-path test script tự động pass trên board thật

## ✅ Zephyr Stable Release Done
- [ ] CI xanh 100% trên nhánh release
- [ ] Không có P0/P1 open bug
- [ ] Pass smoke test trên target hardware
- [ ] Release notes + version tag (semver) tồn tại

------------------------------------------------------------------------

# IX. FAILURE MODE

Thất bại sẽ do:

-   Push capacity quá sớm\
-   Scope RobotOS không freeze\
-   Không delegate thật sự\
-   Bỏ qua tín hiệu mệt mỏi

------------------------------------------------------------------------

# X. Định nghĩa đầu ra cho Quarter Plan (bắt buộc trước khi lập timeline tuần/ngày)

> Mục đích: 4 mục dưới đây là **điều kiện tiên quyết** để lập Quarter Plan có thể chia milestone tuần/ngày và gắn owner. Nếu chưa điền → tạo Spike ngay, timebox 60'.

------------------------------------------------------------------------

## 10.1 Signee — Demo Scope List `LOCKED`

### 🎯 Demo Objective

- Hoàn thành Signee Series A Demo trước **30/05**
- Feature Freeze: **30/04**

------------------------------------------------------------------------

### 🎬 Demo Scope (Governance Level)

**Main Demo Flow**

- Reference: `SIG-DEMO-MAIN-FLOW vX.X`
- Stored in: Signee project repository (product documentation)
- Owner: Product Lead
- Sau 30/04 không được thay đổi flow.
- Nếu thay đổi sau 30/04 → phải trigger Quarter Review.

**Supporting Flows (Optional)**

Chỉ được demo nếu ổn định trước **20/05**:
- Gallery ↔ Mirror sync
- Basic reconnect / AI retry

Nếu không ổn định → loại khỏi demo, không sửa trong tháng 5.

------------------------------------------------------------------------

### 🔒 Feature Freeze Rule (30/04)

Sau ngày 30/04, **không được:**
- Thêm feature mới
- Refactor lớn
- Mở rộng kiến trúc

Task phát sinh → delegate.

------------------------------------------------------------------------

### 🧪 Tháng 5 — Testing & Stabilization Only

**Chỉ bao gồm:**
- System test
- Demo rehearsal
- P0 / P1 bug fix
- UT nhỏ còn lại

**Không bao gồm:**
- UI polish không critical
- Performance tuning nhỏ
- Edge case ngoài demo flow
- Feature phụ / RC chưa ổn định

------------------------------------------------------------------------

### 🛡 Demo Protection Protocol

Chỉ fix: **P0 · P1 · Demo-breaking bug**

Nếu feature phụ gây rủi ro:
→ Cắt khỏi demo
→ Đưa vào backlog tháng 6

------------------------------------------------------------------------

### 📅 Demo Timeline

| Ngày | Milestone |
|------|-----------|
| **20/05** | Scope hard lock |
| **25/05** | Demo-ready state |
| **26–29/05** | Rehearsal + backup environment |
| **30/05** | Official Demo |

> **Emergency override:** Nếu 25/05 chưa demo-ready → có thể tạm dừng RobotOS tối đa 48h để cứu demo.

------------------------------------------------------------------------

## 10.2 RobotOS — Prototype Definition `LOCKED`

### 🎯 Objective

- Hoàn thành **RobotOS v0.2 Prototype** chạy trên board thật
- Pass **Gate D — 31/05**

------------------------------------------------------------------------

### 📦 Prototype Boundary

**Prototype = v0.1 Bootstrap hoàn tất (cuối tháng 4) + v0.2 Expansion + CNC Demo hoàn chỉnh**

- CNC Demo là evidence app chính
- Không bao gồm full production hardening

------------------------------------------------------------------------

### ✅ MUST Capabilities

**CAP-1 — Boot & Zephyr Integration**
- Build + flash + boot trên board thật
- Zephyr integration ổn định

**CAP-2 — Runtime Foundation**
- Robot Adapter Layer (Thread / Time / Queue) hoạt động
- Không crash trong lifecycle cơ bản

**CAP-3 — Core Robot Framework**
- Stepper (MUST)
- Endstop & Sensors (MUST)
- Robot State Machine (IDLE / HOMING / RUN / FAULT)
- GCode stub đủ cho demo sequence

**CAP-4 — CNC Demo App**
- 1 demo app hoàn chỉnh
- Sequence: HOMING → RUN → STOP
- Có xử lý FAULT cơ bản

**CAP-5 — Signal/Safety**
- Limiter (MUST nếu bảo vệ hardware)
- Filters (MUST nếu ảnh hưởng stability demo)

------------------------------------------------------------------------

### 🔌 MUST Interfaces

| Interface | MUST / NICE |
|-----------|:-----------:|
| Build / Flash / Boot | MUST |
| Control CLI / UART | MUST |
| Sensor Input | MUST |
| Motor Output | MUST |
| Telemetry / Log | MUST |

------------------------------------------------------------------------

### 📊 SHOULD Components

- **Benchmark suite** (jitter / IPC latency / mem) → SHOULD
  - Dùng để so sánh mô hình khác
  - Không block Gate D nếu chưa hoàn chỉnh
  - Không được phép ăn block làm trễ CNC demo

------------------------------------------------------------------------

### ⏱ Stability Requirement

Chạy ổn định liên tục **≥ 10 phút**:
- Không watchdog reset
- Không memory leak rõ ràng
- Không motor runaway

------------------------------------------------------------------------

### 🧪 Verification Rule

Prototype được xem là **"Done"** khi:
- [ ] Boot OK trên board thật
- [ ] CNC Demo chạy end-to-end
- [ ] 10 phút stability pass
- [ ] Happy-path test script verify: boot · homing · move · fault basic

------------------------------------------------------------------------

### 🔒 Scope Protection Rule (Tháng 5)

- Không thêm MUST mới
- Không mở rộng architecture
- Benchmark chỉ làm khi CNC demo đã ổn định

------------------------------------------------------------------------

## 10.3 Zephyr — Stable Release Definition

**Release cadence:** _(vd: mỗi 2 tuần / cuối sprint / theo milestone)_  
→ _(chưa chốt — cần quyết định trong W11)_

**Đầu ra cụ thể mỗi release:**

| Artifact | Bắt buộc? | Ghi chú |
|----------|-----------|---------|
| Git tag / version (semver) | MUST | _(vd: v1.2.3-rc1)_ |
| Release notes (changelog) | MUST | _(auto-gen từ commit message hay viết tay?)_ |
| Test suite pass report | MUST | _(CI output / coverage %)_ |
| Binary / image đã sign | MUST nếu ship | _(chưa rõ có cần không)_ |
| Regression test kết quả | SHOULD | _(test trên board thật hay emulator?)_ |
| Known issues list | SHOULD | _(format?)_ |

**"Stable" đo bằng gì?** _(definition of stable)_
- [ ] CI xanh 100% trên nhánh release
- [ ] Không có P0/P1 open bug
- [ ] Đã pass smoke test trên target hardware
- [ ] _(thêm nếu có SLA hoặc customer requirement)_

> **TODO:** Chưa có release cadence chính thức → Cần ADR "Zephyr Release Cadence" (5 dòng). Giao Module Owner Release draft trong 48h, chốt trong Architect block W11.

------------------------------------------------------------------------

## 10.4 Delegation Map — Tháng 4–5

> Mục tiêu: giải phóng capacity bằng cách phân loại việc chính xác — delegate được thì delegate hết, co-working khi cần quyết định. Không "ném việc", không "cùng làm cho vui".

------------------------------------------------------------------------

### PHẦN A — Delegation (Handoff Work)

**Mục tiêu:** Giao việc để chạy độc lập, giảm context switching, không phải nói lại nhiều.

#### A1) Điều kiện để được phép đưa vào Delegation

Một việc chỉ được đưa vào phần A nếu thỏa **cả 3**:

- [ ] Spec rõ (inputs/outputs, phạm vi, tiêu chuẩn)
- [ ] DoD-0 rõ (done tối thiểu có thể verify)
- [ ] Không chứa decision chiến lược (không cần tradeoff / triết lý)

#### A2) Template cho mỗi work item delegation

| Field | Nội dung |
|-------|----------|
| **Work item** | _(mô tả cụ thể, vd: "viết test harness cho RobotOS module X")_ |
| **Ai làm** | _(Agent2 / CTV / Module Owner)_ |
| **Input cần cung cấp** | _(link, file, outline, constraints)_ |
| **Output mong muốn** | _(file / path / format cụ thể)_ |
| **DoD-0** | _(checklist — đạt là pass)_ |
| **Trace bắt buộc** | _(log / commit / screenshot)_ |
| **Fail protocol** | _(thiếu gì → ghi ERRORS + hỏi đúng 2 câu)_ |

#### A3) Ví dụ loại việc thuộc Phần A

- Formatting / chuẩn hóa docs theo template
- Generate skeleton (doc / code)
- Refactor mechanical theo rule có sẵn
- Viết test theo test plan đã được chốt
- Script automation theo yêu cầu cụ thể
- Thu thập số liệu / tổng hợp changelog / release notes (theo format)

------------------------------------------------------------------------

### PHẦN B — Co-working (Joint Work / Pair Mode)

**Mục tiêu:** Cùng làm để giữ đúng triết lý, ra quyết định nhanh, giảm rủi ro "làm sai hướng".

#### B1) Điều kiện đưa vào Co-working

Một việc thuộc phần B nếu có **ít nhất 1** trong các yếu tố:

- **Decision-heavy:** cần quyết định tradeoff / architecture / boundary
- **Ambiguous input:** thông tin chưa đủ, phải hỏi / khám phá (spike)
- **High risk rewrite:** nếu làm sai → đập đi làm lại nhiều
- **Cross-project coupling:** đụng nhiều project / timeline, dễ lệch ưu tiên

#### B2) Cơ chế hoạt động Co-working

| Vai trò | Trách nhiệm |
|---------|-------------|
| **Owner (bạn)** | Chốt quyết định · scope freeze · accept/reject |
| **Agent1 (ChatGPT)** | Tạo artifact (ADR/PLAN/CHECKLIST) · triage · thiết kế rule/guardrail · viết packet |
| **Agent2 (Executor)** | Chạy các bước thực thi nhỏ theo chỉ đạo rõ · trả trace nhanh |

#### B3) Output bắt buộc sau mỗi phiên Co-working

Cuối phiên phải có **ít nhất 1** artifact kèm trace:

- **ADR** — nếu có quyết định
- **SPIKE notes** — nếu là khám phá
- **PLAN** — nếu là lập kế hoạch (steps + DoD)
- **CHECKLIST** — nếu là gate / quality check

#### B4) Ví dụ loại việc thuộc Phần B

- Scope freeze cho Signee demo flows
- Định nghĩa RobotOS prototype "MUST capabilities"
- Chốt Zephyr release cadence / criteria
- Thiết kế / tinh chỉnh Delegation Map theo tháng
- Xử lý incident làm lệch effort budget

------------------------------------------------------------------------

> **TODO (KHẨN):** Tạo task "Draft Delegation Map tháng 4–5" trong backlog, Spike 45', deadline W12.  
> Output: điền bảng template Phần A cho các work item đã biết + phân loại Phần B cho các việc còn ambiguous.

# 🎯 STRUCTURE SUMMARY

Quarter này có 2 tầng song song:

1.  Delivery Track (deadline cứng)\
2.  Capacity Track (experiment có kiểm soát)

Không cái nào được phá cái kia.


