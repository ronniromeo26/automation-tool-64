import re
from typing import Any, Dict, Optional

# validation constraints for input processing
ALLOWED_KEYS = {'task_id', 'priority', 'payload'}
MAX_PAYLOAD_SIZE = 1024

def validate_task_input(data: Dict[str, Any]) -> Optional[str]:
    """verify input data dictionary integrity."""
    if not isinstance(data, dict):
        return "invalid input format: expected dictionary"
    
    # check for missing keys
    missing = [k for k in ALLOWED_KEYS if k not in data]
    if missing:
        return f"missing required keys: {', '.join(missing)}"
        
    # validate data types
    if not isinstance(data.get('task_id'), int):
        return "task_id must be an integer"
        
    if not isinstance(data.get('payload'), str):
        return "payload must be a string"
        
    # check payload length constraint
    if len(data['payload']) > MAX_PAYLOAD_SIZE:
        return "payload size exceeds maximum limit"
        
    # validate priority range
    priority = data.get('priority')
    if not isinstance(priority, int) or not (1 <= priority <= 5):
        return "priority must be an integer between 1 and 5"
        
    return None

def sanitize_input(text: str) -> str:
    """clean string input of suspicious characters."""
    return re.sub(r'[^a-zA-Z0-9_\-\s]', '', text)