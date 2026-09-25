import os
import json
import logging
from typing import Any, Dict

# setup logging for the automation tool
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_json(filepath: str) -> Dict[str, Any]:
    """load and parse a json configuration file"""
    if not os.path.exists(filepath):
        logger.error(f"file not found: {filepath}")
        return {}
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"invalid json format: {e}")
        return {}

def save_json(filepath: str, data: Dict[str, Any]) -> bool:
    """serialize dictionary to a json file"""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        logger.error(f"failed to write file: {e}")
        return False

def ensure_dir(path: str) -> None:
    """verify directory existence or create it"""
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f"created directory: {path}")

def get_env_var(key: str, default: Any = None) -> Any:
    """fetch environment variables with fallback"""
    return os.environ.get(key, default)