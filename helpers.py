import os
import re
import time
from typing import Any, Dict, List, Optional

def sanitize_filename(name: str, replacement: str = "_") -> str:
    """Clean string to make it safe for file path usage."""
    cleaned = re.sub(r'[\\/*?:"<>|]', replacement, name)
    cleaned = re.sub(r'\s+', '_', cleaned)
    return cleaned.strip("_")

def ensure_directory(path: str) -> bool:
    """Create directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        return True
    return False

def format_timestamp(epoch_time: Optional[float] = None) -> str:
    """Return ISO standard formatted timestamp string."""
    t = epoch_time if epoch_time is not None else time.time()
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

def batch_list(items: List[Any], batch_size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of specified batch size."""
    if batch_size <= 0:
        raise ValueError("Batch size must be a positive integer.")
    return [items[i:i + batch_size] for i in range(0, len(items), batch_size)]

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten nested dictionary structures for reporting."""
    items: List[tuple] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
