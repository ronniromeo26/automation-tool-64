import re
from typing import Any, Dict

class ValidationError(Exception):
    """Raised when validation fails for edge cases."""
    pass

def validate_positive_integer(value: Any, field_name: str = "value") -> int:
    """Ensure value is positive integer, handling None and types."""
    if value is None:
        raise ValidationError(f"{field_name} cannot be None")
    try:
        if isinstance(value, float):
            if not value.is_integer():
                raise ValidationError(f"{field_name} must be integer, not float")
            value = int(value)
        elif not isinstance(value, int):
            value = int(value)
        if value <= 0:
            raise ValidationError(f"{field_name} must be greater than zero")
        return value
    except (ValueError, TypeError):
        raise ValidationError(f"{field_name} must be a valid positive integer")

def validate_non_empty_string(value: Any, field_name: str = "value") -> str:
    """Validate string is not empty or whitespace only."""
    if value is None:
        raise ValidationError(f"{field_name} cannot be None")
    if not isinstance(value, str):
        raise ValidationError(f"{field_name} must be string, got {type(value).__name__}")
    stripped = value.strip()
    if len(stripped) == 0:
        raise ValidationError(f"{field_name} cannot be empty or only whitespace")
    return stripped

def validate_email(email: Any) -> str:
    """Validate email with regex, handling edge cases."""
    email = validate_non_empty_string(email, "email")
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValidationError("Invalid email address format")
    return email.lower()

def validate_url(url: Any) -> str:
    """Validate basic URL format."""
    url = validate_non_empty_string(url, "url")
    if not url.lower().startswith(("http://", "https://")):
        raise ValidationError("URL must start with http:// or https://")
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    if not re.match(pattern, url, re.IGNORECASE):
        raise ValidationError("Invalid URL structure")
    return url

def validate_automation_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """Validate config dict for automation tool, with edge case handling."""
    if not isinstance(config, dict):
        raise ValidationError("Config must be a dictionary")
    if len(config) == 0:
        raise ValidationError("Config dictionary cannot be empty")
    validated: Dict[str, Any] = {}
    required_fields = ["target_url"]
    for field in required_fields:
        if field not in config:
            raise ValidationError(f"Missing required field: {field}")
    if "timeout" in config:
        validated["timeout"] = validate_positive_integer(config["timeout"], "timeout")
    else:
        validated["timeout"] = 60
    if "email" in config:
        validated["email"] = validate_email(config["email"])
    validated["target_url"] = validate_url(config["target_url"])
    if "retries" in config:
        retries = validate_positive_integer(config["retries"], "retries")
        if retries > 5:
            raise ValidationError("Retries must not exceed 5")
        validated["retries"] = retries
    else:
        validated["retries"] = 1
    return validated