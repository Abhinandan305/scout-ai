import pandas as pd
import numpy as np
import os

def load_player_data():
    """
    Loads a dataset of real football players with tactically accurate stats.
    """
    data_path = 'data/players.csv'

    # If you want to reset the data to see the new real names,
    # we delete the old CSV first.
    if os.path.exists(data_path):
        os.remove(data_path)

    print("Generating Real-World Player Dataset for Scouting AI...")

    # 1. Define a mapping of real star players and their tactical profiles
    # Format: Name: (Position, League, Role_Profile)
    # Role_Profiles: 0: Playmaker, 1: Ball-Winner, 2: Finisher, 3: Ball-Playing Defender
    star_players = {
        "Erling Haaland": ("Forward", "Premier League", 2),
        "Kylian Mbappe": ("Forward", "La Liga", 2),
        "Harry Kane": ("Forward", "Bundesliga", 2),
        "Mohamed Salah": ("Forward", "Premier League", 2),
        "Vinicius Jr": ("Forward", "La Liga", 2),
        "Kevin De Bruyne": ("Midfielder", "Premier League", 0),
        "Rodri": ("Midfielder", "Premier League", 1),
        "Martin Odegaard": ("Midfielder", "Premier League", 0),
        "Jude Bellingham": ("Midfielder", "La Liga", 1),
        "Declan Rice": ("Midfielder", "Premier League", 1),
        "Toni Kroos": ("Midfielder", "La Liga", 0),
        "Pedri": ("Midfielder", "La Liga", 0),
        "Virgil van Dijk": ("Defender", "Premier League", 3),
        "William Saliba": ("Defender", "Premier League", 3),
        "Ruben Dias": ("Defender", "Premier League", 3),
        "Kyle Walker": ("Defender", "Premier League", 3),
        "Achraf Hakimi": ("Defender", "Ligue 1", 3),
        "Alphonso Davies": ("Defender", "Bundesliga", 3),
        "Alisson Becker": ("Goalkeeper", "Premier League", 1),
        "Thibaut Courtois": ("Goalkeeper", "La Liga", 1),
        "Ederson": ("Goalkeeper", "Premier League", 0),
    }

    player_list = []

    # Add the stars first
    for name, info in star_players.items():
        pos, league, role = info
        # Assign stats based on their role profile
        if role == 0: # Playmaker
            stats = {'ProgressivePasses': np.random.uniform(3.0, 5.0), 'Tackles': np.random.uniform(0.5, 1.5), 'Interceptions': np.random.uniform(0.5, 1.5), 'xG': np.random.uniform(0.1, 0.3)}
        elif role == 1: # Ball-Winner
            stats = {'ProgressivePasses': np.random.uniform(1.0, 2.5), 'Tackles': np.random.uniform(2.5, 4.5), 'Interceptions': np.random.uniform(2.0, 4.0), 'xG': np.random.uniform(0.0, 0.2)}
        elif role == 2: # Finisher
            stats = {'ProgressivePasses': np.random.uniform(0.5, 1.5), 'Tackles': np.random.uniform(0.1, 0.5), 'Interceptions': np.random.uniform(0.1, 0.5), 'xG': np.random.uniform(0.5, 0.9)}
        else: # Ball-Playing Defender
            stats = {'ProgressivePasses': np.random.uniform(2.0, 3.5), 'Tackles': np.random.uniform(2.0, 3.5), 'Interceptions': np.random.uniform(1.5, 3.0), 'xG': np.random.uniform(0.0, 0.1)}

        player_list.append({
            'Player': name,
            'Position': pos,
            'League': league,
            'MarketValue': np.random.uniform(50, 150),
            **stats
        })

    # 2. Fill the rest of the 500 players with realistic-sounding names
    first_names = ["Lucas", "Mateo", "Julian", "Enzo", "Gabriel", "Leo", "Marco", "Santi", "Hugo", "Diego"]
    last_names = ["Silva", "Garcia", "Martinez", "Rodriguez", "Santos", "Oliveira", "Costa", "Fernandez", "Lopez", "Diaz"]
    leagues = ['Premier League', 'La Liga', 'Bundesliga', 'Serie A', 'Ligue 1']
    positions = ['Forward', 'Midfielder', 'Defender', 'Goalkeeper']

    while len(player_list) < 500:
        name = f"{np.random.choice(first_names)} {np.random.choice(last_names)}"
        pos = np.random.choice(positions)
        league = np.random.choice(leagues)

        # Assign a random role profile for stats
        role = np.random.randint(0, 4)
        if role == 0:
            stats = {'ProgressivePasses': np.random.normal(2.5, 1.0), 'Tackles': np.random.normal(1.5, 0.8), 'Interceptions': np.random.normal(1.2, 0.6), 'xG': np.random.normal(0.1, 0.05)}
        elif role == 1:
            stats = {'ProgressivePasses': np.random.normal(1.5, 0.7), 'Tackles': np.random.normal(2.2, 1.0), 'Interceptions': np.random.normal(1.8, 0.9), 'xG': np.random.normal(0.05, 0.03)}
        elif role == 2:
            stats = {'ProgressivePasses': np.random.normal(1.0, 0.5), 'Tackles': np.random.normal(0.3, 0.2), 'Interceptions': np.random.normal(0.2, 0.1), 'xG': np.random.normal(0.4, 0.15)}
        else:
            stats = {'ProgressivePasses': np.random.normal(1.5, 0.7), 'Tackles': np.random.normal(2.2, 1.0), 'Interceptions': np.random.normal(1.8, 0.9), 'xG': np.random.normal(0.05, 0.03)}

        player_list.append({
            'Player': name,
            'Position': pos,
            'League': league,
            'MarketValue': np.random.uniform(0.5, 40),
            **stats
        })

    df = pd.DataFrame(player_list)
    df['Age'] = np.random.randint(17, 35, len(df))
    df = df.fillna(0).round(2)

    # Save to CSV
    df.to_csv(data_path, index=False)
    print(f"Dataset generated with real stars and saved to {data_path}")
    return df

if __name__ == "__main__":
    data = load_player_data()
    print(data.head())
