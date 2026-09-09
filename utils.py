import functools
import time
import logging
from typing import Callable, Any

# Configure logger for core operations
logger = logging.getLogger('automation-tool-64')

def memoize_with_ttl(ttl_seconds: int = 300):
    """Performance decorator for caching function results with TTL."""
    def decorator(func: Callable):
        cache = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            now = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process(items: list, batch_size: int = 100):
    """Generator for memory-efficient batch processing."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

def timing_decorator(func: Callable):
    """Logging decorator to monitor function execution duration."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        logger.debug(f'{func.__name__} executed in {duration:.4f}s')
        return result
    return wrapper