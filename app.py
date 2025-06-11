import streamlit as st
from resume_agent import ask_agent
from resume_utils import generate_bullets, review_resume

st.set_page_config(page_title="ChatResume AI", layout="centered")
st.title("🧾 ChatResume AI – Your Smart Resume Assistant")

st.subheader("💬 Ask the AI About Resumes")
question = st.text_input("Enter your question (e.g., How to write a summary?)")
if question:
    response = ask_agent(f"Resume advice: {question}")
    st.success(response)

st.subheader("🧠 Generate Resume Bullet Points")
role = st.text_input("Enter your role or achievement")
if role:
    bullets = generate_bullets(role)
    st.markdown("### ✨ Suggested Bullet Points:")
    st.markdown(bullets)

st.subheader("📄 Upload Resume for AI Review (.txt only)")
uploaded = st.file_uploader("Upload Resume", type=["txt"])
if uploaded:
    review = review_resume(uploaded)
    st.markdown("### 🧐 AI Review Feedback:")
    st.info(review)
