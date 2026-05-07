from utils.job_store import jobs
import time
import threading
import uuid
from utils.logger import logger

def process_job(job_id, payload):
    start = time.time()
    jobs[job_id]["status"] = "processing ₹"
    logger.info(f"Job {job_id} processing started at {time.time() - start}")
    time.sleep(10)
    jobs[job_id]["status"] = "completed"
    jobs[job_id]["result"] = {"message": f"processing payload: {payload}"}
    duration = time.time() - start
    logger.info(f"Job {job_id} processing job {payload} took {duration} seconds")
    logger.info(f"Job {job_id} completed")



def submit_job(payload):
    db =
    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "queued",
        "result": None,
    }

    logger.info(f"{job_id} submitting job {payload}")
    threading.Thread(target=process_job, args=(job_id, payload)).start()

    return job_id

def job_status(job_id):
    return jobs.get(job_id, {"error": "Job Id not found"})