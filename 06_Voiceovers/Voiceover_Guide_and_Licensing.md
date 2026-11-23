# Voiceover Guide & Commercial Licensing Comparison

> **Core Principle:** Your voice is your channel's #1 retention asset—viewers will forgive simple 2D visuals, **never** robotic or legally risky audio. Every option below was checked against official licensing terms as of November 2026.

---

## 1. Verified Comparison of Natural English AI Voice Options

| Voice Platform | Free Plan & Limits | Paid Starting Price | Commercial Rights on Free Plan? | Voice Quality & Pronunciation | Long-Form (12–16 min) Suitability | Downloadable Formats | Verdict |
|---|---|---|---|---|---|---|---|
| **Google Cloud Text-to-Speech (Chirp 3: HD & Neural2)** | **1,000,000 chars/month FREE** on Chirp 3: HD, Neural2 & Studio *(≈ 10–12 hours/mo! Requires linking billing card; \$0 billed under 1M chars)* | Pay-as-you-go *only* above 1M chars (\$16–\$30/1M) | **YES** — Standard Google Cloud commercial rights | **Very High (8.5/10)** on `Chirp 3: HD` English voices; smooth conversational rhythm | **Excellent** — Handles long scripts cleanly via batch/chunked synthesis | **MP3, WAV (`LINEAR16`), OGG_OPUS** | **#1 FREE COMMERCIAL CLOUD CHOICE** |
| **Microsoft Azure AI Speech (Free F0 Tier)** | **500,000 neural chars/month FREE** permanently *(≈ 5–6 hours/mo!)* | \$15/1M chars (Neural) or \$22/1M (HD) | **YES** — Official commercial use allowed (royalty-free for YouTube) | **High (8/10)** — Natural US/UK Neural & Multilingual voices (e.g., `en-US-AndrewMultilingualNeural`, `en-US-BrianMultilingualNeural`) | **Excellent** — Full SSML control for pauses, pitch & emphasis | **MP3, WAV/PCM, OGG/Opus** | **#2 FREE COMMERCIAL CLOUD CHOICE** |
| **Kokoro TTS (`hexgrad/kokoro` 82M)** | **100% FREE forever** (runs locally on your own Windows PC!) | \$0 self-hosted | **YES — Apache 2.0 License** (unrestricted commercial use) | **High (8/10)** — Surprisingly warm, crisp English narration (`af_heart`, `am_michael`, `bm_george`) | **Very Good** — Zero character limits; fast local WAV export | **WAV** (convert easily to MP3 with FFmpeg) | **#1 ZERO-CARD LOCAL FREE CHOICE** |
| **Microsoft Clipchamp (Built-in TTS)** | **Free** inside Windows Clipchamp app / web | ~\$11.99/mo or M365 | **Yes** (for your own original video projects; avoid premium stock) | **Good (7.5/10)** — Uses Microsoft neural voices; easy browser UI | **Good** — Generate in 5–10 min blocks, export clean audio | **MP4/Audio export** (extract WAV/MP3 via FFmpeg) | **EASIEST ZERO-TECH-SETUP STARTER** |
| **ElevenLabs (Starter / Creator)** | Free tier (10K credits/mo) — **DO NOT USE FOR YOUTUBE!** | **Starter \$6/mo** (\$5 annual = 30K chars ≈ 30 min); **Creator \$22/mo** (121K chars ≈ 121 min) | **NO on Free!** *(Strictly non-commercial; never gets retroactive rights even if you upgrade later!)* **YES on Starter (\$6/mo)+** | **Best-in-Class (9.8/10)** — Unmatched documentary warmth, subtle sarcasm & dramatic pacing | **Excellent** — Built specifically for long-form storytelling (Projects/Studio) | **MP3, WAV, PCM** | **#1 PAID QUALITY UPGRADE (\$6–\$22/mo)** |
| **Fish Audio** | Limited free tier | ~\$15/mo or pay-as-you-go (~\$15/1M bytes ≈ 12 hrs) | **No** on free tier; **Yes** on paid/API | **Very High (9/10)** — Expressive natural narration | **Very Good** | **MP3, WAV** | Strong budget paid alternative to ElevenLabs |
| **Unofficial `edge-tts` Wrappers** | Free (scraped consumer endpoint) | N/A | **NO — Unlicensed / Consumer TOS Risk** | Good | Unreliable (endpoints can block) | MP3 | **AVOID for monetized channels** |

