from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime
from src.authentication.auth_controller import AuthController
import os
import jwt


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# In-memory storage for demonstration
projects_db = {}

class ProjectCreate(BaseModel):
    name: str
    description: str
    owner_id: str

class Project(BaseModel):
    project_id: str
    name: str
    description: str
    owner_id: str
    created_at: datetime
    updated_at: datetime

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token.")
        return user_id
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token.")

@router.post("/", response_model=Project)
def create_project(project: ProjectCreate, user_id: str = Depends(get_current_user)):
    if project.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to create project for this user.")
    project_id = str(uuid.uuid4())
    new_project = Project(
        project_id=project_id,
        name=project.name,
        description=project.description,
        owner_id=project.owner_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    projects_db[project_id] = new_project
    return new_project

@router.get("/{project_id}", response_model=Project)
def get_project(project_id: str):
    project = projects_db.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=Project)
def update_project(project_id: str, project_update: ProjectCreate):
    project = projects_db.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    updated_project = Project(
        project_id=project_id,
        name=project_update.name,
        description=project_update.description,
        owner_id=project.owner_id,
        created_at=project.created_at,
        updated_at=datetime.utcnow(),
    )
    projects_db[project_id] = updated_project
    return updated_project

@router.delete("/{project_id}")
def delete_project(project_id: str):
    if project_id in projects_db:
        del projects_db[project_id]
        return {"status": "success", "message": "Project deleted successfully."}
    else:
        raise HTTPException(status_code=404, detail="Project not found")