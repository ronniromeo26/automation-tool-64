import logging
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def validate_payload(data: Dict[str, Any]) -> bool:
    """Validate incoming payload structure and required fields."""
    if not isinstance(data, dict):
        logging.warning("Invalid payload format: expected a dictionary.")
        return False

    required_keys = ["id", "action", "params"]
    missing = [key for key in required_keys if key not in data]
    if missing:
        logging.warning(f"Missing required payload keys: {missing}")
        return False

    if not isinstance(data["id"], (int, str)) or not str(data["id"]).strip():
        logging.warning("Invalid task ID: must be a non-empty string or integer.")
        return False

    if not isinstance(data["params"], dict):
        logging.warning("Invalid params format: expected a dictionary.")
        return False

    return True


def process_batch(tasks: List[Dict[str, Any]]) -> Dict[str, int]:
    """Process a batch of tasks with strict input validation in the main loop."""
    stats = {"processed": 0, "skipped": 0, "failed": 0}

    for idx, task in enumerate(tasks):
        logging.info(f"Evaluating item at index {idx}...")

        # Input validation check before execution
        if not validate_payload(task):
            logging.warning(f"Skipping item at index {idx} due to validation failure.")
            stats["skipped"] += 1
            continue

        try:
            task_id = task["id"]
            action = task["action"]
            logging.info(f"Executing task [{task_id}] with action '{action}'")
            stats["processed"] += 1
        except Exception as err:
            logging.error(f"Error executing task [{task.get('id')}]: {err}")
            stats["failed"] += 1

    return stats
