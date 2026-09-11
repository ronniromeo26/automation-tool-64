import logging
from typing import Any, Dict, List

# Set up logger for tracking validation errors
logger = logging.getLogger("automation_tool.processor")


class DataProcessor:
    """Handles the ingestion, validation, and processing of automation payloads."""

    def __init__(self) -> None:
        self.success_count = 0
        self.failure_count = 0

    def validate_payload(self, payload: Any) -> Dict[str, Any]:
        """Validates the structure and type of individual input payloads."""
        if not isinstance(payload, dict):
            raise TypeError("Payload must be a dictionary object")

        required_keys = {"job_id", "action", "data"}
        missing_keys = required_keys - payload.keys()
        if missing_keys:
            raise ValueError(f"Missing required fields: {', '.join(missing_keys)}")

        if not isinstance(payload["job_id"], (int, str)):
            raise TypeError("Field 'job_id' must be an integer or a string")

        if not isinstance(payload["action"], str) or not payload["action"].strip():
            raise ValueError("Field 'action' must be a non-empty string")

        if not isinstance(payload["data"], dict):
            raise TypeError("Field 'data' must be a dictionary")

        return payload

    def process_queue(self, queue: List[Any]) -> List[Dict[str, Any]]:
        """Iterates through the queue, applying validation prior to task execution."""
        successful_runs = []

        for index, item in enumerate(queue):
            try:
                # Enforce input validation rules inside the main processing loop
                valid_task = self.validate_payload(item)

                job_id = valid_task["job_id"]
                action_type = valid_task["action"].lower()
                payload_data = valid_task["data"]

                # Simulate execution of the validated command
                execution_result = {
                    "job_id": job_id,
                    "status": "completed",
                    "processed_action": action_type,
                    "payload_size": len(payload_data),
                }
                successful_runs.append(execution_result)
                self.success_count += 1

            except (TypeError, ValueError) as validation_err:
                self.failure_count += 1
                logger.error(
                    f"Item at index {index} failed validation: {validation_err}"
                )
            except Exception as system_err:
                self.failure_count += 1
                logger.error(
                    f"Unexpected processing failure at index {index}: {system_err}"
                )

        return successful_runs