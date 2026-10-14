import re
from typing import Any, Dict, Optional

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_payload(data: Dict[str, Any]) -> bool:
    """Validates mandatory schema fields for processing tasks."""
    required_fields = {"task_id": int, "payload": dict, "priority": int}

    for field, field_type in required_fields.items():
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")
        if not isinstance(data[field], field_type):
            raise ValidationError(f"Invalid type for {field}: expected {field_type.__name__}")

    if not (1 <= data["priority"] <= 10):
        raise ValidationError("Priority must be between 1 and 10")

    return True

def sanitize_input(value: str) -> str:
    """Removes potentially malicious shell injection characters."""
    if not isinstance(value, str):
        return ""
    # Allow only alphanumeric and underscores
    return re.sub(r'[^a-zA-Z0-9_]', '', value)

def validate_loop_input(data: Any) -> Optional[Dict[str, Any]]:
    """Main entry point for loop input integrity checks."""
    if not isinstance(data, dict):
        return None
    
    try:
        if validate_payload(data):
            return data
    except ValidationError:
        return None
    return None