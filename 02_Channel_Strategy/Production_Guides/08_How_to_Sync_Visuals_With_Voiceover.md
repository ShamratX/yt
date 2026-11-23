# Step 8 Guide: How to Synchronize Visuals With the Voiceover

> **Core Principle:** The **voiceover timeline is the boss**. Every single visual scene must start on the exact second the narrator introduces that idea—and switch cleanly at the end of a thought or sentence.

---

## How Synchronization Works in Our System

### Step A: Measure Exact Voiceover Duration First
Once `02_voiceover/voiceover_FINAL.mp3` (or `.wav`) is saved inside your episode folder, give **Antigravity / Claude**:
1. Your topic
2. `01_script/script_APPROVED.md`
3. `02_voiceover/voiceover_FINAL.mp3`

Antigravity checks the exact audio length with `ffprobe` (for example, `792.4 seconds` = `13:12`) and maps your approved script paragraphs onto exact start/end timestamps.

### Step B: Build the Timestamped Scene Plan (`scene_plan.json`)
Using `07_AI_Image_Prompts/Prompt_05_Scene_Breakdown.md`, Antigravity creates `03_scene_plan/scene_plan.json`, where every scene specifies:
- `scene_id` (`scene_001`)
- `start` and `end` time in seconds (e.g., `0.0` to `5.5`)
- `narration_line` (the exact sentence spoken during this scene)
- `image` (`04_images/scene_001.png`)
- `motion` (`zoom_in`, `pan_right`, `zoom_out`, `static`, etc.)

### Step C: Automated Assembly Checks Exact Sync
When you run `08_Video_Production/scripts/assemble_video.py`:
- Each image is rendered for its **exact scene duration** (`end - start`) so scenes never drift out of sync by even half a second over a 15-minute video!
- If you tweak one timestamp in `scene_plan.json` (e.g., changing a cut from `14.0s` to `15.2s`), simply re-run the script to rebuild cleanly.

---

## Simple Visual Sync Rules That Keep Viewers Hooked
- **Cut on visual nouns & twists:** When the narrator says *"Now rewind 50,000 years..."*, cut immediately from the modern bedroom scene to the prehistoric night savanna on the word *"rewind"*.
- **Avoid "talking heads" staring silently:** Never leave one static character on screen for 30+ seconds.
- **Give charts/diagrams breathing room:** Hold infographics for 8–12 seconds with `static` or very slow zoom so viewers can read the numbers easily.
