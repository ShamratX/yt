#!/usr/bin/env python3
"""
Automated YouTube Video Assembler (Voice-First, FFmpeg-Powered)
---------------------------------------------------------------
Assembles a 1080p YouTube-ready MP4 video strictly driven by an approved
English voiceover file and a timestamped scene_plan.json.

Requirements (already verified on this Windows PC):
  - Python 3.x (standard library only; Pillow optional for auto-checks)
  - FFmpeg & FFprobe on PATH (tested with FFmpeg 8.1.1)

Usage:
  python assemble_video.py --project "path/to/EP01_Folder"
  python assemble_video.py --project "path/to/EP01_Folder" --music "05_music_sfx/bg_music.mp3" --burn-subtitles

Expected folder layout inside --project:
  02_voiceover/voiceover_FINAL.mp3 (or .wav)
  03_scene_plan/scene_plan.json
  04_images/scene_001.png, scene_002.png, ...
  05_music_sfx/ (optional background music)
  06_subtitles/captions.srt (optional)
  08_final_export/ (output directory)
"""

import argparse
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run_cmd(cmd: list[str], desc: str) -> str:
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"[ERROR] {desc} failed (exit {result.returncode}):\n"
            f"CMD: {' '.join(cmd)}\n"
            f"STDERR:\n{result.stderr[-2000:]}"
        )
    return result.stdout


def get_audio_duration(audio_path: Path) -> float:
    out = run_cmd(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(audio_path),
        ],
        f"Probing duration of {audio_path.name}",
    )
    return float(out.strip())


def find_voiceover(project_dir: Path, explicit: str | None) -> Path:
    if explicit:
        p = Path(explicit)
        if not p.is_absolute():
            p = project_dir / p
        if not p.exists():
            raise FileNotFoundError(f"Voiceover not found: {p}")
        return p

    vo_dir = project_dir / "02_voiceover"
    for name in ["voiceover_FINAL.wav", "voiceover_FINAL.mp3", "voiceover.wav", "voiceover.mp3"]:
        cand = vo_dir / name
        if cand.exists():
            return cand
    for ext in ("*.wav", "*.mp3", "*.m4a"):
        matches = sorted(vo_dir.glob(ext))
        if matches:
            return matches[0]
    raise FileNotFoundError(
        f"No voiceover audio found in {vo_dir}. Save your approved voiceover first (Script -> Voice -> Video)."
    )


def build_motion_filter(motion: str, frames: int, fps: int, width: int, height: int) -> str:
    """
    Smooth Ken Burns / camera motion using 2x oversampling before zoompan
    to prevent jitter on crisp editorial 2D illustrations.
    """
    up_w = width * 2
    up_h = height * 2
    base = (
        f"scale={up_w}:{up_h}:force_original_aspect_ratio=increase,"
        f"crop={up_w}:{up_h},setsar=1"
    )
    frames = max(frames, 1)

    if motion == "static":
        return (
            f"scale={width}:{height}:force_original_aspect_ratio=increase,"
            f"crop={width}:{height},setsar=1,fps={fps},format=yuv420p"
        )
    elif motion == "zoom_in":
        zp = (
            f"zoompan=z='1+0.08*on/{frames}':"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s={width}x{height}:fps={fps}"
        )
    elif motion == "zoom_out":
        zp = (
            f"zoompan=z='1.08-0.08*on/{frames}':"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s={width}x{height}:fps={fps}"
        )
    elif motion == "pan_right":
        zp = (
            f"zoompan=z='1.08':"
            f"x='(iw-iw/zoom)*on/{frames}':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s={width}x{height}:fps={fps}"
        )
    elif motion == "pan_left":
        zp = (
            f"zoompan=z='1.08':"
            f"x='(iw-iw/zoom)*(1-on/{frames})':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s={width}x{height}:fps={fps}"
        )
    elif motion == "drift_up":
        zp = (
            f"zoompan=z='1.08':"
            f"x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(1-on/{frames})':"
            f"d={frames}:s={width}x{height}:fps={fps}"
        )
    else:
        zp = (
            f"zoompan=z='1+0.06*on/{frames}':"
            f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d={frames}:s={width}x{height}:fps={fps}"
        )

    return f"{base},{zp},format=yuv420p"


def escape_srt_path_for_ffmpeg(srt_path: Path) -> str:
    # FFmpeg subtitles filter on Windows requires forward slashes and escaped drive colon
    s = str(srt_path.resolve()).replace("\\", "/")
    if len(s) >= 2 and s[1] == ":":
        s = s[0] + "\\:" + s[2:]
    s = s.replace("'", "\\'")
    return s


