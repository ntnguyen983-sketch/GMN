# BÀN GIAO CHI TIẾT CÔNG VIỆC

## THE WAR OF A.I. — Production Handover v1.0

**Repository:** `ntnguyen983-sketch/GMN`  
**Branch:** `main`  
**Ngày bàn giao:** 2026-09-07  
**Phạm vi:** Tiếp nhận và tiếp tục pipeline sản xuất phim ngắn cinematic **THE WAR OF A.I.** theo specification đã khóa.

---

## 1. Mục tiêu và hợp đồng sản xuất

Dự án phải tạo một phim ngắn cinematic dài **600 giây, dung sai ±5 giây**, thuộc thể loại near-future science-fiction / political thriller, với mô hình sản xuất đa tác vụ và orchestration theo state machine trong `THE-WAR-OF-AI-MANUS-ORCHESTRATION-SPEC.md`.

Các nguyên tắc tuyệt đối cần giữ nguyên:

1. Không thay đổi premise, causal graph, narrative order hoặc ending.
2. Không bỏ qua state trong execution graph.
3. Không bắt đầu một generation job trước khi đã kiểm tra capability và dependency.
4. Không tạo toàn bộ phim trong một generation job; phải tách scene/shot và các lớp voice, music, ambience, SFX, news, subtitle.
5. Task độc lập chạy song song khi có thể; task có dependency chỉ chạy sau khi dependency PASS.
6. Khi lỗi chỉ nằm ở một unit, chỉ repair unit nhỏ nhất cần thiết.
7. Không ghi nhận hoàn thành nếu `FINAL_AUDIT.md` chưa PASS.

---

## 2. Tài liệu và artifact đã khóa

Các tài liệu sau là nguồn sự thật của dự án và không được tự ý sửa nội dung khóa:

| Artifact | Vai trò | Trạng thái |
|---|---|---|
| `THE-WAR-OF-AI-SCREENPLAY-v1.0.md` | Kịch bản và narrative contract | Đã khóa |
| `THE-WAR-OF-AI-DATA-SCHEMAS.md` | Schema dữ liệu | Đã khóa |
| `THE-WAR-OF-AI-MANUS-ORCHESTRATION-SPEC.md` | Quy trình orchestration, QC gates, state machine | Đã khóa |
| `CHARACTER_BIBLE.md` | Minh, Lan và năm AI | Đã khóa |
| `WORLD_BIBLE.md` | Thế giới 2034 và visual direction | Đã khóa |
| `CAUSAL_GRAPH.json` | Chuỗi nguyên nhân–hậu quả | Đã khóa |
| `SCENE_MANIFEST.json` | 19 scene, tổng runtime 600 giây | Đã tạo và cần bảo toàn |
| `SHOT_MANIFEST.json` | 76 shot, dependency và prompt fields | Đã tạo và cần bảo toàn |
| `ASSET_MANIFEST.json` | Danh mục reference/production assets | Đã tạo |
| `MASTER_TIMELINE.json` | Timeline 600 giây | Đã tạo |
| `TOOL_CAPABILITY_MATRIX.md` | Capability discovery và primary/fallback | Đã tạo |
| `EXECUTION_GRAPH.md` | Execution graph của dự án | Đã tạo |
| `QC_REPORT.md` | Báo cáo QC hiện tại | Đã tạo, chưa phải final PASS |
| `REPAIR_LOG.md` | Nhật ký repair | Đã tạo |
| `FINAL_AUDIT.md` | Audit contract cuối | Đã tạo, không được coi là PASS nếu chưa có master video |

Reference assets đã tồn tại ngoài repository tại:

- `/home/ubuntu/webdev-static-assets/the-war-of-ai/visual-target.png`
- `/home/ubuntu/webdev-static-assets/the-war-of-ai/character-sheet.png`
- `/home/ubuntu/webdev-static-assets/the-war-of-ai/world-sheet.png`

Asset dùng cho shot thử nghiệm đầu tiên là `visual-target.png`, không thay thế bằng hình ảnh khác nếu chưa có quyết định continuity được ghi nhận.

---

## 3. Trạng thái tại thời điểm bàn giao

`PROJECT_STATE.json` hiện ghi:

