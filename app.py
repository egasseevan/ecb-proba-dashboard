import streamlit as st
import plotly.graph_objects as go
import datetime

# Config générale
st.set_page_config(
    page_title="ECB Repricing Dashboard",
    page_icon="💶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# 🎨 CSS Custom Pro
st.markdown("""
    <style>
        body {
            background-color: #0F1117;
            color: #FFFFFF;
        }
        .block-container {
            padding-top: 2rem;
        }
        .sidebar .sidebar-content {
            background-color: #1C1F26;
        }
        h1, h2, h3 {
            color: #4A90E2 !important;
        }
        .stButton>button {
            background-color: #4A90E2;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# 📊 Données fictives pour le graphique
x = ['Septembre', 'Octobre', 'Décembre']
y = [1.9973, 1.9923, 1.9475]

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name='Taux implicites BCE', line=dict(color='#4A90E2', width=3)))

fig.update_layout(
    title="Repricing BCE par échéance",
    xaxis_title="Réunions",
    yaxis_title="Taux Implicites",
    template="plotly_dark",
    paper_bgcolor="#0F1117",
    plot_bgcolor="#0F1117",
    font=dict(color="white")
)

# -------------------------------
# 📋 SIDEBAR - Infos contextuelles
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/5/5e/ECB_logo.svg", width=150)
st.sidebar.markdown("### Dashboard BCE")
st.sidebar.write("Ce tableau suit le **repricing implicite** sur les futures de la Banque Centrale Européenne.")

with st.sidebar.expander("ℹ️ À propos"):
    st.write("""
    Créé par Evan E.
    - Données macro simulées
    - Affichage professionnel
    - Prochainement : intégration réelle via API STIR ou futures EUREX
    """)

# -------------------------------
# 📈 Affichage principal
st.title("📊 ECB Repricing Dashboard")
st.markdown("#### Taux implicites par réunion monétaire (calculés depuis les futures)")

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# 📰 Bloc Data économique récente
st.markdown("### Dernières publications macro 📅")
st.info("🇪🇺 Inflation Core : 2.9% (en baisse)\n\n🇩🇪 PMI Manufacturier : 42.3 (faible)\n\n🇫🇷 Taux de chômage : 7.1%")

# -------------------------------
# 📆 Footer
st.markdown("---")
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("<p style='text-align:center;'>Fait avec ❤️ par Evan — 2025 | <a style='color:#4A90E2;' href='https://github.com/tonrepo'>GitHub</a></p>", unsafe_allow_html=True)
