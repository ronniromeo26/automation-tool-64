import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

def validate_input_schema(data: Any, expected_keys: list) -> bool:
    """Ensures input data is a dictionary and contains required keys."""
    try:
        if not isinstance(data, dict):
            logger.error(f"Invalid data type: expected dict, got {type(data).__name__}")
            return False
        
        missing = [key for key in expected_keys if key not in data]
        if missing:
            logger.warning(f"Missing required keys: {', '.join(missing)}")
            return False
            
        return True
    except Exception as e:
        logger.critical(f"Unexpected error during schema validation: {str(e)}")
        return False

def sanitize_path(path: Optional[str]) -> str:
    """Safely handles path strings to prevent NoneType errors."""
    if path is None:
        logger.debug("Received null path input, defaulting to empty string")
        return ""
        
    try:
        return str(path).strip()
    except (ValueError, TypeError) as e:
        logger.error(f"Sanitization failed for path input: {str(e)}")
        return ""