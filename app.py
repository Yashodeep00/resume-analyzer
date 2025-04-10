import streamlit as st
import openai
from backend.parser import read_pdf, read_docx
from backend.analyzer import analyze_resume

# Load API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["sk-...HJsAv"]

st.title("GPT-4 Resume Analyzer")

resume_file = st.file_uploader("Upload Your Resume (PDF or DOCX)", type=["pdf", "docx"])
job_desc = st.text_area("Paste the Job Description")

if st.button("Analyze Resume") and resume_file and job_desc:
    with st.spinner("Analyzing resume with GPT-4..."):
        if resume_file.name.endswith(".pdf"):
            resume_text = read_pdf(resume_file)
        else:
            resume_text = read_docx(resume_file)

        result = analyze_resume(resume_text, job_desc)
        st.subheader("AI Feedback Report")
        st.write(result)
