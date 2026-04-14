from models.log_model import Log, LogDB, LogUpdateOptional
from db import local_session


def get_logs(type: str = None, limit: int = None):
    db = local_session()
    if (type is not None):
        logs = db.query(LogDB).filter(LogDB.level == type.lower()).limit(limit).all()
    else:
        logs = db.query(LogDB).all()
    db.close()
    return logs

def add_logs(log: Log):
    db = local_session()
    log = LogDB(level= log.level.lower(), message=log.message)
    db.add(log)
    db.commit()
    db.close()
    return {"message": "Log Added Successfully"}

def update_log(log_id, new_data: Log):
    db = local_session()
    log = db.query(LogDB).filter(LogDB.id == log_id).first()

    if not log:
        db.close()
        return None

    log.level = new_data.level.lower()
    log.message = new_data.message
    db.commit()
    db.close()
    return log

def delete_log(log_id: int):
    db = local_session()
    log= db.query(LogDB).filter(LogDB.id == log_id).first()

    if not log:
        db.close()
        return None

    db.delete(log)
    db.commit()
    db.close()
    return True

def patch_log(log_id: int, new_data: LogUpdateOptional):
    db = local_session()
    log = db.query(LogDB).filter(LogDB.id == log_id).first()

    if not log:
        db.close()
        return None

    if new_data.level is not None:
        log.level = new_data.level.lower()

    if new_data.message is not None:
        log.message = new_data.message

    db.commit()
    db.close()
    return True