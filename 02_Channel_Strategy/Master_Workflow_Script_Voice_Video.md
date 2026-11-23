# Master Production Workflow: Script First → Voice Second → Video Third

> **Golden Rule:** **NEVER generate or assemble video scenes before the English voiceover audio file is finalized and approved.** Every visual scene, camera move, subtitle line, and music cue must follow the exact spoken timing of your real voiceover.

---

## Why This Order Works Best
1. **Zero awkward pacing:** You never speed up, cut, or stretch narration to fit pre-made clips.
2. **Exact visual synchronization:** Antigravity / Claude reads your exact voiceover duration and maps every 6–12 second illustration directly to what is being spoken.
3. **Zero wasted image credits:** You only generate illustrations for lines that actually survived script approval.
4. **Higher YouTube retention:** Clean pacing + matched visuals keep viewers past the crucial 30-second and 3-minute drop-off points.

---

## The 11-Step End-to-End Production Workflow

| Step | Owner | Action | Saved Inside Video Folder |
|---:|---|---|---|
| **STEP 1** | **You** | Pick 1 topic from `03_Topic_Ideas/Topic_Database_100_Ideas.md` and copy `_VIDEO_TEMPLATE` into a new numbered project folder inside `08_Video_Production/` (e.g., `EP01_3AM_Wakeup`). | `video_brief.md` |
| **STEP 2** | **You + AI** | Run `Prompt_01_Topic_Research.md` to gather 4–6 verified studies/sources, then run `Prompt_02_YouTube_Scriptwriting.md` to draft the 12–15 min script (~1,850–2,300 words). | `01_script/research_notes.md`<br>`01_script/script_draft.md` |
| **STEP 3** | **You** | Run `Prompt_03_Script_Fact_Checking.md`. Read the entire script aloud once. Cut boring filler, fix awkward sentences, remove any AI phrasing, and save the **APPROVED** script. | `01_script/script_APPROVED.md` |
| **STEP 4** | **You** | Run `Prompt_04_Voiceover_Preparation.md` to clean pronunciation (dates, scientific names, pauses), then generate the complete English voiceover using your **one locked channel voice** (see `06_Voiceovers/Voiceover_Guide_and_Licensing.md`). | *(Generated in TTS tool)* |
| **STEP 5** | **You** | Download the clean voiceover as high-quality `.mp3` (192kbps+) or `.wav` (48kHz), listen once for glitches, and save it in the video folder. | `02_voiceover/voiceover_FINAL.mp3` (or `.wav`) |
| **STEP 6** | **You → AI** | Give **Antigravity / Claude** three things: (1) Video Topic, (2) `script_APPROVED.md`, and (3) `voiceover_FINAL.mp3`. | *(Handoff point)* |
| **STEP 7** | **Antigravity / Claude** | Measure exact voiceover length, generate/align timestamps, and run `Prompt_05_Scene_Breakdown.md` to create a **scene-by-scene visual plan** (`scene_plan.json`) matched to the real audio timing (55–75 unique scenes). | `03_scene_plan/scene_plan.md`<br>`03_scene_plan/scene_plan.json` |
| **STEP 8** | **You + AI** | Run `Prompt_06_AI_Image_Generation.md` (and optionally `Prompt_07_Image_to_Video_Animation.md` for 2–3 hero scenes) to generate original, non-repetitive illustrations strictly matching our channel art style (`05_characters/`). Save numbered files `scene_001.png` ... `scene_065.png`. | `04_images/scene_001.png` ... |
| **STEP 9** | **Antigravity / FFmpeg Script** | Run our tested local assembly script (`08_Video_Production/scripts/assemble_video.py`) to sync every image to the voiceover timestamps and apply gentle Ken Burns camera motion & transitions. | `08_final_export/rough_cut.mp4` |
| **STEP 10** | **Antigravity / You** | Generate clean `.srt` captions (`Prompt_09_Subtitle_Generation.md`), select 1–2 copyright-safe YouTube Audio Library tracks + soft SFX, mix background music quietly (-24 dB to -28 dB), and export final 1080p MP4. | `06_subtitles/captions.srt`<br>`08_final_export/FINAL_VIDEO.mp4` |
| **STEP 11** | **You** | Watch the full exported MP4 end-to-end (check audio levels, visual sync, spelling). Create 2 thumbnail variants (`Prompt_10_Thumbnail_Generation.md`) and SEO title/description/sources (`Prompt_11_SEO_Title_and_Description.md`), upload with **Test & Compare**, add 1 YouTube Quiz, and log in `10_Published_Videos/`. | `07_thumbnail/thumb_A.png`<br>`07_thumbnail/thumb_B.png`<br>`10_Published_Videos/` |

---

## Simple Quality Checklist Before Every Upload
- [ ] Voiceover was finalized *before* building the scene plan.
- [ ] Every factual claim and study in the script was verified and cited in the description.
- [ ] Zero recycled scenes from previous videos; every scene has unique framing/composition.
- [ ] Background music stays quiet beneath the narration (never fights the voice).
- [ ] Full 1080p MP4 watched start-to-finish with zero dead silence, typos, or visual glitches.
- [ ] YouTube's **Altered or synthetic content** disclosure checkbox reviewed honestly before publishing.
