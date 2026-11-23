# Prompt 09: Subtitle Generation Prompt (Clean `.srt` Captions)

Use this prompt to generate clean, readable `.srt` subtitles aligned with your approved script and voiceover timeline (or export `.srt` free via Microsoft Clipchamp Free).

---

```text
Create a clean, YouTube-ready SubRip (`.srt`) subtitle file for this video.

VIDEO TOPIC: [VIDEO_TOPIC]
VOICEOVER FILE: [VOICEOVER_FILE]
EXACT VOICEOVER DURATION: [VIDEO_DURATION]
SCENE TIMESTAMPS / APPROVED SCRIPT:
[SCRIPT]

SUBTITLE FORMATTING RULES:
1. Use valid `.srt` syntax (`HH:MM:SS,mmm --> HH:MM:SS,mmm`) covering the exact span of [VIDEO_DURATION].
2. Keep every caption block easy to read: maximum 2 lines per block, maximum 42 characters per line (2–4 seconds on screen).
3. Break lines at natural phrases—never split a person's name or short phrase awkwardly across lines.
4. Use exact verified spelling for all scientific terms, names, dates, and numbers (this makes YouTube Search indexing and YouTube Auto-Dubbing far more accurate!).
5. Output ONLY the clean `.srt` block ready to save as `06_subtitles/captions.srt`.
```
