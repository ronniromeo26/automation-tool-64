import re
from typing import Any, Optional

def validate_input_schema(data: dict) -> bool:
    """
    Validates core input structure and field requirements.
    Ensures 'task_id' is alphanumeric and 'payload' is dict.
    """
    required_fields = {'task_id': str, 'payload': dict}
    
    for field, field_type in required_fields.items():
        if field not in data or not isinstance(data[field], field_type):
            return False
            
    # Validate task_id pattern (alphanumeric, 4-12 chars)
    if not re.match(r'^[a-zA-Z0-9]{4,12}$', data['task_id']):
        return False
        
    return True

def sanitize_payload(payload: dict) -> dict:
    """
    Removes null entries and limits key count.
    """
    sanitized = {k: v for k, v in payload.items() if v is not None}
    return dict(list(sanitized.items())[:50])

if __name__ == '__main__':
    # Test validation logic
    sample = {'task_id': 'proc001', 'payload': {'mode': 'fast'}}
    is_valid = validate_input_schema(sample)
    print(f'Input validation result: {is_valid}')