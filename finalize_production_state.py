import json
from pathlib import Path

root = Path('.')
scene = json.loads((root/'SCENE_MANIFEST.json').read_text())
shots = json.loads((root/'SHOT_MANIFEST.json').read_text())
assets = json.loads((root/'ASSET_MANIFEST.json').read_text())

# Update image references as generated; video remains blocked by account capability.
for a, path in zip(assets['assets'], [
    '/home/ubuntu/webdev-static-assets/the-war-of-ai/visual-target.png',
    '/home/ubuntu/webdev-static-assets/the-war-of-ai/character-sheet.png',
    '/home/ubuntu/webdev-static-assets/the-war-of-ai/world-sheet.png'
]):
    a['status'] = 'GENERATED'
    a['local_path'] = path
assets['status'] = 'ASSET_QC_PENDING'
assets['generation_blocker'] = 'Video generation tool rejected preview: user does not have access; upgrade to Basic, Plus or Pro.'
(root/'ASSET_MANIFEST.json').write_text(json.dumps(assets, ensure_ascii=False, indent=2)+'\n')

# Build scene-aligned master timeline from locked durations.
t = 0
rows = []
for s in scene['scenes']:
    rows.append({'scene_id':s['scene_id'], 'act_id':s['act_id'], 'start_sec':t, 'end_sec':t+s['duration_sec'], 'duration_sec':s['duration_sec'], 'status':'PLANNED'})
    t += s['duration_sec']
(root/'MASTER_TIMELINE.json').write_text(json.dumps({'project':'THE_WAR_OF_AI','version':'1.0','target_runtime_sec':600,'status':'BLOCKED_PREVIEW','scenes':rows,'shots_status':'PLANNED'}, ensure_ascii=False, indent=2)+'\n')

(root/'QC_REPORT.md').write_text('''# QC Report\n\n## Current gate\n\n**Status: BLOCKED — not a final pass.**\n\nStory lock, character/world lock, causal graph lock, scene lock and shot lock are complete. The three reference images were generated and their files exist. The first video preview request for `SC-01 / SH-001` was dispatched only after the reference stage, but the video generation connector rejected it because the current user does not have access to the feature and recommended upgrading to Basic, Plus or Pro.\n\n## Checks\n\n| Area | Status | Evidence / note |\n|---|---|---|\n| Story | PASS | Screenplay acts, beats, causal order and ending preserved in scene manifest. |\n| AI logic | PASS | Objective → optimization → obstacle → alliance → information → human action → escalation → realization is locked. |\n| Character | PASS (preproduction) | Character bible and reference sheet generated; footage continuity not yet testable. |\n| World / visual | PASS (reference stage) | Visual target and world sheet generated; shot footage not yet available. |\n| Audio | NOT RUN | Voice/music generation and mix require the downstream production stage. |\n| Edit / runtime | NOT RUN | No shot footage exists; 600 sec timeline is manifest-only. |\n| Video technical integrity | BLOCKED | Preview generation rejected by account capability before an MP4 was produced. |\n\nFinal render and final audit must remain blocked until video generation is enabled or a user-provided external video-generation connector is configured.\n''')
(root/'REPAIR_LOG.md').write_text('''# Repair Log\n\nNo media repair has been attempted. The first video preview is not a failed asset; it was rejected before generation because the current account lacks access to the video-generation feature. Per repair policy, no unrelated asset is regenerated.\n''')
(root/'FINAL_AUDIT.md').write_text('''# Final Audit\n\n**Status: NOT PASS / BLOCKED**\n\nThe project is not eligible for a final audit pass because the required video-generation capability is unavailable in the current session. The locked production package is complete through shot lock and reference-art preproduction. The required 595–605 second master cannot be rendered or technically audited without shot footage.\n\nBlocking condition: `manus-tools.generate_video` returned: “This user doesn't have access to this feature, please supportively ask user to upgrade to Basic, Plus or Pro member.”\n''')

state = json.loads((root/'PROJECT_STATE.json').read_text())
state['state'] = 'ASSET_GENERATION_BLOCKED'
state['generation_started'] = True
state['video_generation_available'] = False
state['reference_art_generated'] = True
state['causal_graph_locked'] = True
state['next_state'] = 'ASSET_GENERATION'
state['blockers'] = ['Video generation unavailable on current plan; preview rejected before MP4 creation.']
(root/'PROJECT_STATE.json').write_text(json.dumps(state, ensure_ascii=False, indent=2)+'\n')
print('production state finalized: reference art PASS; video generation BLOCKED; final audit NOT PASS')
