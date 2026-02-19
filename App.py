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
# CUSTOM CSS (ChatGPT Style Layout)
# -------------------------------------------------
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .block-container {
            padding-top: 2rem;
            padding-bottom: 1rem;
            max-width: 900px;
        }

        .top-bar {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 10px;
        }

        .title {
            font-size: 40px;
            font-weight: 600;
            margin: 0;
        }

        .subtitle {
            font-size: 16px;
            color: #6e6e6e;
            margin-bottom: 25px;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER (Logo LEFT of Title)
# -------------------------------------------------
col1, col2 = st.columns([1, 8])

with col1:
    logo_path = "Logo.png"
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        st.image(logo, width=80)

with col2:
    st.markdown('<div class="title">HobbyHub</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">Discover hobbies. Explore passions.</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# CHAT SYSTEM
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input (stays at bottom automatically)
prompt = st.chat_input("Ask about hobbies...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = "That sounds interesting! Tell me more about what you enjoy."
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
