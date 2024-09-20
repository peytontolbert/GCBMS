import git
from .models import VCSRepository
from sqlalchemy.orm import Session
import uuid
class VCSIntegrator:
    def __init__(self, db: Session):
        self.db = db

    def clone_repository(self, repo_url: str, branch: str, clone_path: str) -> VCSRepository:
        git.Repo.clone_from(repo_url, clone_path, branch=branch)
        vcs_repo = VCSRepository(repo_url=repo_url, branch=branch, id=str(uuid.uuid4()), project_id=clone_path)
        self.db.add(vcs_repo)
        self.db.commit()
        self.db.refresh(vcs_repo)
        return vcs_repo

    def commit_changes(self, repo_path: str, commit_message: str) -> bool:
        repo = git.Repo(repo_path)
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        return True

    def push_changes(self, repo_path: str) -> bool:
        repo = git.Repo(repo_path)
        origin = repo.remote(name='origin')
        origin.push()
        return True
