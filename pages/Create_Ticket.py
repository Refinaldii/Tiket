

import streamlit as st
from utils.ticket_db import create_ticket
from utils.style import comic_style

# ==============================
# ⚙️ Page Settings (Fix Sidebar)
# ==============================
st.set_page_config(
    page_title="Create Ticket",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# 🔥 Apply Comic Style
# ==============================
st.markdown(comic_style, unsafe_allow_html=True)

# ==============================
# 🧭 Floating Navbar
# ==============================
st.markdown("""
<div class="navbar-floating">
    <a href="/?nav=dashboard">Dashboard</a>
    <a href="/?nav=create">Create Ticket</a>
    <a href="/?nav=queue">Ticket Queue</a>
    <a href="/?nav=reports">Reports</a>
</div>
""", unsafe_allow_html=True)

# ==============================
# 📝 Create Ticket Form
# ==============================
st.title("📝 Create Ticket ")

st.markdown('<div class="card-comic">', unsafe_allow_html=True)

with st.form("newTicketForm"):
    title = st.text_input("Judul Incident")
    severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
    asset = st.text_input("Asset / Sistem")
    reporter = st.text_input("Reporter")
    assignee = st.text_input("Assign ke")
    summary = st.text_area("Deskripsi Kejadian")

    submitted = st.form_submit_button("🚀 Buat Tiket", use_container_width=True)

# ==============================
# 💾 Save to DB
# ==============================
if submitted:
    new_ticket = create_ticket({
        "title": title,
        "severity": severity,
        "asset": asset,
        "reporter": reporter,
        "assignee": assignee,
        "summary": summary
    })

    st.success(f"🎉 Tiket berhasil dibuat! ID: {new_ticket}")

st.markdown('</div>', unsafe_allow_html=True)
