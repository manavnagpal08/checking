import streamlit as st

st.set_page_config(page_title="AI Campus", layout="wide")

# ----------------------- CSS EXACT MATCH -----------------------
st.markdown("""
<style>
/* GLOBAL */
body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* TOP FADED BAR */
.top-gradient {
    width: 100%;
    height: 180px;
    background: linear-gradient(180deg, #f8f6ff 0%, #f3f0ff 60%, rgba(255,255,255,0) 100%);
    border-radius: 0 0 40px 40px;
    margin-bottom: -80px;
}

/* BADGE */
.badge {
    display: inline-block;
    background: #ebe4ff;
    color: #4b2bb6;
    padding: 10px 25px;
    border-radius: 999px;
    font-weight: 600;
    font-size: 15px;
    margin-left: 40px;
}

/* MAIN HERO */
.hero-title {
    font-size: 50px;
    font-weight: 800;
    line-height: 1.15;
    margin-top: 30px;
    margin-left: 40px;
}

.ai-gradient {
    background: linear-gradient(90deg, #b06bff, #ffce64);
    -webkit-background-clip: text;
    color: transparent;
}

.hero-desc {
    font-size: 18px;
    color: #4b4b4b;
    max-width: 520px;
    margin-left: 40px;
    margin-top: 20px;
}

/* BUTTONS */
.btn-outline {
    display: inline-block;
    padding: 14px 30px;
    border: 2px solid #dcdcdc;
    border-radius: 35px;
    font-weight: 600;
    color: #1f1f1f;
    text-decoration: none;
    margin-left: 40px;
}

.btn-primary {
    display: inline-block;
    padding: 14px 30px;
    background: #ffd21f;
    border-radius: 35px;
    font-weight: 600;
    color: #1f1f1f;
    text-decoration: none;
    margin-left: 20px;
}

/* RIGHT SIDE ORBIT */
.orbit-wrapper {
    position: relative;
    width: 550px;
    height: 550px;
    margin-top: -30px;
}

.orbit-circle {
    width: 100%;
    height: 100%;
    border: 2px dotted #d9caff;
    border-radius: 50%;
    position: absolute;
    top: 0;
    right: 0;
}

/* GLOW BACKGROUND */
.glow {
    width: 450px;
    height: 450px;
    background: radial-gradient(circle, rgba(200,160,255,0.35), rgba(255,255,255,0));
    border-radius: 50%;
    position: absolute;
    top: 50px;
    right: 50px;
}

/* CENTER ROUNDED BOX */
.center-box {
    width: 180px;
    height: 180px;
    background: radial-gradient(circle, #ffffff, #ede3ff);
    border-radius: 30px;
    position: absolute;
    top: 185px;
    right: 185px;
    box-shadow: 0 0 60px rgba(160,110,255,0.25);
}
</style>
""", unsafe_allow_html=True)

# ------------------ TOP GRADIENT STRIP ------------------
st.markdown('<div class="top-gradient"></div>', unsafe_allow_html=True)

# ------------------ HERO SECTION ------------------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="badge">Built by IIT-Madras & TU Delft Alumni</div>', unsafe_allow_html=True)

    st.markdown("""
        <h1 class="hero-title">
            Transform Your Institution<br>
            into an <span class="ai-gradient">AI Campus</span>
        </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
        <p class="hero-desc">
        ScreenerPro empowers educational institutions with <b>Intelligent Learning Infrastructure (ILI)</b>
        to personalize learning, enhance curriculum, reduce faculty workload,
        and improve student outcomes via AI-powered analytics.
        </p>
    """, unsafe_allow_html=True)

    st.markdown("""
        <a href="#" class="btn-outline">Book a Demo</a>
        <a href="#" class="btn-primary">Initiate Pilot</a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="orbit-wrapper">
        <div class="orbit-circle"></div>
        <div class="glow"></div>
        <div class="center-box"></div>
    </div>
    """, unsafe_allow_html=True)
