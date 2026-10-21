"""Optional basic slideshow renderer. Requires FFmpeg and locally supplied licensed images."""
from pathlib import Path
import subprocess
import sys

images = sorted(Path("assets/images").glob("scene_*.jpg"))
if not images:
    sys.exit("No images found. Add licensed/original assets/images/scene_01.jpg, scene_02.jpg, etc.")
if not Path("assets/audio/voice.mp3").exists():
    sys.exit("No voice file found at assets/audio/voice.mp3. Add your own licensed voice-over.")

Path("output").mkdir(exist_ok=True)
# Build a concat list; image durations are simple defaults and should be edited for pacing.
concat_file = Path("output/concat.txt")
with concat_file.open("w", encoding="utf-8") as f:
    for image in images:
        f.write(f"file '{image.resolve().as_posix()}'\n")
        f.write("duration 4\n")
    f.write(f"file '{images[-1].resolve().as_posix()}'\n")

cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file),
    "-i", "assets/audio/voice.mp3", "-vf",
    "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
    "-shortest", "-r", "30", "-c:v", "libx264", "-c:a", "aac",
    "output/animal_story_draft.mp4"
]
subprocess.run(cmd, check=True)
print("Rendered output/animal_story_draft.mp4 — review before publishing.")
