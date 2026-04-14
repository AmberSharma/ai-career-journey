from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///log.db")
local_session = sessionmaker(bind=engine)