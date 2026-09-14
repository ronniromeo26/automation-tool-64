import time
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def with_retry(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Execute a callable with exponential backoff on failure."""
    last_exception = None
    
    for attempt in range(retries):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            last_exception = e
            wait_time = delay * (2 ** attempt)
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
            time.sleep(wait_time)
        except Exception as e:
            logger.error(f"Unrecoverable error during execution: {e}")
            raise e
            
    logger.error("Maximum retry attempts reached.")
    raise last_exception if last_exception else Exception("Retry failed")

def fetch_data(url: str):
    """Simulated network operation wrapper."""
    def operation():
        # Placeholder for actual network logic
        return {"status": "success", "url": url}
    
    return with_retry(operation)