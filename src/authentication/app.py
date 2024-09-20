from fastapi import FastAPI
from src.api.endpoints.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

# ... existing routes if any ...