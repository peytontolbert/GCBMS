import json
import os
from typing import Dict

class ConfigFilesManager:
    def read_config(self, file_path: str) -> Dict:
        """Reads a configuration file and returns its contents as a dictionary."""
        with open(file_path, 'r') as file:
            return json.load(file)

    def write_config(self, file_path: str, config_data: Dict) -> None:
        """Writes configuration data to a specified file."""
        with open(file_path, 'w') as file:
            json.dump(config_data, file, indent=4)

    def delete_config(self, file_path: str) -> None:
        """Deletes a specified configuration file."""
        os.remove(file_path)