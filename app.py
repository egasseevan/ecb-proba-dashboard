import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="MacroCentral - Central Bank Dashboard", layout="wide", page_icon="📊")

# CSS pour un menu horizontal custom
st.markdown("""
<style>
    /* Barre de menu horizontale */
    .menu {
        display: flex;
        justify-content: center;
        gap: 30px;
        padding: 1rem 0 1rem 0;
        background-color: #f8f9fa;
        border-bottom: 1px solid #ddd;
    }
    .menu button {
        background: none;
        border: none;
        padding: 0.5rem 1rem;
        font-size: 16px;
        cursor: pointer;
        color: #4A90E2;
        font-weight: 600;
        transition: color 0.3s ease;
    }
    .menu button:hover {
        color: #1E3A8A;
    }
    .menu .active {
        border-bottom: 3px solid #4A90E2;
        font-weight: 700;
        color: #1E3A8A;
    }
</style>
""", unsafe_allow_html=True)

# Liste des banques centrales
banks = ["Fed", "BCE", "BoE", "BoJ", "BoC", "SNB", "RBA", "RBNZ"]

# Gestion de la sélection avec session_state
if 'selected_bank' not in st.session_state:
    st.session_state.selected_bank = "Fed"

def select_bank(bank):
    st.session_state.selected_bank = bank

# Menu horizontal en header
cols = st.columns(len(banks))
for i, bank in enumerate(banks):
    if cols[i].button(bank):
        select_bank(bank)

# Style bouton actif (via markdown hack)
st.markdown(f"""
    <script>
    const buttons = window.parent.document.querySelectorAll('button[kind="secondary"]');
    buttons.forEach(btn => {{
        if(btn.textContent.trim() == '{st.session_state.selected_bank}') {{
            btn.classList.add('active');
        }} else {{
            btn.classList.remove('active');
        }}
    }});
    </script>
""", unsafe_allow_html=True)

st.write(f"### Banque centrale sélectionnée : {st.session_state.selected_bank}")

# Fake data (à remplacer par tes vraies datas)
data_store = {
    "Fed": {"Sept 2025": {"Hold": 35, "Cut 25bps": 55, "Cut 50bps": 10}},
    "BCE": {"Sept 2025": {"Hold": 78.7, "Cut 25bps": 21.3}},
    "BoE": {"Sept 2025": {"Hold": 70, "Cut 25bps": 30}},
    # Ajoute les autres banques ici...
}

meetings = list(data_store.get(st.session_state.selected_bank, {}).keys())
if meetings:
    selected_meeting = st.selectbox("Choisis une réunion", meetings)
    scenarios = list(data_store[st.session_state.selected_bank][selected_meeting].keys())
    probas = list(data_store[st.session_state.selected_bank][selected_meeting].values())

    df = pd.DataFrame({"Scenario": scenarios, "Probability": probas})

    # Plotly bar chart
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
            showlegend=False
        ))
    fig.update_layout(
        title=f"Probabilités {selected_meeting} - {st.session_state.selected_bank}",
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
        height=450
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Aucune donnée disponible pour cette banque centrale.")

# Footer
st.markdown("---")
st.markdown("<center>© 2025 MacroCentral — Professionnel & Propre</center>", unsafe_allow_html=True)
