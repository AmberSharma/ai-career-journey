from utils.file_handler import validate_type, read_logs, filter_logs, write_logs
from models.log_model import Log

# @app.get("/logs")
def get_logs(type: str = None, limit: int = None):
    validate_type(type)
    logs = read_logs()

    filtered_logs = filter_logs(logs, type)

    if limit is not None and limit > 0:
        filtered_logs = filtered_logs[:limit]

    return filtered_logs

# @app.post("/logs")
def add_logs(log: Log):
    validate_type(log.level)

    write_logs(log)
    return {"message": "Log Added Successfully"}