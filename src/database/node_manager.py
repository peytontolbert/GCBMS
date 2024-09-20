import logging
from .query_engine import QueryEngine

class NodeManager:
    def __init__(self):
        self.query_engine = QueryEngine()
        self.logger = logging.getLogger(__name__)

    def create_execution(self, project_id):
        self.logger.info(f"Creating execution record for project_id: {project_id}")
        query = """
        INSERT INTO executions (project_id, status, started_at)
        VALUES (%s, %s, NOW())
        RETURNING id
        """
        execution_id = self.query_engine.execute_query(query, (project_id, 'Running'))
        self.logger.info(f"Execution record created with id: {execution_id}")
        return execution_id

    def get_execution_status(self, execution_id):
        self.logger.info(f"Fetching status for execution_id: {execution_id}")
        query = "SELECT status FROM executions WHERE id = %s"
        status = self.query_engine.execute_query(query, (execution_id,), fetch_one=True)
        self.logger.info(f"Status for execution_id {execution_id}: {status}")
        return status

    def update_execution_status(self, execution_id, status):
        self.logger.info(f"Updating status for execution_id: {execution_id} to {status}")
        query = "UPDATE executions SET status = %s, ended_at = NOW() WHERE id = %s"
        self.query_engine.execute_query(query, (status, execution_id))
        self.logger.info(f"Execution_id {execution_id} updated to status: {status}")

    def get_execution_logs(self, execution_id):
        self.logger.info(f"Retrieving logs for execution_id: {execution_id}")
        query = "SELECT logs FROM executions WHERE id = %s"
        logs = self.query_engine.execute_query(query, (execution_id,), fetch_one=True)
        self.logger.info(f"Logs retrieved for execution_id {execution_id}")
        return logs