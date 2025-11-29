import streamlit as st
from utils.ticket_db import get_ticket, add_comment, COMMENTS, list_tickets
from utils.style import comic_style

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
# 🔍 Ticket Detail Content
# ============================
st.title("🔍 Detail Tiket ")

# ============================
# 🔽 Ganti Text Input Jadi Dropdown
# ============================
all_tickets = list_tickets()

if len(all_tickets) == 0:
    st.warning("Belum ada tiket.")
    st.stop()

# Contoh tampilan:
# "Budi — Server Down (ID: a91233aa)"
ticket_options = {
    f"{t['reporter']} — {t['title']} (ID: {t['id']})": t['id']
    for t in all_tickets
}

selected_label = st.selectbox("Pilih Tiket", list(ticket_options.keys()))

ticket_id = ticket_options[selected_label]

# Ambil datanya
t = get_ticket(ticket_id)

# ============================
# 🔍 Tampilkan Detail Tiket
# ============================
if not t:
    st.error("❌ Tiket tidak ditemukan")
else:
    st.markdown('<div class="card-comic">', unsafe_allow_html=True)

    # ============================
    # 📝 Header Detail
    # ============================
    st.subheader(f"{t['title']} — (ID: {t['id']})")

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Severity: **{t['severity']}**")
        st.write(f"Asset: **{t['asset']}**")
    with col2:
        st.write(f"Assignee: **{t['assignee']}**")
        st.write(f"Reporter: **{t['reporter']}**")

    st.markdown("---")

    # ============================
    # 💬 Add Comment
    # ============================
    st.subheader("Tambah Komentar")

    comment = st.text_area("Komentar")

    if st.button("💬 Tambah Komentar", key="addc"):
        if comment.strip() == "":
            st.warning("Komentar tidak boleh kosong!")
        else:
            add_comment(ticket_id, "Analyst", comment)
            st.success("Komentar berhasil ditambahkan!")

    st.markdown("---")

    # ============================
    # 📜 Comment Timeline
    # ============================
    st.subheader("Timeline Komentar")

    if ticket_id not in COMMENTS or len(COMMENTS[ticket_id]) == 0:
        st.info("Belum ada komentar.")
    else:
        for c in COMMENTS[ticket_id]:
            st.markdown(f"""
            <div style="
                background: white;
                border: 3px solid black;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                box-shadow: 5px 5px 0px #000;
            ">
                <b>{c['author']}</b> — <i>{c['at']}</i>
                <br/>
                {c['text']}
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
