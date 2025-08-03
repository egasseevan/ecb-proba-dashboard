import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.title("Probabilités Banques Centrales")

data = {
    "Scenario": ["Hold", "Cut -25bps"],
    "Target_Rate_bps": [200, 175],
    "Probability": [78.7, 21.3]
}

df = pd.DataFrame(data)

fig = go.Figure()

for i, row in df.iterrows():
    fig.add_trace(go.Bar(
        x=[row["Target_Rate_bps"]],
        y=[row["Probability"]],
        marker_color="#4A90E2",
        text=[f"{row['Probability']:.1f}%"],
        textposition="outside",
        textfont=dict(color="black", size=14),
        showlegend=False
    ))

fig.update_layout(
    title="Target Rate Probabilities for 11 Sept. 2025 ECB Meeting",
    plot_bgcolor="white",
    width=1000,
    height=600,
    margin=dict(t=60, l=80, r=80, b=120),
    xaxis=dict(title="Target Rate (in bps)"),
    yaxis=dict(title="Probability", range=[0, 110]),
    bargap=0.4
)

st.plotly_chart(fig)
