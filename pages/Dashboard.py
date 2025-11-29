
import streamlit as st

st.title("📊 Dashboard")


import streamlit as st
import pandas as pd
from utils.ticket_db import list_tickets
from utils.style import comic_style

# =====================================
# ⚙️ Page Settings — Hilangkan Sidebar
# =====================================
st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
# 📊 DASHBOARD CONTENT
# =====================================
st.title("📢 Dashboard Incident ")

tickets = list_tickets()

# ------- Card Comic Wrapper -------
st.markdown('<div class="card-comic">', unsafe_allow_html=True)
st.subheader("Ringkasan Tiket")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total", len(tickets))
col2.metric("Open", sum(t['status'] == "New" for t in tickets))
col3.metric("Progress", sum(t['status'] == "In Progress" for t in tickets))
col4.metric("Critical", sum(t['severity'] == "Critical" for t in tickets))

st.markdown('</div>', unsafe_allow_html=True)

# =====================================
# 📈 Chart Severity
# =====================================
if len(tickets) > 0:
    df = pd.DataFrame(tickets)
    st.subheader("📊 Grafik Severity")
    st.bar_chart(df["severity"].value_counts())
else:
    st.info("Belum ada tiket.")
