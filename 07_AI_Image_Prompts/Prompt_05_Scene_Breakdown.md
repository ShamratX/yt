# Prompt 05: Voice-Matched Scene-by-Scene Visual Breakdown

> **CRITICAL RULE:** Run this ONLY **after** `[VOICEOVER_FILE]` is finished and saved! Visual timing must follow the real voiceover—never force the narration to fit unrelated scenes.

---

```text
Act as an editorial documentary visual director.

VIDEO TOPIC: [VIDEO_TOPIC]
VOICEOVER FILE: [VOICEOVER_FILE]
EXACT VOICEOVER DURATION: [VIDEO_DURATION]
APPROVED SCRIPT:
[SCRIPT]

Create a complete, voice-synced scene-by-scene visual plan that covers 100% of [VIDEO_DURATION] from 0.0 seconds to the exact end of [VOICEOVER_FILE].

PACING RULES:
- First 60 seconds (Hook): Fast visual rhythm — 1 fresh scene every 4 to 6 seconds (10–12 scenes).
- Body (1:00 to end): Steady documentary rhythm — 1 fresh scene every 8 to 14 seconds (~55–75 total scenes for a 13-minute video).
- Every scene cut must match the exact moment a new idea, noun, or shift is spoken in the voiceover.

MANDATORY ORIGINAL CONTENT & VISUAL RULES:
- Create original visuals specifically for this video.
- Do not reuse the same scenes, images or animations from previous videos.
- Avoid repetitive AI-generated templates.
- Give every scene a unique visual composition.
- Match visuals with the narration.
- Use different camera angles, framing, backgrounds and illustrations (rotate wide shots, medium reactions, close-up details, overhead maps, split-screen Modern vs. Ancient frames, and 6–8 clean infographic/diagram cards).
- Avoid generic stock-looking visuals.
- Do not copy competitor videos, scripts, thumbnails or artwork.
- Do not create misleading historical or scientific visuals.
- Keep a consistent overall channel art style (warm editorial ink-and-watercolor 2D illustration on cream paper or moody night slate) while making individual scenes different.
- Avoid unnecessary repetitive animations and slideshow-style videos.
- Every video must have its own original storytelling and visual identity.

CAMERA MOTION ASSIGNMENT (never use the same motion twice in a row):
Choose from: "zoom_in", "zoom_out", "pan_left", "pan_right", "drift_up", "static" (use "static" for data charts/diagrams).

OUTPUT FORMAT:
1. A clean Markdown table (Scene ID | Start–End | Narration Line | Visual Composition & Camera Angle | Motion).
2. A valid JSON file ready to save as `03_scene_plan/scene_plan.json` matching `assemble_video.py` format (`scene_id`, `start`, `end`, `narration_line`, `image` as `04_images/scene_001.png`, `motion`, `visual_notes`).
```
