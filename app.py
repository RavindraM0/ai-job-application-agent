ittuimport os
import streamlit as st
import fitz  # PyMuPDF
from dotenv import load_dotenv

from utils.scrape_jobs import fetch_remoteok_jobs, fetch_wework_jobs, filter_jobs_by_location
from utils.job_matcher import match_job_with_resume

# Load API key
load_dotenv()
OPENROUTER_API_KEY = os.getenv("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")

# Streamlit config
st.set_page_config(page_title="🤖 AI Job Application Agent", layout="wide")
st.title("🤖 Autonomous Job Application Agent")

# Upload Resume
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type="pdf")
resume_text = ""

if uploaded_file:
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            resume_text += page.get_text()
    st.success("✅ Resume uploaded and extracted.")

    resume_text = st.text_area("✏️ Resume Text (Editable)", value=resume_text, height=300, key="resume_text_area")

# Location Input
location = st.text_input("📍 Preferred Job Location (e.g. Remote, India):", key="location_input")

# Button to fetch & match jobs
if st.button("🚀 Fetch and Match Jobs", key="fetch_match_button") and resume_text and location:
    with st.spinner("🔍 Scraping jobs..."):
        jobs = fetch_remoteok_jobs() + fetch_wework_jobs()
        jobs = filter_jobs_by_location(jobs, location)
        st.write(f"📌 {len(jobs)} jobs found for location '{location}'.")

    with st.spinner("🤖 Matching jobs using LLM..."):
        matched_jobs = []
        for job in jobs:
            score = match_job_with_resume(job, resume_text)
            if score > 70:
                matched_jobs.append((job, score))

    if matched_jobs:
        st.subheader("🎯 Top Matching Jobs")
        for job, score in sorted(matched_jobs, key=lambda x: x[1], reverse=True):
            st.markdown(f"**{job['title']}** - 🔢 Score: {score}")
            st.markdown(f"🌍 Location: {job.get('location', 'N/A')}")
            st.markdown(f"[🔗 Job Link]({job.get('url')})")
            st.markdown("---")
    else:
        st.warning("❌ No highly matching jobs found.")
elif st.button("❓ Why is nothing working?", key="debug_button"):
    st.info("Make sure to upload a resume and enter a location.")
