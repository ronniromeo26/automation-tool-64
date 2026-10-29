import time
import functools
import logging

# Configure basic logger for automation-tool-64
logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=2, backoff=2):
    """
    Decorator to retry network-bound operations with exponential backoff.
    
    Args:
        retries: Number of attempts to make.
        delay: Initial sleep duration in seconds.
        backoff: Multiplier for the delay after each failure.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None

            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}")
                    if attempt < retries:
                        time.sleep(current_delay)
                        current_delay *= backoff
            
            logger.error(f"Final attempt failed after {retries} retries")
            raise last_exception
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=1)
def example_network_call(url):
    """
    Placeholder for actual network request logic.
    """
    # Example: raise Exception("Connection Timeout")
    return f"Successfully connected to {url}"