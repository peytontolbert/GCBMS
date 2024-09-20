import os
from typing import Dict
from dotenv import load_dotenv

class EnvVarsLoader:
    def load_env(self, env: str) -> Dict:
        """Loads environment variables for a specified environment."""
        env_file = f'.env.{env}'
        load_dotenv(env_file)
        return {key: value for key, value in os.environ.items() if key.startswith(env.upper())}

    def set_env_var(self, key: str, value: str) -> None:
        """Sets an environment variable."""
        os.environ[key] = value