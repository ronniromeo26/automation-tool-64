import os
from pathlib import Path
from typing import Dict, Any

class AppConfig:
    """Centralized configuration management for automation-tool-64."""

    def __init__(self) -> None:
        self.base_dir: Path = Path(__file__).resolve().parent
        self.env: str = os.getenv("APP_ENV", "production")
        self.log_level: str = os.getenv("LOG_LEVEL", "INFO")
        self.timeout: int = int(os.getenv("APP_TIMEOUT", "30"))

    def get_settings(self) -> Dict[str, Any]:
        """Return dict representation of current settings."""
        return {
            "env": self.env,
            "log_level": self.log_level,
            "timeout": self.timeout,
            "base_path": str(self.base_dir)
        }

def load_config() -> AppConfig:
    """Factory function to instantiate AppConfig."""
    return AppConfig()