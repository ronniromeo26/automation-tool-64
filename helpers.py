import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, delay=2, backoff=2):
    """Decorator for retrying functions on network exceptions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_attempts:
                        logger.error(f"Final attempt {attempt} failed for {func.__name__}")
                        raise e
                    
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

def execute_with_retry(func, *args, **kwargs):
    """Functional wrapper for one-off retry logic."""
    return retry_network_operation()(func)(*args, **kwargs)