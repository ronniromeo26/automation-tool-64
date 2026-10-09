import time
import logging
from typing import List, Dict, Any, Optional

# Configure basic logging for automation task
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("automation-tool-64")

class AutomationEngine:
    """Handles execution of automated task sequences."""

    def __init__(self, tasks: List[Dict[str, Any]]) -> None:
        self.tasks: List[Dict[str, Any]] = tasks
        self.results: List[Optional[str]] = []

    def execute_all(self, delay: float = 0.5) -> List[Optional[str]]:
        """Executes a list of queued tasks sequentially."""
        for task in self.tasks:
            task_name = task.get("name", "unknown")
            logger.info(f"Starting task: {task_name}")
            
            try:
                result = self._process_task(task)
                self.results.append(result)
            except Exception as e:
                logger.error(f"Task {task_name} failed: {e}")
                self.results.append(None)
            
            time.sleep(delay)
        
        return self.results

    def _process_task(self, task: Dict[str, Any]) -> str:
        """Internal logic for single task execution."""
        # Logic simulating automation steps
        action = task.get("action", "noop")
        return f"Success: {action}"

if __name__ == "__main__":
    engine = AutomationEngine([{"name": "cleanup", "action": "delete_tmp"}])
    engine.execute_all()