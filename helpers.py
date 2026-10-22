import logging
import os
from typing import Any, Optional

logger = logging.getLogger('automation-tool-64')

def safe_load_env(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback."""
    try:
        value = os.getenv(key)
        if value is None:
            if default is None:
                raise KeyError(f"Environment variable {key} not set")
            return default
        return value
    except Exception as e:
        logger.error(f"Unexpected error reading {key}: {e}")
        raise

def parse_config_int(value: Any) -> int:
    """Safely converts config values to integers."""
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        logger.warning(f"Invalid integer config '{value}': {e}. Defaulting to 0.")
        return 0

def execute_task(func: callable, *args: Any, **kwargs: Any) -> Any:
    """Wraps task execution with generic error handling."""
    try:
        return func(*args, **kwargs)
    except PermissionError:
        logger.error("Insufficient permissions to perform task")
    except FileNotFoundError:
        logger.error("Required file missing from file system")
    except Exception as e:
        logger.exception(f"Unexpected critical failure: {e}")
    return None