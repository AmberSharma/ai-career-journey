from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Column, Integer, String
from models.base import Base


class Log(BaseModel):
    level: str
    message: str

class LogUpdateOptional(BaseModel):
    level: Optional[str] = None
    message: Optional[str] = None

class LogRequest(BaseModel):
    logs: List[Log]

class LogDB(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    level = Column(String)
    message = Column(String)

    def __repr__(self):
        return f"Log(id={self.id}, level={self.level}, message={self.message})"

class Queue(BaseModel):
    data: dict = {}
