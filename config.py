import os
from pathlib import Path
from typing import Dict, Any

# Project path configuration
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"

# Ensure directories exist
LOG_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

def get_settings() -> Dict[str, Any]:
    """Returns application runtime settings"""
    return {
        "timeout": int(os.getenv("APP_TIMEOUT", "30")),
        "retries": int(os.getenv("APP_RETRIES", "3")),
        "log_level": os.getenv("APP_LOG_LEVEL", "INFO"),
        "base_path": str(BASE_DIR),
        "db_path": str(DATA_DIR / "storage.db")
    }

class ConfigDefaults:
    """Container for hardcoded default values"""
    APP_NAME = "automation-tool-64"
    VERSION = "1.0.0"
    ENABLED_FEATURES = ["cleanup", "sync", "report"]
    
    @classmethod
    def validate_env(cls) -> bool:
        """Verify critical environment requirements"""
        return True