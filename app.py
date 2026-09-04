import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from src.data_loader import load_player_data
from src.similarity_engine import find_similar_players
from src.visualizer import create_radar_chart
import joblib
import os

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="ScoutAI | Tactical Recruitment Engine",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS FOR AESTHETICS ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stMetric {
        background-color: #161b22;
        border-radius: 10px;
        padding: 15px;
        border: 1px solid #30363d;
    }
    div[data-testid="stMetricValue"] {
        color: #00ffcc !important;
    }
    .stButton>button {
        background-color: #00ffcc;
        color: black;
        border-radius: 20px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #00cca3;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA LOADING ---
@st.cache_data
def get_data():
    return load_player_data()

df = get_data()
df_clustered = pd.read_csv('data/players_clustered.csv')

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("⚽ ScoutAI")
st.sidebar.markdown("---")
page = st.sidebar.selectbox(
    "Navigate",
    ["🏠 Home", "🔍 Player Discovery", "🤖 AI Similarity Search", "📈 Tactical Analytics"]
)

# --- PAGE 1: HOME ---
if page == "🏠 Home":
    st.title("ScoutAI: Tactical Recruitment Engine")
    st.markdown("""
    Welcome to the **next generation of football scouting**.
    ScoutAI doesn't just look at goals and assists—it analyzes **tactical profiles** using
    Unsupervised Machine Learning to find undervalued gems.

    ### 🚀 Key Features:
    - **Tactical Clustering**: Groups players into roles like *Deep Lying Playmaker* or *Clinical Finisher*.
    - **AI Similarity Engine**: Find a 'statistical twin' for any star player.
    - **Performance Profiling**: Compare players using high-dimensional radar charts.
    """)

    # Highlight a "Gem" of the week
    st.markdown("---")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/shot_map_demo.png", caption="Sample Tactical Shot Map")
    with col2:
        st.subheader("💎 Scout's Gem of the Week")
        gem = df_clustered.iloc[0]
        st.metric("Player", gem['Player'])
        st.metric("Role", gem['TacticalRole'])
        st.metric("Market Value", f"€{gem['MarketValue']}M")
        st.write(f"This player exhibits a high correlation with elite {gem['TacticalRole']} profiles.")

# --- PAGE 2: PLAYER DISCOVERY ---
elif page == "🔍 Player Discovery":
    st.title("Player Discovery")
    st.markdown("Filter through the database to find players fitting your tactical needs.")

    col1, col2, col3 = st.columns(3)
    with col1:
        pos_filter = st.multiselect("Position", df['Position'].unique(), default=df['Position'].unique())
    with col2:
        league_filter = st.multiselect("League", df['League'].unique(), default=df['League'].unique())
    with col3:
        val_filter = st.slider("Max Market Value (€M)", 0.0, 100.0, 100.0)

    filtered_df = df[
        (df['Position'].isin(pos_filter)) &
        (df['League'].isin(league_filter)) &
        (df['MarketValue'] <= val_filter)
    ]

    st.dataframe(filtered_df, use_container_width=True)

# --- PAGE 3: AI SIMILARITY SEARCH ---
elif page == "🤖 AI Similarity Search":
    st.title("AI Similarity Engine")
    st.markdown("Enter a player's name to find their **statistical twins** across the globe.")

    target_player = st.selectbox("Select Player", df['Player'].unique())

    if st.button("Find Twins"):
        with st.spinner("Analyzing tactical vectors..."):
            sim_df, error = find_similar_players(target_player)

            if error:
                st.error(error)
            else:
                st.success(f"Found top matches for {target_player}!")

                # Display as a beautiful table
                st.table(sim_df[['Player', 'Similarity', 'TacticalRole', 'MarketValue']])

                # Radar Comparison
                st.markdown("### 📊 Tactical Profile Comparison")

                # Get stats for radar (scaled)
                df_scaled = pd.read_csv('data/players_scaled.csv')
                p1_stats = df_scaled[df_scaled['Player'] == target_player].iloc[0, 5:].values.tolist()
                p2_stats = df_scaled[df_scaled['Player'] == sim_df.iloc[0]['Player']].iloc[0, 5:].values.tolist()

                labels = ['ProgressivePasses', 'Tackles', 'Interceptions', 'xG']
                fig = create_radar_chart(p1_stats, p2_stats, labels)
                st.plotly_chart(fig, use_container_width=True)

# --- PAGE 4: TACTICAL ANALYTICS ---
elif page == "📈 Tactical Analytics":
    st.title("Tactical Analytics")
    st.markdown("Deep dive into the clustering distributions.")

    role = st.selectbox("Select Role to Analyze", df_clustered['TacticalRole'].unique())
    role_data = df_clustered[df_clustered['TacticalRole'] == role]

    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"{role} Distribution")
        st.bar_chart(role_data['MarketValue'])
    with col2:
        st.subheader("Role Characteristics")
        st.write(f"The {role} profile is characterized by specific distributions in the scaled feature space.")
        st.dataframe(role_data[['Player', 'MarketValue', 'League']])
