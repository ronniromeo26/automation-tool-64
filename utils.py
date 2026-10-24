import time
import functools
import logging

# Configure logger for automation-tool-64
logger = logging.getLogger('automation-tool-64')

def retry_network_op(retries=3, delay=2, backoff=2):
    """
    Decorator for retrying network operations with exponential backoff.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed for {func.__name__}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_op(retries=3)
def fetch_data(url):
    """
    Example network operation wrapper.
    """
    # Placeholder for actual request logic
    logger.info(f"Fetching from {url}")
    return True