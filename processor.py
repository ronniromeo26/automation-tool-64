import time
import logging
import urllib.error
import urllib.request
from typing import Any, Callable, Tuple, Type

logger = logging.getLogger(__name__)


class NetworkProcessor:
    """Executes network operations with configurable exponential backoff retries."""

    def __init__(
        self,
        max_retries: int = 3,
        backoff_factor: float = 1.5,
        retry_exceptions: Tuple[Type[Exception], ...] = (
            urllib.error.URLError,
            urllib.error.HTTPError,
            TimeoutError,
            ConnectionError,
        ),
    ):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.retry_exceptions = retry_exceptions

    def execute_with_retry(
        self,
        func: Callable[..., Any],
        *args: Any,
        **kwargs: Any
    ) -> Any:
        """Executes a network callable with backoff retry logic."""
        delay = 1.0
        for attempt in range(1, self.max_retries + 1):
            try:
                return func(*args, **kwargs)
            except self.retry_exceptions as exc:
                if attempt == self.max_retries:
                    logger.error(
                        "Operation failed after %d retries: %s",
                        self.max_retries,
                        exc,
                    )
                    raise exc

                sleep_time = delay * (self.backoff_factor ** (attempt - 1))
                logger.warning(
                    "Attempt %d/%d failed: %s. Retrying in %.2fs...",
                    attempt,
                    self.max_retries,
                    exc,
                    sleep_time,
                )
                time.sleep(sleep_time)


def fetch_url_data(
    url: str, timeout: float = 10.0, max_retries: int = 3
) -> bytes:
    """Helper function to fetch URL payload using network retry processor."""
    processor = NetworkProcessor(max_retries=max_retries)

    def _request():
        req = urllib.request.Request(
            url, headers={"User-Agent": "AutomationTool64/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read()

    return processor.execute_with_retry(_request)
