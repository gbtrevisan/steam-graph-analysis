# steam-graph-analysis

This project aims to model the **Steam online game platform** as a graph in order to analyze the relationships between different games and genres.

In this graph model:
- **nodes represent games**
- **edges represent similarity between games**

The similarity between two games is measured based on the **overlap of their player bases**, using metrics such as the number of common players and similarity scores (e.g., Jaccard index).

The main goal is to explore:
- communities of similar games
- structural relationships between genres
- central and bridge games in the network
- graph-based game recommendations

## Project Structure

- **`notebooks/`** – Contains the main graph analysis notebook (`steam_graph_analysis.ipynb`) with data loading, preprocessing, graph construction, and analysis
- **`config/`** – Environment configuration files including paths to data and output locations
- **`data/raw/`** – Raw datasets downloaded from external sources (games, users, recommendations)
- **`data/processed/`** – Built graphs in GraphML format ready for visualization and further analysis
- **`scripts/`** – Utility scripts for downloading and preparing datasets

## Quick Start

### 1. Set Up Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Analysis

Open and run the notebook:

```bash
jupyter notebook notebooks/steam_graph_analysis.ipynb
```

The notebook will load the raw data, build the game similarity graph, and export the results to `data/processed/`.
