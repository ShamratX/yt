# Prompt 08: Video Editing & Automated Assembly Prompt (For Antigravity / Claude)

Copy this prompt to Antigravity when your topic, approved script, approved voiceover, and generated images (`04_images/scene_001.png` ...) are ready inside your episode folder.

---

```text
Assemble the complete YouTube video for this episode using our tested local Python + FFmpeg workflow (`08_Video_Production/scripts/assemble_video.py`).

EPISODE FOLDER: [EPISODE_FOLDER_PATH]
VIDEO TOPIC: [VIDEO_TOPIC]
VOICEOVER FILE: [VOICEOVER_FILE]
EXACT VIDEO DURATION: [VIDEO_DURATION]
BACKGROUND MUSIC FILE (optional, YouTube Audio Library): [MUSIC_FILE]
BURN SUBTITLES? [No — keep clean artwork + separate .srt for YouTube CC / Yes — subtle bottom captions]

STRICT PRODUCTION RULES:
1. Voiceover First: Verify exact audio duration of [VOICEOVER_FILE] with `ffprobe` and confirm `03_scene_plan/scene_plan.json` matches the real voiceover timing from 0.0s to the final second.
2. Original Visual Verification: Confirm all numbered scene images exist in `04_images/`, are original visuals made specifically for this video (no reused images from earlier episodes), have varied framing/compositions matching the narration, and avoid repetitive slideshow patterns.
3. Motion Variety: Ensure `scene_plan.json` varies camera motion (`zoom_in`, `zoom_out`, `pan_left`, `pan_right`, `drift_up`, `static` for diagrams) so consecutive scenes never feel repetitive.
4. Audio Mix: Normalize voiceover loudness and mix background music quietly underneath (default `--music-volume 0.07`, approx. -23 dB to -26 dB) with clean fade-in and fade-out.
5. Export & Verify: Run `assemble_video.py` to export `08_final_export/FINAL_VIDEO.mp4` (1920x1080, 30fps, H.264/AAC), then verify video/audio streams and exact duration using `ffprobe` and report any issues.
```
