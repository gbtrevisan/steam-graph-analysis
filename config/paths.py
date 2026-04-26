from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

STEAM_DATASET_PATH = RAW_DATA_DIR / "steam-200k.csv"
STEAM_RECOMMENDATIONS_PATH = RAW_DATA_DIR / "recommendations.csv"
STEAM_GAMES_DATASET_PATH = RAW_DATA_DIR / "games.csv"
STEAM_USERS_DATASET_PATH = RAW_DATA_DIR / "users.csv"
SAMPLE_GRAPH_OUTPUT_PATH = PROCESSED_DATA_DIR / "steam_game_similarity_sample_1pct.graphml"
SAMPLE_GRAPH_VISUAL_OUTPUT_PATH = PROCESSED_DATA_DIR / "steam_game_similarity_visual_sample_1pct.graphml"