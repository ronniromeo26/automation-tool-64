"""General data handling utilities for automation-tool-64."""

from typing import Any, Dict, List, Union


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary into single-level key-value pairs."""
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries, giving priority to dict2 values."""
    result = dict1.copy()
    for key, value in dict2.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def chunk_iterable(
    data: Union[List[Any], tuple], chunk_size: int
) -> List[List[Any]]:
    """Split a list or tuple into smaller sub-lists of a specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    return [
        list(data[i : i + chunk_size]) for i in range(0, len(data), chunk_size)
    ]
