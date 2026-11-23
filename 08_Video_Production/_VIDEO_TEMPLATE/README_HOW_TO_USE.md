# How to Use This Reusable Video Template (`_VIDEO_TEMPLATE`)

**Never edit `_VIDEO_TEMPLATE` directly.** Copy it once for every new episode!

## 4 Simple Steps for Every New Video

### 1. Copy This Folder
Copy `_VIDEO_TEMPLATE` inside `08_Video_Production/` and rename the copy:
- Example: `08_Video_Production/EP01_3AM_Wakeup`

### 2. Provide Your 3 Inputs (Script First, Voice Second!)
Place only these 3 things into your new episode folder:
1. Fill in `video_brief.md` (your topic).
2. Save your approved script as `01_script/script_APPROVED.md`.
3. Save your approved English voiceover as `02_voiceover/voiceover_FINAL.mp3` (or `.wav`).

### 3. Hand Off to Antigravity / Claude
Tell Antigravity:
> *"I am ready to produce `EP01_3AM_Wakeup`. My approved script and voiceover are inside the folder. Please measure the voiceover duration, create the timestamped `scene_plan.json`, generate the original image prompts for `04_images/`, create `06_subtitles/captions.srt`, and run `assemble_video.py` once the images are saved."*

### 4. Assemble Automatically via Command Line (One Command!)
Once your original images (`scene_001.png`, `scene_002.png`, ...) are inside `04_images/`:

**Standard YouTube Export (Clean artwork + separate `.srt` uploaded to YouTube CC):**
```powershell
python "C:\Users\Shamrat\Desktop\YouTube Channel Project\08_Video_Production\scripts\assemble_video.py" --project "C:\Users\Shamrat\Desktop\YouTube Channel Project\08_Video_Production\EP01_3AM_Wakeup" --music "05_music_sfx/bg_music.mp3"
```

**Optional Export With Subtle Burned-In Subtitles:**
```powershell
python "C:\Users\Shamrat\Desktop\YouTube Channel Project\08_Video_Production\scripts\assemble_video.py" --project "C:\Users\Shamrat\Desktop\YouTube Channel Project\08_Video_Production\EP01_3AM_Wakeup" --music "05_music_sfx/bg_music.mp3" --burn-subtitles
```

Your finished 1080p MP4 appears automatically in `08_final_export/FINAL_VIDEO.mp4`.
