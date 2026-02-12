import streamlit as st
import random

# -----------------------------
# LOAD PERSONALITY & PROMPTS
# -----------------------------

def load_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().strip()

PERSONALITY = load_text("personality.txt")
PROMPTS = load_text("prompts.txt")

SYSTEM_CONTEXT = f"{PERSONALITY}\n\n{PROMPTS}"

# -----------------------------
# MOCK LLM (NO DUMPING PROMPTS)
# -----------------------------

def mock_llm(user_input, history):
    # Light conversational behavior
    follow_ups = [
        "Tell me more about that.",
        "What got you interested in it?",
        "How much experience do you have with it?",
        "That sounds fun — what part interests you most?",
        "Is this something you want to do casually or seriously?"
    ]

    # Simple topic awareness
    if "hello" in user_input.lower():
        return "Hey! What hobby are you thinking about?"

    if "i like" in user_input.lower() or "i enjoy" in user_input.lower():
        return random.choice(follow_ups)

    return random.choice(follow_ups)

# -----------------------------
# STREAMLIT UI
# -----------------------------

st.set_page_config(page_title="HobbyHub")
st.title("HobbyHub")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Ask HobbyHub about hobbies")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    reply = mock_llm(user_input, st.session_state.messages)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.chat_message("assistant").write(reply)
