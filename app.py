import streamlit as st
import plotly.graph_objs as go

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Global Central Bank Watch",
    page_icon="📊",
    layout="wide"
)

# -------------------- SIDEBAR --------------------
st.sidebar.title("🌍 Navigation Globale")
bc_list = [
    "🇺🇸 Fed",
    "🇪🇺 BCE",
    "🇬🇧 BoE",
    "🇯🇵 BoJ",
    "🇨🇦 BoC",
    "🇦🇺 RBA",
    "🇳🇿 RBNZ",
    "🇨🇭 SNB"
]
selected_bc = st.sidebar.radio("Choisis une Banque Centrale :", bc_list)

# -------------------- HEADER --------------------
st.title("📈 G8 Central Bank Macro Dashboard")
st.markdown("---")
st.markdown(f"### Focus : {selected_bc}")

# -------------------- FAKE TABS FOR MEETINGS --------------------
meeting_tabs = ["🗓️ Prochaine Réunion", "📉 Scénarios Décembre", "📊 Taux Implicites", "🧠 Repricing", "📁 Notes"]
selected_tab = st.selectbox("Navigation Réunionnelle", meeting_tabs, key="meeting")

# -------------------- DYNAMIC CONTENT --------------------
if selected_tab == "🗓️ Prochaine Réunion":
    st.subheader("🗓️ Détail de la prochaine réunion")
    st.markdown("- Date : 18 septembre 2025\n- Probabilité de mouvement : 62.5%\n- Consensus : Cut de 25bps")

elif selected_tab == "📉 Scénarios Décembre":
    st.subheader("📉 Scénarios pour Décembre 2025")
    st.markdown("**Taux actuel :** 5.25%\n\n- 🔴 Aucun cut (5.25%) → 20%\n- 🟡 Un cut (5.00%) → 40%\n- 🟢 Deux cuts (4.75%) → 30%\n- 🔵 Trois cuts (4.50%) → 10%")

elif selected_tab == "📊 Taux Implicites":
    st.subheader("📊 Graphique des Taux Implicites")

    # Fake data for plot
    meetings = ["Août", "Sept", "Oct", "Nov", "Déc"]
    rates = [5.27, 5.20, 5.15, 5.00, 4.85]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meetings, y=rates, mode='lines+markers', name='Taux Implicite'))
    fig.update_layout(title="Évolution des Taux Implicites", yaxis_title="%", xaxis_title="Réunion")

    st.plotly_chart(fig, use_container_width=True)

elif selected_tab == "🧠 Repricing":
    st.subheader("🧠 Repricing récent des attentes")
    st.markdown("> Depuis les derniers chiffres de l'emploi, le marché a intégré +32.5 bps de cut sur les 3 prochaines réunions.\n\nLe pivot anticipé est avancé de 1 mois.")

elif selected_tab == "📁 Notes":
    st.subheader("📁 Notes et commentaires fondamentaux")
    st.text_area("📝 Observations", "La Fed reste data dependent. Les risques restent équilibrés mais la faiblesse de la croissance pourrait accélérer le cycle de détente.", height=200)

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("Made with ❤️ for macro traders | Powered by Streamlit")
