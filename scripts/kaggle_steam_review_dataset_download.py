from pathlib import Path
from config.paths import RAW_DATA_DIR
import shutil
import kagglehub

download_path = Path(
    kagglehub.dataset_download(
        "antonkozyriev/game-recommendations-on-steam"
    )
)

print(download_path)
print(list(download_path.iterdir()))

raw_dir = Path(RAW_DATA_DIR)
raw_dir.mkdir(parents=True, exist_ok=True)

for file_name in ["games.csv", "recommendations.csv", "users.csv"]:
    shutil.copy(download_path / file_name, raw_dir / file_name)

print("Files copied to data/raw")