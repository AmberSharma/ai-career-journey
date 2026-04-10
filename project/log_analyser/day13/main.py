import json
from fastapi import FastAPI, HTTPException
from pathlib import Path
from pydantic import BaseModel
from typing import List
from datetime import datetime


app = FastAPI()

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent

class Log(BaseModel):
    level: str
    message: str

class LogRequest(BaseModel):
    logs: List[Log]


def read_logs():
    with open(SCRIPT_DIR / "logs.json","r") as f:
        return json.load(f)

def filter_logs(logs: List[str], log_type: str) -> List[str]:
    if log_type == "error":
        return [log for log in logs if log["level"] == "ERROR"]
    elif log_type == "info":
        return [log for log in logs if log["level"] == "INFO"]

    return logs

def write_logs(new_log):
    with open(SCRIPT_DIR / "logs.json","r") as f:
        logs = json.load(f)
    print(new_log, flush=True)
    # new_log.timestamp = str(datetime.now())
    log_with_timestamp = new_log.model_dump()
    log_with_timestamp["timestamp"] = str(datetime.now().isoformat(timespec='seconds'))
    logs.append(log_with_timestamp)
    with open(SCRIPT_DIR / "logs.json","w") as f:
        json.dump(logs, f, indent=2)

def validate_type(log_type: str):
    if log_type is not None and log_type.lower() not in ["error", "info", None]:
        raise HTTPException(status_code=400, detail="Invalid log type")
    return True


'''
Return Total Logs and Total Errors
'''
def log_analyser():
    logs = read_logs()

    total_logs = len(logs)
    total_errors = sum(1 for log in logs if log["level"] == "ERROR")
    error_percentage = int(total_errors/total_logs*100)
    return {"total_logs":total_logs, "total_errors":total_errors, "error_percentage":error_percentage}


@app.post("/analyse")
def analyse(data: LogRequest):
    logs = data.logs
    total_logs = len(logs)
    total_errors = sum(1 for log in logs if log.level == "ERROR")
    error_percentage = int(total_errors/total_logs*100)
    return {"logs":logs, "total_logs":total_logs, "total_errors":total_errors, "error_percentage":error_percentage}

@app.get("/logs")
def logs(type: str = None, limit: int = None):
    validate_type(type)
    logs = read_logs()

    filtered_logs = filter_logs(logs, type)

    if limit is not None and limit > 0:
        filtered_logs = filtered_logs[:limit]

    return {"logs":[l for l in  filtered_logs]}

@app.post("/logs")
def add_logs(log: Log):
    validate_type(log.level)

    write_logs(log)
    return {"message": "Log Added Successfully"}

@app.get("/logs/count")
def log_count(type: str = None):
    validate_type(type)
    logs = read_logs()
    filtered_logs = filter_logs(logs, type)

    return {"count":len(filtered_logs)}

@app.get("/log/summary")
def summary():
    return log_analyser()

@app.get("/log/errors")
def error():
    logs = read_logs()
    errors = filter_logs(logs, "error")
    return {"errors": errors}

@app.get("/log/infos")
def info():
    logs = read_logs()
    infos = sum(1 for log in logs if log.count("INFO") > 0)
    return {"infos": infos}