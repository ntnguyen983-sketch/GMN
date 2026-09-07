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
