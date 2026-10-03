from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import Any, Dict, List


class TaskPipeline:
    """Core execution pipeline with concurrent batch execution and caching."""

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self._executor = ThreadPoolExecutor(max_workers=self.max_workers)

    @lru_cache(maxsize=256)
    def _cached_transform(self, data_hash: int, raw_data: str) -> str:
        # Cache result of expensive data transformation steps
        return raw_data.strip().upper()

    def _process_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        data = item.get("data", "")
        data_hash = hash(data)
        processed = self._cached_transform(data_hash, data)
        return {"id": item.get("id"), "result": processed, "status": "success"}

    def execute_batch(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Execute a batch of tasks concurrently using worker pool."""
        if not items:
            return []
        return list(self._executor.map(self._process_item, items))

    def shutdown(self) -> None:
        """Gracefully shutdown the thread pool executor."""
        self._executor.shutdown(wait=True)
