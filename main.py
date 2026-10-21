from pathlib import Path
from agents.story_agent import make_story_package

def main():
    output = Path("output")
    output.mkdir(exist_ok=True)

    package = make_story_package()

    (output / "story_draft.txt").write_text(
        package["story"], encoding="utf-8"
    )

    (output / "scene_plan.txt").write_text(
        package["scene_plan"], encoding="utf-8"
    )

    (output / "subtitles.srt").write_text(
        package["subtitles"], encoding="utf-8"
    )

    (output / "video_metadata.txt").write_text(
        package["metadata"], encoding="utf-8"
    )

    print("YAKAMA Animal Story Factory completed!")

if __name__ == "__main__":
    main()
