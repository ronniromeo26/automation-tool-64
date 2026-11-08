from typing import Any, Dict, List, Tuple


class ValidationError(Exception):
    """Raised when input task fails validation checks."""
    pass


def validate_task_payload(item: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Validates a single data payload before processing.
    Checks for required structure, data types, and value constraints.
    """
    if not isinstance(item, dict):
        return False, "Task item must be a dictionary"

    required_keys = ["task_id", "command", "params"]
    for key in required_keys:
        if key not in item:
            return False, f"Missing required payload key: '{key}'"

    if not str(item["task_id"]).isalnum():
        return False, "'task_id' must be alphanumeric"

    allowed_commands = ["fetch", "transform", "export", "clean"]
    if item["command"] not in allowed_commands:
        return False, f"Unsupported command '{item['command']}'. Allowed: {allowed_commands}"

    if not isinstance(item["params"], dict):
        return False, "'params' must be a key-value dictionary"

    return True, "Validation successful"


def sanitize_loop_input(raw_items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Filters raw inputs for the main processing loop, skipping invalid entries.
    """
    valid_items = []
    for idx, raw_item in enumerate(raw_items):
        is_valid, message = validate_task_payload(raw_item)
        if is_valid:
            valid_items.append(raw_item)
        else:
            # Record rejected item for loop skip
            print(f"Validation failed at index {idx}: {message}")
            
    return valid_items
