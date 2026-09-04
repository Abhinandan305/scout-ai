import pandas as pd
from sklearn.cluster import KMeans
import joblib
import os

def perform_clustering(n_clusters=4):
    """
    Clusters players into tactical roles based on their performance metrics.
    """
    df = pd.read_csv('data/players_scaled.csv')

    # Use only the scaled feature columns for clustering
    scaled_cols = [col for col in df.columns if col.startswith('scaled_')]
    X = df[scaled_cols]

    # Apply K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df['Role_ID'] = kmeans.fit_predict(X)

    # Map Role IDs to Human Readable Names (Simplified for this project)
    # In a real project, you'd analyze the centroids to name these.
    role_mapping = {
        0: "Ball Winning Midfielder",
        1: "Deep Lying Playmaker",
        2: "Clinical Finisher",
        3: "Ball Playing Defender"
    }
    df['TacticalRole'] = df['Role_ID'].map(role_mapping)

    # Save the clustered data
    df.to_csv('data/players_clustered.csv', index=False)

    # Save the model
    joblib.dump(kmeans, 'models/clustering_model.pkl')

    print("Tactical Clustering complete. Roles assigned and saved to data/players_clustered.csv")
    return df

if __name__ == "__main__":
    perform_clustering()
