#!/usr/bin/env python3
"""Deterministic assembly gate for THE WAR OF A.I.

The script refuses to assemble unless every locked shot has a valid MP4. It
never duplicates or stretches a shot to fake the 600-second master.
"""
from __future__ import annotations
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def run_probe(path: Path) -> dict:
    cmd = [
        'ffprobe', '-v', 'error', '-show_entries',
        'format=duration:stream=codec_type,codec_name,width,height,avg_frame_rate,nb_frames',
        '-of', 'json', str(path)
    ]
    return json.loads(subprocess.check_output(cmd, text=True))

def shot_ids() -> list[str]:
    manifest = json.loads((ROOT / 'SHOT_MANIFEST.json').read_text())
    shots = manifest.get('shots', manifest if isinstance(manifest, list) else [])
    return [s['shot_id'] for s in shots]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--input-dir', type=Path, default=ROOT / 'evidence')
    ap.add_argument('--output', type=Path, default=ROOT / 'evidence' / 'THE-WAR-OF-AI_MASTER_v001.mp4')
    ap.add_argument('--allow-duration-outside-target', action='store_true')
    args = ap.parse_args()

    ids = shot_ids()
    missing = []
    invalid = []
    concat = []
    total = 0.0
    for sid in ids:
        candidates = [args.input_dir / f'{sid}.mp4', args.input_dir / f'{sid}_preview_v001.mp4']
        path = next((p for p in candidates if p.exists()), None)
        if path is None:
            missing.append(sid)
            continue
        try:
            probe = run_probe(path)
            streams = probe.get('streams', [])
            video = next(s for s in streams if s.get('codec_type') == 'video')
            duration = float(probe['format']['duration'])
            if video.get('codec_name') not in {'h264', 'hevc', 'vp9', 'av1'}:
                raise ValueError(f'unsupported codec {video.get("codec_name")}')
            total += duration
            concat.append(path)
        except Exception as exc:
            invalid.append({'shot_id': sid, 'path': str(path), 'error': str(exc)})

    report = {'required_shots': len(ids), 'found_valid_shots': len(concat), 'missing': missing, 'invalid': invalid, 'duration_sec': total}
    print(json.dumps(report, indent=2))
    if missing or invalid:
        print('ASSEMBLY_BLOCKED: all locked shot MP4s are required; no output was written.', file=sys.stderr)
        return 2
    if not args.allow_duration_outside_target and not 595 <= total <= 605:
        print(f'ASSEMBLY_BLOCKED: duration {total:.3f}s outside 595–605s target.', file=sys.stderr)
        return 3

    list_file = args.output.with_suffix('.concat.txt')
    list_file.write_text(''.join(f"file '{p.resolve()}'\n" for p in concat))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', str(list_file), '-c', 'copy', str(args.output)], check=True)
    print(f'ASSEMBLY_PASS {args.output}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
