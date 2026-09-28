import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).parent


def run_step(script):

    print()
    print("=" * 60)
    print(f"Running: {script}")
    print("=" * 60)

    result = subprocess.run(
        [
            sys.executable,
            str(script),
        ]
    )

    if result.returncode != 0:

        print(
            f"\nPipeline failed at: {script}"
        )

        sys.exit(
            result.returncode
        )


def main():

    run_step(BASE_DIR / "src" / "validate_data.py")

    run_step(BASE_DIR / "src" / "process_data.py")

    run_step(BASE_DIR / "src" / "feature_engineering.py")

    print()
    print("=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()
