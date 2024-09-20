import docker
import logging

class EnvironmentProvisioner:
    def __init__(self):
        self.client = docker.from_env()
        self.logger = logging.getLogger(__name__)

    def create_environment(self, project_config):
        self.logger.info(f"Creating environment for project_config: {project_config}")
        container = self.client.containers.run(
            image='python:3.9-slim',
            command='sleep infinity',
            detach=True,
            name=f"env_{project_config}",
            ports={'8000/tcp': None},
            environment={'PROJECT_CONFIG': project_config}
        )
        self.logger.info(f"Environment created with container ID: {container.id}")
        return container

    def destroy_environment(self, environment_id):
        self.logger.info(f"Destroying environment with ID: {environment_id}")
        try:
            container = self.client.containers.get(environment_id)
            container.stop()
            container.remove()
            self.logger.info(f"Environment {environment_id} destroyed successfully.")
        except docker.errors.NotFound:
            self.logger.warning(f"Environment {environment_id} not found.")
        except Exception as e:
            self.logger.error(f"Error destroying environment {environment_id}: {e}")