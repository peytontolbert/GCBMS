from celery import Celery
from .environment_provisioner import EnvironmentProvisioner
from .security_sandbox import SecuritySandbox
from src.database.node_manager import NodeManager
from src.database.edge_manager import EdgeManager
import logging

# Configure Celery
celery_app = Celery('execution_manager', broker='redis://localhost:6379/0')

# Initialize components
env_provisioner = EnvironmentProvisioner()
security_sandbox = SecuritySandbox()
node_manager = NodeManager()
edge_manager = EdgeManager()

class ExecutionManager:
    def start_execution(self, project_id):
        logger = logging.getLogger(__name__)
        logger.info(f"Starting execution for project_id: {project_id}")
        execution_id = node_manager.create_execution(project_id)
        celery_app.send_task('tasks.execute_project', args=[execution_id])
        return execution_id

    def monitor_execution(self, execution_id):
        logger = logging.getLogger(__name__)
        status = node_manager.get_execution_status(execution_id)
        logger.info(f"Monitoring execution_id: {execution_id}, status: {status}")
        return status

    def terminate_execution(self, execution_id):
        logger = logging.getLogger(__name__)
        logger.info(f"Terminating execution_id: {execution_id}")
        celery_app.control.revoke(execution_id, terminate=True)
        node_manager.update_execution_status(execution_id, 'Terminated')
        env_provisioner.destroy_environment(execution_id)
        return True

    def get_execution_logs(self, execution_id):
        logger = logging.getLogger(__name__)
        logs = node_manager.get_execution_logs(execution_id)
        logger.info(f"Retrieved logs for execution_id: {execution_id}")
        return logs

@celery_app.task(name='tasks.execute_project')
def execute_project_task(execution_id):
    logger = logging.getLogger(__name__)
    logger.info(f"Executing project for execution_id: {execution_id}")
    try:
        env = env_provisioner.create_environment(execution_id)
        security_sandbox.initialize_sandbox(env.id)
        security_sandbox.enforce_security_policies(execution_id)
        # Placeholder for actual execution logic
        # e.g., run scripts, handle processes
        node_manager.update_execution_status(execution_id, 'Running')
        # After execution
        node_manager.update_execution_status(execution_id, 'Completed')
        env_provisioner.destroy_environment(env.id)
    except Exception as e:
        logger.error(f"Execution failed for execution_id: {execution_id} with error: {e}")
        node_manager.update_execution_status(execution_id, 'Failed')
        env_provisioner.destroy_environment(env.id)