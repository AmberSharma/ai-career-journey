import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from models.log_model import Log
from utils.file_handler import read_logs, filter_logs, validate_type
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from routes.logs import router


app = FastAPI()

app.include_router(router)




