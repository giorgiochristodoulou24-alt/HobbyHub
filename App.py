st.set_page_config(
    page_title="HobbyHub",
    page_icon="logo.png",
    layout="wide"
)

st.image("logo.png", width=150)

st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }

    .main {
        background-color: #f5f7fa;
    }

    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 8px;
    }

    .stChatMessage[data-testid="stChatMessage-user"] {
        background-color: #d0e8ff;
    }

    .stChatMessage[data-testid="stChatMessage-assistant"] {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
    }

    h1 {
        color: #2c3e50;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)


import streamlit as st
from openai import OpenAI

def load_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().strip()

PERSONALITY = load_text("personality.txt")
PROMPTS = load_text("prompts.txt")

SYSTEM_CONTEXT = f"{PERSONALITY}\n\n{PROMPTS}"

client = OpenAI()

st.set_page_config(page_title="HobbyHub")
st.title("HobbyHub")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_CONTEXT}
    ]

# Display conversation (skip system message)
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Ask HobbyHub about hobbies")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Call OpenAI
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=st.session_state.messages,
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.chat_message("assistant").write(reply)
