

import streamlit as st
import pandas as pd
from utils.ticket_db import list_tickets
from utils.style import comic_style

# =====================================
# 🎨 Apply Comic Style
# =====================================
st.markdown(comic_style, unsafe_allow_html=True)

# =====================================
# 🧭 Floating Navbar
# =====================================
st.markdown("""
<div class="navbar-floating">
    <a href="/?nav=dashboard">Dashboard</a>
    <a href="/?nav=create">Create Ticket</a>
    <a href="/?nav=queue">Ticket Queue</a>
    <a href="/?nav=reports">Reports</a>
</div>
""", unsafe_allow_html=True)

# =====================================
# 📊 REPORT CONTENT
# =====================================
st.title("📈 Laporan & Statistik ")

tickets = list_tickets()

if len(tickets) == 0:
    st.warning("Belum ada data laporan.")
else:
    df = pd.DataFrame(tickets)

    # ------- Card Comic Wrapper -------
    st.markdown('<div class="card-comic">', unsafe_allow_html=True)
    st.subheader("Grafik per Severity")
    st.bar_chart(df["severity"].value_counts())
    st.markdown('</div>', unsafe_allow_html=True)

    # Tambahan grafik baru biar lebih keren
    st.markdown('<div class="card-comic">', unsafe_allow_html=True)
    st.subheader("Grafik Status Tiket")
    st.bar_chart(df["status"].value_counts())
    st.markdown('</div>', unsafe_allow_html=True)

    # Tambahkan tabel ringkas
    st.markdown('<div class="card-comic">', unsafe_allow_html=True)
    st.subheader("Ringkasan Laporan Tiket")
    st.dataframe(df)
    st.markdown('</div>', unsafe_allow_html=True)
