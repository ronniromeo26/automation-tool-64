import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


def validate_item(item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Validate incoming task payload before processing."""
    if not isinstance(item, dict):
        logger.warning(f"Invalid item type: expected dict, got {type(item).__name__}")
        return None

    task_id = item.get("id")
    if not task_id or not isinstance(task_id, (int, str)):
        logger.warning(f"Missing or invalid 'id' field in payload: {item}")
        return None

    action = item.get("action")
    if not action or not isinstance(action, str):
        logger.warning(f"Missing or invalid 'action' string for task {task_id}")
        return None

    # Extract and normalize payload structure
    payload = item.get("payload", {})
    if not isinstance(payload, dict):
        logger.warning(f"Invalid payload format for task {task_id}, using default")
        payload = {}

    return {
        "id": str(task_id),
        "action": action.strip().lower(),
        "payload": payload,
    }


def process_batch(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Process a batch of incoming items with input validation."""
    results = []
    
    for raw_item in items:
        # Validate input structure prior to execution
        validated_item = validate_item(raw_item)
        if not validated_item:
            logger.warning("Skipping invalid item in batch loop")
            continue

        try:
            logger.info(f"Processing task {validated_item['id']} ({validated_item['action']})")
            status = "completed" if validated_item["action"] != "fail" else "failed"
            results.append({
                "id": validated_item["id"],
                "status": status,
                "data": validated_item["payload"]
            })
        except Exception as err:
            logger.error(f"Error processing item {validated_item['id']}: {err}")
            results.append({"id": validated_item["id"], "status": "error", "error": str(err)})

    return results
