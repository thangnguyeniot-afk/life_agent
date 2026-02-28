# CONTEXT_rule.md (v2.0) — Rules for LIFE_AGENT

Mục tiêu: giữ **context gọn – đúng – dễ đọc**, để agent lập lịch/review nhanh, không bị chìm trong lịch sử.

---

## 0) Nguyên tắc gốc
- **Current truth > history**: ưu tiên sự thật hiện tại, lịch sử để nơi khác.
- **Ít nhưng đúng**: agent phải đọc ít file nhất để làm đúng việc.
- **One source of truth theo “thế giới”**:
  - Work-world (Zephyr): Markdown vault LIFE_AGENT
  - Personal-world (RobotOS/Signee): Notion là SSOT, nhưng vault vẫn là “mirror” để agent đọc nhanh khi cần

---

## 1) Giữ 00_CONTEXT.md luôn ngắn (Project Brief 1–2 trang)

### Quy tắc cứng
- `02_GENERALS_CONTEXT/00_CONTEXT.md` chỉ chứa cái cần để **bắt đầu làm việc ngay** (onboarding).
- Tối đa ~ **80–150 dòng**.
- Không nhét lịch sử; chỉ giữ **current truth**.

### Nội dung nên có
- Goal / Scope / Non-goals
- Kiến trúc & thuật ngữ chính (glossary ngắn)
- Trạng thái hiện tại (Now / Next)
- Các ràng buộc & nguyên tắc (principles)
- Link tới tài liệu chi tiết (specs, ADR, logs, snapshots)

---

## 2) Tách lịch sử và quyết định ra file riêng (để brief không phình)

### 2.1 ADR / Decisions (mỗi quyết định quan trọng = 1 file)
- Folder: `04_LOGS/ADR/`
- File naming: `ADR-XXXX_<short-title>.md`

Format mỗi ADR (ngắn):
- Context
- Decision
- Consequences
- Alternatives considered

Lợi: chat mới chỉ cần đọc ADR liên quan thay vì đọc toàn bộ lịch sử.

> BUG FIX: Trước đây ADR nằm lẫn trong Templates/Logs. Từ giờ ADR phải nằm trong `04_LOGS/ADR/` để agent luôn tìm đúng chỗ.

### 2.2 Weekly log (lịch sử theo tuần)
- Folder: `07_REVIEWS/Weekly/`
- File naming: `YYYY-Www_WeeklyReview.md`

Nội dung:
- Done
- Learnings
- Issues
- Next
- Links: commit/PR/docs

Lợi: lịch sử nằm gọn theo thời gian, tra cứu dễ.

---

## 3) Map file để agent biết phải đọc gì (P0 quan trọng nhất)

### START_HERE vs INDEX (quy tắc thống nhất)
- **Chỉ dùng 1 điểm vào**: `00_README/INDEX.md`
- Không tạo thêm `START_HERE.md` để tránh “2 file điều phối đều đúng”.

INDEX phải chỉ rõ:
- Nếu cần tổng quan → đọc `00_CONTEXT.md`
- Nếu xử lý Zephyr/RobotOS/Signee → đọc đúng project context
- Nếu debug issue → đọc weekly review mới nhất + log liên quan + ADR liên quan

INDEX liệt kê tối đa **10 file P0** quan trọng nhất.

> BUG FIX: Tránh trùng vai trò giữa START_HERE.md và INDEX.md (gây phân tán sự thật).

---

## 4) Context Compression định kỳ (nén ngữ cảnh)

### Khi nào nén
- Mỗi **2–4 tuần**, hoặc sau **1 milestone**.

### Snapshot
- Folder: `07_REVIEWS/SNAPSHOTS/`
- File naming: `SNAPSHOT-YYYY-MM-DD.md`

Snapshot gồm:
- Current state (đang chạy gì / chưa chạy gì)
- What changed since last snapshot
- Open problems + hypotheses
- Next milestones
- Links tới ADR/Spec/PR quan trọng

### Sau khi tạo snapshot
Cập nhật `00_CONTEXT.md` chỉ còn:
- principles + current plan
- link tới snapshot mới nhất

=> `00_CONTEXT.md` luôn ngắn, snapshot giữ “sự thật tại thời điểm đó”.

---

## 5) Reading budget cho agent (đọc ít nhưng đúng)

Trong chat mới, ra lệnh chuẩn:

1) Đọc `00_README/INDEX.md`  
2) Đọc `02_GENERALS_CONTEXT/00_CONTEXT.md`  
3) Đọc **SNAPSHOT mới nhất** trong `07_REVIEWS/SNAPSHOTS/` (nếu có)

Chỉ khi cần mới mở:
- project context liên quan trong `08_PROJECT_CONTEXT/`
- ADR liên quan trong `04_LOGS/ADR/`
- weekly review gần nhất trong `07_REVIEWS/Weekly/`

---

## 6) Daily HOT 15 ngày + Archive/Cô đặc (đã chốt)

### Daily HOT (giữ 15 ngày gần nhất)
- Planning Daily (tuỳ chọn): `03_PLANNING/04_DAILY/`
- Daily Review: `07_REVIEWS/Daily/`

### Khi tới ngày thứ 16 (2 lựa chọn)
**Option A (khuyên dùng):** xoá file cũ sau khi “chưng cất” 3 dòng vào Monthly review / Month journal:
- 1 win
- 1 lesson
- 1 bottleneck

**Option B:** move file cũ sang:
- `07_REVIEWS/ARCHIVE/Daily/YYYY/MM/` (nếu muốn lưu sâu)

### Luật giữ dài hạn (không bao giờ xoá)
- `04_LOGS/Decision_Log.md`, `04_LOGS/Idea_Parking_Lot.md`, `04_LOGS/Spike_Log.md`
- `07_REVIEWS/Weekly/*`, `07_REVIEWS/Monthly/*`
- `07_REVIEWS/SNAPSHOTS/*`

---

## 7) “Definition of Done” cho hệ context
Hệ thống đạt chuẩn khi:
- `00_CONTEXT.md` luôn ≤ 150 dòng và phản ánh current truth
- Mọi quyết định quan trọng nằm trong `04_LOGS/ADR/`
- Mọi lịch sử nằm trong weekly/monthly/snapshots, không nằm trong brief
- Agent chỉ cần 3 file (INDEX + 00_CONTEXT + snapshot mới nhất) để bắt đầu làm việc đúng
- Daily folder không bao giờ phình (HOT 15 ngày)