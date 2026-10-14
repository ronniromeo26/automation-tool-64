import time
from typing import Any, Dict, List, Optional

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes empty strings and null values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None and v != ""}

def format_timestamp(ts: float, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Converts a unix timestamp into a readable string format."""
    return time.strftime(fmt, time.localtime(ts))

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Splits a large list into smaller sub-lists of specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [items[i:i + size] for i in range(0, len(items), size)]

def retry_operation(func: callable, retries: int = 3, delay: float = 1.0) -> Optional[Any]:
    """Executes a function with simple retry logic on failure."""
    for attempt in range(retries):
        try:
            return func()
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(delay)
    return None