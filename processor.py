import json
from typing import Any, Dict, Optional

def clean_data(data: Any, strip_strings: bool = True) -> Any:
    """Recursively cleans dictionary or list data structures."""
    if isinstance(data, dict):
        return {k: clean_data(v, strip_strings) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [clean_data(item, strip_strings) for item in data]
    if isinstance(data, str) and strip_strings:
        return data.strip()
    return data

def safe_json_parse(json_str: str) -> Optional[Dict[str, Any]]:
    """Safely parses JSON strings into dictionaries."""
    try:
        parsed = json.loads(json_str)
        return parsed if isinstance(parsed, dict) else None
    except (json.JSONDecodeError, TypeError):
        return None

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens nested dictionaries for flat file storage."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)