import os
from pathlib import Path

# Base application paths
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"

# Application configuration defaults
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
CHUNK_SIZE = 1024 * 1024  # 1MB chunks

# Environment specific keys
ENV_PREFIX = "AUTO64_"
API_KEY = os.getenv(f"{ENV_PREFIX}API_KEY", "default_secret_key")
DEBUG_MODE = os.getenv(f"{ENV_PREFIX}DEBUG", "False").lower() == "true"

# Supported file extensions
SUPPORTED_EXTENSIONS = {".json", ".csv", ".yaml", ".toml"}

# User agent configuration
USER_AGENT = "automation-tool-64/1.0.0"

# Log formatting configuration
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"