import re
from typing import Any, Dict

def validate_input_data(data: Dict[str, Any]) -> bool:
    """Validates dictionary structure for processing loop."""
    required_keys = {"id", "payload", "timestamp"}
    if not all(key in data for key in required_keys):
        return False

    # Validate ID format (must be alphanumeric)
    if not isinstance(data["id"], str) or not re.match(r"^[a-zA-Z0-9]+$", data["id"]):
        return False

    # Validate payload type
    if not isinstance(data["payload"], dict):
        return False

    return True

def process_data_stream(stream: list) -> list:
    """Filters and validates incoming data stream."""
    valid_records = []
    for entry in stream:
        if validate_input_data(entry):
            valid_records.append(entry)
        else:
            # Log invalid record silently
            continue
    return valid_records