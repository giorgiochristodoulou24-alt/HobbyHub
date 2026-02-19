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
# CUSTOM CSS
# -------------------------------------------------
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 1rem;
            max-width: 1000px;
        }

        .header-container {
            display: flex;
            align-items: center;
            gap: 25px;
            margin-bottom: 10px;
        }

        .title {
            font-size: 70px;
            font-weight: 700;
            margin: 0;
            line-height: 1;
        }

        .subtitle {
            font-size: 28px;
            font-weight: 500;
            margin-top: 10px;
            color: inherit;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER SECTION
# -------------------------------------------------
st.markdown('<div class="header-container">', unsafe_allow_html=True)

logo_path = "Logo.png"

if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=105)  # 1.5x visual proportion relative to large title

st.markdown('<div>', unsafe_allow_html=True)
st.markdown('<div class="title">HobbyHub</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Discover hobbies. Explore passions.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

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
