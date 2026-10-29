import os
from pathlib import Path

# Base application directories
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
TEMP_DIR = BASE_DIR / "temp"

# Configuration settings
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
CHUNK_SIZE = 1024 * 8

# Supported file extensions for automation
SUPPORTED_EXTENSIONS = {'.txt', '.json', '.csv', '.yaml'}

# Environment specific keys
API_KEY_ENV = "AUTOMATION_API_KEY"
DB_CONNECTION_STR = os.getenv("DB_URL", "sqlite:///default.db")

# Logging format and levels
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"

# Task processing constraints
CONCURRENT_TASKS = 4
IDLE_THRESHOLD_SECONDS = 300

def ensure_directories():
    """Initialize application filesystem structure."""
    for directory in [LOG_DIR, TEMP_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    ensure_directories()