import time
import functools
import requests
from typing import Callable, Any

def retry_operation(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """
    Decorator to retry network operations with exponential backoff.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    if attempt == retries - 1:
                        raise e
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_operation(retries=3, delay=2.0)
def fetch_url_data(url: str) -> dict:
    """
    Example network operation fetching JSON data.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()