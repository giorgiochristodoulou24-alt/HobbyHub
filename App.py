import streamlit as st

# Page config
st.set_page_config(
    page_title="HobbyHub Chatbot",
    page_icon="🎨",
    layout="centered"
)

st.title("🎯 HobbyHub Chatbot")
st.write("Talk to me about hobbies, interests, and things you enjoy!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me about hobbies...")

def hobby_bot_reply(user_text):
    text = user_text.lower()

    if "music" in text:
        return "🎵 Music is awesome! Do you like playing instruments or just listening?"
    elif "sports" in text:
        return "🏀 Sports keep you active! Are you more into team sports or solo ones?"
    elif "art" in text or "drawing" in text:
        return "🎨 Art is a great creative outlet! Digital or traditional?"
    elif "gaming" in text:
        return "🎮 Gaming is fun! Console, PC, or mobile?"
    elif "reading" in text or "books" in text:
        return "📚 Reading is a great hobby. Fiction or non-fiction?"
    else:
        return "🤔 That sounds interesting! Tell me more about your hobbies."

# When user sends a message
if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    bot_response = hobby_bot_reply(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })

    with st.chat_message("assistant"):
        st.markdown(bot_response)
