from fastapi import Header, HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

SECRET = "mysecret"
ALGORITHM = "HS256"

def get_current_user(token: str = Header()):
    payload = verify_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return payload

def admin_only(user):
    if user.get("user") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")

def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now(timezone.utc) + timedelta(minutes=30)})
    return jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    except JWTError:
        return None