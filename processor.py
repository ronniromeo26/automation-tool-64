import concurrent.futures
from typing import Any, Callable, Dict, List, Tuple


class BatchProcessor:
    """Optimized batch task processor using thread pools and result caching."""

    def __init__(self, max_workers: int = 4, cache_enabled: bool = True):
        self.max_workers = max_workers
        self.cache_enabled = cache_enabled
        self._cache: Dict[str, Any] = {}

    def _generate_key(self, task_name: str, args: Tuple[Any, ...]) -> str:
        return f"{task_name}:{hash(args)}"

    def process_task(self, func: Callable, task_name: str, *args: Any) -> Any:
        """Executes a single task with result caching when enabled."""
        if self.cache_enabled:
            cache_key = self._generate_key(task_name, args)
            if cache_key in self._cache:
                return self._cache[cache_key]

            result = func(*args)
            self._cache[cache_key] = result
            return result

        return func(*args)

    def process_batch(
        self, tasks: List[Tuple[Callable, str, Tuple[Any, ...]]]
    ) -> List[Any]:
        """Executes multiple automated tasks concurrently to improve throughput."""
        results = []
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:
            futures = [
                executor.submit(self.process_task, func, name, *args)
                for func, name, args in tasks
            ]
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
        return results

    def clear_cache(self) -> None:
        """Flushes the internal result cache."""
        self._cache.clear()
