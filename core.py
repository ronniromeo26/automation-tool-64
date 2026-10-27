import logging
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def validate_item(item: Any) -> bool:
    """Validate incoming item payload structure and required fields."""
    if not isinstance(item, dict):
        logging.warning(f"Invalid input type: expected dict, got {type(item).__name__}")
        return False

    required_keys = {"id", "action", "payload"}
    if not required_keys.issubset(item.keys()):
        missing = required_keys - set(item.keys())
        logging.warning(f"Item {item.get('id', 'unknown')} missing keys: {missing}")
        return False

    if not isinstance(item["id"], (int, str)) or not str(item["id"]).strip():
        logging.warning("Item ID must be a non-empty string or integer")
        return False

    return True


def execute_task(item: Dict[str, Any]) -> Dict[str, Any]:
    """Execute processing logic for a validated task item."""
    item_id = item["id"]
    action = item["action"]
    logging.info(f"Processing task {item_id} with action '{action}'")
    return {"id": item_id, "status": "success", "details": f"Processed {action}"}


def process_batch(items: List[Any]) -> List[Dict[str, Any]]:
    """Main processing loop with input validation for batch items."""
    results = []
    for raw_item in items:
        if not validate_item(raw_item):
            logging.error(f"Skipping invalid item: {raw_item}")
            continue

        try:
            result = execute_task(raw_item)
            results.append(result)
        except Exception as err:
            logging.error(f"Failed to process task {raw_item.get('id')}: {err}")

    return results


if __name__ == "__main__":
    sample_payloads = [
        {"id": "task-101", "action": "cleanup", "payload": {}},
        {"id": "", "action": "sync", "payload": {}},
        {"id": "task-102", "payload": {}},
        "invalid_payload_format",
        {"id": "task-103", "action": "export", "payload": {"target": "/tmp"}},
    ]

    processed = process_batch(sample_payloads)
    logging.info(f"Successfully processed {len(processed)} tasks")