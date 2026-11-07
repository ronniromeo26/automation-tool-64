import json
import os
from typing import Any, Optional

def load_json_file(file_path: str) -> dict:
    """Reads and parses a JSON file into a dictionary."""
    if not os.path.exists(file_path):
        return {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_json_file(file_path: str, data: Any) -> bool:
    """Writes data to a JSON file with pretty formatting."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, sort_keys=True)
        return True
    except (IOError, TypeError):
        return False

def safe_get(data: dict, key: str, default: Any = None) -> Any:
    """Retrieves nested dictionary values safely."""
    keys = key.split('.')
    current = data
    try:
        for k in keys:
            current = current[k]
        return current
    except (KeyError, TypeError):
        return default

def sanitize_data(data: dict) -> dict:
    """Recursively removes null values from a dictionary."""
    return {
        k: v for k, v in data.items() 
        if v is not None and (not isinstance(v, dict) or sanitize_data(v))
    }