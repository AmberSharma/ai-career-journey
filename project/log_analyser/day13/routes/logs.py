from fastapi import APIRouter, HTTPException, Header, Depends, BackgroundTasks
from services.log_service import get_logs, add_logs, update_log, delete_log, patch_log
from sqlalchemy.testing.pickleable import User
from utils.file_handler import write_logs, read_logs, filter_logs, validate_type, log_analyser
from models.log_model import Log, LogRequest, LogUpdateOptional
from utils.auth import get_current_user, admin_only
from utils.ai import analyse_log_with_ai

router = APIRouter()

def validate_token(token: str):
    if token != "secret123":
        raise HTTPException(status_code=401, detail="Unauthorized")

async def run_ai_analysis():
    error_logs = get_logs("error")
    if error_logs:
        insights = await analyse_log_with_ai(error_logs)
        print("insights", insights)

@router.post("/logs/ai-background")
def ai_background(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_ai_analysis)
    return {
        "message": "AI task started in background"
    }

@router.get("/logs")
def fetch_logs(type: str = None, user = Depends(get_current_user)):
    # return token
    # validate_token(token)
    logs = get_logs(type)
    return {"logs": [
        {"id": log.id, "level": log.level, "message": log.message} for log in logs
    ]}

@router.post("/logs")
def create_logs(log: Log):
    add_logs(log)
    return {"log": "Log created successfully"}

@router.post("/logs/ai_analyse")
async def ai_analyse(user = Depends(get_current_user)):
    logs = get_logs("error")
    print(logs)
    insights = await analyse_log_with_ai(logs)
    return {"insights": insights}

@router.put("/log")
def update_logs(log_id: int, data: Log):
    response = update_log(log_id, data)
    if response:
        return "Log updated successfully"
    else:
        return "Log with id:"+str(log_id)+" not found"

@router.delete("/log")
def delete_logs(log_id: int, user = Depends(get_current_user)):
    admin_only(user)
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