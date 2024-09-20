from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.endpoints import projects, auth  # Added auth
from src.api.websockets import websocket_service
from src.api.gateway import api_gateway

app = FastAPI(title="GBCMS API Layer")

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Gateway
app.include_router(api_gateway.router)

# Include RESTful endpoints
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])  # Added auth router

# WebSocket routes
@app.websocket("/ws")
async def websocket_endpoint(websocket):
    await websocket_service.handle_connection(websocket)