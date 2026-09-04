import pandas as pd
import numpy as np
import os

def load_player_data():
    """
    Loads the football player dataset.
    In a production environment, this would connect to an API or SQL DB.
    For this project, we use a curated dataset of player stats.
    """
    data_path = 'data/players.csv'

    if os.path.exists(data_path):
        print("Loading existing data from CSV...")
        return pd.read_csv(data_path)

    print("Dataset not found. Generating high-fidelity synthetic dataset for Scouting AI...")
    # To ensure the project is immediately runnable and "cool" for the portfolio,
    # we generate a dataset that mimics real-world football distributions.
    # A real scout would use FBref or StatsBomb.

    np.random.seed(42)
    num_players = 500

    # Basic Info
    players = {
        'Player': [f'Player_{i}' for i in range(num_players)],
        'Age': np.random.randint(17, 35, num_players),
        'Position': np.random.choice(['Forward', 'Midfielder', 'Defender', 'Goalkeeper'], num_players, p=[0.2, 0.3, 0.4, 0.1]),
        'League': np.random.choice(['Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Ligue 1'], num_players),
        'MarketValue': np.random.uniform(0.5, 100, num_players).round(1), # In Millions
    }

    df = pd.DataFrame(players)

    # Generate Position-Specific Stats (to make Clustering AI work)
    # We create 'profiles' so the AI can actually find patterns.

    # Midfielders (Passers, Ball winners, etc.)
    mid_mask = df['Position'] == 'Midfielder'
    df.loc[mid_mask, 'ProgressivePasses'] = np.random.normal(2.5, 1.0, sum(mid_mask))
    df.loc[mid_mask, 'Tackles'] = np.random.normal(1.5, 0.8, sum(mid_mask))
    df.loc[mid_mask, 'Interceptions'] = np.random.normal(1.2, 0.6, sum(mid_mask))
    df.loc[mid_mask, 'xG'] = np.random.normal(0.1, 0.05, sum(mid_mask))

    # Forwards (Goal scorers, Dribblers)
    fwd_mask = df['Position'] == 'Forward'
    df.loc[fwd_mask, 'ProgressivePasses'] = np.random.normal(1.0, 0.5, sum(fwd_mask))
    df.loc[fwd_mask, 'Tackles'] = np.random.normal(0.3, 0.2, sum(fwd_mask))
    df.loc[fwd_mask, 'Interceptions'] = np.random.normal(0.2, 0.1, sum(fwd_mask))
    df.loc[fwd_mask, 'xG'] = np.random.normal(0.4, 0.15, sum(fwd_mask))

    # Defenders (Ball recovery, Clearance)
    def_mask = df['Position'] == 'Defender'
    df.loc[def_mask, 'ProgressivePasses'] = np.random.normal(1.5, 0.7, sum(def_mask))
    df.loc[def_mask, 'Tackles'] = np.random.normal(2.2, 1.0, sum(def_mask))
    df.loc[def_mask, 'Interceptions'] = np.random.normal(1.8, 0.9, sum(def_mask))
    df.loc[def_mask, 'xG'] = np.random.normal(0.05, 0.03, sum(def_mask))

    # Fill NaNs for other positions/randomness
    df = df.fillna(0).round(2)

    # Save to CSV for future use
    df.to_csv(data_path, index=False)
    print(f"Dataset generated and saved to {data_path}")
    return df

if __name__ == "__main__":
    data = load_player_data()
    print(data.head())
