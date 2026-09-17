from typing import List, Dict, Optional, Any

class AutomationHandler:
    """Handles execution tasks for automation-tool-64."""

    def __init__(self, task_name: str, max_retries: int = 3) -> None:
        self.task_name = task_name
        self.max_retries = max_retries
        self.history: List[Dict[str, Any]] = []

    def process_task(self, data: Dict[str, Any]) -> bool:
        """
        Processes a task with provided input data.
        Returns True if successful, False otherwise.
        """
        try:
            if not data:
                return False
            
            # Simulate processing logic
            result: Dict[str, Any] = {"status": "success", "data": data}
            self.history.append(result)
            return True
        except Exception:
            return False

    def get_logs(self) -> List[Dict[str, Any]]:
        """
        Retrieves the task history logs.
        """
        return self.history

    def reset_task(self, new_name: Optional[str] = None) -> None:
        """
        Clears execution history and optionally updates task name.
        """
        if new_name:
            self.task_name = new_name
        self.history = []