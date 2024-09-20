from .models import Project, User
from sqlalchemy.orm import Session

class ProjectManager:
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, project_info: dict) -> Project:
        project = Project(**project_info)
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def delete_project(self, project_id: str) -> bool:
        project = self.db.query(Project).filter(Project.id == project_id).first()
        if project:
            self.db.delete(project)
            self.db.commit()
            return True
        return False

    def get_project(self, project_id: str) -> Project:
        return self.db.query(Project).filter(Project.id == project_id).first()

    def list_projects(self, user_id: str) -> list:
        return self.db.query(Project).filter(Project.owner_id == user_id).all()
