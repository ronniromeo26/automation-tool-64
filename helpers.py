import os
import json
import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def load_json(filepath: str) -> Optional[dict]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(filepath):
        logger.error(f"File not found: {filepath}")
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Failed to load JSON: {e}")
        return None

def save_json(data: Any, filepath: str) -> bool:
    """Writes data structure to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError as e:
        logger.error(f"Failed to save JSON: {e}")
        return False

def ensure_directory(path: str) -> None:
    """Creates target directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f"Created directory: {path}")

def get_env_variable(key: str, default: Any = None) -> Any:
    """Retrieves environment variable with fallback default."""
    return os.environ.get(key, default)