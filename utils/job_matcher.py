import requests
import os

def match_job_with_resume(job, resume_text):
    prompt = f"""
You are a job-matching AI assistant. Given the job title and location:

Job Title: {job['title']}
Location: {job['location']}

And the candidate resume below:

Resume:
{resume_text}

Return a match score (0 to 100) for how well this resume fits the job.
Only return the number.
"""
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "mistralai/mistral-7b-instruct",  # free OpenRouter model
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
        score = int("".join(filter(str.isdigit, response.json()["choices"][0]["message"]["content"])))
        return score
    except Exception as e:
        print("Matching error:", e)
        return 0
