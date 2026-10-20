import os
import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional

# Configure basic logger for automation-tool-64
logger = logging.getLogger('automation-tool-64')

def load_json_config(file_path: str) -> Dict[str, Any]:
    """Loads and parses a JSON configuration file."""
    path = Path(file_path)
    if not path.exists():
        logger.error(f"Config file missing: {file_path}")
        return {}
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.warning(f"Error reading config {file_path}: {e}")
        return {}

def ensure_directory(dir_path: str) -> bool:
    """Creates a directory if it does not exist."""
    try:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        logger.error(f"Directory creation failed for {dir_path}: {e}")
        return False

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Safely retrieves environment variables with default fallback."""
    return os.getenv(key, default or "")

def format_byte_size(size_bytes: int) -> str:
    """Converts byte counts into human readable strings."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"