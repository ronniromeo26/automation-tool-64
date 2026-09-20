import os
import json
import time
import re
from typing import Any, Callable, Dict, Optional

def sanitize_filename(filename: str, replacement: str = "_") -> str:
    """Removes or replaces characters that are invalid in filenames."""
    # Control characters, slashes, backslashes, colons, stars, question marks, quotes, angles, pipes
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', replacement, filename)
    return cleaned.strip()

def safe_load_json(file_path: str) -> Optional[Dict[str, Any]]:
    """Safely loads a JSON file, returning None if the file does not exist or is invalid."""
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def safe_write_json(file_path: str, data: Any, indent: int = 4) -> bool:
    """Safely writes data to a JSON file, creating directories if needed."""
    try:
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        return True
    except IOError:
        return False

def retry_operation(func: Callable[..., Any], retries: int = 3, delay: float = 1.0, *args: Any, **kwargs: Any) -> Any:
    """Retries a function a specified number of times if it raises an exception."""
    last_exception = None
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            last_exception = e
            if attempt < retries - 1:
                time.sleep(delay)
    raise last_exception or RuntimeError("Operation failed after retries")