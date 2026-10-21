from pathlib import Path
from agents.story_agent import make_story_package

out = Path("output")
out.mkdir(parents=True, exist_ok=True)
package = make_story_package()
(out / "story_draft.txt").write_text(package["story"], encoding="utf-8")
(out / "scene_plan.txt").write_text(package["scene_plan"], encoding="utf-8")
(out / "subtitles.srt").write_text(package["subtitles"], encoding="utf-8")
(out / "video_metadata.txt").write_text(package["metadata"], encoding="utf-8")
print("Story draft, scene plan, subtitles, and metadata created.")
