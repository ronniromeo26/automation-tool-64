import os
import shutil
import tempfile
from contextlib import contextmanager
from typing import Any, Callable, List, Optional


class AutomationEngine:
    """Core engine managing task execution and temporary working resources."""

    def __init__(self, work_dir: Optional[str] = None) -> None:
        self.work_dir = work_dir or tempfile.mkdtemp(prefix="auto_tool_")
        self.tasks: List[Callable[[], Any]] = []

    def register_task(self, task_func: Callable[[], Any]) -> None:
        """Register an automation step function for execution."""
        self.tasks.append(task_func)

    @contextmanager
    def execution_context(self):
        """Context manager preparing task runtime and ensuring resource cleanup."""
        os.makedirs(self.work_dir, exist_ok=True)
        try:
            yield self.work_dir
        finally:
            self.cleanup()

    def run_all(self) -> List[Any]:
        """Execute all registered tasks within an isolated context."""
        results = []
        with self.execution_context():
            for task in self.tasks:
                results.append(task())
        return results

    def cleanup(self) -> None:
        """Remove temporary directory and artifacts generated during execution."""
        if os.path.exists(self.work_dir):
            shutil.rmtree(self.work_dir, ignore_errors=True)


def create_pipeline(steps: List[Callable[[], Any]], temp_path: Optional[str] = None) -> AutomationEngine:
    """Helper function to construct and initialize a task pipeline."""
    engine = AutomationEngine(work_dir=temp_path)
    for step in steps:
        engine.register_task(step)
    return engine