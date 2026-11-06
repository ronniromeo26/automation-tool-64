import functools
import time
from typing import Callable, Any, Dict

# Cache for storing function results based on arguments
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache expensive function calls."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

def batch_process(items: list, batch_size: int = 100):
    """Generator to yield chunks from a list for memory efficiency."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

def timed_execution(func: Callable) -> Callable:
    """Decorator to measure execution time of functions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution of {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper