import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import io

st.set_page_config(page_title="Probabilités Banques Centrales", layout="wide")

st.title("📊 Probabilités Banques Centrales - Dashboard Interactif")

# --- Données structurées par banque centrale et réunion ---
data_dict = {
    "ECB": {
        "Septembre 2025": {
            "Scenario": ["Hold", "Cut -25bps"],
            "Target_Rate_bps": [200, 175],
            "Probability": [78.7, 21.3],
            "Date": "2025-07-31"
        },
        "Octobre 2025": {
            "Scenario": ["Hold", "Cut -25bps"],
            "Target_Rate_bps": [200, 175],
            "Probability": [70.0, 30.0],
            "Date": "2025-08-15"
        }
    },
    "Fed": {
        "Septembre 2025": {
            "Scenario": ["Hold", "Cut -25bps", "Cut -50bps"],
            "Target_Rate_bps": [525, 500, 475],
            "Probability": [60, 30, 10],
            "Date": "2025-07-30"
        }
    },
    "BoE": {
        "Septembre 2025": {
            "Scenario": ["Hold", "Cut -25bps"],
            "Target_Rate_bps": [450, 425],
            "Probability": [65, 35],
            "Date": "2025-07-29"
        }
    }
}

# --- Sidebar pour choix utilisateur ---
st.sidebar.header("🔧 Choix Utilisateur")

bc_choice = st.sidebar.selectbox("Choisissez la Banque Centrale", list(data_dict.keys()))
meeting_choice = st.sidebar.selectbox("Choisissez la réunion", list(data_dict[bc_choice].keys()))

# --- Chargement des données selon choix ---
data = data_dict[bc_choice][meeting_choice]
df = pd.DataFrame({
    "Scenario": data["Scenario"],
    "Target_Rate_bps": data["Target_Rate_bps"],
    "Probability": data["Probability"]
})

date_source = data["Date"]

# --- Couleur principale ---
cme_blue = "#4A90E2"

# --- Création du graphique ---
fig = go.Figure()

for i, row in df.iterrows():
    fig.add_trace(go.Bar(
        x=[row["Target_Rate_bps"]],
        y=[row["Probability"]],
        marker_color=cme_blue,
        text=[f"{row['Probability']:.1f}%"],
        textposition="outside",
        textfont=dict(color="black", size=14),
        hovertemplate=(
            f"Scenario: {row['Scenario']}<br>"
            f"Target Rate: {row['Target_Rate_bps']} bps<br>"
            f"Probability: {row['Probability']:.1f}%"
        ),
        showlegend=False
    ))

fig.update_layout(
    title=dict(
        text=f"Target Rate Probabilities for {meeting_choice} {bc_choice} Meeting",
        x=0.03,
        y=0.99,
        xanchor="left",
        yanchor="top",
        font=dict(size=16, color="black")
    ),
    plot_bgcolor="white",
    width=900,
    height=600,
    margin=dict(t=80, l=80, r=80, b=140),
    xaxis=dict(
        title="Target Rate (in bps)",
        tickmode='array',
        tickvals=df["Target_Rate_bps"],
        ticktext=[str(t) for t in df["Target_Rate_bps"]],
        showgrid=False,
        zeroline=False,
        linecolor="black",
        ticks="outside",
        showline=True,
        side='bottom',
    ),
    yaxis=dict(
        title="Probability",
        title_standoff=20,
        range=[0, 110],
        showgrid=True,
        gridcolor="lightgray",
        griddash="dot",
        gridwidth=1,
        zeroline=False,
        dtick=20,
        tickvals=[0, 20, 40, 60, 80, 100],
        ticktext=["0%", "20%", "40%", "60%", "80%", "100%"],
        linecolor="black",
        ticks="outside",
        showline=True,
        side='left',
    ),
    bargap=0.4,
    showlegend=False,
    shapes=[
        dict(
            type="line",
            xref="paper",
            x0=0, x1=1,
            yref="y",
            y0=100, y1=100,
            line=dict(color="lightgray", width=1, dash="dot"),
            layer="below"
        )
    ]
)

fig.add_annotation(
    text=f"Current target rate is {df['Target_Rate_bps'].max()}",
    xref="paper", yref="y",
    x=0.5, y=103,
    showarrow=False,
    font=dict(size=12, color="black"),
    xanchor='center',
    yanchor='bottom'
)

fig.add_annotation(
    text=f"Data source date: {date_source}",
    xref="paper", yref="paper",
    x=1, y=-0.18,
    showarrow=False,
    font=dict(size=10, color="gray"),
    xanchor='right',
    yanchor='top',
    opacity=0.6
)

st.plotly_chart(fig, use_container_width=True)

# --- Affichage d'un tableau résumé ---
st.markdown("### 📋 Tableau des Probabilités")

# Préparation du tableau avec colonnes formatées
table_df = df.copy()
table_df["Probability"] = table_df["Probability"].map(lambda x: f"{x:.1f}%")
table_df = table_df.rename(columns={
    "Scenario": "SCENARIO",
    "Target_Rate_bps": "TARGET RATE (bps)",
    "Probability": "PROBABILITY (%)"
})

st.dataframe(table_df.style.format({
    "TARGET RATE (bps)": "{:.0f}",
    "PROBABILITY (%)": "{}"
}).set_properties(**{
    'text-align': 'center',
    'font-size': '14px'
}))

# --- Téléchargement CSV ---
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Télécharger les données CSV",
    data=csv,
    file_name=f"{bc_choice}_{meeting_choice}_probabilities.csv",
    mime="text/csv"
)

# --- Téléchargement PNG ---
import tempfile
import os
from PIL import Image

def fig_to_png_bytes(fig):
    img_bytes = fig.to_image(format="png")
    return img_bytes

png_bytes = fig_to_png_bytes(fig)

st.download_button(
    label="⬇️ Télécharger le graphique PNG",
    data=png_bytes,
    file_name=f"{bc_choice}_{meeting_choice}_chart.png",
    mime="image/png"
)

# --- Section infos/détails ---
with st.expander("ℹ️ Plus d'informations sur les données"):
    st.markdown(f"""
    - **Banque Centrale:** {bc_choice}  
    - **Réunion sélectionnée:** {meeting_choice}  
    - **Date de mise à jour des données:** {date_source}  
    - Ce dashboard affiche les probabilités implicites des décisions de taux à venir  
    - Les données sont extraites du ECB Watch Tool, Fed Watch Tool, ou autres sources officielles selon la banque centrale  
    - Ce projet est open-source et peut être adapté pour intégrer plus de banques centrales et réunions
    """)

