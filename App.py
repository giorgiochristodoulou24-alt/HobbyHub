import streamlit as st
import random

def load_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

PERSONALITY = load_text("personality.txt")
PROMPTS = load_text("prompts.txt")

def bot_reply(user_text):
    """
    This simulates an LLM-style response:
    - No hardcoded greetings
    - No dumping system text
    - Neutral, conversational tone
    """

    generic_responses = [
        "That’s interesting. Can you tell me more?",
        "Why do you feel that way?",
        "What got you interested in that?",
        "That sounds like something worth exploring further.",
        "Can you explain a bit more what you mean?",
        "What are you hoping to learn or do with that?",
    ]

    reflective_responses = [
        f"It sounds like you’re thinking about {user_text}.",
        f"You mentioned {user_text}. What about it stands out to you?",
    ]

    # Light variation to feel less scripted
    if len(user_text.split()) > 4:
        return random.choice(reflective_responses)
    else:
        return random.choice(generic_responses)

st.title("HobbyHub")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Ask HobbyHub something")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    reply = bot_reply(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.chat_message("assistant").write(reply)
