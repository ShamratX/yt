# Step 9 Guide: How to Add Subtitles, Sound Effects and Background Music

> **Goal:** Make your video sound like a polished documentary while keeping 100% copyright safety and clean visual legibility.

---

## 1. Subtitles & Captions (Long-Form vs. Shorts Rule)
- **For Long-Form Videos (12–16 min):**
  - **Best Practice (Verified across 10/10 top long-form competitors):** Do **NOT** burn giant TikTok-style text across the middle of your 2D illustrations—it covers your artwork and hurts the documentary feel.
  - Instead, create a clean, accurate **`.srt` subtitle file** (`06_subtitles/captions.srt`) and upload it as **YouTube Closed Captions (CC)** inside YouTube Studio! This improves accessibility, boosts SEO indexing, and makes YouTube's **Auto-Dubbing** far more accurate.
  - *(Optional: If you ever want subtle clean bottom subtitles burned directly into the MP4, our tested script `assemble_video.py` supports `--burn-subtitles` with clean small bottom styling!)*
- **How to Generate `.srt` Free:**
  - **Microsoft Clipchamp Free** (upload your `voiceover_FINAL.mp3`, click *Captions → Transcribe → Download `.srt`*), **OR** ask Antigravity to generate a timed `.srt` from `script_APPROVED.md` + `scene_plan.json` using `Prompt_09_Subtitle_Generation.md`.

---

## 2. Background Music (100% Copyright-Safe)
- **Source:** **YouTube Audio Library** inside YouTube Studio (100% YPP monetization safe, zero Content ID claims!). Filter by **"Attribution not required"** to keep descriptions tidy.
- **Music Vibe for Our Niche:** Soft, curious marimba/plucked acoustic, subtle documentary piano, warm atmospheric underscore—never loud EDM, heavy drums, or vocals!
- **Volume Rule (CRITICAL):** Background music must sit **-24 dB to -28 dB** beneath your narration (~6% to 10% volume). If you notice the music while listening, it is too loud!
- **Automatic Mixing:** Our script `assemble_video.py` automatically loops your background music track, fades it in/out smoothly, and mixes it cleanly underneath your normalized voiceover.

---

## 3. Sound Effects (Less Is More!)
Use **subtle, purposeful SFX** (also free from YouTube Audio Library → *Sound effects* tab) only on key moments:
- **Opening Hook (0:00–0:45):** 1–2 realistic atmospheric cues (e.g., quiet clock tick, distant night crickets, crackling campfire).
- **Chapter Transitions:** 1 very soft paper-turn, subtle brush-whoosh, or gentle wooden chime at each major chapter shift.
- **Rule:** Never spam loud cartoon boings, vine booms, or constant swooshes—they feel amateurish in an editorial documentary channel.
