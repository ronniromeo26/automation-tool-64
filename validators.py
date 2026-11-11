import re
from typing import Any, Dict

def validate_input_data(data: Dict[str, Any]) -> bool:
    """Checks if input structure and types are valid."""
    required_keys = ['task_id', 'payload', 'retries']
    
    # ensure all keys exist
    if not all(key in data for key in required_keys):
        return False

    # validate task_id format
    if not isinstance(data['task_id'], str) or not re.match(r'^task-\d+$', data['task_id']):
        return False

    # validate payload constraints
    if not isinstance(data['payload'], dict):
        return False

    # validate retry count range
    if not isinstance(data['retries'], int) or not (0 <= data['retries'] <= 5):
        return False

    return True

def process_main_loop(items: list):
    """Entry point for validated batch processing."""
    for item in items:
        if validate_input_data(item):
            print(f"Processing task: {item['task_id']}")
        else:
            print(f"Skipping invalid item: {item.get('task_id', 'unknown')}")