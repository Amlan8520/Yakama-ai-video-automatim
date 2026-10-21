from pathlib import Path
import subprocess, sys
images = sorted(Path("assets/images").glob("scene_*.jpg"))
audio = Path("assets/audio/voice.mp3")
if not images:
    sys.exit("Add original/licensed assets/images/scene_01.jpg, scene_02.jpg, etc.")
if not audio.exists():
    sys.exit("Add original/licensed voice-over at assets/audio/voice.mp3.")
Path("output").mkdir(exist_ok=True)
concat = Path("output/concat.txt")
with concat.open("w", encoding="utf-8") as f:
    for p in images:
        f.write(f"file '{p.resolve().as_posix()}'\\n")
        f.write("duration 5\\n")
    f.write(f"file '{images[-1].resolve().as_posix()}'\\n")
subprocess.run([
    "ffmpeg","-y","-f","concat","-safe","0","-i",str(concat),"-i",str(audio),
    "-vf","scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
    "-shortest","-r","30","-c:v","libx264","-c:a","aac","output/animal_story_draft.mp4"
], check=True)
print("Created output/animal_story_draft.mp4; review before publishing.")
