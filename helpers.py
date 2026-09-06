import logging
from typing import Any, Optional, Callable

logger = logging.getLogger('automation-tool-64')

def safe_execute(func: Callable, *args: Any, **kwargs: Any) -> Optional[Any]:
    """Execute function with robust error handling for edge cases."""
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid input provided to {func.__name__}: {e}")
    except ConnectionError as e:
        logger.warning(f"Network transient failure in {func.__name__}: {e}")
    except Exception as e:
        logger.critical(f"Unexpected system failure in {func.__name__}: {str(e)}")
    return None

def validate_payload(data: Any) -> bool:
    """Validate payload structure before processing automation tasks."""
    if data is None:
        return False
    
    if not isinstance(data, dict):
        return False
        
    # Ensure required keys exist and are not empty
    required_keys = ['task_id', 'payload']
    return all(key in data and data[key] is not None for key in required_keys)