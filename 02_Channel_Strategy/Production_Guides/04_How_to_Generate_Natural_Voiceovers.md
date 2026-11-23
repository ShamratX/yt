# Step 4 Guide: How to Generate Natural English Voiceovers

> **Golden Rule:** Finish and approve the audio file **before** building the scene plan or creating images. The video must always match the real voiceover—never the other way around.

---

## Step-by-Step Voiceover Process

### 1. Clean Your Script for Speaking (`Prompt_04_Voiceover_Preparation.md`)
Written text and spoken text are different. Before pasting into your TTS tool:
- Remove visual stage directions, `[Chapter titles]`, URLs, and citation brackets.
- Spell out awkward abbreviations or scientific terms phonetically if needed (e.g., `BCE` → `B C E`, `DRD4` → `D-R-D-4`, `1990s` → `nineteen nineties`, `3:07 AM` → `three oh seven A M`).
- Break long paragraphs into short 2–3 sentence beats with clean line breaks so the AI naturally breathes.

### 2. Generate in 2–3 Minute Chunks (Not All 2,000 Words at Once)
- Split your cleaned script by chapter (6–7 chunks of ~300 words each).
- Why? Chunking prevents the AI voice from flattening out, drifting in pitch, or rushing—and lets you re-generate one 15-second mistake in seconds without wasting credits.

### 3. Recommended Commercial-Safe Tools (Details in `06_Voiceovers/Voiceover_Guide_and_Licensing.md`)
- **Free (\$0/mo) Cloud:** **Google Cloud TTS (`Chirp 3: HD`)** (1M free chars/mo) or **Azure AI Speech F0** (500K free chars/mo).
- **Free (\$0/mo) Zero-Card:** **Kokoro TTS** (Apache 2.0 local on Windows) or **Microsoft Clipchamp Free**.
- **Best Paid Upgrade:** **ElevenLabs Starter (\$6/mo)** or **Creator (\$22/mo)**. *(Never use ElevenLabs Free—strictly non-commercial!)*

### 4. Combine & Inspect Your Audio File
- Export each chunk as `WAV` (48kHz) or high-bitrate `MP3` (192kbps+).
- Listen all the way through once with headphones:
  - Are any names or dates mispronounced? Re-generate just that sentence.
  - Are there awkward 2-second silences? Trim them down to ~0.35–0.5 seconds.
- Join the chunks cleanly (or let Antigravity / FFmpeg join them automatically) and save the single master file as:
  `02_voiceover/voiceover_FINAL.mp3` (or `.wav`).
