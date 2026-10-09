import re
from typing import Optional

def validate_email(email: str) -> bool:
    """Validate email format using regex pattern.

    Args:
        email: The email string to validate.

    Returns:
        True if format is valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_numeric_input(value: str, min_val: Optional[int] = None) -> bool:
    """Check if input string is numeric and optionally above minimum.

    Args:
        value: String representation of a number.
        min_val: Optional lower bound integer check.

    Returns:
        True if valid numeric criteria are met.
    """
    if not value.isdigit():
        return False
    
    if min_val is not None:
        return int(value) >= min_val
    
    return True

def sanitize_identifier(name: str) -> str:
    """Remove non-alphanumeric characters from identifier strings.

    Args:
        name: Raw identifier string.

    Returns:
        Sanitized version with only alphanumerics.
    """
    return re.sub(r'[^a-zA-Z0-9]', '', name)