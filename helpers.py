import os
import time
from typing import Any, Callable, Generator, Iterable, TypeVar

T = TypeVar("T")


def format_bytes(size_in_bytes: int) -> str:
    """Convert byte count into a human-readable string format."""
    byte_val = float(size_in_bytes)
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if byte_val < 1024.0:
            return f"{byte_val:.2f} {unit}"
        byte_val /= 1024.0
    return f"{byte_val:.2f} PB"


def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> Generator[list[T], None, None]:
    """Yield successive chunks of specified size from an iterable."""
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def retry_operation(
    func: Callable[..., Any],
    max_attempts: int = 3,
    delay_seconds: float = 1.0,
    *args: Any,
    **kwargs: Any,
) -> Any:
    """Retry a function call multiple times with a fixed delay upon failure."""
    last_exception = None
    for attempt in range(1, max_attempts + 1):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            last_exception = exc
            if attempt < max_attempts:
                time.sleep(delay_seconds)
    if last_exception:
        raise last_exception


def safe_filename(name: str) -> str:
    """Sanitize a string to be safely usable as a file system name."""
    keep_chars = ("-", "_", ".", " ")
    cleaned = "".join(c for c in name if c.isalnum() or c in keep_chars)
    return cleaned.strip().replace(" ", "_")
