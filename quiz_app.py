
import streamlit as st
import random

# Sample question
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    }
]

st.set_page_config(page_title="Quick Quiz", layout="centered")
st.title("🧠 Quick Quiz Game")
st.subheader("Answer the following question:")

# Pick a random question (in case you add more)
q = random.choice(questions)

st.write(f"**{q['question']}**")
user_answer = st.radio("Choose your answer:", q["options"])

if st.button("Submit"):
    if user_answer == q["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Wrong! The correct answer is: **{q['answer']}**")
