import os
import re
from urllib.parse import urlparse

# Regular expression to match basic 5-field Cron expressions
CRON_REGEX = re.compile(
    r"^((((\d+,)+\d+|(\d+(\/|-)\d+)|\d+|\*)\s+){4}(((\d+,)+\d+|(\d+(\/|-)\d+)|\d+|\*)))$"
)

def is_valid_url(url: str) -> bool:
    """Verify if a string is a valid HTTP or HTTPS URL."""
    if not url:
        return False
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except ValueError:
        return False

def is_safe_path(base_directory: str, target_path: str) -> bool:
    """Ensure the target path resolves within the base directory to prevent traversal attacks."""
    try:
        resolved_base = os.path.abspath(base_directory)
        resolved_target = os.path.abspath(os.path.join(base_directory, target_path))
        return resolved_target.startswith(resolved_base)
    except (ValueError, OSError):
        return False

def is_valid_cron(expression: str) -> bool:
    """Validate if a string matches a basic 5-field cron schedule format."""
    if not expression:
        return False
    return bool(CRON_REGEX.match(expression.strip()))

def validate_execution_limit(limit: int, max_allowed: int = 86400) -> bool:
    """Verify that the execution timeout limit is within acceptable bounds."""
    return 0 < limit <= max_allowed
