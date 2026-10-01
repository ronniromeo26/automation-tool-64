import os
import json
import time
from functools import wraps
from typing import Any, Callable, Dict, Optional

def safe_read_json(file_path: str, default: Optional[Dict] = None) -> Dict:
    """Safely read a JSON file and return its content, or a default value on failure."""
    if default is None:
        default = {}
    if not os.path.exists(file_path):
        return default
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default

def ensure_directory(path: str) -> bool:
    """Create a directory path if it does not exist. Returns True if created/exists."""
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except OSError:
        return False

def retry(retries: int = 3, delay: float = 1.0) -> Callable:
    """Decorator to retry a function call if it raises an exception."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(delay)
            raise last_exception or RuntimeError('Retry failed')
        return wrapper
    return decorator
