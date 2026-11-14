import json
import os
from typing import Any, Optional

def load_json_file(filepath: str) -> dict[str, Any]:
    """Reads and parses a JSON file with basic error handling."""
    if not os.path.exists(filepath):
        return {}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_json_file(filepath: str, data: dict[str, Any]) -> bool:
    """Writes a dictionary to a JSON file safely."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def sanitize_key(key: str) -> str:
    """Converts a string to a standard snake_case format."""
    return key.strip().lower().replace(' ', '_')

def get_nested_value(data: dict, keys: list[str], default: Any = None) -> Any:
    """Retrieves a value from a deeply nested dictionary."""
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
        else:
            return default
    return current if current is not None else default