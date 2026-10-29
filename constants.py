from typing import Final, Dict, Any

# Application-wide configuration defaults
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Supported file extensions for automation tasks
SUPPORTED_EXTENSIONS: Final[tuple[str, ...]] = ('.json', '.yaml', '.yml', '.csv')

# Log message templates
LOG_FORMAT: Final[str] = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def get_default_config() -> Dict[str, Any]:
    """Retrieve the default automation configuration dictionary."""
    return {
        "timeout": DEFAULT_TIMEOUT,
        "retries": MAX_RETRIES,
        "extensions": list(SUPPORTED_EXTENSIONS)
    }

# Environment status flags
IS_PRODUCTION: Final[bool] = False
DATABASE_URI: Final[str] = "sqlite:///automation.db"

# System constants for resource management
CHUNK_SIZE: Final[int] = 1024 * 1024  # 1MB
MAX_WORKERS: Final[int] = 4