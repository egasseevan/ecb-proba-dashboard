import streamlit as st
import plotly.graph_objects as go

# CONFIG
st.set_page_config(page_title="ECB Rate Cut Probabilities", layout="wide")

# STYLE CSS
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        header, footer {visibility: hidden;}
        .title {
            font-size: 2.5rem;
            color: #1a1a1a;
            font-weight: 600;
        }
        .subtitle {
            color: #666;
            font-size: 1.1rem;
        }
        .stButton button {
            background-color: #0e1117;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1em;
        }
    </style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.title("🔧 Menu")
    st.markdown("Utilise ce menu pour naviguer")
    st.markdown("---")
    st.selectbox("Choisir une Banque Centrale", ["ECB", "Fed", "BoE", "BoJ"])
    st.selectbox("Période", ["Août", "Septembre", "Décembre"])
    st.button("🔄 Recalculer")

# HEADER
st.markdown('<div class="title">📊 ECB Rate Cut Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyse des probabilités de cut via les taux implicites</div>', unsafe_allow_html=True)
st.markdown("---")

# GRAPH PLACEHOLDER
st.subheader("Graphique interactif :")

fig = go.Figure()
fig.add_trace(go.Bar(
    x=["No Cut", "1 Cut", "2 Cuts", "3 Cuts"],
    y=[35, 40, 20, 5],
    marker_color=['#636EFA', '#EF553B', '#00CC96', '#AB63FA']
))
fig.update_layout(
    title="Probabilités intégrées par les marchés (Décembre)",
    xaxis_title="Scénarios",
    yaxis_title="Probabilité (%)",
    template="plotly_white",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# FOOTER
st.markdown("---")
st.markdown(
    "<center><small>© 2025 ECB Tracker | Made with ❤️ by Evan</small></center>",
    unsafe_allow_html=True
)
