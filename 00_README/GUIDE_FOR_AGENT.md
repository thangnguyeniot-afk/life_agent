# LIFE_AGENT – Hướng dẫn vận hành “Agent lập lịch & review” (v1.0)

Tài liệu này giúp bạn **giảm ma sát công cụ** và cho phép “agent” (ChatGPT) hỗ trợ:
- Lập lịch theo block (TickTick Calendar <=> Notion)
- Review ngày/tuần/tháng/quý
- Phân tích task bước đầu (scope, owner, rủi ro, timebox) để bạn chỉ làm phần quan trọng nhất

---

## 1) Bối cảnh công cụ của bạn (đã chốt)

### Zephyr (máy công ty)
- **Không dùng được Notion** (không truy cập Notion cá nhân)
- Vẫn truy cập được **ChatGPT**
- Vẫn có thể dùng **TickTick trên điện thoại** (đã sync với Notion)
- Tool dev (GitHub/OneNote/Teams…) dùng như bình thường, **không gộp** vào hệ lập lịch cá nhân

=> Vì vậy Zephyr cần một “core tối giản” ngay trên máy công ty: **Markdown Vault** (folder LIFE_AGENT) để:
- ghi context tuần/tháng, decision log, spike/DoD
- tạo output gọn để bạn copy sang nơi cần (Teams/Jira/GitHub)

### RobotOS & Signee (máy cá nhân)
- Dùng **Notion làm trung tâm** (SSOT cho personal projects)
- TickTick (task & calendar) sync với Notion

### Calendar
- Dùng **TickTick Calendar** (đồng bộ với Notion)

### GitHub Projects / Jira
- Dùng để quản lý task của team (hệ “team”), **tách khỏi hệ cá nhân**
- Hệ cá nhân chỉ cần liên kết bằng link/ID khi cần theo dõi

---

## 2) Kiến trúc hệ thống để “work smooth”

### 2.1 Một nguyên tắc vàng: 1 SSOT cho mỗi “thế giới”
Bạn có 2 thế giới tách biệt vì ràng buộc thiết bị:

**(A) Work-world (Zephyr / máy công ty)**
- SSOT = Markdown Vault (folder `LIFE_AGENT` trên máy công ty)

**(B) Personal-world (RobotOS, Signee / máy cá nhân)**
- SSOT = Notion

TickTick đóng vai trò **Execution Layer** (chạy việc hàng ngày) cho cả hai, thông qua điện thoại.

### 2.2 “Giao diện” (interfaces) giữa các tool
- **TickTick**: task/day plan + calendar blocks
- **Notion** (personal): OS, project context, review, logs
- **Markdown Vault** (work): OS rút gọn, context Zephyr, logs Zephyr
- **ChatGPT**: agent thực hiện “lập lịch & review & phân tích task” dựa trên các file `.md` trong Vault

---

## 3) Những gì Agent sẽ làm cho bạn (và những gì KHÔNG làm)

### Agent làm (đầu vào ít – đầu ra nhiều)
1) **Weekly Planning**: Big/Small/KTLO + capacity budget + office hours + 2 deep blocks/day
2) **Daily Planning**: 2 deep blocks + builder list (max 5) + delegation list
3) **Task triage**: phân loại 4 bucket (Execution/Management/System/Ideas) + timebox Spike/Plan/Execute
4) **Decision/Spike/RFC**: tạo 1 trang “đủ chạy” (70% + pilot)
5) **Review**: daily shutdown / weekly review / monthly review (siêu nhẹ)

### Agent KHÔNG làm (để bạn không bị ảo tưởng hệ thống)
- Không thay bạn quyết định mục tiêu đời sống
- Không tự động push task lên Jira/GitHub (bạn dùng team tool theo quy trình team)
- Không tối ưu quá mức (tránh biến năng suất thành dự án)

---

## 4) Cấu trúc thư mục đề xuất (Markdown Vault)

