import functools
import time
import logging
from typing import Callable, Any

logger = logging.getLogger('automation-tool-64')

CACHE_TTL = 300

_cache = {}

def memoize_with_expiry(func: Callable) -> Callable:
    """Decorator to cache function results with a time-to-live mechanism."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        now = time.time()

        if key in _cache:
            result, timestamp = _cache[key]
            if now - timestamp < CACHE_TTL:
                return result

        result = func(*args, **kwargs)
        _cache[key] = (result, now)
        return result
    return wrapper

def batch_process(items: list, batch_size: int = 100):
    """Generator to yield chunks from a list for memory efficiency."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

def clear_cache() -> None:
    """Clears the internal memoization storage."""
    _cache.clear()
    logger.info("cache storage cleared")