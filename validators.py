import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input_config(data: Any) -> bool:
    """Validates configuration dictionary structure and values."""
    if not isinstance(data, dict):
        logger.error(f"Invalid configuration type: {type(data).__name__}")
        raise ValidationError("Configuration must be a dictionary")

    required_keys = ['id', 'path', 'retries']
    for key in required_keys:
        if key not in data:
            logger.warning(f"Missing required config key: {key}")
            raise ValidationError(f"Missing required key: {key}")

    if not isinstance(data.get('retries'), int) or data['retries'] < 0:
        logger.error("Invalid retry configuration detected")
        raise ValidationError("Retries must be a non-negative integer")

    return True

def safe_path_access(path: Optional[str]) -> str:
    """Sanitizes and validates filesystem paths."""
    if not path or not isinstance(path, str):
        logger.debug("Path access denied: empty or invalid path type")
        return "/tmp/default"
    
    # Prevent traversal attempts
    if '..' in path or path.startswith('/'):
        logger.warning(f"Security risk detected in path: {path}")
        raise ValidationError("Path traversal attempt or invalid absolute path")

    return path.strip()