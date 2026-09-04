import json
import os
from datetime import datetime
from typing import Any, Dict, Optional

def read_json_file(path: str) -> Dict[str, Any]:
    """Reads and parses a JSON file into a dictionary."""
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json_file(path: str, data: Dict[str, Any]) -> None:
    """Serializes dictionary data into a JSON file."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def format_timestamp() -> str:
    """Generates an ISO format timestamp for logging."""
    return datetime.now().isoformat()

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback default."""
    return os.environ.get(key, default or "")

def sanitize_filename(name: str) -> str:
    """Removes invalid characters from file names."""
    keepcharacters = (' ', '.', '_', '-')
    return "".join(c for c in name if c.isalnum() or c in keepcharacters).strip()

def batch_process(items: list, chunk_size: int = 10):
    """Yields successive chunks from a list."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]