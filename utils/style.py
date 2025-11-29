comic_style = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&family=Poppins:wght@600&display=swap');

html, body {
    font-family: 'Comic Neue', cursive !important;
    background: #f4f4f4;
}

/* === NAVBAR (floating + auto-hide support) === */
.navbar-floating {
    position: fixed !important;
    top: 15px;
    left: 50%;
    transform: translateX(-50%);
    
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(12px);
    
    padding: 14px 38px;
    border-radius: 20px;
    border: 3px solid #000;
    
    display: flex;
    gap: 28px;
    z-index: 9999;
    box-shadow: 6px 6px 0px #000;
    transition: top 0.45s ease;
}

/* auto-hide class */
.navbar-hide {
    top: -80px !important;
}

.navbar-floating a {
    text-decoration: none;
    font-weight: bold;
    color: #111;
    font-size: 18px;
    transition: 0.15s;
}

.navbar-floating a:hover {
    color: #ff9800;
    transform: scale(1.07);
}

/* Cards */
.card-comic {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border: 4px solid #000;
    box-shadow: 6px 6px 0px #000;
}

.comic-btn {
    background: #ffde59;
    border: 3px solid #000;
    padding: 10px 18px;
    font-weight: bold;
    border-radius: 12px;
    box-shadow: 4px 4px 0px #000;
    cursor: pointer;
}

.comic-btn:hover {
    background: #ffca24;
}

h1, h2, h3 {
    font-family: 'Poppins', sans-serif !important;
    font-weight: 700;
}

</style>
"""


# ================================
# 💠 CYBER STYLE (tema cyberpunk)
# ================================
cyber_style = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto:wght@300;400&display=swap');

html, body {
    font-family: 'Orbitron', sans-serif !important;
    background: radial-gradient(circle at top, #00f2ff, #00131a 60%, #00080d);
    color: #d1faff;
}

/* === CYBER NAVBAR (floating + auto-hide support) === */
.navbar-floating {
    position: fixed !important;
    top: 18px;
    left: 50%;
    transform: translateX(-50%);
    padding: 12px 32px;

    background: rgba(0, 255, 255, 0.10);
    border: 1px solid cyan;
    border-radius: 12px;

    backdrop-filter: blur(10px);
    box-shadow: 0 0 15px cyan;

    display: flex;
    gap: 28px;
    z-index: 9999;

    transition: top 0.45s ease;
}

/* auto-hide class */
.navbar-hide {
    top: -80px !important;
}

.navbar-floating a {
    color: cyan !important;
    font-size: 16px;
    text-decoration: none;
    font-weight: bold;
    transition: 0.2s;
}

.navbar-floating a:hover {
    color: #00e6ff !important;
    text-shadow: 0 0 7px cyan;
}

/* Cyber cards */
.cyber-card {
    background: rgba(0, 20, 30, 0.6);
    padding: 20px;
    border-radius: 14px;
    border: 1px solid cyan;
    box-shadow: 0 0 13px cyan;
}

/* Buttons */
.cyber-btn {
    background: cyan;
    color: #00272d;
    padding: 10px 16px;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 0 10px cyan;
}

.cyber-btn:hover {
    background: #00eaff;
}

</style>
"""
