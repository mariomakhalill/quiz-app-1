import streamlit as st
import random

# Custom cyber security questions
questions = [
    {
        "question": "In which Module in CBS can you find leaked credentials extracted by info-stealer malware from the victim’s browser?",
        "options": ["Breached Credentials", "Malware Logs", "Card Leaks", "All of them"],
        "answer": "Malware Logs"
    },
    {
        "question": "If a client sent a newly registered domain and it is a lookalike domain, and requested to take action on it, what should you do?",
        "options": ["Add to monitor", "Attempt to take action"],
        "answer": "Attempt to take action"
    }
]

st.set_page_config(page_title="Cyber Quiz", layout="centered")
st.title("🛡️ Cyber Security Quick Quiz")

# Ask for user's name
user_name = st.text_input("Enter your name to start:")

# Proceed only if name is entered
if user_name:
    st.success(f"Welcome, {user_name}! Let's begin your quiz.")
    
    score = 0
    total = len(questions)
    answers_submitted = []

    for idx, q in enumerate(questions):
        st.write(f"### Q{idx+1}: {q['question']}")
        user_answer = st.radio("Select your answer:", q["options"], key=f"q_{idx}")
        
        if st.button(f"Submit Answer {idx+1}", key=f"submit_{idx}"):
            if user_answer == q["answer"]:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error(f"❌ Wrong! The correct answer is: **{q['answer']}**")
            answers_submitted.append(True)
        st.markdown("---")

    if len(answers_submitted) == total:
        st.write(f"### 🧾 {user_name}, your final score: **{score} / {total}**")
else:
    st.info("Please enter your name to begin.")
