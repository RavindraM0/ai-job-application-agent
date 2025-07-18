# 🤖 AI Job Application Agent

This is an open-source AI-powered job application assistant that automatically scrapes remote job listings, filters them by location, semantically matches them to your resume, and presents highly relevant job opportunities.

## 🚀 Features

- 📄 Upload your resume (PDF)
- 🌐 Scrapes jobs from:
  - [RemoteOK](https://remoteok.com)
  - [We Work Remotely](https://weworkremotely.com)
- 📍 Filters jobs based on preferred location
- 🤖 Matches jobs with your resume using LLM (OpenRouter API)
- 🎯 Displays only high-matching jobs (score > 70)

## 🧠 How It Works

1. Resume text is extracted from the uploaded PDF using `PyMuPDF`.
2. Job listings are scraped using `requests` and `BeautifulSoup`.
3. Jobs are filtered by location keyword.
4. Semantic matching is done via OpenRouter's free LLM API.
5. Top-matching jobs are displayed with scores and links.

## 📂 Folder Structure

ai-job-application-agent/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── .env # Contains your OpenRouter API key (not pushed)
│
├── utils/
│ ├── scrape_jobs.py # Job scraping + filtering
│ └── job_matcher.py # Semantic resume-job matching using OpenRouter
│
└── README.md

RUN
Python -m streamlit run app.py
