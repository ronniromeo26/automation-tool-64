"""Data handling utilities for automation workflows."""

from typing import Any, Dict, List, Optional


def flatten_dict(data: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Recursively flatten a nested dictionary using key paths."""
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def get_nested_value(data: Dict[str, Any], path: str, default: Optional[Any] = None, sep: str = ".") -> Any:
    """Extract value from nested dictionary using dot-delimited path string."""
    keys = path.split(sep)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def sanitize_records(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Clean string fields in a list of data records by stripping whitespace."""
    sanitized_records = []
    for record in records:
        cleaned = {}
        for k, v in record.items():
            cleaned[k] = v.strip() if isinstance(v, str) else v
        sanitized_records.append(cleaned)
    return sanitized_records
