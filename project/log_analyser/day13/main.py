import sys
from pathlib import Path
from models.base import Base
from db import engine
from models.log_model import LogDB
from models.job_model import JobDB

sys.path.insert(0, str(Path(__file__).parent))

Base.metadata.create_all(bind=engine)
from models.log_model import Log
from utils.file_handler import read_logs, filter_logs, validate_type
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from routes.logs import router
from routes.auth import router as auth_router
from routes.queue_routes import router as queue_router


app = FastAPI()

app.include_router(router)
app.include_router(auth_router)
app.include_router(queue_router)




