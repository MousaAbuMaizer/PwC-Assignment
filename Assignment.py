import streamlit as st
from backend import generate_quiz_questions

def init_session_state():
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []
    if 'submit_clicked' not in st.session_state:
        st.session_state.submit_clicked = False

st.title('AI Powered Quiz Generator')

init_session_state()

# User inputs for topic and number of questions
if not st.session_state.questions:
    topic = st.text_input("Enter the topic for the quiz:")
    num_questions = st.number_input("Enter the number of questions:", min_value=1, max_value=20, value=5)

    if st.button('Generate Quiz'):
        if topic and num_questions > 0:
            with st.spinner('Generating quiz questions...'):
                st.session_state.questions = generate_quiz_questions(topic, num_questions)
                st.session_state.user_answers = [None] * len(st.session_state.questions)

# Display quiz questions and answer options
if st.session_state.questions:
    for i, question in enumerate(st.session_state.questions):
        st.subheader(f"Question {i + 1}: {question['question']}")
        st.session_state.user_answers[i] = st.radio(f"Select an answer for question {i + 1}", 
                                                    question['options'], 
                                                    key=f"question_{i}")

    if st.button('Submit Quiz'):
        st.session_state.submit_clicked = True

# Show feedback under each question after submission
if st.session_state.submit_clicked:
    correct_count = 0
    for i, (user_answer, question) in enumerate(zip(st.session_state.user_answers, st.session_state.questions)):
        if user_answer == question['correct_answer']:
            correct_count += 1
            st.caption(f"Question {i + 1}: Correct! ✅")
        else:
            st.caption(f"Question {i + 1}: Incorrect ❌. Correct Answer: {question['correct_answer']}")
    st.write("## Quiz Result")
    st.write(f"You got {correct_count} out of {len(st.session_state.questions)} questions correct.")

    if st.button("Start a New Quiz"):
        st.session_state.questions = []
        st.session_state.user_answers = []
        st.session_state.submit_clicked = False
        st.experimental_rerun()