import streamlit as st
from utils.style import cyber_style, comic_style

st.set_page_config(
    page_title="CyberSOC",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject CSS
st.markdown(cyber_style, unsafe_allow_html=True)
st.markdown(comic_style, unsafe_allow_html=True)

# TITLE UTAMA
st.title("⚡ CyberSOC Incident Platform")
st.write("Selamat datang di platform monitoring insiden keamanan yang modern & responsif.")

# NAVBAR HTML (dekoratif)
st.markdown("""
<div class="navbar-floating">
    <a href="/Dashboard">Dashboard</a>
    <a href="/Create_Ticket">Create Ticket</a>
    <a href="/Ticket_Queue">Ticket Queue</a>
    <a href="/Reports_SLA">Reports</a>
</div>
""", unsafe_allow_html=True)
