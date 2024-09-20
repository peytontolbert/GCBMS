from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from src.logging.log_manager import logger
import jwt
from jwt import PyJWTError
import os

router = APIRouter()

@router.middleware("http")
async def api_gateway_middleware(request: Request, call_next):
    # Logging incoming request
    logger.info(f"Incoming request: {request.method} {request.url}")
    
    # Authentication
    if request.url.path.startswith("/api/"):
        auth_header = request.headers.get("Authorization")
        if auth_header:
            try:
                token_type, token = auth_header.split()
                if token_type.lower() != "bearer":
                    raise HTTPException(status_code=401, detail="Invalid authentication scheme.")
                payload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
                request.state.user = payload
            except (ValueError, PyJWTError):
                raise HTTPException(status_code=401, detail="Invalid or expired token.")
        else:
            raise HTTPException(status_code=401, detail="Authorization header missing.")
    
    # Rate Limiting can be implemented here
    
    try:
        response = await call_next(request)
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    # Logging response
    logger.info(f"Response status: {response.status_code}")
    return response