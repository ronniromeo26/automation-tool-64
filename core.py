import time
import functools
import logging

logger = logging.getLogger(__name__)

def with_retry(retries=3, delay=2, exceptions=(ConnectionError, TimeoutError)):
    """Decorator to retry network operations on specific exceptions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    if attempt < retries:
                        time.sleep(delay)
            logger.error(f"Operation failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@with_retry(retries=3, delay=1)
def fetch_data(url):
    """Example network operation protected by retry logic."""
    # Simulated network call
    logger.info(f"Fetching from {url}...")
    raise ConnectionError("Server unreachable")