def render_scene_clip(
    image_path: Path,
    duration: float,
    motion: str,
    out_clip: Path,
    fps: int,
    width: int,
    height: int,
    fade_in: bool = False,
    fade_out: bool = False,
) -> None:
    frames = max(1, int(round(duration * fps)))
    vf = build_motion_filter(motion, frames, fps, width, height)
    if fade_in:
        vf += ",fade=t=in:st=0:d=0.45"
    if fade_out and duration > 0.6:
        vf += f",fade=t=out:st={max(0.0, duration - 0.55):.3f}:d=0.55"

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", str(image_path),
        "-t", f"{duration:.3f}",
        "-vf", vf,
        "-r", str(fps),
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-an",
        str(out_clip),
    ]
    run_cmd(cmd, f"Rendering scene {out_clip.name} ({motion}, {duration:.2f}s)")


def assemble_video(args: argparse.Namespace) -> Path:
    project_dir = Path(args.project).resolve()
    if not project_dir.exists():
        raise FileNotFoundError(f"Project folder does not exist: {project_dir}")

    voiceover_path = find_voiceover(project_dir, args.voiceover)
    vo_duration = get_audio_duration(voiceover_path)
    print(f"[INFO] Voiceover: {voiceover_path.name} ({vo_duration:.2f}s)")

    plan_path = project_dir / "03_scene_plan" / "scene_plan.json"
    if not plan_path.exists():
        raise FileNotFoundError(f"Missing scene plan: {plan_path}")

    with open(plan_path, "r", encoding="utf-8") as f:
        plan = json.load(f)

    scenes = plan.get("scenes", [])
    if not scenes:
        raise ValueError("scene_plan.json contains no scenes.")

    fps = int(args.fps)
    width = int(args.width)
    height = int(args.height)

    # Validate images and ensure total visual length matches voiceover duration
    resolved_scenes = []
    for idx, sc in enumerate(scenes):
        img_rel = sc["image"]
        img_path = Path(img_rel)
        if not img_path.is_absolute():
            img_path = project_dir / img_rel
        if not img_path.exists():
            raise FileNotFoundError(f"Scene #{idx + 1} image missing: {img_path}")

        start = float(sc["start"])
        end = float(sc["end"])
        if idx == len(scenes) - 1 and end < vo_duration:
            # Automatically extend final scene slightly so video never cuts off voiceover
            end = vo_duration
        dur = max(0.5, end - start)
        resolved_scenes.append(
            {
                "id": sc.get("scene_id", f"scene_{idx + 1:03d}"),
                "image": img_path,
                "duration": dur,
                "motion": sc.get("motion", "zoom_in"),
            }
        )

    export_dir = project_dir / "08_final_export"
    export_dir.mkdir(parents=True, exist_ok=True)
    out_name = args.output if args.output else "FINAL_VIDEO.mp4"
    final_mp4 = export_dir / out_name

    # Locate optional music and subtitles
    music_path = None
    if args.music:
        mp = Path(args.music)
        if not mp.is_absolute():
            mp = project_dir / mp
        if not mp.exists():
            raise FileNotFoundError(f"Music file not found: {mp}")
        music_path = mp

    srt_path = None
    if args.burn_subtitles:
        cand = Path(args.subtitles) if args.subtitles else (project_dir / "06_subtitles" / "captions.srt")
        if not cand.is_absolute():
            cand = project_dir / cand
        if not cand.exists():
            raise FileNotFoundError(f"Subtitles file not found: {cand}")
        srt_path = cand

    with tempfile.TemporaryDirectory(prefix="yt_assemble_") as tmp:
        tmp_dir = Path(tmp)
        concat_lines = []

        # 1. Render each scene clip with smooth camera motion
        for idx, sc in enumerate(resolved_scenes):
            clip_path = tmp_dir / f"clip_{idx + 1:03d}.mp4"
            render_scene_clip(
                image_path=sc["image"],
                duration=sc["duration"],
                motion=sc["motion"],
                out_clip=clip_path,
                fps=fps,
                width=width,
                height=height,
                fade_in=(idx == 0),
                fade_out=(idx == len(resolved_scenes) - 1),
            )
            concat_lines.append(f"file '{clip_path.as_posix()}'")
            print(f"[OK] Rendered {sc['id']} ({sc['motion']}, {sc['duration']:.2f}s)")

        concat_txt = tmp_dir / "concat.txt"
        concat_txt.write_text("\n".join(concat_lines), encoding="utf-8")

        video_track = tmp_dir / "video_concat.mp4"
        run_cmd(
            [
                "ffmpeg", "-y",
                "-f", "concat", "-safe", "0",
                "-i", str(concat_txt),
                "-c", "copy",
                str(video_track),
            ],
            "Concatenating rendered scene clips",
        )

        # 2. Optional burned-in subtitles (subtle editorial style at bottom)
        final_video_input = video_track
        if srt_path is not None:
            subbed_video = tmp_dir / "video_subbed.mp4"
            escaped_srt = escape_srt_path_for_ffmpeg(srt_path)
            style = (
                "FontName=Arial,FontSize=20,PrimaryColour=&H00FFFFFF,"
                "OutlineColour=&H00181818,BackColour=&H64000000,"
                "BorderStyle=1,Outline=2,Shadow=1,MarginV=36"
            )
            run_cmd(
                [
                    "ffmpeg", "-y",
                    "-i", str(video_track),
                    "-vf", f"subtitles='{escaped_srt}':force_style='{style}'",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                    "-pix_fmt", "yuv420p", "-an",
                    str(subbed_video),
                ],
                "Burning subtitles into video",
            )
            final_video_input = subbed_video
            print(f"[OK] Burned subtitles from {srt_path.name}")

        # 3. Mix normalized voiceover + optional quiet background music
        if music_path is not None:
            music_vol = float(args.music_volume)
            fade_out_start = max(0.0, vo_duration - 2.0)
            audio_filter = (
                f"[1:a]loudnorm=I=-16:TP=-1.5:LRA=11[vo];"
                f"[2:a]volume={music_vol:.3f},afade=t=in:st=0:d=1.5,"
                f"afade=t=out:st={fade_out_start:.2f}:d=2.0[bg];"
                f"[vo][bg]amix=inputs=2:duration=first:dropout_transition=2:normalize=0[aout]"
            )
            cmd = [
                "ffmpeg", "-y",
                "-i", str(final_video_input),
                "-i", str(voiceover_path),
                "-stream_loop", "-1", "-i", str(music_path),
                "-filter_complex", audio_filter,
                "-map", "0:v:0",
                "-map", "[aout]",
                "-c:v", "copy",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                "-shortest",
                "-movflags", "+faststart",
                str(final_mp4),
            ]
        else:
            cmd = [
                "ffmpeg", "-y",
                "-i", str(final_video_input),
                "-i", str(voiceover_path),
                "-filter_complex", "[1:a]loudnorm=I=-16:TP=-1.5:LRA=11[aout]",
                "-map", "0:v:0",
                "-map", "[aout]",
                "-c:v", "copy",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                "-shortest",
                "-movflags", "+faststart",
                str(final_mp4),
            ]

        run_cmd(cmd, "Muxing final video and audio")

    print(f"[DONE] Exported final video: {final_mp4}")
    return final_mp4