---

## 2. Final Practical Recommendation (Based on Verified Licensing)

### If Starting at \$0/Month (100% Legally Monetizable):
- **Primary Pick:** **Google Cloud TTS (`Chirp 3: HD` English)** *or* **Azure AI Speech Free Tier (F0)** — both give you **500K to 1M free characters every month** (enough for 20–40 long-form videos/month!), full commercial rights, direct MP3/WAV downloads, and natural conversational voices.
- **No-Credit-Card Alternative:** **Microsoft Clipchamp Free** (zero setup) or **Kokoro TTS** (100% local Apache 2.0 on your PC).

### The Best Single Paid Upgrade Once You Commit (or Hit Monetization):
- **ElevenLabs Starter (\$6/mo)** for Month 1 (2 videos/mo ≈ 26–30 min of audio), upgrading to **ElevenLabs Creator (\$22/mo)** once publishing 4–8 videos/month. For storytelling channels like `@Inkexplainer96` and `@Basically-Primitive`, human-like inflection is the #1 driver of 10+ minute Average View Duration.
- **NEVER** publish audio generated on ElevenLabs Free—even before monetization—because you cannot legally monetize those older videos later without re-recording them.

---

## 3. What Voice Style Fits Our Niche Best?
Our niche (**Human Origins, Evolutionary Paradoxes & Everyday Anthropology**) performs best with a voice that sounds like:
- **Warm, curious, intelligent documentary storyteller** (calm baritone or clear mid-register conversational voice — think *Veritasium / Kurzgesagt / Ink Explainer*).
- **Avoid:** Hyper-excited "Top 10 MrBeast" shouting, overly dramatic movie-trailer growling, or monotonous robotic newsreader voices.
- **Accent Choice:** Neutral **General American** or **Clear British English** performs strongest globally (highest comprehension for US/UK/CA/AU Tier-1 viewers *and* non-native English listeners worldwide).

---

## 4. How to Maintain ONE Consistent Voice Across Every Video

1. **Pick and Lock ONE Voice ID Before Video #1:**
   - Test 3 candidate voices on the exact same 45-second hook paragraph. Listen on both **phone speakers** and **headphones**.
   - Write down your locked settings right here in your project and **never change them**:
     - **Platform:** `[e.g., Google Cloud TTS / Azure F0 / Kokoro / ElevenLabs Starter]`
     - **Locked Voice Name / ID:** `[e.g., en-US-Chirp3-HD-Charon or en-US-AndrewMultilingualNeural or ElevenLabs Voice ID]`
     - **Speed / Rate:** `1.00x to 1.04x` (slightly crisp, never rushed)
     - **Stability / Style Settings (if ElevenLabs):** Lock exact sliders (e.g., Stability `45–55%`, Similarity `75%`, Style `10–15%`)
     - **Export Format:** `WAV (48kHz, 16-bit)` or `MP3 (192kbps+, 44.1/48kHz)`
2. **Generate in Clean 2–3 Minute Chapters (Not All 2,200 Words at Once):**
   - Smaller chunks prevent TTS pitch drift, keep energy consistent from minute 1 to minute 14, and make fixing one mispronounced scientific name take 10 seconds instead of re-rendering the entire file.
3. **Standardize Audio Loudness Automatically:**
   - Our automated FFmpeg assembly script (`08_Video_Production/scripts/assemble_video.py`) automatically normalizes your voiceover loudness so Video #1 and Video #50 sound identical in volume.
4. **Always Disclose Honestly When Required:**
   - As proven by `@Inkexplainer96` (19M views), `@Basically-Primitive` (1.2M), and `@HistoryInMinsYT` (653K), checking YouTube's **Altered or synthetic content** disclosure when using realistic AI narration does **not** hurt reach and keeps your channel YPP-safe.
