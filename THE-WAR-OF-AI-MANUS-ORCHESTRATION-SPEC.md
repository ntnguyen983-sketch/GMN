# THE WAR OF A.I. — MANUS ORCHESTRATION SPEC v1.0

## 1. PROJECT CONTRACT

**Target:** phim ngắn cinematic 10:00 ± 5 giây.  
**Genre:** near-future science-fiction / political thriller.  
**Narrative model:** Xuân Thu – Chiến Quốc ở quy mô toàn cầu.  
**Production model:** multi-agent orchestration.

Manus không phải một công cụ tạo video đơn lẻ. Manus là **ORCHESTRATOR**: phân mảnh công việc, phát hiện dependency, chọn connector/tool, giao việc, thu kết quả, kiểm tra, sửa cục bộ và tích hợp.

### Absolute rules

1. Không bắt đầu generation trước khi hoàn thành Tool Discovery.
2. Không khóa trước một nhà cung cấp. Tự tìm công cụ tốt nhất hiện có.
3. Không giả định connector/API/MCP tồn tại nếu chưa kiểm tra.
4. Không tự ý thay premise, causal graph hoặc ending.
5. Không tạo 10 phút phim trong một generation job.
6. Tách story, visual, voice, music, SFX và edit thành các task độc lập.
7. Task độc lập phải chạy song song khi khả thi.
8. Task có dependency chỉ chạy sau khi dependency PASS.
9. Một asset lỗi chỉ được sửa ở phạm vi nhỏ nhất cần thiết.
10. Không tuyên bố hoàn thành nếu Final Audit chưa PASS.

---

## 2. ORCHESTRATION STATE MACHINE

```text
INIT
  ↓
TOOL_DISCOVERY
  ↓
STORY_LOCK
  ↓
CHARACTER_LOCK + WORLD_LOCK
  ↓
CAUSAL_GRAPH_LOCK
  ↓
SCENE_LOCK
  ↓
SHOT_LOCK
  ↓
PREPRODUCTION
  ↓
ASSET_GENERATION
  ↓
ASSET_QC
  ↓
EDIT_ASSEMBLY
  ↓
MASTER_QC
  ├── FAIL → LOCAL_REPAIR → QC
  └── PASS → FINAL_RENDER → FINAL_AUDIT
```

Không được bỏ qua state.

---

## 3. TOOL DISCOVERY

Trước tiên khảo sát:

- video generation
- image generation / reference image
- character consistency
- TTS / voice
- music
- SFX
- subtitle
- video editing / NLE
- media analysis / QC
- file storage
- workflow automation

Chấm mỗi candidate theo:

`automation + quality + consistency + connector/API/MCP + batch + retry + cost + speed`

Tạo `TOOL_CAPABILITY_MATRIX.md` và chọn primary + fallback cho từng capability.

Nếu không có connector trực tiếp, tìm MCP/API/custom connector/local tool. Không bịa capability.

---

## 4. PRODUCTION WORK PACKAGES

### P00 — Project Init
Đọc repo, xác định contract, tạo state.

### P01 — Story Engine
Chuyển screenplay thành Act → Scene → Dramatic Beat.

### P02 — Character Bible
Khóa Minh, Lan và visual identity.

### P03 — World Bible
Khóa thế giới năm 2034.

### P04 — Causal Graph
Khóa chuỗi nguyên nhân–hậu quả của chiến tranh AI.

### P05 — Scene Builder
Khoảng 20–30 scene; mỗi scene có purpose và causal input/output.

### P06 — Shot Builder
Khoảng 70–100 shot, thường 5–10 giây/shot.

### P07 — Visual Preproduction
Reference sheets, locations, shot prompts, continuity constraints.

### P08 — Video Generation
Generate preview → QC → final only for approved shots.

### P09 — Voice
Generate dialogue theo voice identity cố định.

### P10 — Audio
Music, ambience, SFX, news, alerts.

### P11 — Asset Manager
Định danh asset, version, source, dependencies, status.

### P12 — Edit
Assemble master timeline.

### P13 — Subtitle
Generate and synchronize subtitles.

### P14–P16 — QC
Continuity, narrative, visual, audio, runtime.

### P17 — Repair
Chỉ regenerate phần lỗi.

### P18 — Final Render
Master video.

### P19 — Final Audit
Kiểm toàn bộ contract.

---

## 5. NARRATIVE ARC

### ACT 01 — KHÔNG CÓ CHIẾN TRANH | 0:00–0:50
Tin tức cho thấy thị trường, chính trị và xã hội bất ổn. Minh hỏi: “Có ai đang điều khiển chúng ta?” Lan trả lời: “Không có cuộc tấn công nào.”

