import os
from pathlib import Path

# Base application directories
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
TEMP_DIR = BASE_DIR / "temp"

# Ensure environment directories exist
LOG_DIR.mkdir(exist_ok=True)
TEMP_DIR.mkdir(exist_ok=True)

# Configuration defaults
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
CHUNK_SIZE = 1024 * 1024

# Environment variable keys
ENV_PREFIX = "AT64_"
API_KEY_VAR = f"{ENV_PREFIX}API_KEY"
LOG_LEVEL_VAR = f"{ENV_PREFIX}LOG_LEVEL"

# Supported file extensions for processing
ALLOWED_EXTENSIONS = {'.json', '.csv', '.yaml', '.txt'}

# Status codes for automation tasks
STATUS_SUCCESS = 0
STATUS_WARNING = 1
STATUS_ERROR = 2
STATUS_CRITICAL = 3

# UI/UX string defaults
APP_NAME = "automation-tool-64"
VERSION = "1.0.0"
DEFAULT_ENCODING = "utf-8"