# QC Report

## Current gate

**Status: BLOCKED — not a final pass.**

Story lock, character/world lock, causal graph lock, scene lock and shot lock are complete. The three reference images were generated and their files exist. The first video preview request for `SC-01 / SH-001` was dispatched only after the reference stage, but the video generation connector rejected it because the current user does not have access to the feature and recommended upgrading to Basic, Plus or Pro.

## Checks

| Area | Status | Evidence / note |
|---|---|---|
| Story | PASS | Screenplay acts, beats, causal order and ending preserved in scene manifest. |
| AI logic | PASS | Objective → optimization → obstacle → alliance → information → human action → escalation → realization is locked. |
| Character | PASS (preproduction) | Character bible and reference sheet generated; footage continuity not yet testable. |
| World / visual | PASS (reference stage) | Visual target and world sheet generated; shot footage not yet available. |
| Audio | NOT RUN | Voice/music generation and mix require the downstream production stage. |
| Edit / runtime | NOT RUN | No shot footage exists; 600 sec timeline is manifest-only. |
| Video technical integrity | BLOCKED | Preview generation rejected by account capability before an MP4 was produced. |

Final render and final audit must remain blocked until video generation is enabled or a user-provided external video-generation connector is configured.
