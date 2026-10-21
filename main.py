from pathlib import Path
from agents.master_agent import run_pipeline

if __name__ == "__main__":
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    result = run_pipeline(output_dir)
    print("Draft package created:")
    for path in result:
        print(f" - {path}")
    print("\nReview every file before publishing. No upload was performed.")
