import time
import functools
import logging

# Logger setup for automation-tool-64
logger = logging.getLogger(__name__)

def retry_operation(retries=3, delay=2, exceptions=(Exception,)):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(f"Failed after {retries} attempts: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
        return wrapper
    return decorator

@retry_operation(retries=3, delay=1)
def fetch_url_content(url):
    """Example of a network operation with retry logic."""
    # Simulating a network call here
    logger.info(f"Fetching data from {url}")
    # raise ConnectionError("Network timeout")
    return {"status": 200, "data": "sample content"}