- `state`: `ASSET_GENERATION_BLOCKED`
- `next_state`: `ASSET_GENERATION`
- `premise_locked`: `true`
- `causal_graph_locked`: `true`
- `ending_locked`: `true`
- `generation_started`: `true`
- `video_generation_available`: `false`
- `reference_art_generated`: `true`

Blocker chính được ghi nhận là provider video generation ban đầu bị từ chối trên capability/plan hiện tại trước khi tạo MP4. Sau đó đã tìm và cấu hình route miễn phí bằng Google Colab với notebook Wan2.1 I2V Q4 GGUF và runtime T4. Environment setup đã từng hoàn tất, gồm PyTorch/CUDA, ComfyUI và model/checkpoint phụ trợ.

Trong lần chạy tiếp theo, một thao tác UI nhập prompt bằng tọa độ đã vô tình làm biến dạng nội dung cell và tạo `SyntaxError`. Notebook đã được reload từ URL GitHub nguyên bản để khôi phục code. Việc reload làm mất runtime/session T4 và form trở về mặc định. Đây là lỗi thao tác môi trường, không phải thay đổi screenplay hay production artifact.

**Không được tuyên bố đã tạo SC-01/SH-001 MP4.** Tại thời điểm bàn giao, chưa có video generation output hợp lệ và chưa được phép chuyển state sang `ASSET_QC`.

---

## 4. Toolchain và execution route tiếp theo

### 4.1 Route ưu tiên

Sử dụng **Google Colab free T4 + Wan2.1 I2V 14B Q4 GGUF** qua notebook:

`https://colab.research.google.com/github/Isi-dev/Google-Colab_Notebooks/blob/main/Wan2_1_14B_I2V_GGUF_Free.ipynb`

Route này là open-source/free GPU route, không yêu cầu thêm paid provider, không yêu cầu API key mới và phù hợp với yêu cầu image-to-video từ reference asset.

### 4.2 Thông số generation cho SC-01/SH-001

| Trường | Giá trị cần dùng |
|---|---|
| Reference image | `visual-target.png` |
| Model | Wan2.1 I2V 14B, Q4 GGUF |
| GPU | Colab T4 free runtime |
| Width | 832 |
| Height | 480 |
| Frames | 33 |
| FPS | 16 |
| Steps | 20 |
| Seed | 0 hoặc seed deterministic đã ghi vào manifest |
| Output | MP4 |
| Shot duration | Theo `SHOT_MANIFEST.json`; không tự ý kéo dài bằng prompt |
| Prompt | Lấy từ locked shot manifest, chỉ chuẩn hóa cú pháp notebook nếu cần |

Prompt phải thể hiện thế giới 2034 chân thực, cinematic, political thriller; Minh trong AI operations center; data/network/screen consequences; camera push-in có kiểm soát; ánh sáng xanh xám thực dụng; không humanoid robot, không cyberpunk neon overload, không cartoon/anime, không superhero và không villain cliché.

### 4.3 Các bước thực thi bắt buộc

1. Mở notebook Colab từ URL nêu trên.
2. Đăng nhập Google nếu Colab yêu cầu.
3. Chọn và kết nối runtime **T4 GPU**.
4. Chạy cell `Prepare Environment`; chờ dòng `Environment Setup Complete!`.
5. Không sửa code cell. Chỉ thay đổi các widget/input field của cell `Generate Video`.
6. Upload đúng file `/home/ubuntu/webdev-static-assets/the-war-of-ai/visual-target.png`.
7. Nhập các thông số generation trong bảng ở mục 4.2.
8. Dùng prompt đã khóa cho `SC-01/SH-001`; không viết lại premise hoặc causal logic.
9. Chạy generation một lần; không bấm Run All vì có thể cài lại environment hoặc tạo execution ngoài ý muốn.
10. Chờ job kết thúc; không reset runtime trong khi model đang inference.
11. Tải MP4 về sandbox và đặt tên `SC-01_SH-001_preview_v001.mp4`.
12. Chạy `ffprobe` để xác nhận codec, kích thước, FPS, frame count và duration.
13. Nếu MP4 hợp lệ, tạo checksum và cập nhật asset record; nếu lỗi, ghi vào `REPAIR_LOG.md` và chỉ chạy lại shot đó.
14. Chỉ sau khi preview PASS mới chuyển sang `ASSET_QC`; không sửa `SCENE_MANIFEST.json`, `SHOT_MANIFEST.json`, `CAUSAL_GRAPH.json` hoặc screenplay.

