import streamlit as st

with open('./style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = 0

def quiz():
    st.title("Welcome to my computer quiz!")

    playing = st.checkbox("Would you like to start the quiz? (Check for Yes, Uncheck for No)")

    if not playing:
        st.write("")
        st.stop()

    st.write("Okay, let's play!")
    
    # Get user input and check answers for each question
    question_1 = st.text_input("What does CPU stand for?")
    show_answer_1 = st.button("Check Answer 1", key="answer_1")
    if show_answer_1:
        if question_1.lower() == "central processing unit":
            st.write("Correct answer!")
            st.session_state.score += 1
        else:
            st.error("Oops, the answer is incorrect.")

    question_2 = st.text_input("What does GPU stand for?")
    show_answer_2 = st.button("Check Answer 2", key="answer_2")
    if show_answer_2:
        if question_2.lower() == "graphics processing unit":
            st.write("Correct answer!")
            st.session_state.score += 1
        else:
            st.error("Oops, the answer is incorrect.")

    question_3 = st.text_input("What does RAM stand for?")
    show_answer_3 = st.button("Check Answer 3", key="answer_3")
    if show_answer_3:
        if question_3.lower() == "random access memory":
            st.write("Correct answer!")
            st.session_state.score += 1
        else:
            st.error("Oops, the answer is incorrect.")

    question_4 = st.text_input("What does PSU stand for?")
    show_answer_4 = st.button("Check Answer 4", key="answer_4")
    if show_answer_4:
        if question_4.lower() == "power supply":
            st.write("Correct answer!")
            st.session_state.score += 1
        else:
            st.error("Oops, the answer is incorrect.")

    # Display the final score
    st.write(f'You got {st.session_state.score} questions correct')
    st.write(f'You got {(st.session_state.score / 4) * 100} % of the questions correct!')

if __name__ == "__main__":
    quiz()
