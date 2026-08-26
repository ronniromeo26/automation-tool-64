import json
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    """Custom exception for data processing errors."""
    pass

def safe_process_payload(raw_data: Optional[str]) -> Dict[str, Any]:
    """Process raw JSON string input with robust error handling for edge cases."""
    if raw_data is None:
        logger.warning("Received null payload for processing")
        return {"status": "ignored", "reason": "null_input"}

    if not isinstance(raw_data, str):
        logger.error("Invalid payload type: expected string, got %s", type(raw_data))
        raise ProcessingError("Payload must be a string")

    if not raw_data.strip():
        logger.warning("Received empty string payload")
        return {"status": "ignored", "reason": "empty_input"}

    try:
        parsed_data = json.loads(raw_data)
    except json.JSONDecodeError as err:
        logger.error("Failed to parse JSON payload: %s", err)
        raise ProcessingError(f"Invalid JSON format: {err}") from err

    if not isinstance(parsed_data, dict):
        logger.error("Parsed JSON is not a dictionary: %s", type(parsed_data))
        raise ProcessingError("Payload root must be a JSON object")

    result = {
        "status": "success",
        "data": parsed_data,
        "item_count": len(parsed_data)
    }
    
    logger.info("Successfully processed payload with %d items", result["item_count"])
    return result
