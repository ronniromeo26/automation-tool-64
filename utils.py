import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def with_retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries:
                        logger.error(f"Final attempt {attempt} failed for {func.__name__}")
                        raise e
                    
                    logger.warning(f"Attempt {attempt} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@with_retry(retries=3)
def fetch_data(url: str):
    """Example network operation function."""
    # Simulating actual network logic here
    print(f"Fetching from {url}")
    return {"status": 200, "data": "sample"}