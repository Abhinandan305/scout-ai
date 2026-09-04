import matplotlib.pyplot as plt
from mplsoccer import Pitch
import plotly.graph_objects as go
import numpy as np
import pandas as pd

def create_radar_chart(player1_stats, player2_stats, labels):
    """
    Creates a professional radar chart comparing two players.
    """
    # Add first value to the end to close the circle
    p1 = player1_stats + [player1_stats[0]]
    p2 = player2_stats + [player2_stats[0]]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=p1, theta=labels + [labels[0]],
        fill='toself', name='Player 1', line_color='cyan'
    ))
    fig.add_trace(go.Scatterpolar(
        r=p2, theta=labels + [labels[0]],
        fill='toself', name='Player 2', line_color='magenta'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True,
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def create_shot_map(player_role):
    """
    Generates a mock shot map based on player role.
    Demonstrates use of mplsoccer.
    """
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#222222', line_color='#ffffff')
    fig, ax = pitch.draw()

    # Generate random coordinates based on role
    if player_role == 'Clinical Finisher':
        x = np.random.uniform(100, 120, 10)
        y = np.random.uniform(30, 70, 10)
    elif player_role == 'Deep Lying Playmaker':
        x = np.random.uniform(40, 80, 10)
        y = np.random.uniform(20, 80, 10)
    else:
        x = np.random.uniform(50, 110, 10)
        y = np.random.uniform(10, 90, 10)

    # Randomly assign goal/no-goal
    colors = np.random.choice(['green', 'red'], 10)

    plt.scatter(x, y, c=colors, s=100, edgecolors='white', zorder=3)
    plt.title(f"Projected Shot Map: {player_role}", color='white', fontsize=15)

    # Save as image for the dashboard
    img_path = 'assets/shot_map_demo.png'
    plt.savefig(img_path, facecolor=fig.get_facecolor())
    plt.close()
    return img_path

if __name__ == "__main__":
    # Test Radar
    labels = ['Passes', 'Tackles', 'Interceptions', 'xG']
    p1 = [0.8, 0.2, 0.3, 0.9]
    p2 = [0.4, 0.9, 0.8, 0.1]
    fig = create_radar_chart(p1, p2, labels)
    # fig.show() # Streamlit will handle this

    # Test Shot Map
    create_shot_map('Clinical Finisher')
    print("Visualizations generated.")
