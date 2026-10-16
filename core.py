import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_operation(max_retries=3, delay=1.0, backoff=2):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            current_delay = delay
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    retries += 1
                    if retries == max_retries:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    logger.warning(f"Attempt {retries} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_operation(max_retries=3, delay=2.0)
def fetch_data(url):
    """Example network call wrapper."""
    # Simulation of actual network request logic
    logger.info(f"Fetching data from {url}")
    return {"status": 200, "data": "sample"}