from typing import Final, Dict, Any

# Configuration constants for automation-tool-64
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Environment mapping settings
ENV_VAR_PREFIX: Final[str] = "AT64_"

# Supported operation types
OPERATION_MODES: Final[list[str]] = ["sync", "async", "batch"]

# Default logging configuration
LOG_FORMAT: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL: Final[str] = "INFO"

# System status codes
STATUS_SUCCESS: Final[int] = 0
STATUS_FAILURE: Final[int] = 1

# API request configuration
HEADERS: Final[Dict[str, str]] = {
    "Content-Type": "application/json",
    "User-Agent": "automation-tool-64-agent"
}

def get_app_metadata() -> Dict[str, Any]:
    """Returns the default application metadata configuration."""
    return {
        "timeout": DEFAULT_TIMEOUT,
        "retries": MAX_RETRIES,
        "modes": OPERATION_MODES
    }