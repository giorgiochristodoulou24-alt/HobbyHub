import streamlit as st
from PIL import Image
import os
import random

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="HobbyHub",
    page_icon="🎯",
    layout="wide",
)

# -------------------------------------------------
# LOAD DOCUMENTS
# -------------------------------------------------
def load_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""

PERSONALITY = load_file("Documents/personality.txt")
PROMPTS = load_file("Documents/prompts.txt").split("\n")

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
with st.sidebar:
    st.title("🎯 HobbyHub")

    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.write("Discover hobbies and explore new interests.")

# -------------------------------------------------
# CSS
# -------------------------------------------------
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
.block-container{padding-top:1rem; max-width:900px;}
.title{font-size:55px; font-weight:700;}
.subtitle{font-size:20px; color:gray;}
.logo-container{display:flex; align-items:center; gap:20px; margin-bottom:10px;}
.suggested{border:1px solid #e6e6e6; padding:14px; border-radius:12px; cursor:pointer;}
.suggested:hover{background:#f7f7f7;}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
logo_path = "Logo.png"
col_logo, col_text = st.columns([2,5])

with col_logo:
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        st.image(logo, width=450)

with col_text:
    st.markdown('<div class="title">HobbyHub</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Discover hobbies. Explore passions.</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# CHAT MEMORY
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------------------------
# SUGGESTED PROMPTS (ONLY IF CHAT EMPTY)
# -------------------------------------------------
if len(st.session_state.messages) == 0:
    st.write("### Start with one of these")
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    if col1.button("🎨 Suggest creative hobbies"):
        st.session_state.messages.append({"role":"user","content":"creative"})
    if col2.button("🏃 Suggest active hobbies"):
        st.session_state.messages.append({"role":"user","content":"active"})
    if col3.button("🎮 Suggest digital hobbies"):
        st.session_state.messages.append({"role":"user","content":"digital"})
    if col4.button("🧠 Hobbies that teach skills"):
        st.session_state.messages.append({"role":"user","content":"skills"})

# -------------------------------------------------
# STATIC RESPONSE FUNCTION
# -------------------------------------------------
def generate_reply(user_input):
    """
    Rule-based hobby suggestions.
    """
    user_input = user_input.lower()

    hobbies = {
        "creative": [
            "Painting 🎨",
            "Photography 📸",
            "Creative writing ✍️",
            "DIY crafts 🛠️",
            "Calligraphy 🖌️"
        ],
        "active": [
            "Running 🏃",
            "Cycling 🚴",
            "Hiking 🥾",
            "Yoga 🧘",
            "Martial arts 🥋"
        ],
        "digital": [
            "Gaming 🎮",
            "Coding 💻",
            "3D modeling 🖥️",
            "Digital art 🖌️",
            "Video editing 🎬"
        ],
        "skills": [
            "Learning a new language 🗣️",
            "Cooking 🍳",
            "Playing a musical instrument 🎵",
            "Public speaking 🗣️",
            "Photography 📸"
        ]
    }

    for key in hobbies.keys():
        if key in user_input:
            return f"Here are some {key} hobbies you might enjoy:\n\n" + "\n".join(hobbies[key])

    # Default reply if no keyword matches
    return random.choice([
        "Sorry, I didn't get that. Can you try asking for creative, active, digital, or skill-building hobbies?",
        "Let's explore hobbies! Try selecting one of the categories above."
    ])

# -------------------------------------------------
# DISPLAY CHAT
# -------------------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"] if msg["role"]=="user" else msg["content"])

# -------------------------------------------------
# CHAT INPUT
# -------------------------------------------------
prompt = st.chat_input("Message HobbyHub...")

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a local reply
    reply = generate_reply(prompt)

    st.session_state.messages.append({"role":"assistant","content":reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
