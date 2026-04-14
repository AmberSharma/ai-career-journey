from fastapi import APIRouter
from services.log_service import get_logs, add_logs, update_log, delete_log, patch_log
from utils.file_handler import write_logs, read_logs, filter_logs, validate_type, log_analyser
from models.log_model import Log, LogRequest, LogUpdateOptional

router = APIRouter()

@router.get("/logs")
def fetch_logs(type: str = None):
    logs = get_logs(type)
    return {"logs": [
        {"id": log.id, "level": log.level, "message": log.message} for log in logs
    ]}

@router.post("/logs")
def create_logs(log: Log):
    add_logs(log)
    return {"log": "Log created successfully"}

@router.put("/log")
def update_logs(log_id: int, data: Log):
    response = update_log(log_id, data)
    if response:
        return "Log updated successfully"
    else:
        return "Log with id:"+str(log_id)+" not found"

@router.delete("/log")
def delete_logs(log_id: int):
    response = delete_log(log_id)
    if response:
        return "Log deleted successfully"
    else:
        return "Log with id:"+str(log_id)+" not found"

@router.patch("/log")
def patch_logs(log_id: int, data: LogUpdateOptional):
    response = patch_log(log_id, data)
    if response:
        return "Log updated successfully"
    else:
        return "Log with id:"+str(log_id)+" not found"

@router.get("/log/errors")
def error():
    logs = get_logs()
    # errors = filter_logs(logs, "error")
    return {"errors": logs}

@router.get("/log/infos")
def info():
    logs = get_logs("info")
    # infos = filter_logs(logs, "info")
    return {"infos": logs}

@router.get("/logs/count")
def log_count(type: str = None):
    # validate_type(type)
    logs = get_logs(type)
    # filtered_logs = filter_logs(logs, type)

    return {"count":len(logs)}


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