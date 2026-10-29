import json
from typing import Any, Dict, Optional

def safe_load_json(file_path: str) -> Dict[str, Any]:
    """Safely load and parse a JSON file from disk."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading {file_path}: {e}")
        return {}

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten a nested dictionary structure."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_input(value: Optional[str]) -> str:
    """Remove whitespace and strip non-alphanumeric chars."""
    if not value:
        return ""
    return "".join(char for char in value.strip() if char.isalnum())

if __name__ == "__main__":
    # Test data processing
    sample = {"meta": {"id": 1}, "name": " tool_64 "}
    print(flatten_dict(sample))
    print(sanitize_input(sample['name']))