from typing import Any, Optional, Dict, Union

def validate_payload(data: Any, schema: Dict[str, type]) -> bool:
    """Validates a dictionary against a type schema."""
    if not isinstance(data, dict):
        return False

    for key, expected_type in schema.items():
        if key not in data or not isinstance(data[key], expected_type):
            return False
    return True

def sanitize_input(value: Optional[str]) -> str:
    """Trims whitespace and handles null inputs."""
    if value is None:
        return ""
    return str(value).strip()

def is_safe_identifier(name: str) -> bool:
    """Checks if string contains only safe characters."""
    return bool(name and name.isalnum())

def format_data_entry(data: Dict[str, Any]) -> Dict[str, Any]:
    """Standardizes data keys to lowercase."""
    return {k.lower(): v for k, v in data.items()}