### 4.4 QC tối thiểu cho MP4

Cần xác nhận tối thiểu:

- File tồn tại và đọc được.
- Container là MP4.
- Có video stream, codec hợp lệ và không có frame decode error.
- Kích thước gần hoặc đúng `832x480` theo giới hạn notebook.
- FPS là 16 hoặc giá trị thực tế được ghi rõ nếu notebook tự điều chỉnh.
- Frame count và duration phù hợp với 33 frames / 16 FPS, sai số do container phải được ghi nhận.
- Hình ảnh giữ được identity của reference, Minh không bị biến dạng nghiêm trọng, không xuất hiện robot/hình ảnh fantasy ngoài specification.
- Camera motion liên tục, không có flicker, freeze, text overlay, watermark hoặc artifact lớn.

Lệnh kiểm tra gợi ý:

```bash
ffprobe -v error -show_entries format=duration:stream=index,codec_name,codec_type,width,height,avg_frame_rate,nb_frames -of json SC-01_SH-001_preview_v001.mp4
sha256sum SC-01_SH-001_preview_v001.mp4
```

---

## 5. Execution graph sau bàn giao

```text
RUNTIME_RECONNECT
  ↓
TOOLCHAIN_VERIFY
  ↓
REFERENCE_UPLOAD
  ↓
SC-01/SH-001_GENERATION
  ↓
SHOT_QC
  ├── FAIL → REPAIR_LOG → regenerate SH-001 only → SHOT_QC
  └── PASS → ASSET_MANIFEST update
                 ↓
          remaining shot generation
                 ↓
          voice / music / ambience / SFX / news / subtitle
                 ↓
          EDIT_ASSEMBLY
                 ↓
          MASTER_QC
          ├── FAIL → smallest-unit repair → QC
          └── PASS → FINAL_RENDER
                         ↓
                    FINAL_AUDIT
```

Các shot độc lập có thể chạy song song chỉ khi asset reference, prompt, model capability và retry policy đã được xác nhận. Không chạy hàng loạt trước khi SC-01/SH-001 tạo được một baseline PASS.

---

## 6. Những việc không được làm

Không sửa kịch bản để phù hợp model. Không đổi ending `PERFECTION`. Không biến AI thành nhân vật robot có cảm xúc thù ghét. Không đưa thêm nhân vật, phe phái hoặc động cơ ngoài character/world/causal bible. Không dùng paid video provider nếu chưa có yêu cầu mới. Không đánh dấu `video_generation_available: true` chỉ vì notebook setup thành công; chỉ đánh dấu sau khi có MP4 decode được. Không xóa blocker cũ nếu chưa có bằng chứng thay thế. Không commit file video lớn vào repository nếu specification không yêu cầu; lưu asset ở storage/asset location và ghi URI/checksum trong manifest.

---

## 7. Quy trình bàn giao mẫu cho các pha làm việc khác

Mẫu này áp dụng cho mọi phase từ Story, Visual, Voice, Audio, Edit đến QC/Repair.

### 7.1 Header bàn giao

- **Phase:** `[Pxx — tên phase]`
- **Owner:** `[agent/tool/person]`
- **Ngày và phiên bản:** `[timestamp / version]`
- **Input contract:** `[file và version]`
- **Output contract:** `[file, schema, media format]`
- **Current state:** `[state machine state]`
- **Gate:** `[PASS / FAIL / BLOCKED]`
- **Next owner:** `[agent/tool/person]`

### 7.2 Nội dung bàn giao bắt buộc

