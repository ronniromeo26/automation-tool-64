"""Input validation utilities for automation workflows."""

from typing import Any, Dict, List, Union


class ValidationError(Exception):
    """Raised when data validation fails."""
    pass


def validate_task_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and sanitize automation task configuration dictionaries.
    
    Handles edge cases like missing keys, invalid types, blank strings,
    and out-of-bounds numerical parameters.
    """
    if not isinstance(config, dict):
        raise ValidationError(f"Expected dict, got {type(config).__name__}")

    if not config:
        raise ValidationError("Task configuration cannot be empty")

    sanitized = {}
    
    # Validate task_name
    task_name = config.get("task_name")
    if not task_name or not isinstance(task_name, str):
        raise ValidationError("Missing or invalid 'task_name'")
    
    sanitized_name = task_name.strip()
    if not sanitized_name:
        raise ValidationError("'task_name' cannot be blank or whitespace-only")
    sanitized["task_name"] = sanitized_name

    # Validate timeout
    timeout = config.get("timeout", 30)
    try:
        timeout_val = float(timeout)
        if timeout_val <= 0 or timeout_val > 3600:
            raise ValidationError("Timeout must be between 0 and 3600 seconds")
        sanitized["timeout"] = timeout_val
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid timeout value: {timeout}")

    # Validate retry codes
    retries = config.get("retry_codes", [500, 502, 503, 504])
    if not isinstance(retries, (list, tuple)):
        raise ValidationError("'retry_codes' must be a list or tuple")
    
    clean_codes = []
    for code in retries:
        try:
            int_code = int(code)
            if 100 <= int_code <= 599:
                clean_codes.append(int_code)
        except (ValueError, TypeError):
            continue  # Safely ignore unparseable status codes
            
    sanitized["retry_codes"] = clean_codes
    return sanitized