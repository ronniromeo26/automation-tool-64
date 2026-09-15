import os
import re
import time
from functools import wraps
from typing import Callable, Any

def ensure_directory(path: str) -> None:
    """Safely creates a directory path if it does not already exist."""
    if not path:
        return
    os.makedirs(path, exist_ok=True)

def slugify(text: str) -> str:
    """Converts a string into a URL-friendly/file-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

def retry(retries: int = 3, delay: float = 1.0) -> Callable:
    """Decorator to retry a function if it raises an exception."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(current_delay)
                        current_delay *= 2
            raise last_exception or RuntimeError("Function failed after retries")
        return wrapper
    return decorator