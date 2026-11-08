import re
import time
from functools import wraps
from typing import Any, Callable, Dict, Generator, List, Tuple


def sanitize_filename(name: str, replacement: str = "_") -> str:
    """Sanitize a string to make it safe for use as a filename."""
    cleaned = re.sub(r'[\\/*?:	
"<>|]', replacement, name)
    cleaned = cleaned.strip(". ")
    return cleaned or "unnamed"


def chunk_list(items: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """Yield successive chunks of specified size from a list."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    for i in range(0, len(items), chunk_size):
        yield items[i : i + chunk_size]


def flatten_dict(data: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flatten a nested dictionary into a single level dictionary with dotted keys."""
    items: List[Tuple[str, Any]] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def retry_operation(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator to retry a function if it raises an exception."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    if attempt == max_attempts:
                        raise err
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator
