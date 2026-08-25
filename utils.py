import os
import json
from datetime import datetime
from typing import Dict, Any, List

# Utility functions reorganized for better readability and maintainability

def load_json_config(filepath: str) -> Dict[str, Any]:
    """Load and return JSON configuration from file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json_config(filepath: str, data: Dict[str, Any]) -> None:
    """Save dictionary data to JSON file with formatting."""
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def get_current_timestamp() -> str:
    """Return formatted current date and time."""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def sanitize_input(text: str) -> str:
    """Clean input string by keeping only alphanumeric and spaces."""
    return ''.join(c for c in text if c.isalnum() or c.isspace()).strip()

def split_into_chunks(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """Divide a list into smaller chunks of specified size."""
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

def create_directory_if_missing(path: str) -> None:
    """Ensure the given directory path exists, creating it if needed."""
    if not os.path.exists(path):
        os.makedirs(path)

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries, with dict2 overriding dict1."""
    result = dict1.copy()
    result.update(dict2)
    return result