import time
import functools
import logging

# Setup basic logging for the automation tool
logger = logging.getLogger('automation-tool-64')

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """Decorator for retrying network operations on failure."""
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
                        logger.error(f"Final attempt {attempts} failed for {func.__name__}")
                        raise
                    
                    sleep_time = delay * (2 ** (attempts - 1))
                    logger.warning(f"Attempt {attempts} failed: {e}. Retrying in {sleep_time}s...")
                    time.sleep(sleep_time)
        return wrapper
    return decorator