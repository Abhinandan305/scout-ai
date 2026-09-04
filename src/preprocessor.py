import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os

def preprocess_player_data():
    """
    Prepares player data for AI models by normalizing features.
    """
    # Load data
    df = pd.read_csv('data/players.csv')

    # Define the features we want the AI to use for profiling
    # These are "performance" metrics, not "identity" metrics (like Age or League)
    features = ['ProgressivePasses', 'Tackles', 'Interceptions', 'xG']

    # Initialize the Scaler
    scaler = StandardScaler()

    # Scale the features
    scaled_values = scaler.fit_transform(df[features])

    # Create a new dataframe with scaled features
    scaled_df = pd.DataFrame(scaled_values, columns=[f'scaled_{f}' for f in features])

    # Merge back with original identity info
    final_df = pd.concat([df[['Player', 'Age', 'Position', 'League', 'MarketValue']], scaled_df], axis=1)

    # Save the scaled data
    final_df.to_csv('data/players_scaled.csv', index=False)

    # Save the scaler itself (Crucial for the Similarity Engine later)
    os.makedirs('models', exist_ok=True)
    joblib.dump(scaler, 'models/scaler.pkl')

    print("Data preprocessing complete. Scaled data saved to data/players_scaled.csv")
    return final_df

if __name__ == "__main__":
    preprocess_player_data()
