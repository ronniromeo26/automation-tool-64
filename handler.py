import os
import json
import shutil
import logging
import time
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

def safe_load_json(file_path: str) -> Dict[str, Any]:
    """Safely loads a JSON file, returning an empty dict on failure."""
    if not os.path.exists(file_path):
        logger.warning(f"File not found: {file_path}")
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Failed to read JSON from {file_path}: {e}")
        return {}

def ensure_directory(dir_path: str) -> bool:
    """Creates a directory if it does not exist."""
    try:
        os.makedirs(dir_path, exist_ok=True)
        return True
    except OSError as e:
        logger.error(f"Failed to create directory {dir_path}: {e}")
        return False

def archive_file(source_path: str, dest_dir: str) -> Optional[str]:
    """Moves a file to an archive directory with a timestamp to prevent overwrites."""
    if not os.path.isfile(source_path):
        logger.error(f"Source file does not exist: {source_path}")
        return None
    
    if not ensure_directory(dest_dir):
        return None

    filename = os.path.basename(source_path)
    base, ext = os.path.splitext(filename)
    timestamp = int(time.time())
    new_filename = f"{base}_{timestamp}{ext}"
    dest_path = os.path.join(dest_dir, new_filename)

    try:
        shutil.move(source_path, dest_path)
        return dest_path
    except OSError as e:
        logger.error(f"Failed to move file to {dest_path}: {e}")
        return None