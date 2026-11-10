import json
import os
import time
from datetime import datetime
from typing import Any, List, Dict, Optional, Callable


def generate_timestamp(fmt: str = "%Y%m%d_%H%M%S") -> str:
    """Generate a formatted timestamp string for filenames or logs."""
    return datetime.now().strftime(fmt)


def chunk_list(data: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    return [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]


def deep_merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries, giving precedence to dict2."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def safe_load_json(file_path: str, default: Optional[Any] = None) -> Any:
    """Safely load JSON data from a file, returning default on error."""
    if not os.path.exists(file_path):
        return default
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default


def retry_operation(func: Callable, retries: int = 3, delay: float = 1.0, *args, **kwargs) -> Any:
    """Retry a function execution multiple times with a specified delay."""
    last_exception = None
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            last_exception = exc
            if attempt < retries - 1:
                time.sleep(delay)
    if last_exception:
        raise last_exception
