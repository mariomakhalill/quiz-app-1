import streamlit as st

# Define your quiz questions
questions = [
    {
        "question": "In which Module in CBS can you find leaked credentials extracted by info-stealer malware from the victim’s browser?",
        "options": ["Breached Credentials", "Malware Logs", "Card Leaks", "All of them"],
        "answer": "Malware Logs",
        "correct_users": []
    },
    {
        "question": "If a client sent a newly registered domain and it is a lookalike domain, and requested to take action on it, what should you do?",
        "options": ["Add to monitor", "Attempt to take action"],
        "answer": "Attempt to take action",
        "correct_users": []
    }
]

# Initialize session state
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answered_questions" not in st.session_state:
    st.session_state.answered_questions = [False] * len(questions)

# Page setup
st.set_page_config(page_title="Cyber Quiz", layout="centered")
st.title("CTA's Quizes")

# Get player name
if not st.session_state.user_name:
    name = st.text_input("Enter your name to start:")
    if name:
        st.session_state.user_name = name
        st.rerun()
    st.stop()

st.markdown(f"**Player:** {st.session_state.user_name}")

# Show current question
q_index = st.session_state.current_question
if q_index < len(questions):
    q = questions[q_index]
    st.markdown(f"### Q{q_index + 1}: {q['question']}")
    user_answer = st.radio("Select your answer:", q["options"], key=f"q_{q_index}")

    if not st.session_state.answered_questions[q_index]:
        if st.button("Submit Answer"):
            if user_answer == q["answer"]:
                st.success("✅ Correct!")
                if st.session_state.user_name not in q["correct_users"]:
                    q["correct_users"].append(st.session_state.user_name)
            else:
                st.error(f"❌ Incorrect! The correct answer is: **{q['answer']}**")
            st.session_state.answered_questions[q_index] = True
            st.rerun()

    # Show users who answered correctly
    if q["correct_users"]:
        st.info("✔️ Correct answers from:")
        for u in q["correct_users"]:
            st.markdown(f"- {u}")

    if st.button("Next"):
        st.session_state.current_question += 1
        st.rerun()
else:
    st.success("🎉 You have completed the quiz!")
    st.balloons()
