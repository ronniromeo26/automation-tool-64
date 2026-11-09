import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

logger = logging.getLogger("automation_tool")


def safe_load_json(file_path: Union[str, Path], fallback: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Safely load JSON data from a file path with edge case handling."""
    default_fallback = fallback if fallback is not None else {}
    
    try:
        path = Path(file_path).resolve()
    except (ValueError, RuntimeError) as err:
        logger.error(f"Invalid path provided '{file_path}': {err}")
        return default_fallback

    if not path.exists():
        logger.warning(f"File not found: {path}")
        return default_fallback

    if not path.is_file():
        logger.error(f"Target path is not a regular file: {path}")
        return default_fallback

    try:
        if path.stat().st_size == 0:
            logger.warning(f"File is empty: {path}")
            return default_fallback

        with path.open("r", encoding="utf-8", errors="replace") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                logger.warning(f"JSON content in {path} is not a dictionary")
                return default_fallback
            return data
    except (json.JSONDecodeError, OSError) as err:
        logger.error(f"Failed to read or parse JSON file {path}: {err}")
        return default_fallback


def safe_get_nested(data: Any, keys: List[str], default: Any = None) -> Any:
    """Extract nested dict values safely handling non-dict structures and None values."""
    if not isinstance(keys, (list, tuple)):
        return default

    current = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
        if current is None:
            return default

    return current
