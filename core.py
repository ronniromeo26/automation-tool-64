import time
from typing import List, Dict, Any, Callable
from functools import wraps
from concurrent.futures import ThreadPoolExecutor

class CoreEngine:
    """Core engine optimized for parallel batch processing and task caching."""

    def __init__(self, max_workers: int = 4, cache_size: int = 128):
        self.max_workers = max_workers
        self.cache_size = cache_size
        self._cache: Dict[str, Any] = {}

    def memoize_task(self, func: Callable) -> Callable:
        """Decorator to cache results of repetitive automation steps."""
        cache = self._cache

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{args}:{sorted(kwargs.items())}"
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]

        return wrapper

    def batch_process(self, items: List[Any], worker_fn: Callable, chunk_size: int = 10) -> List[Any]:
        """Execute tasks in parallel chunks to optimize runtime and RAM usage."""
        if not items:
            return []

        results = []
        chunks = [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for chunk in chunks:
                futures = [executor.submit(worker_fn, item) for item in chunk]
                results.extend([future.result() for future in futures])

        return results

    def clear_cache(self) -> None:
        """Clear in-memory cache when system memory threshold is reached."""
        self._cache.clear()
