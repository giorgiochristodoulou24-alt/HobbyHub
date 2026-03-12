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
# SIDEBAR
# -------------------------------------------------

with st.sidebar:
    st.title("About HobbyHub")
    st.write(
        "HobbyHub helps people discover hobbies and learn how to start them."
    )

    st.write("Built as a school project using Streamlit.")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------------------------------------------
# CSS STYLING
# -------------------------------------------------

st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container{
    padding-top: 1rem;
    max-width: 1400px;
}

.title{
    font-size: 95px;
    font-weight: 800;
    line-height: 1;
    margin-top: 60px;
    margin-bottom: 10px;
}

.subtitle{
    font-size: 36px;
    font-weight: 600;
    margin-top: 0px;
}

.divider-adjust{
    margin-top: -45px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

logo_path = "Logo.png"

col_logo, col_text = st.columns([4,6], vertical_alignment="top")

with col_logo:
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        st.image(logo, width=450)

with col_text:
    st.markdown('<div class="title">HobbyHub</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Discover hobbies. Explore passions.</div>', unsafe_allow_html=True)

st.markdown('<div class="divider-adjust">', unsafe_allow_html=True)
st.divider()
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# SUGGESTED PROMPTS (CHATGPT STYLE)
# -------------------------------------------------

st.write("### Try asking:")

col1, col2, col3, col4 = st.columns(4)

if col1.button("🎨 Creative hobbies"):
    prompt = "Suggest creative hobbies"

elif col2.button("🏃 Active hobbies"):
    prompt = "Suggest active hobbies"

elif col3.button("🎮 Digital hobbies"):
    prompt = "Suggest digital hobbies"

elif col4.button("🧠 Learning hobbies"):
    prompt = "Suggest hobbies that teach new skills"

else:
    prompt = None

# -------------------------------------------------
# HOBBY KNOWLEDGE BASE
# -------------------------------------------------

hobby_database = {
    "creative": [
        "Painting",
        "Photography",
        "Drawing",
        "Pottery",
        "Creative writing"
    ],
    "active": [
        "Running",
        "Cycling",
        "Rock climbing",
        "Swimming",
        "Hiking"
    ],
    "digital": [
        "Game development",
        "3D modeling",
        "Video editing",
        "Graphic design",
        "Programming"
    ],
    "learning": [
        "Learning guitar",
        "Language learning",
        "Reading history",
        "Chess",
        "Coding"
    ]
}

# -------------------------------------------------
# CHAT HISTORY
# -------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------------------------
# CHAT INPUT
# -------------------------------------------------

user_input = st.chat_input("Ask about hobbies...")

if user_input:
    prompt = user_input

# -------------------------------------------------
# RESPONSE SYSTEM
# -------------------------------------------------

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = ""

    lower_prompt = prompt.lower()

    if "creative" in lower_prompt:
        response = "Here are some creative hobbies:\n\n" + "\n".join(
            f"- {h}" for h in hobby_database["creative"]
        )

    elif "active" in lower_prompt:
        response = "Here are some active hobbies:\n\n" + "\n".join(
            f"- {h}" for h in hobby_database["active"]
        )

    elif "digital" in lower_prompt:
        response = "Here are some digital hobbies:\n\n" + "\n".join(
            f"- {h}" for h in hobby_database["digital"]
        )

    elif "learn" in lower_prompt or "skill" in lower_prompt:
        response = "Here are hobbies that help you learn new skills:\n\n" + "\n".join(
            f"- {h}" for h in hobby_database["learning"]
        )

    else:
        response = (
            "Here are some hobbies you might enjoy:\n\n"
            "- Photography\n"
            "- Playing guitar\n"
            "- Hiking\n"
            "- Painting\n"
            "- Learning a new language"
        )

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
