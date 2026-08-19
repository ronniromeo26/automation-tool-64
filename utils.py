import json
from typing import Any, Dict, List


def read_json_file(file_path: str) -> Dict[str, Any]:
    """Reads a JSON file and returns its contents as a dictionary."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    """Writes a dictionary to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def merge_dictionaries(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merges two dictionaries into one, prioritizing dict2 values."""
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def filter_list(data: List[Any], condition) -> List[Any]:
    """Returns a list of items that meet the condition specified by the provided function."""
    return [item for item in data if condition(item)]


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """Flattens a list of lists into a single list."""
    return [item for sublist in nested_list for item in sublist]
