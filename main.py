from pathlib import Path
from agents.story_agent import make_story_package
from voice_agent import generate_voice

def main():
    output = Path("output")
    output.mkdir(exist_ok=True)

    package = make_story_package()

    story_file = output / "story_draft.txt"
    story_file.write_text(package["story"], encoding="utf-8")

    (output / "scene_plan.txt").write_text(
        package["scene_plan"], encoding="utf-8"
    )

    (output / "subtitles.srt").write_text(
        package["subtitles"], encoding="utf-8"
    )

    (output / "video_metadata.txt").write_text(
        package["metadata"], encoding="utf-8"
    )

    voice_ok = generate_voice(
        package["story"],
        str(output / "voice.mp3")
    )

    if voice_ok:
        print("Voice generation completed.")
    else:
        print("Voice generation skipped; check espeak-ng setup.")

    print("YAKAMA Story Factory completed!")

if __name__ == "__main__":
    main()
