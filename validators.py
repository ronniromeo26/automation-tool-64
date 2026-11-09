import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Checks if provided string is a valid email format."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def sanitize_input(data: Any) -> str:
    """Strips whitespace and converts non-string types to string."""
    if not isinstance(data, str):
        data = str(data)
    return data.strip()

def check_required_fields(data: dict, fields: list) -> list:
    """Returns a list of missing keys from dictionary."""
    return [field for field in fields if field not in data or not data[field]]

def normalize_numeric(value: Any) -> Optional[float]:
    """Converts input to float or returns None if invalid."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None