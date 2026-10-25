import logging
from typing import Any, Dict, List, Tuple, Optional

logger = logging.getLogger(__name__)


def validate_item(item: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """Validate raw input dictionary for required fields and types."""
    if not isinstance(item, dict):
        return False, "Item must be a dictionary"
    
    required_fields = {
        "id": (int, str),
        "action": str,
        "payload": dict
    }
    
    for field, expected_type in required_fields.items():
        if field not in item:
            return False, f"Missing required field: '{field}'"
        if not isinstance(item[field], expected_type):
            return False, f"Field '{field}' must be of type {expected_type}"

    if isinstance(item["id"], str) and not item["id"].strip():
        return False, "Field 'id' cannot be an empty string"

    return True, None


def process_batch(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Process a list of input tasks with pre-validation."""
    successful = []
    failed = []

    for idx, item in enumerate(items):
        logger.debug("Validating item at index %d", idx)
        is_valid, error_message = validate_item(item)
        
        if not is_valid:
            logger.warning("Validation failed for item %d: %s", idx, error_message)
            failed.append({"index": idx, "raw_item": item, "error": error_message})
            continue

        try:
            # Processing verified item
            result = {
                "id": item["id"],
                "status": "processed",
                "action_performed": item["action"].upper(),
                "keys_processed": len(item["payload"])
            }
            successful.append(result)
        except Exception as err:
            logger.error("Processing error on item %s: %s", item.get("id"), str(err))
            failed.append({"index": idx, "raw_item": item, "error": str(err)})

    return {
        "total_count": len(items),
        "success_count": len(successful),
        "failure_count": len(failed),
        "successful": successful,
        "failed": failed
    }
