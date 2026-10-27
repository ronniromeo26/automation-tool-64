import os
from pathlib import Path

# Base application paths
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"

# Ensure required directories exist
for directory in [LOG_DIR, DATA_DIR]:
    directory.mkdir(exist_ok=True)

# Environment configuration keys
ENV_PREFIX = "AT64"
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3

# Supported file extensions
SUPPORTED_EXTENSIONS = {".json", ".yaml", ".yml", ".csv"}

# Status codes for automation operations
STATUS_SUCCESS = 0
STATUS_WARNING = 1
STATUS_ERROR = 2

# Timing constants in seconds
RETRY_DELAY = 2.0
REQUEST_TIMEOUT = 10.0

# User-agent configuration
USER_AGENT = "automation-tool-64/1.0.0 (compatible; internal-task-runner)"

def get_full_path(filename: str) -> Path:
    """Helper to resolve path within the project directory."""
    return BASE_DIR / filename
