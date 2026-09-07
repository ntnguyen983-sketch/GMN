# THE WAR OF A.I. — Production Checklist & Runbook

## 1. Mục tiêu và phạm vi

Mục tiêu cuối là master cinematic dài **600 giây ±5 giây**, gồm 19 scene và 76 shot theo các manifest đã khóa. Quy trình này chỉ cho phép chuyển trạng thái khi có bằng chứng thực tế; không dùng ảnh tĩnh, lặp shot hoặc kéo dài frame để thay thế footage còn thiếu.

## 2. Các file nguồn sự thật

| Nhóm | File | Quy tắc |
|---|---|---|
| Narrative | `THE-WAR-OF-AI-SCREENPLAY-v1.0.md` | Không sửa premise, narrative order hoặc ending |
| Logic | `CAUSAL_GRAPH.json` | Không thay đổi objective, escalation hoặc realization |
| Continuity | `CHARACTER_BIBLE.md`, `WORLD_BIBLE.md` | Dùng cho mọi reference và prompt |
| Shot contract | `SHOT_MANIFEST.json` | Không sửa shot để hợp output; lấy prompt và thông số từ đây |
| Timeline | `MASTER_TIMELINE.json` | Assembly phải giữ tổng runtime 600 giây |
| QC | `QC_REPORT.md`, `FINAL_AUDIT.md`, `REPAIR_LOG.md` | Ghi bằng chứng, không ghi PASS khi thiếu artifact |

## 3. Gate trước mỗi shot

- [ ] Shot có trong `SHOT_MANIFEST.json` và status còn `PLANNED` hoặc đang retry chính shot đó.
- [ ] Xác định đúng `shot_id`, `scene_id`, duration, subject, action, camera, movement và locked prompt.
- [ ] Reference continuity R2 tồn tại và đúng file `visual-target.png` khi shot yêu cầu reference.
- [ ] Colab runtime là T4 và đã kết nối.
- [ ] `Prepare Environment` đã kết thúc với marker hoàn tất; không chạy `Run all`.
- [ ] Không có cell khác đang inference.
- [ ] Tạo thư mục output/evidence và ghi timestamp trước khi chạy.

## 4. Quy trình generation thực tế

1. Mở notebook Wan2.1 I2V GGUF từ URL trong handover.
2. Kết nối T4 và chỉ chạy `Prepare Environment` một lần. Chờ `Environment Setup Complete!`.
3. Không dùng browser file chooser nếu bridge trả về file rỗng. Tải reference trực tiếp vào `/content/ComfyUI/input/visual-target.png`, rồi xác nhận kích thước file trước inference.
4. Tạo một cell generation riêng cho đúng một shot; không sửa cell gốc khóa và không chạy nhiều shot đồng thời.
5. Dùng prompt trong manifest; chỉ truyền các tham số notebook bắt buộc: width 832, height 480, steps 20, cfg 3, sampler `uni_pc`, scheduler `simple`, frames 33, fps 16, output MP4.
6. Không reset runtime khi model đã bắt đầu inference. Theo dõi dòng tiến độ và đợi cell kết thúc.
7. Tìm output thực tế trong `/content/ComfyUI/output` thay vì giả định tên ở thư mục gốc.
8. Dùng `google.colab.files.download()` để tải đúng MP4 về sandbox; đổi tên theo `evidence/SH-XXX.mp4`.

## 5. Technical QC bắt buộc cho từng shot

- [ ] File tồn tại, đọc được và là MP4.
- [ ] Có video stream, codec hợp lệ, không có decode error.
- [ ] Độ phân giải, FPS, frame count và duration được ghi bằng `ffprobe`.
- [ ] SHA-256 được ghi vào `evidence/SH-XXX-QC.json`.
- [ ] Visual review không có watermark, text overlay, freeze, flicker nghiêm trọng, biến dạng identity hoặc robot/fantasy ngoài bible.
- [ ] Nếu FAIL, ghi `REPAIR_LOG.md` và chỉ retry shot đó; không thay đổi manifest khóa.

Lệnh chuẩn:

```bash
ffprobe -v error -show_entries \
  format=duration,size:stream=codec_name,codec_type,width,height,r_frame_rate,nb_frames \
  -of json evidence/SH-XXX.mp4
sha256sum evidence/SH-XXX.mp4
```

## 6. Cập nhật sau mỗi shot PASS

- [ ] Tạo `evidence/SH-XXX.mp4` và `evidence/SH-XXX-QC.json`.
- [ ] Ghi timestamp, route, model, reference revision, tham số, output, ffprobe, checksum và qualification.
- [ ] Cập nhật `PROJECT_STATE.json`, `QC_REPORT.md`, `REPAIR_LOG.md` nếu có repair.
- [ ] Commit và push GitHub.
- [ ] Kiểm tra `git status` sạch.
- [ ] Chỉ sau đó chuyển sang shot tiếp theo.

## 7. Gate chuyển sang assembly

- [ ] Có đủ 76 MP4 hợp lệ, không thiếu `SH-001` đến `SH-076`.
- [ ] Tổng duration source nằm trong khoảng 595–605 giây hoặc có kế hoạch conform được ghi rõ.
- [ ] Voice, music, ambience, SFX, news và subtitle stems đã tồn tại và được QC.
- [ ] Chạy `python3 assemble_master.py`; script phải không còn báo `ASSEMBLY_BLOCKED`.
- [ ] Kiểm tra master bằng `ffprobe`, decode test và runtime.
- [ ] Chạy narrative/continuity/audio/master QC trước khi final audit.

## 8. Các lỗi thường gặp và cách xử lý

| Lỗi | Cách xử lý |
|---|---|
| `No image uploaded` | Không retry vô hạn file chooser; tải trực tiếp reference vào input runtime và xác nhận file size |
| Setup stall | Không chạy generation; lưu output cuối, reconnect một lần và chạy lại setup |
| Runtime disconnect | Không tuyên bố PASS; ghi checkpoint và chỉ tiếp tục sau khi toolchain được xác nhận |
| MP4 thiếu hoặc rỗng | Không cập nhật shot PASS; tìm output path thực tế, tải lại hoặc retry chính shot |
| Sai prompt/tham số | Đánh dấu shot FAIL, không sửa manifest; rerun đúng prompt locked |
| Assembly thiếu shot | Dừng; không lặp hoặc kéo dài footage để đủ runtime |

## 9. Handover tối thiểu

Mỗi lần bàn giao phải có: timestamp, state, gate, shot inventory, missing list, Colab URL, runtime, model, reference revision, setup status, generation status, output paths, ffprobe, checksum, lỗi, repair unit, next action và acceptance condition. `FINAL_AUDIT.md` chỉ được PASS khi master 595–605 giây và mọi artifact bắt buộc đã được QC.

## 10. Trạng thái tại lần cập nhật này

`SH-001` đã technical-QC PASS. `SH-002` là shot kế tiếp đang chờ generation. `SH-003`–`SH-076` vẫn pending. Assembly gate đã được cài trong `assemble_master.py` và hiện phải chặn đúng vì chưa đủ source shots.
