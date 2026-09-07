# QC Report

## Current gate

**Status: BLOCKED — not a final pass.**

Story lock, character/world lock, causal graph lock, scene lock and shot lock are complete. The three reference images were regenerated as continuity revision R2 and their files exist with recorded checksums. The Google Colab fallback route was reopened, Google login succeeded and a GPU runtime connected. The single `Prepare Environment` cell was run once with Q4 mode, but setup stalled after PyTorch/CUDA installation while the Wan2.1 model download was approximately 9.3/9.5 GiB (97%); no `Environment Setup Complete!` marker appeared. No MP4 was generated.

## Checks

| Area | Status | Evidence / note |
|---|---|---|
| Story | PASS | Screenplay acts, beats, causal order and ending preserved in scene manifest. |
| AI logic | PASS | Objective → optimization → obstacle → alliance → information → human action → escalation → realization is locked. |
| Character | PASS (preproduction, R2) | Character bible and regenerated continuity sheet exist; footage continuity not yet testable. |
| World / visual | PASS (reference stage, R2) | Regenerated visual target and world sheet exist; shot footage not yet available. |
| Colab runtime | PASS (connected) | Google login succeeded; free GPU runtime connected. |
| Colab environment | FAIL / SETUP_STALL | `Prepare Environment` ran once; model download reached about 97% without completion marker. |
| Audio | NOT RUN | Voice/music generation and mix require the downstream production stage. |
| Edit / runtime | NOT RUN | No shot footage exists; 600 sec timeline is manifest-only. |
| Video technical integrity | BLOCKED | No MP4 was produced, so ffprobe/decode QC cannot run. |

Final render and final audit must remain blocked until the environment setup passes, video generation produces valid shot footage, and all downstream QC evidence exists. The next repair unit is only the `Prepare Environment` cell; see `OPERATIONS-GUIDE.md`.