def main() -> None:
    parser = argparse.ArgumentParser(description="Voice-First YouTube Video Assembler (FFmpeg)")
    parser.add_argument("--project", required=True, help="Path to episode folder (copied from _VIDEO_TEMPLATE)")
    parser.add_argument("--voiceover", default=None, help="Optional custom voiceover file path")
    parser.add_argument("--music", default=None, help="Optional background music path (e.g., 05_music_sfx/bg.mp3)")
    parser.add_argument("--music-volume", type=float, default=0.07, help="Background music volume multiplier (default 0.07 ≈ -23 dB)")
    parser.add_argument("--burn-subtitles", action="store_true", help="Burn captions.srt directly into the MP4")
    parser.add_argument("--subtitles", default=None, help="Optional custom .srt path")
    parser.add_argument("--width", type=int, default=1920, help="Output width (default 1920)")
    parser.add_argument("--height", type=int, default=1080, help="Output height (default 1080)")
    parser.add_argument("--fps", type=int, default=30, help="Output FPS (default 30)")
    parser.add_argument("--output", default="FINAL_VIDEO.mp4", help="Output filename inside 08_final_export/")
    args = parser.parse_args()

    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        print("[ERROR] FFmpeg / FFprobe not found on PATH.", file=sys.stderr)
        sys.exit(1)

    assemble_video(args)


if __name__ == "__main__":
    main()
