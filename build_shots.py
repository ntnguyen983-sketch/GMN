import json
from pathlib import Path

manifest = json.loads(Path('SCENE_MANIFEST.json').read_text())
shots = []
cameras = [
    ('establishing wide', 'slow push-in'),
    ('medium interface or two-shot', 'controlled lateral move'),
    ('close detail / screen insert', 'minimal drift'),
    ('reaction or network composition', 'locked-off hold')
]
for scene in manifest['scenes']:
    base = scene['duration_sec'] // 4
    remainder = scene['duration_sec'] % 4
    for idx in range(4):
        duration = base + (1 if idx < remainder else 0)
        shot_num = len(shots) + 1
        camera, movement = cameras[idx]
        dialogue = scene['dialogue'][idx] if idx < len(scene['dialogue']) else ''
        subject = scene['characters'][idx % max(1, len(scene['characters']))]
        if scene['scene_id'] == 'SC-19' and idx == 2:
            subject = 'PERFECTION title card'
        if scene['scene_id'] == 'SC-19' and idx == 3:
            subject = 'THE WAR OF A.I. title card'
        shots.append({
            'shot_id': f'SH-{shot_num:03d}',
            'scene_id': scene['scene_id'],
            'duration_sec': duration,
            'camera': camera,
            'movement': movement,
            'subject': subject,
            'action': scene['action'],
            'environment': scene['location'],
            'lighting': 'realistic practical and screen illumination; restrained cool institutional palette',
            'dialogue': dialogue,
            'sfx': scene['audio_requirement'],
            'music': 'act-appropriate restrained tension cue; preserve silence at realization beats',
            'reference_assets': ['CHARACTER_BIBLE.md', 'WORLD_BIBLE.md'],
            'generation_prompt': f"Realistic cinematic near-future political thriller, 2034, {camera}, {subject}, {scene['action']} Environment: {scene['location']}. No humanoid robots, no cyberpunk neon overload, no cartoon styling, no villain framing. Preserve continuity with locked character and world bibles.",
            'status': 'PLANNED'
        })
assert len(shots) == 76
assert sum(s['duration_sec'] for s in shots) == 600
Path('SHOT_MANIFEST.json').write_text(json.dumps({'project':'THE_WAR_OF_AI','version':'1.0','status':'LOCKED','shot_count':len(shots),'total_duration_sec':600,'shots':shots}, ensure_ascii=False, indent=2)+'\n')
print(f'wrote {len(shots)} shots / {sum(s["duration_sec"] for s in shots)} sec')
