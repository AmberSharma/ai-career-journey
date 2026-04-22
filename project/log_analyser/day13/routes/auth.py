from fastapi import APIRouter
from utils.auth import create_token

router = APIRouter()

@router.post("/login")
def login():
    token = create_token({"user": "normal"})
    return {"access_token": token}

