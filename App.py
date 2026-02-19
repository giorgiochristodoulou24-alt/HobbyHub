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
# CLEAN UI
# -------------------------------------------------
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .block-container {
            padding-top: 1rem;
            max-width: 1300px;
        }

        .title {
            font-size: 95px;
            font-weight: 800;
            line-height: 0.95;
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 36px;
            font-weight: 600;
            margin-top: 0;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER LAYOUT (WIDER + BALANCED)
# -------------------------------------------------

logo_path = "Logo.png"

# Much more space given to logo column
col_logo, col_text = st.columns([3, 7], vertical_alignment="center")

with col_logo:
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        st.image(logo, width=350)  # SIGNIFICANTLY larger
    else:
        st.warning("Logo.png not found.")

with col_text:
    st.markdown('<div class="title">HobbyHub</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Discover hobbies. Explore passions.</div>', unsafe_allow_html=True)

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
