import re
from typing import Any, Dict, Optional

def validate_payload(data: Any) -> Dict[str, Any]:
    """
    Validates input schema for automation processing.
    Ensures required fields exist and match expected types.
    """
    if not isinstance(data, dict):
        raise ValueError("Payload must be a dictionary")

    required_fields = {"task_id": str, "priority": int}
    for field, expected_type in required_fields.items():
        if field not in data:
            raise KeyError(f"Missing required field: {field}")
        if not isinstance(data[field], expected_type):
            raise TypeError(f"Field {field} must be of type {expected_type.__name__}")

    return data

def validate_task_id_format(task_id: str) -> bool:
    """
    Verifies task ID follows standard naming convention.
    Allows alphanumeric strings with underscores/dashes.
    """
    pattern = r"^[a-zA-Z0-9_-]+$"
    if not re.match(pattern, task_id):
        return False
    return True

def sanitize_input(value: str) -> str:
    """
    Basic sanitization to strip potential command injection characters.
    """
    return re.sub(r"[^a-zA-Z0-9_\s-]/", "", value).strip()