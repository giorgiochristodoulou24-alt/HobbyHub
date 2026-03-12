import streamlit as st
from PIL import Image
from openai import OpenAI
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
# OPENAI CLIENT
# -------------------------------------------------

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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
    else:
        st.warning("Logo.png not found.")

with col_text:
    st.markdown('<div class="title">HobbyHub</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Discover hobbies. Explore passions.</div>', unsafe_allow_html=True)

st.markdown('<div class="divider-adjust">', unsafe_allow_html=True)
st.divider()
st.markdown('</div>', unsafe_allow_html=True)

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

prompt = st.chat_input("Ask about hobbies...")

if prompt:

    # show user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # generate AI response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are HobbyHub, a friendly assistant that helps users discover hobbies, learn about them, and get started."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    reply = response.choices[0].message.content

    # store assistant response
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # display response
    with st.chat_message("assistant"):
        st.markdown(reply)
