"""Data handling utilities for automation-tool-64."""

from typing import Any, Dict, List


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary structure using delimited keys.

    Args:
        data: The nested dictionary to flatten.
        parent_key: The base key prefix for recursion.
        sep: The separator string between nested keys.

    Returns:
        A single-level dictionary with flattened key paths.
    """
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict) and value:
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def clean_dict(
    data: Dict[str, Any], drop_none: bool = True, drop_empty_str: bool = False
) -> Dict[str, Any]:
    """Recursively remove unwanted key-value pairs from a dictionary.

    Args:
        data: Input dictionary to clean.
        drop_none: Remove keys where value is None.
        drop_empty_str: Remove keys where value is an empty string.

    Returns:
        A new cleaned dictionary.
    """
    cleaned = {}
    for key, value in data.items():
        if isinstance(value, dict):
            value = clean_dict(value, drop_none=drop_none, drop_empty_str=drop_empty_str)

        if drop_none and value is None:
            continue
        if drop_empty_str and value == "":
            continue

        cleaned[key] = value
    return cleaned
