import json
import re
import time
from pathlib import Path
from typing import Any, Callable, Generator, List, Optional, TypeVar

T = TypeVar("T")


def retry_operation(
    func: Callable[..., T],
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
) -> Callable[..., T]:
    """Retry a function call with exponential backoff on failure."""

    def wrapper(*args: Any, **kwargs: Any) -> T:
        current_delay = delay
        last_exception = None
        for attempt in range(1, retries + 1):
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                last_exception = exc
                if attempt == retries:
                    break
                time.sleep(current_delay)
                current_delay *= backoff
        raise last_exception if last_exception else RuntimeError("Operation failed")

    return wrapper


def slugify(text: str) -> str:
    """Convert text into a clean filename-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "_", text)


def chunk_list(items: List[T], chunk_size: int) -> Generator[List[T], None, None]:
    """Yield successive n-sized chunks from a list."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    for i in range(0, len(items), chunk_size):
        yield items[i : i + chunk_size]


def safe_load_json(file_path: str, default: Optional[Any] = None) -> Any:
    """Safely load JSON data from a file path with fallback default."""
    path = Path(file_path)
    if not path.is_file():
        return default
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default
