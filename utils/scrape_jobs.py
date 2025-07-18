import requests

def fetch_remoteok_jobs():
    try:
        response = requests.get("https://remoteok.com/api")
        jobs = response.json()[1:]  # Skip first element (metadata)
        job_list = []
        for job in jobs:
            job_list.append({
                "title": job.get("position") or job.get("title"),
                "location": job.get("location", "Remote"),
                "url": job.get("url")
            })
        return job_list
    except Exception as e:
        print("Error fetching from RemoteOK:", e)
        return []

def fetch_wework_jobs():
    try:
        response = requests.get("https://weworkremotely.com/remote-jobs.json")
        jobs = response.json()["jobs"]
        job_list = []
        for job in jobs:
            job_list.append({
                "title": job.get("title"),
                "location": job.get("location", "Remote"),
                "url": "https://weworkremotely.com" + job.get("url")
            })
        return job_list
    except Exception as e:
        print("Error fetching from WeWorkRemotely:", e)
        return []

def filter_jobs_by_location(jobs, location):
    return [job for job in jobs if location.lower() in job["location"].lower()]
