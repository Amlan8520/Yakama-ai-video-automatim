# YAKAMA AI Animal Stories Factory

A starter project for an original Hindi animal-story YouTube workflow.
It prepares story concepts, scores ideas, creates a draft script/metadata package,
and optionally renders a simple video from locally supplied images/audio using FFmpeg.

## Important
- This starter does **not** guarantee views, virality, or monetization.
- It does not scrape YouTube or imitate other creators.
- Generated material must be reviewed for originality, quality, copyright, child safety, and factual claims.
- The default workflow creates a draft package only. Uploading is intentionally not automatic.
- For content intended for children, set the correct "Made for Kids" audience setting in YouTube Studio.

## Quick start (Windows / Android via Termux / Linux)
1. Install Python 3.10+.
2. Extract this ZIP.
3. In the project folder:
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # Linux/macOS/Termux: source .venv/bin/activate
   pip install -r requirements.txt
   python main.py
   ```
4. Draft files appear in `output/`.

This starter works without paid API keys. The initial script uses a template-based story draft.
To use an LLM later, implement `agents/story_agent.py` using a provider you choose and keep API keys in environment variables or GitHub Secrets.

## Optional video rendering
Install FFmpeg and place your own licensed/original visuals in `assets/images/`.
Add images named `scene_01.jpg`, `scene_02.jpg`, etc. Then run:
```bash
python render_video.py
```
The renderer makes a basic slideshow video. It does not create animation or voice by itself.

## GitHub Actions
The workflow `.github/workflows/draft.yml` runs manually or weekly and creates draft files as an artifact.
GitHub Actions minutes/storage limits apply. Long video rendering may require a separate computer/cloud runner.

## Suggested agent roles
- Master: orchestrates steps.
- Research: brainstorms evergreen story ideas (no automated scraping).
- Audience: checks age-appropriateness and clarity.
- Story: writes an original outline/script.
- Quality: checks length, repeated phrases, and safety markers.
- SEO: drafts title/description/tags.
- Analytics: reads a manually exported CSV later; it does not promise outcomes.

## Next upgrades
1. Connect a script-generation API.
2. Add licensed text-to-speech.
3. Add licensed image generation.
4. Add YouTube Data API OAuth upload only after human approval.
5. Add YouTube Analytics API reporting.
