# ⚽ ScoutAI: Tactical Player Profiling & Recruitment Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://your-app-link.streamlit.app)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-AI-orange.svg)](https://scikit-learn.org/)

## 🎯 Project Overview
ScoutAI is an end-to-end football analytics platform designed for professional scouts to identify undervalued players based on **tactical profiles** rather than raw stats. Instead of searching for "the best midfielder," ScoutAI allows scouts to find "a player who plays like Rodri but costs less than €15M."

## 🧠 The AI Engine
This project implements a two-stage Machine Learning pipeline:

### 1. Tactical Clustering (Unsupervised Learning)
Using **K-Means Clustering**, the engine analyzes high-dimensional performance metrics (xG, Progressive Passes, Tackles, etc.) to group players into specific tactical roles. 
- **Outcome**: Players are automatically categorized into roles such as *Deep Lying Playmaker*, *Ball Winning Midfielder*, and *Clinical Finisher*.

### 2. Player Similarity Engine (Recommendation System)
Implemented using **Cosine Similarity** on normalized feature vectors.
- **Outcome**: A recommendation system that calculates the "distance" between players in a multi-dimensional tactical space, allowing for the discovery of "statistical twins."

## 🛠️ Tech Stack
- **Backend**: Python (Pandas, NumPy, Scikit-Learn)
- **Visuals**: Plotly, mplsoccer, Matplotlib
- **Frontend**: Streamlit
- **Deployment**: Streamlit Cloud

## 📂 Project Structure
```text
├── data/               # Raw and processed CSVs
├── models/             # Saved AI models (.pkl)
├── src/                # Modular source code
│   ├── data_loader.py  # Data acquisition pipeline
│   ├── preprocessor.py # Normalization and scaling
│   ├── clustering_engine.py # K-Means implementation
│   ├── similarity_engine.py # Cosine similarity logic
│   └── visualizer.py   # Tactical chart generation
├── assets/             # Static images and CSS
├── app.py              # Streamlit Dashboard
└── requirements.txt    # Dependencies
```

## 🚀 How to Run
1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/scout-ai.git
   cd scout-ai
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the AI pipeline**:
   ```bash
   python src/data_loader.py
   python src/preprocessor.py
   python src/clustering_engine.py
   ```
4. **Launch the Dashboard**:
   ```bash
   streamlit run app.py
   ```

## 📈 Key Analytics Implemented
- **Radar Charts**: Multi-axis comparison of player strengths.
- **Shot Maps**: Spatial analysis of shooting efficiency.
- **Similarity Matrix**: Identifying undervalued recruitment targets.

---
**Developed by [Your Name]** | Aspiring Football Data Scientist
