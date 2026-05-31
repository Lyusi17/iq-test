import streamlit as st
import random

st.title("🧠 IQ Test")

def generate_question():
    start = random.randint(1, 20)
    step = random.randint(2, 10)

    seq = [start + step*i for i in range(4)]
    answer = start + step*4

    options = [
        answer,
        answer + random.randint(1, 5),
        answer - random.randint(1, 5),
        answer + random.randint(6, 10)
    ]

    random.shuffle(options)

    return {
        "q": f"{seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ?",
        "options": options,
        "answer": answer
    }

if "questions" not in st.session_state:
    st.session_state.questions = [generate_question() for _ in range(15)]
    st.session_state.index = 0
    st.session_state.score = 0

if st.session_state.index < 15:

    q = st.session_state.questions[st.session_state.index]

    st.write(f"Հարց {st.session_state.index + 1}")
    st.write(q["q"])

    choice = st.radio("Ընտրիր:", q["options"])

    if st.button("Հաջորդ"):

        if choice == q["answer"]:
            st.session_state.score += 1

        st.session_state.index += 1
        st.rerun()

else:

    iq = 85 + st.session_state.score * 5

    st.success(f"Քո IQ ≈ {iq}")
    st.write("Ճիշտ պատասխաններ:", st.session_state.score)