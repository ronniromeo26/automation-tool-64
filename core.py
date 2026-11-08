import time
import logging
from typing import List, Dict, Any, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AutomationTask:
    """Represents a discrete automation task to be executed."""

    def __init__(self, task_id: str, payload: Dict[str, Any]) -> None:
        self.task_id = task_id
        self.payload = payload
        self.is_completed: bool = False

    def execute(self) -> bool:
        """Executes the task logic and marks as completed."""
        try:
            logger.info(f"Processing task: {self.task_id}")
            time.sleep(0.1)
            self.is_completed = True
            return True
        except Exception as e:
            logger.error(f"Task {self.task_id} failed: {e}")
            return False

class AutomationEngine:
    """Orchestrates multiple automation tasks."""

    def __init__(self, tasks: List[AutomationTask]) -> None:
        self.tasks = tasks

    def run_all(self) -> List[bool]:
        """Runs all queued tasks and returns status list."""
        results: List[bool] = []
        for task in self.tasks:
            success = task.execute()
            results.append(success)
        return results

if __name__ == "__main__":
    queue = [AutomationTask("A1", {"data": 1}), AutomationTask("A2", {"data": 2})]
    engine = AutomationEngine(queue)
    engine.run_all()