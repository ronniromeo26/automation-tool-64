import time
import logging
import random
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_on_failure(
    retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """
    Decorator to retry a function call with exponential backoff on specified exceptions.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = backoff_factor
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(
                            f"Failed '{func.__name__}' after {retries} attempts. Error: {e}"
                        )
                        raise e
                    
                    # Apply jitter to avoid thundering herd problem
                    jitter = random.uniform(0.1, 0.5)
                    sleep_time = delay + jitter
                    logger.warning(
                        f"Attempt {attempt} failed for '{func.__name__}': {e}. "
                        f"Retrying in {sleep_time:.2f}s..."
                    )
                    time.sleep(sleep_time)
                    delay *= 2
            return wrapper
        return decorator

@retry_on_failure(retries=4, backoff_factor=1.0)
def execute_network_request(url: str) -> str:
    """
    Executes a network request with a timeout and returns decoded content.
    """
    import urllib.request
    with urllib.request.urlopen(url, timeout=5) as response:
        return response.read().decode('utf-8')
