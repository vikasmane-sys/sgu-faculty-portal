import streamlit as st

st.set_page_config(
    page_title="SGU Examination ERP",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- CSS ----------
st.markdown("""
<style>
    .stApp {
        background: #020617;
    }

    header {
        visibility: hidden;
    }

    .main-container {
        min-height: 90vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .login-box {
        width: 100%;
        max-width: 1050px;
        min-height: 600px;
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 24px;
        overflow: hidden;
        box-shadow: 0 25px 60px rgba(0,0,0,0.45);
    }

    .brand-section {
        background: linear-gradient(145deg, #0f172a, #111827);
        padding: 55px;
        min-height: 600px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .brand-title {
        color: white;
        font-size: 32px;
        font-weight: 900;
        line-height: 1.15;
        margin-top: 25px;
    }

    .brand-subtitle {
        color: #cbd5e1;
        font-size: 16px;
        line-height: 1.7;
        margin-top: 20px;
    }

    .feature {
        color: #cbd5e1;
        font-size: 14px;
        margin-top: 12px;
    }

    .login-section {
        padding: 55px;
        background: #0f172a;
    }

    .login-title {
        color: white;
        font-size: 30px;
        font-weight: 900;
    }

    .login-subtitle {
        color: #94a3b8;
        margin-top: 8px;
    }

    .role-title {
        color: #cbd5e1;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    div[data-testid="stButton"] button {
        width: 100%;
        border-radius: 12px;
        min-height: 48px;
        font-weight: 800;
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 12px;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)


# ---------- Logo ----------
# सुरुवातीच्या demo साठी SGU text logo.
# Actual embedded SGU logo आपण पुढच्या step मध्ये तुमच्या existing
# SGULogo code मधून घेऊ.
logo_html = """
<div style="
    width:90px;
    height:100px;
    border-radius:20px;
    background:rgba(59,130,246,0.12);
    border:1px solid rgba(96,165,250,0.35);
    display:flex;
    align-items:center;
    justify-content:center;
    color:#60a5fa;
    font-size:28px;
    font-weight:900;">
    SGU
</div>
"""


# ---------- Login State ----------
if "login_role" not in st.session_state:
    st.session_state.login_role = "Faculty"


# ---------- Page ----------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

left, right = st.columns([1, 1], gap="large")

# ---------- LEFT ----------
with left:
    st.markdown('<div class="brand-section">', unsafe_allow_html=True)

    st.markdown(logo_html, unsafe_allow_html=True)

    st.markdown("""
    <div class="brand-title">
        SANJAY GHODAWAT<br>
        UNIVERSITY
    </div>

    <div style="
        display:inline-block;
        margin-top:10px;
        padding:5px 10px;
        border-radius:6px;
        background:rgba(245,158,11,0.10);
        border:1px solid rgba(245,158,11,0.35);
        color:#fbbf24;
        font-size:11px;
        font-weight:800;
        letter-spacing:1px;">
        KOLHAPUR
    </div>

    <div class="brand-subtitle">
        Examination Department ERP
    </div>

    <div class="feature">✓ Paper Setting Order Management</div>
    <div class="feature">✓ Faculty Portal</div>
    <div class="feature">✓ Remuneration Bill Management</div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- RIGHT ----------
with right:
    st.markdown('<div class="login-section">', unsafe_allow_html=True)

    st.markdown(
        '<div class="login-title">ERP Login</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="login-subtitle">'
        'Sanjay Ghodawat University Examination Department'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown('<div class="role-title">Login Type</div>', unsafe_allow_html=True)

    role = st.selectbox(
        "Login Type",
        ["Faculty", "Admin"],
        label_visibility="collapsed"
    )

    st.write("")

    login_id = st.text_input(
        "Login ID",
        placeholder="Enter Login ID"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter Password"
    )

    st.write("")

    if st.button("Login", type="primary", use_container_width=True):
        if not login_id or not password:
            st.error("Please enter Login ID and Password.")
        else:
            st.info(
                f"{role} login demo is ready. "
                "Actual authentication will be connected in the next step."
            )

    st.markdown(
        '<div class="footer">'
        'Sanjay Ghodawat University • Examination Department'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
