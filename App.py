import streamlit as st
from openai import OpenAI

client = OpenAI()

def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

PERSONALITY = load_text("prompts/personality.txt")
PROMPTS = load_text("prompts/prompts.txt")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": PERSONALITY},
        {"role": "system", "content": PROMPTS},
    ]

st.title("My Chatbot")

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
