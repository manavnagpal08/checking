import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="AI Campus | ScreenerPro", layout="wide")

# ---------------------------- STYLES ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* Gradient Background */
.hero-section {
    background: linear-gradient(135deg, #fdfbff 0%, #f3f1ff 40%, #ffffff 100%);
    padding: 80px 0px;
    border-radius: 0px 0px 40px 40px;
}

/* Headline */
.hero-title {
    font-size: 54px;
    font-weight: 800;
    line-height: 1.2;
    color: #1f1f1f;
}

.ai-gradient {
    background: linear-gradient(90deg, #a855f7, #f4c763);
    -webkit-background-clip: text;
    color: transparent;
}

/* Subtext */
.hero-subtext {
    font-size: 18px;
    color: #5b5568;
    margin-top: 20px;
    max-width: 600px;
}

/* Buttons */
.btn-primary {
    display: inline-block;
    padding: 14px 28px;
    background: #facc15;
    border-radius: 25px;
    font-weight: 600;
    color: black;
    text-decoration: none;
}

.btn-outline {
    display: inline-block;
    padding: 14px 28px;
    border: 2px solid #d4d4d8;
    border-radius: 25px;
    font-weight: 600;
    color: #333;
    text-decoration: none;
}

/* Top Badge */
.top-badge {
    background: #ede9fe;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
    color: #6b21a8;
}

/* Right Side Circle Illustration Placeholder */
.circle-container {
    width: 480px;
    height: 480px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(148,107,255,0.4) 0%, rgba(235,228,255,0.1) 70%);
    display: flex;
    justify-content: center;
    align-items: center;
    border: 2px dotted #dcd2ff;
}

.circle-center {
    width: 180px;
    height: 180px;
    background: radial-gradient(circle, #ffffff, #e8ddff);
    border-radius: 30px;
    box-shadow: 0 0 30px rgba(140,82,255,0.25);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------- LAYOUT ----------------------------
hero = st.container()
with hero:
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("""<p class="top-badge">Built by IIT-Madras & TU Delft Alumni</p>""", unsafe_allow_html=True)

        st.markdown("""
        <h1 class="hero-title">
            Transform Your Institution<br>
            into an <span class="ai-gradient">AI Campus</span>
        </h1>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p class="hero-subtext">
        ScreenerPro empowers educational institutions with <strong>Intelligent Learning Infrastructure (ILI)</strong> 
        to personalize learning, enhance curriculum, reduce faculty workload, 
        and improve student outcomes via AI-powered analytics.
        </p>
        """, unsafe_allow_html=True)

        st.write("<br>", unsafe_allow_html=True)

        c1, c2 = st.columns([0.4, 0.6])
        with c1:
            st.markdown('<a class="btn-outline" href="#">Book a Demo</a>', unsafe_allow_html=True)
        with c2:
            st.markdown('<a class="btn-primary" href="#">Initiate Pilot</a>', unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="circle-container">
            <div class="circle-center"></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
