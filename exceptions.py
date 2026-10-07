import time
import random
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts=3, base_delay=1.0, exceptions=(ConnectionError, TimeoutError)):
    """Decorator to retry network-related functions with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Failed after {max_attempts} attempts: {e}")
                        raise
                    
                    # Exponential backoff with jitter
                    sleep_time = (base_delay * (2 ** (attempts - 1))) + (random.uniform(0, 0.1))
                    logger.warning(f"Attempt {attempts} failed, retrying in {sleep_time:.2f}s...")
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator