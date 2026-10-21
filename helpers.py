import logging
import os
from typing import Any, Optional, Union

logger = logging.getLogger(__name__)

def safe_file_read(filepath: str, default: Any = None) -> Union[str, Any]:
    """Reads file content with robust error handling for common edge cases."""
    if not filepath or not isinstance(filepath, str):
        logger.error(f"Invalid filepath provided: {filepath}")
        return default

    try:
        if not os.path.exists(filepath):
            logger.warning(f"File path does not exist: {filepath}")
            return default

        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
            
    except PermissionError:
        logger.error(f"Insufficient permissions to read: {filepath}")
    except OSError as e:
        logger.error(f"OS error occurred while reading {filepath}: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error reading {filepath}: {e}")
        
    return default

def parse_int_safe(value: Any, fallback: int = 0) -> int:
    """Converts input to integer with fallback for invalid types."""
    try:
        return int(value)
    except (ValueError, TypeError):
        logger.debug(f"Failed to convert {value} to int, returning fallback")
        return fallback