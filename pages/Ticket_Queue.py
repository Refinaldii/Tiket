

import streamlit as st
import pandas as pd
from utils.ticket_db import list_tickets
from utils.style import comic_style

# ============================
# ⚙️ Page Config — Hilangkan Sidebar
# ============================
st.set_page_config(
    page_title="Ticket Queue",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================
# 🎨 Apply Comic Theme
# ============================
st.markdown(comic_style, unsafe_allow_html=True)

# ============================
# 🧭 Floating Navbar
# ============================
st.markdown("""
<div class="navbar-floating">
    <a href="/?nav=dashboard">Dashboard</a>
    <a href="/?nav=create">Create Ticket</a>
    <a href="/?nav=queue">Ticket Queue</a>
    <a href="/?nav=reports">Reports</a>
</div>
""", unsafe_allow_html=True)

# ============================
# 📂 Ticket Queue
# ============================
st.title("📂 Daftar Tiket")

tickets = list_tickets()

# Comic card wrapper
st.markdown('<div class="card-comic">', unsafe_allow_html=True)

if len(tickets) == 0:
    st.info("Belum ada tiket.")
else:
    df = pd.DataFrame(tickets)

    # urutan kolom biar rapi
    preferred_cols = ["id", "title", "severity", "status", "assignee", "reporter", "asset", "summary"]
    df = df[[c for c in preferred_cols if c in df.columns]]

    st.subheader("📋 Semua Tiket")
    st.dataframe(df, use_container_width=True, height=450)

st.markdown('</div>', unsafe_allow_html=True)
