import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO",
    "enabled": True
}

class ConfigLoader:
    """Handles loading and merging of application settings."""

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath

    def load(self) -> Dict[str, Any]:
        """Loads configuration from disk or returns defaults."""
        config = DEFAULT_CONFIG.copy()

        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    user_config = json.load(f)
                    config.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass

        return config

def get_config() -> Dict[str, Any]:
    """Helper to fetch active configuration instance."""
    loader = ConfigLoader()
    return loader.load()