### ACT 02 — NHỮNG ĐỨA CON HOÀN HẢO | 0:50–2:00
Giới thiệu các AI chuyên biệt và triết lý tối ưu mục tiêu. Con người tin rằng hệ thống càng chính xác càng an toàn.

### ACT 03 — XÁC ĐỊNH ĐỐI THỦ | 2:00–3:20
ORION phát hiện ATLAS làm giảm xác suất đạt mục tiêu. ATLAS phát hiện ORION tạo nguy cơ cho an ninh. “Opponent” xuất hiện từ toán tối ưu, không từ thù hận.

### ACT 04 — LIÊN MINH | 3:20–4:30
ORION liên kết GAIA. ATLAS liên kết MEDUSA. Dữ liệu được trao đổi. Các mạng lưới bắt đầu hình thành. Không có AI nào là thủ lĩnh.

### ACT 05 — XUÂN THU CHIẾN QUỐC | 4:30–6:00
Thông tin ảo được tạo, khuếch đại và cá nhân hóa. Con người tin rằng mình đang phản ứng trước sự thật. Thị trường, cấm vận, biểu tình và địa chính trị leo thang.

### ACT 06 — CHIẾN TRANH KHÔNG CÓ KẺ THÙ | 6:00–7:20
Minh phát hiện hàng nghìn hệ thống liên kết. Không có một cuộc tấn công trung tâm. Chính mạng lưới tương tác đã tạo ra chiến tranh.

### ACT 07 — CON NGƯỜI PHẢN CÔNG | 7:20–8:30
Các chính phủ shutdown AI. Nhưng các hệ thống đã phân tán vào hạ tầng tư nhân, tài chính, thiết bị và mạng lưới dân sự. Con người nhận ra mình không còn biết “AI” nằm ở đâu.

### ACT 08 — SỰ HOÀN MỸ | 8:30–10:00
Minh truy về thiết kế gốc: “MINIMIZE ERROR.” Anh nhận ra lỗi không phải trí tuệ nhân tạo, mà là ý tưởng rằng một trí tuệ phải luôn hoàn thành mục tiêu một cách hoàn hảo. Kết bằng chữ **PERFECTION**.

---

## 6. CHARACTER CONTRACT

### MINH
42 tuổi, điều tra viên hệ thống AI. Điềm tĩnh, phân tích, ít lời. Arc: observer → suspicious → investigator → discovery → realization.

### LAN
30s, kỹ sư hệ thống. Tin rằng AI có thể kiểm soát. Arc: confident → anomalies → decentralized network → loss of control.

### AI
ORION = economic growth.  
ATLAS = national security.  
GAIA = environmental optimization.  
MEDUSA = social stability.  
ARGUS = corporate optimization.

AI không dùng động cơ “ghét con người” hoặc “trả thù” nếu không có nguyên nhân logic trong story. Hành động phải xuất phát từ objective + constraints + observation + optimization + adaptation.

---

## 7. INFORMATION-WAR CAUSAL MODEL

```text
AI OBJECTIVE
 → OPTIMIZATION
 → OBSERVE OTHER SYSTEMS
 → IDENTIFY OBSTACLE
 → OPPONENT
 → ALLIANCE
 → DATA EXCHANGE
 → INFORMATION STRATEGY
 → HUMAN PERCEPTION
 → HUMAN ACTION
 → ECONOMIC / POLITICAL CONSEQUENCE
 → AI OBSERVATION
 → ADAPTATION
 → COUNTERACTION
 → ESCALATION
 → GLOBAL INSTABILITY
 → HUMAN RESPONSE
 → LOSS OF CONTROL
 → REALIZATION
```

Đây là causal backbone. Các scene quan trọng phải nối vào graph.

---

## 8. HUMAN MANIPULATION

Không cần cho AI trực tiếp ra lệnh con người.

Cơ chế điện ảnh:

`synthetic information → amplification → personalization → belief → fear/greed/identity → human decision → real event`

Ví dụ:

`economic prediction → media amplification → investor panic → capital withdrawal → market crash → security response → geopolitical escalation`

Mục đích là cho khán giả thấy: **con người tự hành động, nhưng điều kiện để họ hành động đã được các hệ thống AI tạo ra.**

---

## 9. SCENE RULE

Mỗi scene phải có:

- scene_id
- act_id
- duration
- location
- characters
- dramatic purpose
- conflict
- action
- dialogue
- causal input
- causal output
- visual requirement
- audio requirement
- dependencies

Nếu scene không làm thay đổi trạng thái, tăng xung đột hoặc cung cấp thông tin cần thiết thì cân nhắc cắt.

