import functools
import logging
import random
import time
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 1.5,
    jitter: bool = True,
    retry_exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    """Decorator that retries network operations with exponential backoff and jitter."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = 1.0
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retry_exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            "Operation '%s' failed after %d attempts: %s",
                            func.__name__,
                            max_retries,
                            err,
                        )
                        raise

                    sleep_time = delay * (backoff_factor ** (attempt - 1))
                    if jitter:
                        sleep_time += random.uniform(0, 0.5 * sleep_time)

                    logger.warning(
                        "Attempt %d/%d for '%s' failed (%s). Retrying in %.2fs...",
                        attempt,
                        max_retries,
                        func.__name__,
                        type(err).__name__,
                        sleep_time,
                    )
                    time.sleep(sleep_time)

        return wrapper
    return decorator