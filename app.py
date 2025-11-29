import streamlit as st
from utils.style import cyber_style

st.set_page_config(
    page_title="CyberSOC",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(cyber_style, unsafe_allow_html=True)

st.title("⚡ CyberSOC Incident Platform")
st.write("Selamat datang di platform monitoring insiden keamanan yang modern & responsif.")

from utils.style import comic_style
import streamlit as st

st.markdown(comic_style, unsafe_allow_html=True)

st.markdown("""
<div class="navbar-floating">
    <a href="/?nav=dashboard">Dashboard</a>
    <a href="/?nav=create">Create Ticket</a>
    <a href="/?nav=queue">Ticket Queue</a>
    <a href="/?nav=reports">Reports</a>
</div>
""", unsafe_allow_html=True)
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

# === FLOATING AUTO-HIDE NAVBAR ===
st.markdown("""
<style>
/* Floating Top Navbar */
.navbar-floating {
    position: fixed;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(30, 30, 30, 0.9);
    padding: 12px 30px;
    border-radius: 12px;
    z-index: 9999;
    display: flex;
    gap: 25px;
    transition: top 0.4s ease;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.35);
}

/* Navbar items */
.navbar-floating a {
    color: #fff;
    text-decoration: none;
    font-weight: 600;
    font-size: 15px;
}

.navbar-floating a:hover {
    color: #00eaff;
}

/* Hidden state */
.navbar-hide {
    top: -70px !important;
}
</style>

<script>
let lastScroll = window.pageYOffset;

window.addEventListener("scroll", function() {
    let current = window.pageYOffset;
    let navbar = document.querySelector('.navbar-floating');

    if (!navbar) return;

    if (current > lastScroll) {
        // Scrolling down → hide
        navbar.classList.add("navbar-hide");
    } else {
        // Scrolling up → show
        navbar.classList.remove("navbar-hide");
    }
    lastScroll = current;
});
</script>

<div class="navbar-floating">
    <a href="/?nav=dashboard">Dashboard</a>
    <a href="/?nav=create">Create Ticket</a>
    <a href="/?nav=queue">Ticket Queue</a>
    <a href="/?nav=reports">Reports</a>
</div>
""", unsafe_allow_html=True)


