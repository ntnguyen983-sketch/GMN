# THE WAR OF A.I. — Operations Guide

## Phạm vi

Tài liệu này hướng dẫn vận hành route Google Colab free T4 + Wan2.1 I2V 14B Q4 GGUF được chỉ định trong `BAN-GIAO-CHI-TIET-CONG-VIEC.md`. Mục tiêu trước mắt là tạo baseline `SC-01/SH-001` bằng reference continuity revision R2. Tài liệu không thay thế screenplay, manifest hoặc execution graph.

## Nguyên tắc bất biến

Không sửa screenplay, `CAUSAL_GRAPH.json`, `SCENE_MANIFEST.json`, `SHOT_MANIFEST.json`, character bible hoặc world bible. Không chạy toàn bộ notebook bằng `Run all`. Không chuyển `PROJECT_STATE.json` sang `ASSET_QC` nếu chưa có MP4 thật, ffprobe evidence và checksum. Không coi việc runtime kết nối hoặc model tải gần xong là setup PASS.

## Route và input chuẩn

Notebook: <https://colab.research.google.com/github/Isi-dev/Google-Colab_Notebooks/blob/main/Wan2_1_14B_I2V_GGUF_Free.ipynb>

| Trường | Giá trị |
|---|---|
| Runtime | Google Colab free T4 |
| Model | Wan2.1 I2V 14B Q4 GGUF |
| Reference | `visual-target.png` continuity R2 |
| Width / height | `832 / 480` |
| Frames / FPS | `33 / 16` |
| Steps | `20` |
| Seed | `0` |
| Output | `mp4` |
| Prompt | `SHOT_MANIFEST.json`, shot `SH-001` |
| Output filename | `SC-01_SH-001_preview_v001.mp4` |

## Quy trình chuẩn

1. Mở notebook từ URL trên và đăng nhập Google nếu được yêu cầu.
2. Kết nối runtime T4. Ghi nhận runtime chỉ là `CONNECTED`, chưa phải toolchain PASS.
3. Chạy duy nhất cell `Prepare Environment`, giữ `useQ6` tắt để dùng Q4 trên T4.
4. Chờ output cuối có `Environment Setup Complete!` hoặc thông báo tương đương của notebook.
5. Chỉ sau setup PASS mới mở/cấu hình widget `Generate Video`. Không sửa code cell.
6. Upload `/home/ubuntu/webdev-static-assets/the-war-of-ai/visual-target.png`.
7. Nhập prompt từ shot manifest và các thông số chuẩn ở bảng trên.
8. Chạy cell generation một lần, không reset runtime trong lúc inference.
9. Tải MP4 về sandbox với tên chuẩn.
10. Chạy ffprobe, kiểm tra decode và tạo SHA-256.
11. Chỉ khi technical QC PASS mới cập nhật asset record và chuyển sang `ASSET_QC`.

## Tiêu chí setup PASS

Setup chỉ PASS khi cell đã kết thúc, nút chạy không còn trạng thái đang thực thi, output có thông báo hoàn tất và các thành phần tối thiểu của notebook/model đã được khởi tạo. Runtime connected, disk tăng, package download đạt 97% hoặc output dừng ở `Preparing metadata ... done` đều chưa đủ bằng chứng.

## Xử lý `SETUP_STALL`

Dấu hiệu `SETUP_STALL` là cell vẫn giữ trạng thái thực thi quá lâu, hoặc đã kết thúc ở log tải model gần hoàn tất nhưng không có `Environment Setup Complete!`. Ví dụ checkpoint ngày 2026-09-07: runtime T4 connected, PyTorch/CUDA đã được thay thế, model Wan2.1 hiển thị khoảng 9.3/9.5 GiB (97%), cell mất khoảng 20 phút nhưng không có completion marker.

Khi gặp tình huống này:

1. Không chạy `Generate Video`, không chạy `Run all`, không bấm cell setup lần thứ hai trong cùng trạng thái.
2. Chụp/lưu bằng chứng gồm timestamp, runtime type, output cuối và disk/RAM.
3. Đánh dấu failed unit là `Prepare Environment`, không đánh dấu video capability hoặc asset generation PASS.
4. Nếu output rõ ràng đã kết thúc nhưng thiếu completion marker, mở phần output đầy đủ để tìm traceback trước khi quyết định retry.
5. Nếu không có traceback nhưng cell không tiến triển, disconnect/reconnect runtime một lần, rồi chạy lại `Prepare Environment` từ notebook nguyên bản. Đây là retry của cùng smallest unit, không phải thay đổi pipeline.
6. Nếu stall lặp lại, chuyển fallback: GPU cloud/persistent GPU hoặc external video connector có capability đã quan sát; cập nhật capability matrix trước khi generation.
7. Không dùng ảnh tĩnh, slideshow hoặc kéo dài frame để giả lập video generation.

## Technical QC cho MP4

```bash
ffprobe -v error \
  -show_entries format=duration:stream=index,codec_name,codec_type,width,height,avg_frame_rate,nb_frames \
  -of json SC-01_SH-001_preview_v001.mp4

sha256sum SC-01_SH-001_preview_v001.mp4
```

MP4 phải tồn tại, đọc được, có video stream và codec hợp lệ. Ghi nhận thực tế về kích thước, FPS, frame count và duration; không tự suy diễn nếu notebook điều chỉnh thông số. Nếu technical QC FAIL, ghi vào `REPAIR_LOG.md` và chỉ retry `SH-001`.

## Handover evidence bắt buộc

Mỗi lần bàn giao phải ghi: timestamp, notebook URL, runtime, model, reference revision, setup status, generation status, output path, ffprobe JSON, checksum, lỗi quan sát được, smallest repair unit và next action. Chỉ tuyên bố `ASSET_QC` khi đủ toàn bộ evidence này.

## Trạng thái cập nhật hiện tại

Tại lần kiểm tra gần nhất, dự án đang ở `ASSET_GENERATION_BLOCKED`. Reference R2 PASS ở preproduction. Colab runtime CONNECTED nhưng `Prepare Environment` là `SETUP_STALL` ở bước tải model khoảng 97%; chưa có MP4, ffprobe output hoặc checksum video. Bước tiếp theo là retry có kiểm soát của đúng cell setup theo mục `Xử lý SETUP_STALL`, không chạy generation trước đó.

## Quy trình mở rộng sau SH-001 — 2026-09-07T22:33:24.429883+00:00

`SH-001` đã pass technical QC. Từ `SH-002` trở đi, mỗi shot chạy theo vòng lặp: đọc shot record khóa → xác nhận runtime/setup → tạo một cell generation riêng → tải trực tiếp reference nếu file chooser lỗi → chờ inference → tải MP4 → ffprobe/checksum → tạo QC JSON → commit/push. Không chạy song song nhiều cell trong cùng một Colab runtime và không chạy `Run all`.

Assembly chỉ được phép khi có đủ 76 MP4, các audio/subtitle stem bắt buộc và tổng duration trong 595–605 giây. Script `assemble_master.py` là gate bắt buộc; nếu thiếu bất kỳ shot nào, script phải dừng và không tạo master. Checklist chi tiết nằm ở `PRODUCTION-CHECKLIST.md`.

## Trạng thái thực tế

Tại 2026-09-07T22:33:24.429883+00:00, `SH-001` là artifact duy nhất đã render/QC. `SH-002` là next action; `SH-003`–`SH-076` pending.
