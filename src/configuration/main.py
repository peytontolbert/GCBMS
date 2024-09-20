from fastapi import FastAPI
from .configuration_api import router as config_router

app = FastAPI()

app.include_router(config_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)