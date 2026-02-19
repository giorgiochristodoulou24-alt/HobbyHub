import streamlit as st
import os
from openai import OpenAI

# --------------------------------------------------
# PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND)
# --------------------------------------------------
st.set_page_config(
    page_title="HobbyHub",
    page_icon="Logo.png",
    layout="wide"
)

# --------------------------------------------------
# LOAD OPENAI (requires billing enabled)
# --------------------------------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --------------------------------------------------
# LOAD DOCUMENTS (Works for file OR folder)
# --------------------------------------------------
def load_documents(path="Documents"):

    # If Documents is a folder
    if os.path.isdir(path):
        content = ""
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    content += f.read() + "\n\n"
        return content

    # If Documents is a single file
    elif os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    return ""

DOCUMENT_CONTENT = load_documents()

# --------------------------------------------------
# SYSTEM CONTEXT
# --------------------------------------------------
SYSTEM_CONTEXT = f"""
You are HobbyHub, a helpful chatbot focused on hobbies and interests.

Use the information below as reference context.
Do not mention the documents directly.
Stay conversational and helpful.

REFERENCE CONTENT:
{DOCUMENT_CONTENT}
"""

# --------------------------------------------------
# HEADER (Logo + Title Centered)
# --------------------------------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("Logo.png", width=150)
    st.markdown(
        "<h1 style='text-align: center;'>HobbyHub</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; color: gray;'>Discover hobbies. Explore passions.</p>",
        unsafe_allow_html=True
    )

# --------------------------------------------------
# CHAT MEMORY
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_CONTEXT}
    ]

# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------
user_input = st.chat_input("Ask about hobbies...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Get AI response
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=st.session_state.messages
    )

    assistant_reply = response.choices[0].message.content

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_reply}
    )
