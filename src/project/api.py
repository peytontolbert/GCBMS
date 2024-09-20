from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Project
from .project_manager import ProjectManager
from .execution_interface import ExecutionInterface
from .vcs_integrator import VCSIntegrator
from .database import get_db  # Assuming a database module for DB session
from uuid import uuid4

router = APIRouter()

@router.post("/api/projects", response_model=dict)
def create_project_endpoint(project: dict, db: Session = Depends(get_db)):
    manager = ProjectManager(db)
    project_id = str(uuid4())
    project_info = {
        "id": project_id,
        "name": project.get("name"),
        "description": project.get("description"),
        "owner_id": project.get("owner_id")  # Ensure owner_id is provided
    }
    created_project = manager.create_project(project_info)
    return {
        "id": created_project.id,
        "name": created_project.name,
        "description": created_project.description,
        "created_at": created_project.created_at,
        "owner_id": created_project.owner_id
    }

@router.delete("/api/projects/{project_id}", response_model=dict)
def delete_project_endpoint(project_id: str, db: Session = Depends(get_db)):
    manager = ProjectManager(db)
    success = manager.delete_project(project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {
        "status": "success",
        "message": "Project deleted successfully."
    }

@router.get("/api/users/{user_id}/projects", response_model=dict)
def list_projects_endpoint(user_id: str, db: Session = Depends(get_db)):
    manager = ProjectManager(db)
    projects = manager.list_projects(user_id)
    return {
        "projects": [
            {
                "id": project.id,
                "name": project.name,
                "description": project.description,
                "created_at": project.created_at
            } for project in projects
        ]
    }
