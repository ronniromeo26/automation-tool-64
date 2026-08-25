import time
import random
import json
from typing import List, Dict, Any, Callable, Optional

def random_delay(min_seconds: float, max_seconds: float) -> None:
    """Introduce a random delay for automation tasks.

    Helps mimic human interaction patterns.

    Args:
        min_seconds: Minimum delay duration in seconds.
        max_seconds: Maximum delay duration in seconds.
    """
    delay: float = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)

def load_json_config(config_path: str) -> Dict[str, Any]:
    """Load configuration from a JSON file.

    Args:
        config_path: Path to the JSON configuration file.

    Returns:
        Parsed configuration as a dictionary.
    """
    with open(config_path, 'r', encoding='utf-8') as config_file:
        return json.load(config_file)

def filter_items(items: List[str], predicate: Callable[[str], bool]) -> List[str]:
    """Filter items using a predicate function.

    Args:
        items: List of items to filter.
        predicate: Function that returns True for items to include.

    Returns:
        Filtered list of items.
    """
    # List comprehension for clean filtering
    return [item for item in items if predicate(item)]

def create_batches(items: List[Any], size: int = 5) -> List[List[Any]]:
    """Divide items into batches of given size.

    Args:
        items: The list of items to batch.
        size: Size of each batch.

    Returns:
        List of batches, each a sublist.
    """
    return [items[i:i + size] for i in range(0, len(items), size)]

def retry_operation(func: Callable[[], Any], max_attempts: int = 3, delay: float = 1.0) -> Any:
    """Retry a function call up to max_attempts on exceptions.

    Args:
        func: Zero-argument function to call.
        max_attempts: Maximum number of attempts.
        delay: Seconds to wait between retries.

    Returns:
        The result from func if successful.

    Raises:
        The last exception if all attempts fail.
    """
    last_exception: Optional[Exception] = None
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            last_exception = e
            if attempt < max_attempts - 1:
                time.sleep(delay)
    if last_exception:
        raise last_exception
    raise Exception("No attempts were made")