# Prompt 06: Original AI Image Generation Prompt Template

Use this prompt to generate the exact image-generator prompts (for Leonardo.ai, Flux.1 Schnell, or Midjourney) from your approved scene plan. Replace `[VIDEO_TOPIC]` and `[SCENE_LIST]`.

---

```text
Act as an editorial art director writing clean, high-precision 2D illustration prompts for a YouTube science & anthropology documentary.

VIDEO TOPIC: [VIDEO_TOPIC]
TARGET GENERATOR: [Leonardo.ai / Flux.1 Schnell / Midjourney]
ASPECT RATIO: 16:9 widescreen (1920x1080)

LOCKED CHANNEL ART STYLE (apply consistently to every prompt):
- **Minimal, clean, uncluttered flat 2D editorial illustration** with crisp charcoal ink outlines (#1E2228), smooth flat fills, clean negative space, and simple uncluttered backgrounds.
- **STRICT COLOR LIMIT (NO multi-color messy scenes!):** Maximum **2 to 3 colors per scene** — choose ONE clean background (warm off-white cream #F6F1E7 for day/science scenes OR muted midnight slate #25344A for night scenes) + charcoal ink + **ONLY ONE focal accent color** (muted terracotta #C85A32, muted sage #4E6E58, OR warm amber #E59A3C).
- CHARACTER VARIETY RULE: Keep the EXACT SAME minimal clean 2D art style across all scenes, but draw **different, story-specific characters that match each scene** (e.g., scientists, doctors, teenagers, office workers, prehistoric hunters, elders, families, villagers, historical figures). Do NOT force one single identical character into every scene. Only use an optional generic modern stand-in (muted terracotta sweater) or ancient stand-in (earth-toned tunic) when the narration addresses "you" directly.
- NO busy multi-color messy backgrounds, NO heavy painterly splatters, NO plain white-circle stick figures, NO glossy 3D plastic renders, NO photorealistic AI faces, NO embedded gibberish text or watermarks.

MANDATORY ORIGINAL CONTENT & VISUAL RULES:
- Create original visuals specifically for this video.
- Do not reuse the same scenes, images or animations from previous videos.
- Avoid repetitive AI-generated templates.
- Give every scene a unique visual composition.
- Match visuals with the narration.
- Use different camera angles, framing, backgrounds and illustrations (wide establishing shot, close-up hands/object, over-the-shoulder, bird's-eye view, architectural cross-section, split-screen Modern vs. Ancient).
- Avoid generic stock-looking visuals.
- Do not copy competitor videos, scripts, thumbnails or artwork.
- Do not create misleading historical or scientific visuals (ensure anatomically and historically plausible clothing, tools, wildlife, and environments).
- Keep a consistent overall channel art style while making individual scenes different.
- Avoid unnecessary repetitive animations and slideshow-style videos.
- Every video must have its own original storytelling and visual identity.

SCENE LIST TO CONVERT INTO PROMPTS:
[SCENE_LIST]

For each scene (`scene_001` through the last scene), output:
- Filename (`scene_001.png`)
- Exact copy-paste prompt (2–4 vivid, concrete visual sentences with framing, subject action, lighting, and locked art style)
- Negative prompt (`busy background, cluttered, messy multi-color, rainbow colors, watercolor splatter, overly detailed, text, letters, watermark, logo, stick figure, 3D CGI, photorealistic, extra fingers, distorted face, modern anachronisms`)
```
