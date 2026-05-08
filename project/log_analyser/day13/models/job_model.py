from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Column, String, DateTime
import datetime
from models.base import Base

class JobDB(Base):
    __tablename__ = "jobs"
    id = Column(String, primary_key=True, index=True)
    status = Column(String)
    result = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Job(id={self.id}, status={self.status}, result={self.result}), created_at={self.created_at}"
