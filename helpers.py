import logging
from typing import Any, Dict, Optional

# Logger setup for automation-tool-64
logger = logging.getLogger(__name__)

def validate_input_data(data: Dict[str, Any]) -> bool:
    """Validates dictionary structure before processing."""
    required_keys = {"task_id", "payload", "priority"}
    
    if not isinstance(data, dict):
        logger.error("Invalid input type: expected dict")
        return False

    if not required_keys.issubset(data.keys()):
        missing = required_keys - data.keys()
        logger.warning(f"Missing required keys in input: {missing}")
        return False

    if not isinstance(data.get("task_id"), int):
        logger.error("Validation failure: task_id must be integer")
        return False

    return True

def sanitize_payload(payload: Any) -> Optional[str]:
    """Ensures payload string integrity."""
    try:
        if isinstance(payload, str):
            return payload.strip()[:1024]
        return str(payload)
    except Exception as e:
        logger.error(f"Sanitization error: {e}")
        return None

def process_main_loop(queue_items: list):
    """Main processing iteration with validation logic."""
    for item in queue_items:
        if not validate_input_data(item):
            continue
            
        cleaned_payload = sanitize_payload(item["payload"])
        if cleaned_payload:
            # Simulate task execution
            logger.info(f"Processing task {item['task_id']} safely")