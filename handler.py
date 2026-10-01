import json
import logging
from typing import Any, Dict, Optional

# Configure logger for automation-tool-64
logger = logging.getLogger(__name__)

def sanitize_data(data: Any) -> Any:
    """Recursively convert complex objects to JSON-serializable types."""
    if isinstance(data, dict):
        return {str(k): sanitize_data(v) for k, v in data.items()}
    if isinstance(data, (list, tuple, set)):
        return [sanitize_data(i) for i in data]
    if hasattr(data, "__dict__"):
        return sanitize_data(vars(data))
    return data

def safe_json_dump(data: Any, filepath: str) -> bool:
    """Write data to a JSON file with error handling."""
    try:
        cleaned_data = sanitize_data(data)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(cleaned_data, f, indent=4)
        return True
    except (TypeError, IOError) as e:
        logger.error(f"failed to write data to {filepath}: {e}")
        return False

def load_json_data(filepath: str) -> Optional[Dict[str, Any]]:
    """Read and return JSON data from a file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error(f"failed to load data from {filepath}: {e}")
        return None