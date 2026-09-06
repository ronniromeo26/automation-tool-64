import re
from typing import Any, Optional

def validate_input_data(data: Any) -> bool:
    """Validates dictionary structure and field constraints."""
    if not isinstance(data, dict):
        return False

    required_fields = ['id', 'action', 'value']
    if not all(field in data for field in required_fields):
        return False

    if not isinstance(data['id'], int) or data['id'] < 0:
        return False

    if not isinstance(data['action'], str) or len(data['action']) < 3:
        return False

    # ensure value is a clean alphanumeric string or number
    if not re.match(r'^[a-zA-Z0-9_]+$', str(data['value'])):
        return False

    return True

def sanitize_input(value: Any) -> str:
    """Converts input to a safe string format."""
    return str(value).strip()

def get_validated_batch(items: list) -> list:
    """Filters a list to return only valid entries."""
    return [item for item in items if validate_input_data(item)]