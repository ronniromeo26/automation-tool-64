from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional
import time


@dataclass
class TaskResult:
    task_id: str
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None
    execution_time: float = 0.0


class BatchProcessor:
    """Handles sequential execution of automation steps with result tracking."""

    def __init__(self, name: str = "default_processor"):
        self.name = name
        self.handlers: Dict[str, Callable[..., Any]] = {}

    def register_handler(self, action: str, handler: Callable[..., Any]) -> None:
        """Register a handler function for a specific action type."""
        self.handlers[action] = handler

    def process_item(self, task_id: str, action: str, payload: Dict[str, Any]) -> TaskResult:
        """Execute a registered action handler on a payload."""
        if action not in self.handlers:
            return TaskResult(
                task_id=task_id,
                success=False,
                error=f"No handler registered for action: '{action}'"
            )

        start_time = time.perf_counter()
        try:
            result_data = self.handlers[action](payload)
            elapsed = time.perf_counter() - start_time
            return TaskResult(
                task_id=task_id,
                success=True,
                data=result_data,
                execution_time=round(elapsed, 4)
            )
        except Exception as err:
            elapsed = time.perf_counter() - start_time
            return TaskResult(
                task_id=task_id,
                success=False,
                error=str(err),
                execution_time=round(elapsed, 4)
            )

    def process_batch(self, items: List[Dict[str, Any]]) -> List[TaskResult]:
        """Process a list of task items sequentially."""
        results = []
        for item in items:
            task_id = item.get("id", "unknown")
            action = item.get("action", "")
            payload = item.get("payload", {})
            results.append(self.process_item(task_id, action, payload))
        return results