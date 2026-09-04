import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def find_similar_players(target_player_name, top_n=5):
    """
    Finds the most similar players to a target player using Cosine Similarity.
    """
    df = pd.read_csv('data/players_clustered.csv')

    # Use only the scaled feature columns
    scaled_cols = [col for col in df.columns if col.startswith('scaled_')]
    X = df[scaled_cols]

    if target_player_name not in df['Player'].values:
        return None, "Player not found in database."

    # Get the vector for the target player
    target_idx = df[df['Player'] == target_player_name].index[0]
    target_vector = X.iloc[target_idx].values.reshape(1, -1)

    # Calculate similarity between target and all players
    similarities = cosine_similarity(target_vector, X)[0]

    # Add similarities to the dataframe
    df['Similarity'] = similarities

    # Sort by similarity (descending) and exclude the target player themselves
    similar_players = df[df['Player'] != target_player_name].sort_values(by='Similarity', ascending=False)

    return similar_players.head(top_n), None

if __name__ == "__main__":
    # Test the engine
    players, error = find_similar_players('Player_0')
    if error:
        print(error)
    else:
        print("Similar Players to Player_0:")
        print(players[['Player', 'Similarity', 'TacticalRole']])
