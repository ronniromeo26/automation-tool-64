import json
import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


def safe_json_loads(data: str, default: Optional[Any] = None) -> Any:
    """Safely parse a JSON string, returning a default value on failure."""
    if not isinstance(data, (str, bytes)):
        logger.warning(f"Expected str or bytes for JSON parsing, got {type(data).__name__}")
        return default
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError, UnicodeDecodeError) as err:
        logger.error(f"Failed to parse JSON content: {err}")
        return default


def get_nested_value(data: Dict[str, Any], keys: List[str], default: Optional[Any] = None) -> Any:
    """Retrieve a value from nested dictionaries without raising KeyError."""
    if not isinstance(data, dict):
        return default

    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def safe_cast_int(val: Any, default: int = 0) -> int:
    """Safely convert an unknown value type to integer."""
    if val is None:
        return default
    try:
        return int(val)
    except (ValueError, TypeError):
        logger.warning(f"Unable to convert '{val}' to integer, falling back to default")
        return default
