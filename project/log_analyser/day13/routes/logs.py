from fastapi import APIRouter
from services.log_service import get_logs
from utils.file_handler import write_logs, read_logs, filter_logs, validate_type, log_analyser
from models.log_model import Log, LogRequest

router = APIRouter()

@router.get("/logs")
def fetch_logs(type: str = None):
    return {"logs": get_logs(type)}

@router.post("/logs")
def create_logs(log: Log):
    write_logs(log)
    return {"log": "Log created successfully"}

@router.get("/log/errors")
def error():
    logs = read_logs()
    errors = filter_logs(logs, "error")
    return {"errors": errors}

@router.get("/log/infos")
def info():
    logs = read_logs()
    infos = filter_logs(logs, "info")
    return {"infos": infos}

@router.get("/logs/count")
def log_count(type: str = None):
    validate_type(type)
    logs = read_logs()
    filtered_logs = filter_logs(logs, type)

    return {"count":len(filtered_logs)}


@router.post("/analyse")
def analyse(data: LogRequest):
    logs = data.logs
    total_logs = len(logs)
    total_errors = sum(1 for log in logs if log.level == "ERROR")
    error_percentage = int(total_errors/total_logs*100)
    return {"logs":logs, "total_logs":total_logs, "total_errors":total_errors, "error_percentage":error_percentage}

@router.get("/log/summary")
def summary():
    return log_analyser()