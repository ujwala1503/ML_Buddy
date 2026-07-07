import streamlit as st
from ai_helper import ask_ml_buddy
st.set_page_config(
    page_title="ML Buddy",
    page_icon="🤖",
    layout="wide"
)
if "history" not in st.session_state:
    st.session_state.history = []
# Title
st.title("🤖 ML Buddy")
st.caption("Your AI-powered Machine Learning Learning Assistant")

st.markdown("""
Welcome! 👋

Select a Machine Learning topic from the sidebar and choose an activity.

ML Buddy can:
- 📖 Explain concepts
- 🌍 Give real-life examples
- ❓ Generate quizzes
- ✅ Evaluate your answers
- 🎓 Teach complete lessons
""")
if st.button("🗑️ Clear Response"):
    st.session_state.clear()
    st.rerun()
# Sidebar
st.sidebar.header("Learning Options")

topic = st.sidebar.selectbox(
    "Select a Machine Learning Topic",
    [
        "Introduction to Machine Learning",
        "Types of Machine Learning",
        "Supervised Learning",
        "Unsupervised Learning",
        "Regression",
        "Classification",
        "Clustering",
        "Decision Trees",
        "Random Forest",
        "K-Nearest Neighbors (KNN)",
        "Support Vector Machine (SVM)",
        "Neural Networks",
        "Overfitting and Underfitting",
        "Evaluation Metrics"
    ]
)

activity = st.sidebar.selectbox(
    "Choose Activity",
    [
        "Explain Topic",
        "Real-Life Example",
        "Generate Quiz",
        "Evaluate Answer",
        "Full Learning Session"
    ]
)

difficulty = st.sidebar.radio(
    "Difficulty Level",
    ["Beginner", "Intermediate", "Advanced"]
)
student_answer = ""

if activity == "Evaluate Answer":
    st.subheader("📝 Answer the Question")
    student_answer = st.text_area(
        "Question: What is Supervised Learning?",
        height=150,
        placeholder="Type your answer here..."
    )
if st.button("Generate"):

    with st.spinner("🤖 ML Buddy is thinking..."):
        
        st.markdown("### 📋 Learning Details")

        col1, col2, col3 = st.columns(3)

        with col1:
         st.info(f"📚 Topic\n\n{topic}")

        with col2:
         st.success(f"🎯 Activity\n\n{activity}")

        with col3:
         st.warning(f"⭐ Level\n\n{difficulty}")

        if activity == "Explain Topic":

            prompt = f"""
            Explain {topic} for a {difficulty} level student.

            Include:
            1. Definition
            2. Why it is important
            3. Real-life example
            4. Applications
            5. Key points

            Use simple English.
            """

        elif activity == "Real-Life Example":

            prompt = f"""
            Give one detailed real-life example of {topic}.

            Explain it in simple English for a {difficulty} learner.
            """

        elif activity == "Generate Quiz":

            prompt = f"""
            Create 5 multiple-choice quiz questions on {topic}.

            After the questions, provide the correct answers with explanations.
            """

        elif activity == "Evaluate Answer":

            prompt = f"""
            You are an expert Machine Learning tutor.

            Question:
            What is Supervised Learning?

            Student's Answer:
            {student_answer}

            Evaluate the answer.

            Give:

            1. Score out of 10
            2. Correct Answer
            3. Mistakes
            4. Suggestions for Improvement
            5. Motivation
    """

        else:

            prompt = f"""
            Teach {topic} from beginning to end.

            Include:
            - Explanation
            - Example
            - Quiz
            - Summary
            """

        response = ask_ml_buddy(prompt)
        st.session_state.history.append({
        "topic": topic,
        "activity": activity,
        "response": response
    })
        st.session_state["response"] = response
        with st.container(border=True):
         st.subheader("🤖 ML Buddy Response")
         st.markdown(response)
         st.download_button(
         label="📥 Download Notes",
         data=response,
         file_name=f"{topic}.txt",
         mime="text/plain"
     )
         
         st.markdown("---")
         st.subheader("📚 Learning History")

         if st.session_state.history:
          for item in reversed(st.session_state.history):
           with st.expander(f"{item['activity']} - {item['topic']}"):
            st.markdown(item["response"])
         else:
          st.info("No learning history yet.")
         st.markdown("---")
         st.caption("Built with ❤️ using Streamlit + Groq API | Infosys AI Empower Her Project")