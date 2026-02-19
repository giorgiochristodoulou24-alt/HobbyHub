import streamlit as st
import os
from openai import OpenAI

# -------------------------
# PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND)
# -------------------------
st.set_page_config(
    page_title="HobbyHub",
    page_icon="Logo.png",
    layout="wide"
)

# -------------------------
# LOAD OPENAI
# -------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# -------------------------
# LOAD DOCUMENTS FOLDER CONTENT
# -------------------------
def load_documents(folder_path="Documents"):
    content = ""
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    content += f.read() + "\n\n"
    return content

DOCUMENT_CONTENT = load_documents()

# -------------------------
# SYSTEM CONTEXT
# -------------------------
SYSTEM_CONTEXT = f"""
You are HobbyHub, a helpful chatbot that only answers questions 
based on the information provided below.

If the answer is not found in the information, say:
"I'm not sure based on the available documents."

DOCUMENTS:
{DOCUMENT_CONTENT}
"""

# -------------------------
# DISPLAY LOGO + TITLE
# -------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("Logo.png", width=150)
    st.markdown("<h1 style='text-align: center;'>HobbyHub</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: gray;'>Explore hobbies and interests</p>",
        unsafe_allow_html=True
    )

# -------------------------
# SESSION MEMORY
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_CONTEXT}
    ]

# -------------------------
# DISPLAY CHAT HISTORY
# -------------------------
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# USER INPUT
# -------------------------
user_input = st.chat_input("Ask about hobbies...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Get response from OpenAI
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=st.session_state.messages
    )

    assistant_reply = response.choices[0].message.content

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_reply}
    )
