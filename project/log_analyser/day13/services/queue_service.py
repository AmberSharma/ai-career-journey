from utils.job_store import jobs
import time
import threading
import uuid
from utils.logger import logger
from db import local_session
from models.job_model import JobDB

def process_job(job_id, payload):
    db = local_session()
    start = time.time()
    job = db.query(JobDB).filter(JobDB.id == job_id).first()
    if job is not None:
        job.status = "processing"

    db.commit()
    logger.info(f"Job {job_id} processing started at {time.time() - start}")
    time.sleep(10)
    job.status = "completed"
    job.result = "AI analysis completed"
    db.commit()
    duration = time.time() - start
    logger.info(f"Job {job_id} processing job {payload} took {duration} seconds")
    logger.info(f"Job {job_id} completed")
    db.close()



def submit_job(payload):
    db = local_session()
    job_id = str(uuid.uuid4())

    job = JobDB(
        id=job_id,
        status="queued",
    )

    db.add(job)
    db.commit()

    logger.info(f"{job_id} submitting job {payload}")
    threading.Thread(target=process_job, args=(job_id, payload)).start()
    db.close()

    return job_id

def job_status(job_id):
    db = local_session()
    job = db.query(JobDB).filter(JobDB.id == job_id).first()
    if job is None:
        return {"error": "Job Id not found"}

    return {
        "job_id": job.id,
        "status": job.status,
        "result": job.result,
    }