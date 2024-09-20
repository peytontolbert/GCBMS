from fastapi import FastAPI
from .api import router as project_router
from .models import Base
from .database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(project_router)
