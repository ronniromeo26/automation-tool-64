import json
from typing import Any, Dict, Optional

def safe_load_json(file_path: str) -> Optional[Dict[str, Any]]:
    """Reads and parses a JSON file with basic error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Data loading error in {file_path}: {e}")
        return None

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens nested dictionaries into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def filter_by_keys(data: Dict[str, Any], keys: list) -> Dict[str, Any]:
    """Filters dictionary to include only allowed keys."""
    return {k: v for k, v in data.items() if k in keys}