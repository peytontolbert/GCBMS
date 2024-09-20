import json
from .models import Project
from sqlalchemy.orm import Session

class ProjectSettings:
    def __init__(self, db: Session):
        self.db = db

    def update_settings(self, project_id: str, settings: dict) -> Project:
        project = self.db.query(Project).filter(Project.id == project_id).first()
        if project:
            project.description = settings.get('description', project.description)
            # Update other settings as needed
            self.db.commit()
            self.db.refresh(project)
        return project

    def get_settings(self, project_id: str) -> dict:
        project = self.db.query(Project).filter(Project.id == project_id).first()
        if project:
            return {
                "name": project.name,
                "description": project.description,
                # Add other settings as needed
            }
        return {}