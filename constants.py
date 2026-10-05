import os
from pathlib import Path

# Base directories for automation storage
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = BASE_DIR / "data"
DEFAULT_LOG_DIR = BASE_DIR / "logs"

# Network and process limits
DEFAULT_TIMEOUT_SECONDS = 30
MAX_RETRIES = 3
BACKOFF_FACTOR_SECONDS = 1.5

# File operations and encoding
DEFAULT_ENCODING = "utf-8"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_ONLY_FORMAT = "%Y-%m-%d"

# Execution status tracking state strings
STATUS_PENDING = "pending"
STATUS_RUNNING = "running"
STATUS_SUCCESS = "success"
STATUS_FAILED = "failed"

# Environment variable lookup keys
ENV_API_KEY = "AUTOMATION_API_KEY"
ENV_ENVIRONMENT = "AUTOMATION_ENV"
ENV_LOG_LEVEL = "AUTOMATION_LOG_LEVEL"

# Process termination and exit codes
EXIT_CODE_SUCCESS = 0
EXIT_CODE_ERROR = 1
EXIT_CODE_CONFIG_INVALID = 2
