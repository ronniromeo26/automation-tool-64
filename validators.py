from typing import Any, Dict, List, Optional


def validate_payload(payload: Dict[str, Any], required_keys: List[str]) -> bool:
    """Ensure all required keys are present and not None in the payload."""
    if not isinstance(payload, dict):
        return False
        
    for key in required_keys:
        if key not in payload or payload[key] is None:
            return False
            
    return True


def sanitize_string(value: Optional[str], max_length: int = 255) -> str:
    """Clean and truncate string input for safe data handling."""
    if not value:
        return ""
        
    cleaned = value.strip()
    if len(cleaned) > max_length:
        return cleaned[:max_length]
        
    return cleaned


def validate_integer_range(value: Any, min_val: int, max_val: int) -> bool:
    """Check if value is an integer within the specified inclusive range."""
    if not isinstance(value, int):
        try:
            value = int(value)
        except (ValueError, TypeError):
            return False
            
    return min_val <= value <= max_val
