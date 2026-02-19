import streamlit as st
from PIL import Image
import os

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="HobbyHub",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# CLEAN UI + CUSTOM HEADER CONTROL
# -------------------------------------------------
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 1100px;
        }

        .header-row {
            display: flex;
            align-items: flex-start;
            gap: 30px;
        }

        .logo-wrapper img {
            margin-top: -20px;   /* Pull logo upward */
        }

        .title {
            font-size: 85px;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 5px;
        }

        .subtitle {
            font-size: 32px;
            font-weight: 600;
            margin-top: 0;
        }

        .divider-adjust {
            margin-top: -10px;  /* Pull divider closer */
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER SECTION
# -------------------------------------------------

logo_path = "Logo.png"

col_logo, col_text = st.columns([2, 6], vertical_alignment="top")

with col_logo:
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        st.markdown('<div class="logo-wrapper">', unsafe_allow_html=True)
        st.image(logo, width=260)  # Larger logo
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Logo.png not found.")

with col_text:
    st.markdown('<div class="title">HobbyHub</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Discover hobbies. Explore passions.</div>', unsafe_allow_html=True)

st.markdown('<div class="divider-adjust">', unsafe_allow_html=True)
st.divider()
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# CHAT SYSTEM
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask about hobbies...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = "That sounds interesting! Tell me more about what you enjoy."
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
