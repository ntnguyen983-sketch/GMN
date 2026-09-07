# THE WAR OF A.I. — Execution Graph

## State machine

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

## Dependency graph

```text
P00 Project Init
  └─> P01 Story Engine
       ├─> P02 Character Bible
       ├─> P03 World Bible
       └─> P04 Causal Graph
            └─> P05 Scene Builder
                 └─> P06 Shot Builder
                      └─> P07 Visual Preproduction
                           ├─> P08A Reference Images
                           ├─> P08B Location / Interface Assets
                           └─> P08C Audio Identity Specs
                                └─> P09 Asset QC
                                     ├─> P10 Video Shot Generation (approved shots only)
                                     ├─> P11 Voice Generation (dialogue stems)
                                     └─> P12 Music / Ambience / SFX Generation
                                          └─> P13 Edit Assembly
                                               └─> P14 Subtitle Sync
                                                    └─> P15 Master QC
                                                         ├─FAIL─> P16 Smallest-Unit Repair ─> P15
                                                         └─PASS─> P17 Final Render ─> P18 Final Audit
```

## Parallelism policy

After `P01 Story Engine` passes, `P02`, `P03`, and `P04` can run in parallel because they have independent outputs but must all pass before scene lock. After `P07` passes, visual assets, audio identity specs, and shot prompt preparation can run in parallel. After asset QC, video shots, voices, and music/SFX can run in parallel, with edit assembly blocked until all required stems pass.

Deterministic operations such as ffmpeg concatenation, duration checks, subtitle muxing, and manifest validation run in one bounded local script rather than as per-file subagents.

## Gates

| Gate | Must pass | Evidence |
|---|---|---|
| Tool Discovery | Capability matrix and selected primary/fallback exist | `TOOL_CAPABILITY_MATRIX.md` |
| Story Lock | Screenplay acts/scenes and dialogue intent preserved | `CHARACTER_BIBLE.md`, `WORLD_BIBLE.md`, scene manifest |
| Causal Lock | Objective → optimization → obstacle → alliance → information → human action → escalation → realization intact | `CAUSAL_GRAPH.json` |
| Scene Lock | Every scene has required fields and causal input/output | `SCENE_MANIFEST.json` |
| Shot Lock | Every shot has required camera, subject, action, audio and prompt fields | `SHOT_MANIFEST.json` |
| Asset QC | Reference continuity and technical integrity pass | `ASSET_MANIFEST.json`, QC records |
| Master QC | Narrative, AI logic, character, visual, audio, edit, runtime checks pass | `QC_REPORT.md` |
| Final Audit | Runtime 595–605 sec and all required artifacts present | `FINAL_AUDIT.md` |

## Repair loop

`FAIL → identify smallest failed unit → re-dispatch only that unit → QC → continue.` Every repair is appended to `REPAIR_LOG.md`; unrelated shots, voices, or scenes are never regenerated.

## Current execution position

`TOOL_DISCOVERY` is complete. Generation is intentionally not started until the locked production manifests are written and validated.
