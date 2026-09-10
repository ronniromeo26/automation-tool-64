import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "host": "127.0.0.1",
    "port": 8080,
    "debug": False,
    "timeout": 30,
    "retry_limit": 3,
}

class ConfigLoader:
    """Loads configuration from JSON files, falling back to default values."""

    def __init__(self, filepath: str = "config.json") -> None:
        self.filepath = filepath
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from file and updates active settings."""
        if not os.path.exists(self.filepath):
            return self.config

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    self.config.update(user_config)
        except (json.JSONDecodeError, IOError):
            # Fallback to default configuration on load errors
            pass

        return self.config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a specific configuration option with an optional override default."""
        return self.config.get(key, default)
