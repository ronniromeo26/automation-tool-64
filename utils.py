import json
import logging
from pathlib import Path
from typing import Any, Optional, Type, Union

logger = logging.getLogger(__name__)


def safe_cast(val: Any, to_type: Type, default: Any = None) -> Any:
    """Safely cast a value to a target type handling conversion errors."""
    if val is None:
        return default
    try:
        return to_type(val)
    except (ValueError, TypeError) as err:
        logger.debug(f"Failed to cast {val!r} to {to_type.__name__}: {err}")
        return default


def get_nested_val(data: Any, key_path: str, default: Any = None) -> Any:
    """Traverse nested dict/list structures safely using dot notation."""
    if not isinstance(key_path, str) or not key_path.strip():
        return default

    keys = key_path.strip().split(".")
    current = data

    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
        elif isinstance(current, (list, tuple)):
            try:
                idx = int(key)
                current = current[idx]
            except (ValueError, IndexError):
                return default
        else:
            return default

        if current is None:
            return default

    return current


def safe_load_json(file_path: Union[str, Path], default: Optional[dict] = None) -> Any:
    """Load JSON from file path with comprehensive edge case error handling."""
    path = Path(file_path)
    if not path.exists() or not path.is_file():
        logger.warning(f"File not found or not a valid file: {path}")
        return default if default is not None else {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as err:
        logger.error(f"Invalid JSON in {path}: {err.msg} at line {err.lineno}")
        return default if default is not None else {}
    except (PermissionError, OSError) as err:
        logger.error(f"IO error reading {path}: {err}")
        return default if default is not None else {}
