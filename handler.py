import functools
import time
from typing import Callable, Any

# Cache dictionary for memoization of expensive results
_CACHE = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def process_batch(items: list, operation: Callable) -> list:
    """Batch processing with generator optimization for memory efficiency."""
    return [operation(item) for item in items]

class DataHandler:
    """Core handler with cached performance optimization."""
    def __init__(self, data: list):
        self.data = data

    @memoize
    def compute_heavy_metrics(self, multiplier: int) -> list:
        """Simulates complex calculation on dataset."""
        return [x * multiplier for x in self.data]

def run_optimization_routine(items: list) -> None:
    """Entry point for performance-optimized data handling."""
    handler = DataHandler(items)
    # Execution with cached overhead reduction
    start = time.perf_counter()
    results = handler.compute_heavy_metrics(10)
    duration = time.perf_counter() - start
    print(f"Processed {len(results)} items in {duration:.6f}s")