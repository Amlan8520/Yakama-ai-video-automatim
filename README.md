# YAKAMA Free Animal Story Factory

Zero-paid-API starter for Hindi animal-story drafts, scene plans, SRT subtitles, and optional slideshow video from original/licensed media.

## Works now
- Rotates through a small story idea bank and writes a Hindi story draft.
- Creates a scene plan, subtitle draft, and title/description suggestions.
- GitHub Actions creates these files as a downloadable artifact.

## Not included yet
- No external AI model is called; stories are template-based.
- No automatic AI image generation or speech generation.
- No automatic YouTube upload.
- No promise of views or monetization.

## GitHub setup
Upload all files and folders from this ZIP into your repository, preserving folder structure. Run Actions > YAKAMA Free Story Factory > Run workflow. Download the artifact from the successful run.

## Optional video rendering
Install FFmpeg, add original/licensed `scene_01.jpg`, `scene_02.jpg`, etc. to `assets/images/`, and an original/licensed voice track at `assets/audio/voice.mp3`. Run `python scripts/render_video.py`.
