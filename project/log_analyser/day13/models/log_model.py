from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


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