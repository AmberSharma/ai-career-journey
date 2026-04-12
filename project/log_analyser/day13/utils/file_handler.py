from pathlib import Path
import json
from datetime import datetime
from typing import List
from fastapi import HTTPException

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.parent

def read_logs():
    with open(SCRIPT_DIR / "logs.json","r") as f:
        return json.load(f)

def write_logs(new_log):
    with open(SCRIPT_DIR / "logs.json","r") as f:
        logs = json.load(f)
    log_with_timestamp = new_log.model_dump()
    log_with_timestamp["timestamp"] = str(datetime.now().isoformat(timespec='seconds'))
    logs.append(log_with_timestamp)
    with open(SCRIPT_DIR / "logs.json","w") as f:
        json.dump(logs, f, indent=2)

def filter_logs(logs: List[str], log_type: str) -> List[str]:
    if log_type == "error":
        return [log for log in logs if log["level"] == "ERROR"]
    elif log_type == "info":
        return [log for log in logs if log["level"] == "INFO"]

    return logs

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