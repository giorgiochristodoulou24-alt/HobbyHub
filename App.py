import streamlit as st
from PIL import Image
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="HobbyHub",
    page_icon="🎮",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS (Center Everything)
# -----------------------------
st.markdown("""
    <style>
        .centered {
            text-align: center;
        }
        .logo-container {
            display: flex;
            justify-content: center;
            margin-top: 40px;
        }
        .title {
            text-align: center;
            font-size: 60px;
            font-weight: 700;
            margin-top: 20px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: gray;
            margin-bottom: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD LOGO SAFELY
# -----------------------------
logo_path = "Logo.png"

if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image(logo, width=300)  # 🔥 Bigger Logo
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning("Logo.png not found in project folder.")

# -----------------------------
# TITLE SECTION
# -----------------------------
st.markdown('<div class="title">HobbyHub</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Discover hobbies. Explore passions.</div>', unsafe_allow_html=True)

# -----------------------------
# CHAT INPUT
# -----------------------------
user_input = st.chat_input("Ask about hobbies...")

if user_input:
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(
        "That's awesome! Tell me more about what you're interested in!"
    )
