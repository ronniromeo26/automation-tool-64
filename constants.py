import os
from pathlib import Path

# Base application directories
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

# Ensure required directories exist
for directory in [DATA_DIR, LOG_DIR]:
    directory.mkdir(exist_ok=True)

# Configuration settings
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
CHUNK_SIZE = 1024 * 8

# Supported file extensions
ALLOWED_EXTENSIONS = {".json", ".csv", ".txt"}

# Application identification
APP_NAME = "automation-tool-64"
VERSION = "1.2.0"

# Environment variables fallback
API_KEY = os.getenv("APP_API_KEY", "default-secret-key")
DEBUG_MODE = os.getenv("APP_DEBUG", "False").lower() in ("true", "1")

# Formatting constants
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"