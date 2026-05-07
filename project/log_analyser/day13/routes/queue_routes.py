from fastapi import APIRouter
from services.queue_service import job_status, submit_job
from models.log_model import Queue
from utils.logger import logger

router = APIRouter()

@router.post("/submit")
def submit(payload: Queue):
    logger.info("Received request at /submit")
    job_id = submit_job(payload)
    return {"job_id": job_id}

@router.get("/status/{job_id}")
def status(job_id):
    logger.info(f"Received request at /status/{job_id}")
    return job_status(job_id)
