# THE WAR OF A.I. — Tool Capability Matrix

**Discovery status:** completed before any generation job.
**Discovery date:** 2026-09-07.
**Scope:** capabilities exposed in this Manus session plus local CLI fallbacks. No capability is assumed unless observed.

| Capability | Primary | Fallback | Connector/API/tool evidence | Batch/retry | Decision and limitation |
|---|---|---|---|---|---|
| Workflow orchestration | `workflow.run` | Direct sequential shell/tool calls | `workflow` MCP exposes `run`; deterministic JS orchestration with agent/parallel primitives | Yes, via workflow | Use for independent research/QC planning units; do not use for deterministic ffmpeg loops. |
| Video generation | `manus-tools.generate_video` using `gemini-omni-flash-preview` | `veo3.1-fast`, then `veo3.1` | `manus-tools` tool schema confirmed; 3–10 sec Omni clips, 16:9/9:16, 720p | Per-shot generation; local retry | Generate approved shots only, never a 10-minute single job. Keep audio off for editability. |
| Visual target / reference images | `manus-tools.generate_image` | `generate_image_variation` | `manus-tools` schemas confirmed | Batch up to 5 images | Mandatory before footage generation. Use realistic 2034 political-thriller direction; no robot-war imagery. |
| Character consistency | Generated reference sheets + image/video `references` | Variation tool | `generate_image` and `generate_video` accept reference paths | Per-character/per-location refs | No dedicated character-lock API observed; enforce via approved reference sheets and prompts. |
| Voice / dialogue | `manus-tools.generate_speech` | Local `ffmpeg` concatenation for chunks | Speech schema confirmed; WAV output; max prompt 6000 chars; two-speaker configs supported | Scene/line chunks; retry smallest failed voice unit | Generate Minh/Lan/AI dialogue as separate layers; preserve voice identity and language code. |
| Music | `manus-tools.generate_music` | Local ambience/SFX construction with `ffmpeg` | Music schema confirmed; WAV/MP3; max ~184 sec/call | Generate act-length cues, concatenate with ffmpeg | Instrumental only; separate from dialogue and footage. |
| SFX / ambience / news / alerts | Local `ffmpeg` + generated music/voice layers | Existing generated video audio disabled | No dedicated SFX MCP tool observed; ffmpeg installed at `/usr/bin/ffmpeg` | Scriptable, deterministic | Build as independent audio stems; do not bake final mix into footage. |
| Video editing / NLE | Local `ffmpeg` + ffprobe | None observed | `ffmpeg` and `ffprobe` installed; no NLE MCP tool exposed | Deterministic concat/filtergraph; retry smallest failed layer | Primary assembly fallback. Must validate 595–605 sec and scene order from manifests. |
| Subtitle generation / sync | Local deterministic subtitle writer + `ffmpeg` mux | Manual manifest-driven correction | No subtitle MCP tool observed; ffmpeg available | Per-scene/line repair | Generate `.srt`/embedded track from locked dialogue timing; record repairs. |
| Media QC | `ffprobe` + manifest validators + `ffmpeg` signal checks | Web/browser preview for human review | `ffprobe` installed; WebDev/browser tools available, but no dedicated media-analysis MCP found | Per-asset and master checks | Technical QC automated. Visual/narrative QC requires approved references, manifests, and human-visible review. Do not use model video analysis to judge generated-video aesthetics, per tool contract. |
| File storage / delivery | Sandbox paths + `manus-upload-file` where needed | Git-tracked metadata | CLI exists in environment; no storage MCP tool listed | Per-asset upload | Keep large media outside repo; commit manifests and reports, not generated binaries unless small. |
| Browser / preview | `manus-tools` browser tools | Local ffmpeg frame extraction for technical inspection | Browser navigation/view/click/input tools listed | Per-page | Use only for management UI/preview if needed; not a substitute for source manifests. |
| WebDev host | `manus-tools.webdev_init_project` | Local project + ffmpeg only | WebDev init/checkpoint/screenshot/restart tools listed | Checkpoint-based | This repository is a film production package, not a browser game. Do not create a game host unless a later deliverable explicitly requires it. |

## Selected toolchain

1. **Control plane:** Manus orchestrator + `workflow.run` for independent, non-deterministic specialist tasks.
2. **Story/data plane:** Markdown/JSON manifests validated by local scripts.
3. **Visual plane:** `generate_image` for reference/continuity sheets, then `generate_video` in short approved shots.
4. **Audio plane:** `generate_speech` for dialogue, `generate_music` for score, local `ffmpeg` for ambience/SFX stems and mix.
5. **Edit/QC plane:** local `ffmpeg`/`ffprobe`, manifest validators, and browser/preview review.
6. **Storage plane:** sandbox for working media; `manus-upload-file` only for assets that need external storage.

## Capability gaps and mitigations

- No dedicated NLE, subtitle, SFX, or media-QC MCP tool was observed. These are covered by deterministic local `ffmpeg`/`ffprobe` and manifest-driven scripts.
- No dedicated character-consistency service was observed. Continuity is enforced through locked reference sheets, reference images, stable prompts, and per-shot QC.
- No dedicated video-analysis tool is used for aesthetic judgment because the available generation tool explicitly warns against it; visual QC remains reference/preview based.
- No direct publish target is defined by the repository specification. Final output is therefore a local master plus audit artifacts unless a delivery connector is later requested.

## Contract guardrails

- Do not alter premise, causal graph, narrative order, or ending.
- Do not generate a 10-minute clip in one job.
- Do not start asset generation before this matrix and the execution graph are committed.
- Repair the smallest failed unit and log it in `REPAIR_LOG.md`.
