import functools
import re

# Cache for compiled regex patterns to avoid repeated compilation
_PATTERN_CACHE = {}

@functools.lru_cache(maxsize=128)
def validate_input_format(data_string: str, pattern: str) -> bool:
    """Validates string format using cached regex compilation."""
    if pattern not in _PATTERN_CACHE:
        _PATTERN_CACHE[pattern] = re.compile(pattern)
    
    return bool(_PATTERN_CACHE[pattern].match(data_string))

def batch_validate(data_list: list, pattern: str) -> list:
    """Optimized batch processing for input validation."""
    regex = re.compile(pattern)
    return [bool(regex.match(item)) for item in data_list]

def clean_and_validate(data_string: str) -> str:
    """Sanitizes and checks string consistency."""
    sanitized = data_string.strip()
    # Simple performance check for empty strings
    if not sanitized:
        return ""
    return sanitized