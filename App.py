import streamlit as st
from PIL import Image
import os

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="HobbyHub",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide default Streamlit menu + footer
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .main-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 75vh;
            text-align: center;
        }

        .logo-container {
            margin-bottom: 25px;
        }

        .title {
            font-size: 56px;
            font-weight: 600;
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 18px;
            color: #6e6e6e;
            margin-bottom: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# MAIN CENTERED CONTAINER
# -------------------------------------------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Load Logo
logo_path = "Logo.png"

if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image(logo, width=350)  # Larger logo
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning("Logo.png not found.")

# Title + Subtitle
st.markdown('<div class="title">HobbyHub</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Discover hobbies. Explore passions.</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# CHAT SECTION (Like ChatGPT)
# -------------------------------------------------

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input at bottom
prompt = st.chat_input("Ask about hobbies...")

if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simple placeholder response
    response = "That sounds interesting! Tell me more about what you enjoy."
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
