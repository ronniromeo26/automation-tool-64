import time
import functools
import requests
from typing import Callable, Any

def retry_network_operation(max_retries: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = delay
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(current_delay)
                        current_delay *= 2
                    continue
            
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_retries=3, delay=2.0)
def fetch_url(url: str) -> str:
    """Performs a GET request with automatic retry logic."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

if __name__ == "__main__":
    try:
        content = fetch_url("https://api.example.com/data")
        print("Operation successful")
    except Exception as e:
        print(f"Operation failed after retries: {e}")