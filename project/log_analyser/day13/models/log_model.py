from pydantic import BaseModel
from typing import List

class Log(BaseModel):
    level: str
    message: str

class LogRequest(BaseModel):
    logs: List[Log]