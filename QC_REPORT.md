# QC Report

## Current gate

**Status: BLOCKED — not a final pass.**

Story lock, character/world lock, causal graph lock, scene lock and shot lock are complete. The three reference images were regenerated as continuity revision R2 and their files exist with recorded checksums. The Google Colab fallback route is open and a GPU runtime is connected, but the current kernel has no mounted Google Drive. The Drive bypass diagnostic reported `DRIVE_EXISTS: False`, `TOP: NO_DRIVE`, and `ALL_FILES: []`. The bypass therefore stopped before copying `visual-target.png` into ComfyUI. No MP4 was generated.

## Checks

| Area | Status | Evidence / note |
|---|---|---|
| Story | PASS | Screenplay acts, beats, causal order and ending preserved in scene manifest. |
| AI logic | PASS | Objective → optimization → obstacle → alliance → information → human action → escalation → realization is locked. |
| Character | PASS (preproduction, R2) | Character bible and regenerated continuity sheet exist; footage continuity not yet testable. |
| World / visual | PASS (reference stage, R2) | Regenerated visual target and world sheet exist; shot footage not yet available. |
| Colab runtime | PASS (connected) | Google login succeeded; free GPU runtime connected. |
| Colab environment | PASS previously / current kernel requires input repair | Earlier setup reached the generation widget; current kernel diagnostic confirms Drive is not mounted. |
| Drive/reference input | FAIL / DRIVE_MOUNT_MISSING | `/content/drive/MyDrive` does not exist; `visual-target.png` was not found. |
| Audio | NOT RUN | Voice/music generation and mix require the downstream production stage. |
| Edit / runtime | NOT RUN | No shot footage exists; 600 sec timeline is manifest-only. |
| Video technical integrity | BLOCKED | No MP4 was produced, so ffprobe/decode QC cannot run. |

Final render and final audit must remain blocked until Drive is mounted and the reference path is verified, video generation produces valid shot footage, and all downstream QC evidence exists. The next repair unit is only the current-kernel Drive mount/reference verification; see `OPERATIONS-GUIDE.md` and `REPAIR_LOG.md`.

## Handover execution check — 2026-09-07T20:10:34.880792+00:00

The locked manifests were validated locally: 19 scenes, 76 shots, and 600 seconds total. The designated Colab route could not enter runtime because Google authentication was required in the available sandbox browser. The designated R2 reference file was not present locally. Therefore generation, video technical QC, audio, edit assembly, and master QC remain **NOT RUN/BLOCKED**.

## Colab setup checkpoint — 2026-09-07T21:11:30.136454+00:00

- **Runtime:** Connected to Python 3 Google Compute Engine backend (GPU), reported RAM 12.67 GB and disk 112.64 GB.
- **Cell:** `Prepare Environment` is executing; output shows PyTorch/CUDA package installation and replacement.
- **Observed status:** `Waiting to finish the current execution`; no `Environment Setup Complete!` marker yet.
- **Generation status:** `Generate Video` has not been run. No MP4, ffprobe evidence, or checksum exists.
- **State:** Remains `ASSET_GENERATION_BLOCKED`; do not transition to `ASSET_QC`.
- **Next action:** Wait for this same setup cell to finish; classify as `SETUP_PASS` only if the completion marker appears, otherwise record `SETUP_STALL`/traceback.


## Colab final execution evidence — 2026-09-07T21:45:30.200218+00:00

- Runtime: connected T4 GPU.
- Prepare Environment: completion marker not observed in the available evidence.
- Generate Video: failed before inference because no reference image was uploaded; observed `No image uploaded` and `AttributeError`.
- Output: no MP4, no video stream, no `ffprobe` evidence, no checksum.
- Gate: **BLOCKED**; smallest failed unit is reference upload for `SC-01/SH-001`.


## Colab final execution evidence — 2026-09-07T21:45:39.990970+00:00

- Runtime: connected T4 GPU.
- Prepare Environment: completion marker not observed in the available evidence.
- Generate Video: failed before inference because no reference image was uploaded; observed `No image uploaded` and `AttributeError`.
- Output: no MP4, no video stream, no `ffprobe` evidence, no checksum.
- Gate: **BLOCKED**; smallest failed unit is reference upload for `SC-01/SH-001`.
