# -------------------------------------------------
# CHAT INPUT
# -------------------------------------------------
prompt = st.chat_input("Message HobbyHub...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    reply = ""
    try:
        # Generate AI reply
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "system",
                "content": f"{PERSONALITY}\n{PROMPTS}\nRespond naturally and conversationally."
            }] + st.session_state.messages
        )

        # Safe extraction of AI message
        reply = response.choices[0].message.content or "🤖 (No response received)"

    except Exception as e:
        # Basic fallback if AI is unavailable
        reply = "⚠️ AI temporarily unavailable. Let's still chat! Try a simpler question."

    # Add AI reply to chat
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
