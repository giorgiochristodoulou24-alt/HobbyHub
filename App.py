import os
import streamlit as st

st.write("OPENAI_API_KEY exists:", os.getenv("OPENAI_API_KEY") is not None)

import streamlit as st
from openai import OpenAI

def load_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

PERSONALITY_TEXT = load_text("personality.txt")
PROMPTS_TEXT = load_text("prompts.txt")

client = OpenAI()

st.title("HobbyHub")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": PERSONALITY_TEXT},
        {"role": "system", "content": PROMPTS_TEXT},
    ]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=st.session_state.messages,
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.chat_message("assistant").write(reply)
