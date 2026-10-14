import logging
import os
from typing import Any, Optional

logger = logging.getLogger('automation-tool-64')

class DataProcessingError(Exception):
    """Custom exception for operational flow issues."""
    pass

def safe_load_config(file_path: str) -> dict:
    """Reads configuration file with fallback and error validation."""
    if not os.path.exists(file_path):
        logger.error(f"config file missing at {file_path}")
        return {}

    try:
        with open(file_path, 'r') as f:
            import json
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.warning(f"failed to parse config {file_path}: {e}")
        return {}

def process_payload(data: Any) -> Optional[dict]:
    """Validates input structure before processing downstream."""
    try:
        if not isinstance(data, dict) or 'id' not in data:
            raise DataProcessingError("invalid payload schema")
            
        return {
            "processed": True,
            "id": data['id'],
            "status": "success"
        }
    except DataProcessingError as e:
        logger.error(f"payload error: {e}")
        return None
    except Exception as e:
        logger.critical(f"unexpected failure: {e}")
        return None