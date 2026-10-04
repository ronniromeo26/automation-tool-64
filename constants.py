import os
from pathlib import Path

# Configuration paths
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / 'logs'
DATA_DIR = BASE_DIR / 'data'

# Application constraints
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

# Supported file extensions for processing
SUPPORTED_EXTENSIONS = {'.json', '.csv', '.yaml', '.txt'}

# Environment variables keys
ENV_API_KEY = 'AUTOMATION_API_KEY'
ENV_LOG_LEVEL = 'AUTOMATION_LOG_LEVEL'

# Default operation settings
DEFAULT_CHUNK_SIZE = 1024 * 1024  # 1MB
DEFAULT_ENCODING = 'utf-8'

# Ensure required directories exist on startup
for directory in [LOG_DIR, DATA_DIR]:
    directory.mkdir(exist_ok=True)

# Status codes for automation tasks
STATUS_SUCCESS = 0
STATUS_WARNING = 1
STATUS_ERROR = 2