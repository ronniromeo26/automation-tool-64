import concurrent.futures
from functools import lru_cache
from typing import Any, Dict, List, Tuple


class AutomationCore:
    """Core execution engine for automation tasks with performance optimizations."""

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers

    @staticmethod
    @lru_cache(maxsize=256)
    def _memoized_transform(data_key: str, payload: str) -> str:
        """Cached transformation for repeated automation payloads."""
        return f"processed:{data_key}:{hash(payload)}"

    def execute_task(self, task_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a single task using fast payload lookup."""
        key = str(payload.get("key", "default"))
        data_str = str(payload.get("data", ""))
        
        result_hash = self._memoized_transform(key, data_str)
        return {"task_id": task_id, "status": "completed", "result": result_hash}

    def run_batch(
        self, tasks: List[Tuple[str, Dict[str, Any]]]
    ) -> List[Dict[str, Any]]:
        """Run batch tasks concurrently using thread pool executor."""
        if not tasks:
            return []

        results = []
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:
            futures = [
                executor.submit(self.execute_task, task_id, payload)
                for task_id, payload in tasks
            ]
            for future in concurrent.futures.as_completed(futures):
                try:
                    results.append(future.result())
                except Exception as exc:
                    results.append({"error": str(exc), "status": "failed"})

        return results

    def clear_cache(self) -> None:
        """Flush memoization cache to free memory."""
        self._memoized_transform.cache_clear()
