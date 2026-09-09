import json
from typing import Any, Dict, Optional

def clean_data(data: Any) -> Any:
    """Recursively strips whitespace from string values in nested dicts/lists."""
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_data(item) for item in data]
    elif isinstance(data, str):
        return data.strip()
    return data

def safe_load_json(file_path: str) -> Optional[Dict[str, Any]]:
    """Safely loads and cleans a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            return clean_data(raw_data)
    except (json.JSONDecodeError, FileNotFoundError, IOError):
        return None

def format_output(data: Any, indent: int = 4) -> str:
    """Serializes data to a formatted JSON string."""
    try:
        return json.dumps(data, indent=indent, sort_keys=True)
    except (TypeError, ValueError):
        return str(data)

if __name__ == "__main__":
    # Example usage for testing data pipeline utilities
    sample = {" key1 ": " value1 ", "nested": [" item1 ", " item2 "]}
    cleaned = clean_data(sample)
    print(format_output(cleaned))