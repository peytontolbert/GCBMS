from .models import Execution, ExecutionStatus
from sqlalchemy.orm import Session
import uuid
import datetime

class ExecutionInterface:
    def __init__(self, db: Session):
        self.db = db

    def execute_project(self, project_id: str) -> Execution:
        execution = Execution(
            id=str(uuid.uuid4()),
            project_id=project_id,
            status=ExecutionStatus.RUNNING,
            started_at=datetime.datetime.utcnow()
        )
        self.db.add(execution)
        self.db.commit()
        # Here you would add logic to start the execution asynchronously
        return execution

    def get_execution_status(self, execution_id: str) -> ExecutionStatus:
        execution = self.db.query(Execution).filter(Execution.id == execution_id).first()
        if execution:
            return execution.status
        return None

    def stop_execution(self, execution_id: str) -> bool:
        execution = self.db.query(Execution).filter(Execution.id == execution_id).first()
        if execution and execution.status == ExecutionStatus.RUNNING:
            # Here you would add logic to terminate the execution process
            execution.status = ExecutionStatus.FAILED
            execution.ended_at = datetime.datetime.utcnow()
            self.db.commit()
            return True
        return False
