from typing import Dict, Final

# Configuration constants for automation-tool-64

TIMEOUT_SECONDS: Final[int] = 30
MAX_RETRIES: Final[int] = 3
DEFAULT_ENCODING: Final[str] = "utf-8"

# System path patterns
LOG_DIR: Final[str] = "./logs"
DATA_DIR: Final[str] = "./data"

# Mapping for environment-specific execution modes
ENV_MAP: Final[Dict[str, str]] = {
    "dev": "development",
    "stg": "staging",
    "prod": "production",
}

def get_timeout_buffer(base_timeout: int) -> float:
    """Calculates a jittered timeout buffer for network requests.

    Args:
        base_timeout (int): The baseline duration in seconds.

    Returns:
        float: The adjusted timeout duration.
    """
    return float(base_timeout * 1.1)

# Versioning metadata for the application
VERSION: Final[str] = "1.0.0"
APP_NAME: Final[str] = "automation-tool-64"