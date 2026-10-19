import re
from typing import Any, Optional

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input_schema(data: dict) -> bool:
    """Ensures input data contains required fields and valid formats."""
    required_fields = {'task_id': int, 'payload': str}
    
    for field, field_type in required_fields.items():
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")
        if not isinstance(data[field], field_type):
            raise ValidationError(f"Invalid type for {field}: expected {field_type.__name__}")
            
    if len(data['payload']) > 1024:
        raise ValidationError("Payload exceeds maximum character limit")
        
    return True

def sanitize_identifier(value: str) -> str:
    """Removes non-alphanumeric characters from task identifiers."""
    if not isinstance(value, str):
        raise ValidationError("Identifier must be a string")
    
    clean_value = re.sub(r'[^a-zA-Z0-9_-]', '', value)
    if not clean_value:
        raise ValidationError("Identifier is empty after sanitization")
        
    return clean_value