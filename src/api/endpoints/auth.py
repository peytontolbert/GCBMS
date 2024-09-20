from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta
import os

router = APIRouter()

class AuthRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(auth: AuthRequest):
    # Replace with actual authentication logic
    if auth.username == "admin" and auth.password == "password":
        payload = {
            "sub": auth.username,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, os.getenv("JWT_SECRET"), algorithm="HS256")
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")