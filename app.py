import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="MacroCentral - Central Bank Dashboard",
    layout="wide",
    page_icon="📊"
)

# === Styles CSS propres ===
st.markdown("""
    <style>
    .css-18e3th9 {padding-top: 1rem; padding-bottom: 1rem;}
    .block-container {padding-left: 2rem; padding-right: 2rem;}
    </style>
""", unsafe_allow_html=True)

# === Sidebar navigation ===
st.sidebar.title("Banques Centrales - G8")
bank_choice = st.sidebar.radio(
    "Choisissez une banque centrale",
    ("🇺🇸 Fed", "🇪🇺 BCE", "🇬🇧 BoE", "🇯🇵 BoJ", "🇨🇦 BoC", "🇨🇭 SNB", "🇦🇺 RBA", "🇳🇿 RBNZ")
)

# === Données d’exemple pour chaque BC ===
data_store = {
    "🇺🇸 Fed": {
        "2025-09-17": {"Hold": 35, "Cut 25bps": 55, "Cut 50bps": 10},
        "2025-11-05": {"Hold": 30, "Cut 25bps": 60, "Cut 50bps": 10},
        "2025-12-17": {"Hold": 20, "Cut 25bps": 70, "Cut 50bps": 10},
    },
    "🇪🇺 BCE": {
        "2025-09-11": {"Hold": 78.7, "Cut 25bps": 21.3},
        "2025-10-23": {"Hold": 65, "Cut 25bps": 35},
        "2025-12-11": {"Hold": 50, "Cut 25bps": 50},
    },
    "🇬🇧 BoE": {
        "2025-09-03": {"Hold": 70, "Cut 25bps": 30},
        "2025-11-05": {"Hold": 60, "Cut 25bps": 40},
        "2025-12-17": {"Hold": 55, "Cut 25bps": 45},
    },
    # Tu peux compléter les autres banques ici avec la même structure
}

# === Affichage titre et intro ===
st.title("MacroCentral – Probabilités Banques Centrales du G8")
st.markdown("""
Bienvenue sur MacroCentral, votre dashboard de suivi en temps réel des probabilités implicites  
des décisions de politique monétaire des principales banques centrales mondiales.  
Sélectionnez une banque centrale et une réunion pour afficher les scénarios et leurs probabilités.
""")

# === Choix de la réunion ===
meetings = list(data_store[bank_choice].keys())
selected_meeting = st.selectbox("Sélectionnez une réunion", meetings)

# === Préparation données pour Plotly ===
scenarios = list(data_store[bank_choice][selected_meeting].keys())
probas = list(data_store[bank_choice][selected_meeting].values())

df = pd.DataFrame({
    "Scenario": scenarios,
    "Probability": probas
})

# === Plotly Bar chart ===
cme_blue = "#4A90E2"

fig = go.Figure()
for i, row in df.iterrows():
    fig.add_trace(go.Bar(
        x=[row["Scenario"]],
        y=[row["Probability"]],
        marker_color=cme_blue,
        text=[f"{row['Probability']:.1f}%"],
        textposition="outside",
        textfont=dict(color="black", size=14),
        hovertemplate=f"{row['Scenario']}<br>Probability: {row['Probability']:.1f}%",
        showlegend=False
    ))

fig.update_layout(
    title=f"Probabilités pour la réunion du {selected_meeting} - {bank_choice}",
    plot_bgcolor="white",
    yaxis=dict(
        title="Probabilité (%)",
        range=[0, 110],
        showgrid=True,
        gridcolor="lightgray",
        griddash="dot",
        gridwidth=1,
        dtick=20,
        tickvals=[0, 20, 40, 60, 80, 100],
        ticktext=["0%", "20%", "40%", "60%", "80%", "100%"],
        linecolor="black",
        ticks="outside",
        showline=True,
    ),
    xaxis=dict(
        title="Scenario",
        showgrid=False,
        zeroline=False,
        linecolor="black",
        ticks="outside",
        showline=True,
    ),
    bargap=0.4,
    margin=dict(t=60, b=80),
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# === Footer ===
st.markdown("---")
st.markdown("<center>© 2025 MacroCentral — Built for professional traders</center>", unsafe_allow_html=True)
