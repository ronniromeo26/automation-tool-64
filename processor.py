import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles automated data ingestion and transformation tasks."""

    def process_payload(self, data: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        # validation of input structure
        if not isinstance(data, dict):
            logger.error("invalid payload type: expected dict, got %s", type(data))
            return {"status": "error", "message": "invalid input format"}

        try:
            # simulated resource-heavy logic
            result = self._execute_transformation(data)
            return {"status": "success", "data": result}

        except KeyError as e:
            logger.warning("missing mandatory field in payload: %s", e)
            return {"status": "error", "message": f"missing field: {e}"}
        except ValueError as e:
            logger.error("data transformation failure: %s", e)
            return {"status": "error", "message": "transformation failed"}
        except Exception as e:
            logger.exception("unexpected system error during processing")
            return {"status": "error", "message": "internal server error"}

    def _execute_transformation(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if "id" not in data:
            raise KeyError("id")
        if data.get("value", 0) < 0:
            raise ValueError("negative value not allowed")
        return {"id": data["id"], "processed": True}