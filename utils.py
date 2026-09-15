import os
import json
import time
from typing import Callable, Any, Dict, Optional


def retry_on_failure(retries: int = 3, delay: float = 1.0) -> Callable:
    """Decorator to retry a function if an exception occurs."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(delay)
            raise last_exception if last_exception else RuntimeError("Failed after retries")
        return wrapper
    return decorator


def ensure_directory(path: str) -> bool:
    """Ensures that a directory exists, creating it if necessary."""
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except OSError:
        return False


def safe_read_json(filepath: str, default: Optional[Dict] = None) -> Dict:
    """Safely reads a JSON file, returning a default value on failure."""
    if default is None:
        default = {}
    if not os.path.exists(filepath):
        return default
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default