```
LIFE_AGENT/
  00_README/
    GUIDE_FOR_AGENT.md
  01_OS/
    operating_system_thang_nguyen_v1_1.md
  02_CONTEXT/
    00_CONTEXT.md
    CONTEXT_rule.md
  03_PLANNING/
    Q1_Review_Q2Planning.md
  04_LOGS/
    Decision_Log.md
    Idea_Parking_Lot.md
    Spike_Log.md
  05_TEMPLATES/
    TEMPLATE_Daily.md
    TEMPLATE_Weekly.md
    TEMPLATE_Monthly.md
    TEMPLATE_Spike.md
    TEMPLATE_DoD_0_1_2.md
    TEMPLATE_ADR.md
  06_PROJECTS/
    Zephyr/
      Zephyr_Project_Context.md
    RobotOS/
      RobotOS_CONTEXT.md
    Signee/
      Signee_CONTEXT.md
  07_REVIEWS/
    Daily/
    Weekly/
    Monthly/
  08_SCHEDULE/
    Schedule_Rules.md
    Office_Hours.md
```

> Bạn có thể giữ đúng tên file như ảnh VSCode đang có; chỉ cần thêm thư mục/README để agent dễ “bám”.

---

## 5) Quy trình vận hành (cadence) – ít thao tác nhất

### 5.1 Mỗi ngày (10’ sáng + 10’ tối)
**Morning (10’)**
- Agent xuất `Daily Plan` (2 deep + builder max 5 + delegation)
- Bạn copy sang TickTick (hoặc chỉ dùng để chọn 3 task chính)

**Evening (10’)**
- Agent xuất `Daily Shutdown` (done/not done + unblock + next 48h)
- Bạn dán vào `07_REVIEWS/Daily/YYYY-MM-DD.md`

### 5.2 Mỗi tuần (60’)
- Agent tạo `Weekly Plan`:
  - 1 Big Bet + 2 Small Bets + KTLO (Zephyr)
  - capacity budget (%)
  - office hours
  - top 3 risks
  - owners/delegations
- Bạn chỉ cần duyệt và “chốt 70%”.

### 5.3 Mỗi tháng (45–60’, siêu nhẹ)
- 3 wins / 3 lessons / 3 bottlenecks
- cập nhật capacity (KTLO chiếm bao nhiêu)
- 1 theme tháng (ví dụ “Anti-SPOF”)

---

## 6) Luật chống ma sát (quan trọng nhất)

1) **Một Inbox duy nhất** (tùy thế giới):
   - Zephyr: `04_LOGS/Idea_Parking_Lot.md` + `Decision_Log.md`
   - Personal: Notion Inbox (nếu bạn có), hoặc vẫn dùng file `.md`

2) **Không để “Ideas” chen vào Execution**
   - ý tưởng → ghi 1 dòng → quay lại

3) **Zephyr cần Office Hours để không bị ping cả ngày**
   - 2 khung cố định/ngày, ngoài ra vào ticket/log

4) **DoD tiến hóa 3 mức** (DoD-0/1/2)
   - không cần “thiết kế xong hết” mới giao việc

---

## 7) Cách “đưa file cho agent” để agent làm việc
- Bạn chỉ cần **upload folder LIFE_AGENT** (hoặc các file chính) vào chat.
- Agent sẽ đọc:
  - `01_OS/*`
  - `02_CONTEXT/*`
  - `06_PROJECTS/<project>/*`
  - `04_LOGS/*`
  - review gần nhất trong `07_REVIEWS/*`

---

## 8) Checklist setup trong 30 phút
- [ ] Tạo folder structure (như trên) trên máy công ty và máy cá nhân (nếu muốn)
- [ ] Copy OS vào `01_OS/`
- [ ] Chuyển các file context hiện có vào đúng `06_PROJECTS/`
- [ ] Tạo `Decision_Log`, `Idea_Parking_Lot`, `Spike_Log`
- [ ] Đặt `Office Hours` (2 khung) trong TickTick calendar
- [ ] Bắt đầu từ **Weekly Plan tuần này** (agent làm, bạn duyệt)

---

## 9) “Definition of Done” cho hệ LIFE_AGENT (để biết đã chạy mượt)
Bạn đạt trạng thái “smooth” khi:
- Mỗi ngày bạn chỉ cần:
  - xem 2 deep blocks
  - làm 3–5 việc builder
  - dán 5 dòng shutdown
- Không còn tình trạng:
  - nhiều nơi đều “đúng”
  - không biết việc nào ưu tiên
  - task phức tạp kéo dài không điểm dừng
