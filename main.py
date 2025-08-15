import streamlit as st
from datetime import datetime
import pandas as pd
from ollama_utils import get_reflection

st.set_page_config(page_title="MindMate", layout='centered')
st.title("🧠 MindMate — Your Companion and Listener")

# --- Mood Input ---
st.header("📝 How are you feeling today?")
mood = st.selectbox("Select your current mood:", ["😢 Sad", "😐 Okay", "😊 Happy", "😡 Angry", "😴 Tired", "😖 Confused"])
reason = st.text_input("What happened that made you feel like this?")

if st.button("💾 Save Mood"):
    now = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
    new_entry = pd.DataFrame([[now, mood, reason]], columns=["Date", "Mood", "Reason"])
    try:
        existing = pd.read_csv('mood_data.csv')
        mood_log = pd.concat([existing, new_entry], ignore_index=True)
    except FileNotFoundError:
        mood_log = new_entry
    mood_log.to_csv('mood_data.csv', index=False)
    st.markdown("🫂 _Thanks for sharing. I'm here with you._")

# --- Mood History ---
st.header("📅 How you have felt recently")
try:
    history = pd.read_csv('mood_data.csv')
    st.dataframe(history.tail(7), use_container_width=True)
except FileNotFoundError:
    st.info("You haven't shared anything with me yet.")

# --- AI Companion ---
st.header("💬 Want me to listen or advise?")
user_input = st.text_input("What's on your mind? Type 'listen' or 'advise'.")

if user_input.lower() == 'listen':
    with st.spinner("Ok, I'm here. Just type whatever you want to express."):
        st.info("I’m listening. You can type anything in the mood box above.")
elif user_input.lower() == 'advise':
    problem = st.text_area("Tell me what's bothering you:")
    if st.button("🧠 Get Advice"):
        with st.spinner("Thinking about your problem..."):
            response = get_reflection(problem)
            st.markdown(f"**MindMate says:** {response}")
