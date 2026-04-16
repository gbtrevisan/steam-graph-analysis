from pathlib import Path
import shutil
import kagglehub

def download_steam_dataset():
    project_root = Path(__file__).resolve().parent.parent

    download_path = Path(
        kagglehub.dataset_download("tamber/steam-video-games")
    )

    raw_dir = project_root / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    source_file = download_path / "steam-200k.csv"
    target_file = raw_dir / "steam-200k.csv"

    if not target_file.exists():
        shutil.copy(source_file, target_file)

    print(f"Dataset saved to: {target_file.resolve()}")

if __name__ == "__main__":
    download_steam_dataset()