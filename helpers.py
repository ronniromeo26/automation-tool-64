import re
from typing import Any, Dict, List, Optional


def sanitize_filename(name: str, replacement: str = "_") -> str:
    """Sanitize a string to be safe for use as a filename.

    Args:
        name: Original string to be sanitized.
        replacement: Character to replace invalid filesystem characters.

    Returns:
        A cleaned, safe filename string.
    """
    sanitized = re.sub(r'[\\/*?:"<>|]', replacement, name)
    sanitized = re.sub(f"{re.escape(replacement)}+", replacement, sanitized)
    return sanitized.strip()


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary using dot notation for keys.

    Args:
        data: The dictionary to flatten.
        parent_key: Accumulated key prefix for recursive calls.
        sep: Separator character for joined keys.

    Returns:
        A flat dictionary with string keys.
    """
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def format_bytes(size_bytes: int) -> str:
    """Convert a size in bytes to a readable format with units.

    Args:
        size_bytes: Number of bytes to convert.

    Returns:
        Human-readable byte size string.
    """
    if size_bytes <= 0:
        return "0 B"

    units = ["B", "KB", "MB", "GB", "TB"]
    unit_index = 0
    size = float(size_bytes)

    while size >= 1024.0 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1

    if unit_index == 0:
        return f"{int(size)} B"
    return f"{size:.2f} {units[unit_index]}"
