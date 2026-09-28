import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_operation(retries: int = 3, delay: float = 1.0, backoff: int = 2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries:
                        logger.error(f"Final attempt {attempt} failed for {func.__name__}")
                        raise e
                    
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_operation(retries=3, delay=2.0)
def fetch_url_data(url: str):
    """Example network operation function."""
    # Simulating actual network call
    import random
    if random.random() < 0.7:
        raise ConnectionError("Transient network fault")
    return {"status": "success", "url": url}