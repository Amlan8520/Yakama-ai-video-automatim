from pathlib import Path
import subprocess
import shutil


def generate_voice(text, output_file="output/voice.mp3"):
    """
    Generate Hindi voice using a locally installed espeak-ng.
    Requires espeak-ng and ffmpeg for audio conversion.
    """

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not shutil.which("espeak-ng"):
        print("espeak-ng is not installed. Voice generation skipped.")
        return False

    if not text.strip():
        print("No text provided.")
        return False

    try:
        subprocess.run(
            [
                "espeak-ng",
                "-v", "hi",
                "-s", "135",
                "-w", str(output_path.with_suffix(".wav")),
                text
            ],
            check=True
        )
        print(f"Voice saved: {output_path.with_suffix('.wav')}")
        return True

    except (subprocess.CalledProcessError, OSError) as error:
        print(f"Voice generation failed: {error}")
        return False


if __name__ == "__main__":
    sample_text = (
        "नमस्ते बच्चों! आज हम एक प्यारे हाथी की कहानी सुनेंगे।"
    )
    generate_voice(sample_text)
