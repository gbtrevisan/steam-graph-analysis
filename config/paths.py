from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

STEAM_DATASET_PATH = RAW_DATA_DIR / "steam-200k.csv"
GRAPH_OUTPUT_PATH = PROCESSED_DATA_DIR / "steam_graph.graphml"