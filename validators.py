import re
from typing import Any, Optional

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_task_config(config: dict) -> None:
    """Ensures config dictionary contains required operational keys."""
    required_keys = {'task_id', 'priority', 'payload'}
    
    if not isinstance(config, dict):
        raise ValidationError("Configuration must be a dictionary")
    
    missing = required_keys - config.keys()
    if missing:
        raise ValidationError(f"Missing required keys: {', '.join(missing)}")

def validate_task_id(task_id: Any) -> bool:
    """Checks if task_id matches the required alphanumeric format."""
    if not isinstance(task_id, str):
        return False
    return bool(re.match(r'^[a-zA-Z0-9_-]{4,16}$', task_id))

def validate_priority(priority: Any) -> bool:
    """Verifies priority is an integer within defined bounds."""
    if not isinstance(priority, int):
        return False
    return 1 <= priority <= 10

def process_input_validation(data: dict) -> bool:
    """Orchestrates validation logic for incoming tool payloads."""
    try:
        validate_task_config(data)
        if not validate_task_id(data['task_id']):
            raise ValidationError("Invalid task_id format")
        if not validate_priority(data['priority']):
            raise ValidationError("Priority must be between 1 and 10")
        return True
    except ValidationError:
        return False