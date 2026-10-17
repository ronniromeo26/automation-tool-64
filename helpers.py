import logging
from typing import Any, Callable, Sequence, Type, Union

logger = logging.getLogger(__name__)


def safe_get_nested(data: Any, path: Sequence[Union[str, int]], default: Any = None) -> Any:
    """Safely retrieve a value from nested dictionaries or lists using a key path."""
    current = data
    for key in path:
        if current is None:
            return default
        try:
            if isinstance(current, dict) and isinstance(key, str):
                current = current.get(key, default)
            elif isinstance(current, (list, tuple)) and isinstance(key, int):
                if 0 <= key < len(current):
                    current = current[key]
                else:
                    return default
            else:
                return default
        except (TypeError, KeyError, IndexError, AttributeError) as err:
            logger.debug(f"Error accessing key '{key}' in path {path}: {err}")
            return default
    return current


def safe_cast(value: Any, target_type: Type, default: Any = None) -> Any:
    """Safely cast a value to a target type, returning default on failure."""
    if value is None:
        return default
    try:
        return target_type(value)
    except (ValueError, TypeError) as err:
        logger.debug(f"Failed to cast '{value}' to {target_type.__name__}: {err}")
        return default


def execute_with_fallback(func: Callable, fallback_val: Any, *args: Any, **kwargs: Any) -> Any:
    """Execute a callable with args and return fallback_val if an exception occurs."""
    try:
        return func(*args, **kwargs)
    except Exception as err:
        logger.warning(f"Operation failed with error: {err}. Returning fallback.")
        return fallback_val
