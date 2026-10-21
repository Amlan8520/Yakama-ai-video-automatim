import subprocess
from pathlib import Path


def generate_voice(text, output_file="output/voice.mp3"):
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not text.strip():
        return False

    try:
        subprocess.run(
            [
                "espeak-ng",
                "-v", "hi",
                "-s", "145",
                "-w", str(output_path.with_suffix(".wav")),
                text,
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        wav_file = output_path.with_suffix(".wav")

        subprocess.run(
            [
                "ffmpeg", "-y",
                "-i", str(wav_file),
                str(output_path),
            ],
            check=True,
            capture_output=True,
            text=True,
        )

        return output_path.exists() and output_path.stat().st_size > 0

    except (subprocess.CalledProcessError, FileNotFoundError) as error:
        print(f"Voice generation failed: {error}")
        return False
