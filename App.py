import streamlit as st
import random
import re

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
# MEMORY
# -----------------------------

if "memory" not in st.session_state:
    st.session_state.memory = {
        "hobbies": set(),
        "used_responses": set()
    }

# -----------------------------
# MOCK LLM WITH CONTEXT & MEMORY
# -----------------------------

def mock_llm(user_input, history):
    text = user_input.lower()

    # Detect hobby mentions
    hobby_keywords = [
        "gaming", "drawing", "music", "guitar", "piano",
        "sports", "soccer", "basketball", "coding",
        "art", "painting", "photography", "writing"
    ]

    for hobby in hobby_keywords:
        if hobby in text:
            st.session_state.memory["hobbies"].add(hobby)

    # Personality-influenced tone
    tone_responses = [
        "That sounds like a great interest.",
        "That’s a solid hobby choice.",
        "A lot of people find that really rewarding."
    ]

    follow_ups = [
        "What do you enjoy most about it?",
        "How did you get started?",
        "Do you want to get better at it or just have fun?",
        "Do you usually do it alone or with others?",
        "What part of it do you find most challenging?"
    ]

    # Avoid repeating responses
    available = [
        r for r in follow_ups
        if r not in st.session_state.memory["used_responses"]
    ]

    if not available:
        st.session_state.memory["used_responses"].clear()
        available = follow_ups

    response = random.choice(available)
    st.session_state.memory["used_responses"].add(response)

    # Use memory if available
    if st.session_state.memory["hobbies"]:
        remembered = ", ".join(st.session_state.memory["hobbies"])
        response = f"You mentioned being into {remembered}. {response}"

    # Greeting handling
    if text.
