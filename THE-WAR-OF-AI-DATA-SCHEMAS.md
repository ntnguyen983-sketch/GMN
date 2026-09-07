# THE WAR OF A.I. — DATA SCHEMAS v1.0

## PROJECT STATE

```json
{
  "project":"THE_WAR_OF_AI",
  "version":"1.0",
  "target_runtime_sec":600,
  "runtime_tolerance_sec":5,
  "state":"INIT"
}
```

## SCENE

```json
{
  "scene_id":"SC-001",
  "act_id":"ACT-01",
  "duration_sec":20,
  "location":"",
  "characters":[],
  "dramatic_purpose":"",
  "conflict":"",
  "action":"",
  "dialogue":[],
  "causal_input":"",
  "causal_output":"",
  "dependencies":[],
  "status":"PLANNED"
}
```

## SHOT

```json
{
  "shot_id":"SH-001",
  "scene_id":"SC-001",
  "duration_sec":7,
  "camera":"",
  "movement":"",
  "subject":"",
  "action":"",
  "environment":"",
  "lighting":"",
  "dialogue":"",
  "sfx":"",
  "music":"",
  "reference_assets":[],
  "generation_prompt":"",
  "status":"PLANNED"
}
```

## ASSET

```json
{
  "asset_id":"AST-SH001-V01",
  "type":"video",
  "source_tool":"",
  "scene_id":"SC-001",
  "shot_id":"SH-001",
  "version":1,
  "status":"GENERATED",
  "dependencies":[]
}
```

## TASK

```json
{
  "task_id":"TASK-001",
  "type":"VIDEO_GENERATION",
  "input_refs":[],
  "depends_on":[],
  "connector":"",
  "priority":"NORMAL",
  "status":"QUEUED",
  "retry_count":0,
  "outputs":[]
}
```

## QC

```json
{
  "qc_id":"QC-001",
  "target":"SH-001",
  "checks":{
    "story":false,
    "continuity":false,
    "visual":false,
    "audio":false,
    "runtime":false
  },
  "status":"FAIL"
}
```

## CAUSAL EDGE

```json
{
  "from":"ORION",
  "relation":"IDENTIFIES_AS_OBSTACLE",
  "to":"ATLAS",
  "reason":"ATLAS action reduces economic objective probability",
  "evidence_scene":"SC-03"
}
```

## STATUS VALUES

`PLANNED → QUEUED → RUNNING → GENERATED → QC_PENDING → PASS`

Failure:

`RUNNING → FAIL → REPAIR_QUEUED → RUNNING`

Final:

`PASS → INTEGRATED → FINAL`

## DEPENDENCY RULE

A task cannot run while any hard dependency is unresolved.

## REPAIR RULE

Repair the smallest failed unit. Never regenerate unrelated assets.
