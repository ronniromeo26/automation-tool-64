import math
import os
from typing import Any
from urllib.parse import urlparse


class ValidationError(ValueError):
    """Raised when a validation check fails for inputs."""

    pass


def validate_file_path(path: Any, must_exist: bool = False) -> str:
    """Validate and normalize a file path, checking for edge cases."""
    if not isinstance(path, (str, bytes, os.PathLike)):
        raise TypeError(f"Expected path to be string or PathLike, got {type(path).__name__}")

    str_path = str(path).strip()
    if not str_path:
        raise ValidationError("File path cannot be empty or whitespace")

    normalized = os.path.abspath(str_path)
    if must_exist and not os.path.exists(normalized):
        raise ValidationError(f"Target path does not exist: {normalized}")

    return normalized


def validate_timeout(value: Any, min_val: float = 0.1, max_val: float = 3600.0) -> float:
    """Validate timeout values against edge cases like NaN, Infinity, and invalid types."""
    if isinstance(value, bool):
        raise TypeError("Boolean value is not a valid timeout numeric input")

    try:
        numeric_val = float(value)
    except (ValueError, TypeError) as err:
        raise TypeError(f"Timeout must be a numeric value, got {type(value).__name__}") from err

    if math.isnan(numeric_val) or math.isinf(numeric_val):
        raise ValidationError("Timeout cannot be NaN or Infinite")

    if not (min_val <= numeric_val <= max_val):
        raise ValidationError(f"Timeout {numeric_val} out of bounds [{min_val}, {max_val}]")

    return numeric_val


def validate_url(url: Any) -> str:
    """Validate URL strings ensuring correct scheme and network location."""
    if not isinstance(url, str):
        raise TypeError(f"URL must be a string, got {type(url).__name__}")

    cleaned_url = url.strip()
    if not cleaned_url:
        raise ValidationError("URL string cannot be empty")

    parsed = urlparse(cleaned_url)
    if not parsed.scheme or parsed.scheme not in ("http", "https"):
        raise ValidationError("URL must use http or https scheme")

    if not parsed.netloc:
        raise ValidationError("URL is missing a valid host or domain")

    return cleaned_url
