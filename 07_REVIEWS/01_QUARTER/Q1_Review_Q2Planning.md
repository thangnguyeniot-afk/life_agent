# 🧭 QUARTER REVIEW & PLANNING (FINAL -- Delivery + Capacity)

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

1.  Hoàn thành Signee Series A Demo trước 30/4.\
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

## 📅 Phase 2 (Tháng 5)

-   RobotOS --- Dominant\
-   Zephyr --- Stable\
-   Signee --- Stabilization

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

# V. CAPACITY EXPANSION LAYER

## 🎯 Capacity Objective

Cuối quý đạt:

-   4 block ổn định/ngày\
-   5 block 2--3 ngày/tuần\
-   Không crash năng lượng

------------------------------------------------------------------------

## 🔹 Phase A --- Calibration (2--3 tuần)

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

## 🔹 Phase C --- Sprint Mode (Tháng 5)

-   1 tuần sprint RobotOS\
-   3 ngày liên tiếp 5 block\
-   Sau đó recovery 2 ngày\
-   Ngủ ≥ 6h30\
-   Không tập nặng

------------------------------------------------------------------------

# VI. ENERGY PROTECTION RULES

-   Không tăng block và tăng scope cùng lúc\
-   Nếu mệt mức 4--5 trong 3 ngày liên tiếp → giảm về 3 block/ngày\
-   Không tập nặng trước milestone

------------------------------------------------------------------------

# VII. SUCCESS CRITERIA

Quý này thành công nếu:

-   Signee demo thật sự hoạt động\
-   RobotOS prototype chạy thật\
-   Không mở project mới\
-   Capacity tăng nhưng không crash

------------------------------------------------------------------------

# VIII. FAILURE MODE

Thất bại sẽ do:

-   Push capacity quá sớm\
-   Scope RobotOS không freeze\
-   Không delegate thật sự\
-   Bỏ qua tín hiệu mệt mỏi

------------------------------------------------------------------------

# 🎯 STRUCTURE SUMMARY

Quarter này có 2 tầng song song:

1.  Delivery Track (deadline cứng)\
2.  Capacity Track (experiment có kiểm soát)

Không cái nào được phá cái kia.
