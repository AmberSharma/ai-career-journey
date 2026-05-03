from utils.job_store import jobs
import time
import threading
import uuid

def process_job(job_id, payload):
    jobs[job_id]["status"] = "processing ₹"

    time.sleep(10)
    jobs[job_id]["status"] = "completed"
    jobs[job_id]["result"] = {"message": f"processing payload: {payload}"}


def submit_job(payload):
    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "queued",
        "result": None,
    }
    threading.Thread(target=process_job, args=(job_id, payload)).start()

    return job_id

def job_status(job_id):
    return jobs.get(job_id, {"error": "Job Id not found"})