import streamlit as st

def load_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

PERSONALITY_TEXT = load_text("personality.txt")
PROMPTS_TEXT = load_text("prompts.txt")

def bot_reply(user_text):
    return (
        "🤖 **Chatbot Response (School Version)**\n\n"
        "**Personality:**\n"
        f"{PERSONALITY_TEXT}\n\n"
        "**Rules / Prompts:**\n"
        f"{PROMPTS_TEXT}\n\n"
        "**Your message:**\n"
        f"{user_text}\n\n"
        "_This chatbot uses predefined personality and prompts. "
        "An AI API can be added later._"
    )

st.title("My School Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    reply = bot_reply(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.chat_message("assistant").write(reply)