1. **Mục tiêu phase:** Mô tả kết quả cần đạt, không mô tả một ý tưởng mới ngoài contract.
2. **Nguồn sự thật:** Liệt kê screenplay, bible, causal graph, manifest hoặc artifact mà phase phải tuân theo.
3. **Dependency:** Ghi rõ dependency đã PASS và dependency còn thiếu.
4. **Toolchain:** Ghi provider, connector, MCP, API hoặc local CLI thực tế đã kiểm tra; không suy đoán capability.
5. **Thông số thực thi:** Ghi model, resolution, duration, seed, voice identity, loudness, codec hoặc tham số tương ứng.
6. **Output inventory:** Liệt kê từng file, path/URI, checksum, version và trạng thái.
7. **QC evidence:** Ghi lệnh kiểm tra, kết quả, lỗi quan sát được và tiêu chí PASS/FAIL.
8. **Known issues:** Ghi blocker, artifact, thiếu dependency hoặc giới hạn provider.
9. **Next actions:** Viết theo thứ tự thao tác cụ thể; task nào được chạy song song và task nào phải chờ.
10. **Change boundary:** Nêu rõ file nào được phép sửa và file nào bị khóa.
11. **Rollback/repair:** Nếu FAIL, xác định smallest failed unit và cách quay lại phiên bản PASS gần nhất.
12. **Acceptance condition:** Nêu điều kiện để phase được đóng và chuyển state.

### 7.3 Mẫu điền nhanh

```markdown
# HANDOVER — [PHASE_ID] [PHASE_NAME]

- Owner:
- Timestamp:
- Input state:
- Output state:
- Gate: PASS / FAIL / BLOCKED
- Next owner:

## Objective
[Mục tiêu chính của phase]

## Locked inputs
- [artifact + version]

## Dependencies
- PASS: [dependency]
- Pending: [dependency]

## Toolchain
- Primary: [tool/provider + observed capability]
- Fallback: [tool/provider/local route]
- Limitations: [known limitation]

## Execution steps
1. [step]
2. [step]
3. [step]

## Output inventory
| ID | File/URI | Version | Checksum | Status |
|---|---|---|---|---|
| [id] | [path] | [v] | [sha256] | PASS/FAIL |

## QC evidence
- Command/test:
- Result:
- Acceptance criteria:

## Known issues and repair boundary
- Issue:
- Smallest repair unit:
- Do not modify:

## Next actions
1. [next action]

## Handover acceptance
[Người nhận chỉ xác nhận khi đủ output, evidence và gate]
```

### 7.4 Ví dụ theo từng nhóm phase

| Nhóm phase | Bàn giao phải có | Điều kiện chuyển tiếp |
|---|---|---|
| Story / Scene / Shot | manifest, causal links, runtime totals, locked dialogue | schema valid, causal order intact |
| Visual / Asset | reference, prompt, asset ID, continuity notes, checksum | visual QC PASS |
| Video | MP4, ffprobe output, preview notes, model/seed | decode PASS và shot QC PASS |
| Voice / Audio | WAV/ stems, transcript, sample rate, loudness, sync notes | intelligibility/sync/mix PASS |
| Edit | timeline, clip mapping, transitions, subtitle track | scene order đúng, không thiếu shot |
| QC / Repair | failed unit, evidence, repair diff, rerun result | smallest-unit repair PASS |
| Final render / audit | master file, runtime, codec, audit checklist | `FINAL_AUDIT.md` PASS |

---

## 8. Điều kiện đóng công việc

Công việc chỉ được coi là hoàn thành khi tất cả required artifacts tồn tại, production state phản ánh đúng bằng chứng, master video đạt 595–605 giây, story/AI logic/character/visual/audio/edit QC đều PASS, và `FINAL_AUDIT.md` xác nhận không còn blocker. Tại thời điểm bàn giao này, dự án **chưa đạt điều kiện đóng**; nhiệm vụ tiếp theo là khôi phục runtime T4 và tạo/QC baseline SC-01/SH-001 mà không thay đổi kịch bản hoặc locked artifacts.

---

## 9. Nhật ký phiên bàn giao

- Capability discovery paid providers đã hoàn tất; không dùng paid video provider theo yêu cầu.
- Route miễn phí Colab/Kaggle được khảo sát; Colab Wan2.1 Q4 T4 được chọn làm route thực thi.
- Colab environment đã từng cài thành công các dependency/model cần thiết.
- Lần generation thử chưa tạo được MP4 do notebook bị lỗi UI `SyntaxError`; notebook đã được reload về source nguyên bản.
- Runtime hiện cần reconnect; production state vẫn giữ `ASSET_GENERATION_BLOCKED` cho đến khi có MP4 và QC evidence hợp lệ.

**Người nhận bàn giao:** tiếp tục từ mục 4.3, không khởi tạo lại pipeline story hoặc manifest.

---

*End of handover document.*
