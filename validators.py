import re
from typing import Any, Optional

def validate_email(email: str) -> bool:
    """Verify email address format using regex."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_port(port: Any) -> bool:
    """Check if port is within valid range 1-65535."""
    try:
        val = int(port)
        return 1 <= val <= 65535
    except (ValueError, TypeError):
        return False

def validate_required_fields(data: dict, fields: list) -> Optional[str]:
    """Ensure all required keys exist and are not None."""
    for field in fields:
        if field not in data or data[field] is None:
            return f"missing required field: {field}"
    return None

def sanitize_string(value: str) -> str:
    """Remove non-alphanumeric characters from input."""
    return re.sub(r'[^a-zA-Z0-9_]', '', value)

def is_non_empty_string(value: Any) -> bool:
    """Check if input is a valid non-empty string."""
    return isinstance(value, str) and len(value.strip()) > 0