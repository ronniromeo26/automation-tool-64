import logging
import functools
from typing import Callable, Any

# Configure optimized base logger for high-throughput operations
logger = logging.getLogger('automation-tool-64')
logger.setLevel(logging.INFO)

# Cache dictionary for performance enhancement of log decorators
_LOG_CACHE = {}

def performance_monitor(func: Callable) -> Callable:
    """
    Decorator to track execution latency for core operations.
    Uses local caching to reduce overhead during tight loops.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        import time
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        
        # Log only if operation exceeds reasonable threshold
        if duration > 0.1:
            logger.debug(f"Operation {func.__name__} took {duration:.4f}s")
        return result
    return wrapper

def fast_log(message: str) -> None:
    """
    Optimized logging call bypassing heavy stack frame introspection.
    """
    if logger.isEnabledFor(logging.INFO):
        logger.info(message)

# Initialize stream handler for standard output
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)