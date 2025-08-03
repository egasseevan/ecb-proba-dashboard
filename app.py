import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.title("Probabilités Banques Centrales")

# Données réelles septembre ECB 2025
data = {
    "Scenario": ["Hold", "Cut -25bps"],
    "Target_Rate_bps": [200, 175],
    "Probability": [78.7, 21.3]
}

df = pd.DataFrame(data)

cme_blue = "#4A90E2"

fig = go.Figure()

for i, row in df.iterrows():
    fig.add_trace(go.Bar(
        x=[row["Target_Rate_bps"]],
        y=[row["Probability"]],
        marker_color=cme_blue,
        text=[f"{row['Probability']:.1f}%"],
        textposition="outside",
        textfont=dict(color="black", size=14),
        hovertemplate=f"Target Rate: {row['Target_Rate_bps']} bps<br>Probability: {row['Probability']:.1f}%",
        showlegend=False
    ))

fig.update_layout(
    title=dict(
        text="Target Rate Probabilities for 11 Sept. 2025 ECB Meeting",
        x=0.03,
        y=0.99,
        xanchor="left",
        yanchor="top",
        font=dict(size=14, color="black")
    ),
    plot_bgcolor="white",
    width=1000,
    height=600,
    margin=dict(t=60, l=80, r=80, b=120),  # marge inférieure plus grande pour le texte
    xaxis=dict(
        title="Target Rate (in bps)",
        tickmode='array',
        tickvals=df["Target_Rate_bps"],
        ticktext=[str(t) for t in df["Target_Rate_bps"]],
        showgrid=False,
        zeroline=False,
        linecolor="black",
        mirror=False,
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
        mirror=False,
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
    text="Current target rate is 200",
    xref="paper", yref="y",
    x=0.5, y=103,
    showarrow=False,
    font=dict(size=12, color="black"),
    xanchor='center',
    yanchor='bottom'
)

fig.add_annotation(
    text="ECB Watch Tool Data from: 2025-07-31",
    xref="paper", yref="paper",
    x=1, y=-0.18,  # très bas sous le graphique
    showarrow=False,
    font=dict(size=10, color="gray"),
    xanchor='right',
    yanchor='top',
    opacity=0.6
)

st.plotly_chart(fig, use_container_width=True)
