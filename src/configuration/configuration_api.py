from fastapi import APIRouter, HTTPException
from typing import Dict
from .config_files_manager.py import ConfigFilesManager
from .env_vars_loader.py import EnvVarsLoader

router = APIRouter()
config_manager = ConfigFilesManager()
env_loader = EnvVarsLoader()

@router.get("/configurations/{env}")
def get_configuration(env: str):
    try:
        config = config_manager.read_config(f'configs/{env}.json')
        return {"status": "success", "data": config}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Configuration not found.")

@router.put("/configurations/{env}")
def update_configuration(env: str, config_data: Dict):
    try:
        config_manager.write_config(f'configs/{env}.json', config_data)
        return {"status": "success", "message": "Configuration updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/configurations/{env}/reload")
def reload_configuration(env: str):
    try:
        # Implement reload logic here
        # For example, reloading environment variables
        env_loader.load_env(env)
        return {"status": "success", "message": "Configuration reloaded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))