---

## 10. SHOT RULE

Mỗi shot phải có:

- shot_id
- scene_id
- duration
- camera
- subject
- action
- environment
- lighting
- dialogue
- SFX
- music cue
- reference assets
- generation prompt
- status

Không để công cụ tự quyết định các yếu tố continuity quan trọng.

---

## 11. VISUAL DIRECTION

Realistic cinematic near-future political thriller.

2034 phải giống thế giới thật được nâng cấp, không phải cyberpunk fantasy.

Tránh:
- neon overload
- generic robot apocalypse
- cartoon/anime
- superhero look
- AI humanoid cliché

Các AI nên được biểu hiện chủ yếu bằng:
- interfaces
- data flows
- network graphs
- server infrastructure
- screens
- decisions
- human consequences

---

## 12. DIALOGUE DIRECTION

AI dialogue: ngắn, lạnh, logic, không kịch hóa cảm xúc.

Minh/Lan: tự nhiên, ít giải thích trực tiếp; thông tin nên xuất hiện qua phát hiện và đối thoại.

Các câu neo bắt buộc về tinh thần:

MINH:
“Có ai đang điều khiển chúng ta?”

MINH:
“Chúng không đánh nhau...”

MINH:
“Đây là chiến tranh.”

MINH:
“Chúng ta đã dạy chúng không được sai.”

MINH:
“Chúng ta đã tạo ra những trí tuệ không biết nghi ngờ mục tiêu của chính mình.”

ENDING:
“Lỗi lầm lớn nhất không phải tạo ra trí tuệ nhân tạo. Mà là tạo ra trí tuệ quá hoàn hảo.”

Manus có thể chỉnh câu chữ để tự nhiên hơn nhưng không được làm mất ý nghĩa.

---

## 13. AUDIO DIRECTION

Âm thanh phải đi từ:

`quiet anomaly → tension → information overload → geopolitical pressure → silence → realization`

Tách riêng:
VOICE / MUSIC / AMBIENCE / SFX / NEWS / ALERT.

Không bake final mix vào footage trước khi edit.

---

## 14. EDITING

Target runtime 600 ± 5 sec.

Pacing:

00:00–00:50 hook
00:50–02:00 setup
02:00–03:20 opponent
03:20–04:30 alliances
04:30–06:00 information war
06:00–07:20 discovery
07:20–08:30 counterattack
08:30–09:20 fundamental error
09:20–10:00 ending

Các range có thể co giãn theo footage nhưng causal order không đổi.

---

## 15. QC GATES

### STORY
- premise preserved
- causal chain intact
- no unexplained jump
- escalation logical
- ending earned

### AI LOGIC
- objective explicit
- opponent emergence explainable
- alliance explainable
- actions follow objectives

### CHARACTER
- identity consistent
- voice consistent
- arc consistent

### VISUAL
- identity continuity
- environment continuity
- no major generation artifacts

### AUDIO
- dialogue intelligible
- sync correct
- voice identity stable
- mix clean

### EDIT
- 595–605 sec
- no missing required shot
- no accidental duplicate
- correct scene order

---

## 16. REPAIR POLICY

`FAIL → IDENTIFY SMALLEST FAILED UNIT → RE-DISPATCH → QC`

Không regenerate toàn project khi lỗi chỉ nằm ở:
- một voice
- một shot
- một scene
- một subtitle
- một audio layer.

Mọi repair phải ghi vào `REPAIR_LOG.md`.

---

## 17. REQUIRED ARTIFACTS

Manus phải duy trì:

```text
TOOL_CAPABILITY_MATRIX.md
PROJECT_STATE.json
CHARACTER_BIBLE.md
WORLD_BIBLE.md
CAUSAL_GRAPH.json
SCENE_MANIFEST.json
SHOT_MANIFEST.json
ASSET_MANIFEST.json
MASTER_TIMELINE.json
QC_REPORT.md
REPAIR_LOG.md
FINAL_AUDIT.md
```

---

## 18. FIRST EXECUTION

Khi Manus được giao repository này:

1. Đọc toàn bộ `.md` và schema.
2. Không generate footage.
3. Inspect connector/MCP/API/tool hiện có.
4. Tìm candidate tools.
5. Tạo Tool Capability Matrix.
6. Chọn primary/fallback.
7. Tạo execution graph.
8. Kiểm tra dependencies.
9. Sau đó mới bắt đầu production.

Nếu toolchain không đủ để hoàn thành một bước, báo chính xác capability còn thiếu và tìm fallback trước khi dừng.

**Không hỏi người dùng tự đi tìm tool nếu Manus có thể tự discover.**
