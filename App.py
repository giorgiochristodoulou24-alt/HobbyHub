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
# CLEAN STREAMLIT DEFAULT UI
# -------------------------------------------------
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .block-container {
            padding-top: 0.5rem;
            max-width: 1400px;
        }

        .title {
            font-size: 95px;
            font-weight: 800;
            line-height: 0.95;
            margin-bottom: 5px;
        }

        .subtitle {
            font-size: 36px;
            font-weight: 600;
            margin-top: 0;
        }

        /* Pull divider closer upward */
        .divider-adjust {
            margin-top: -25px;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER LAYOUT
# -------------------------------------------------

logo_path = "Logo.png"

col_logo, col_text = st.columns([4, 6], vertical_alignment="top")

with col_logo:
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)

        # Big enough to compensate for transparent padding
        st.image(logo, width=450)
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
