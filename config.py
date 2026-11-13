import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-64",
    "version": "1.0.0",
    "debug": False,
    "max_workers": 4,
    "timeout": 30,
    "log_level": "INFO",
    "retry_attempts": 3,
}


class ConfigLoader:
    """Loads configuration from JSON files with fallback to built-in defaults."""

    def __init__(self, config_path: str | None = None) -> None:
        self.config_path = config_path
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Load configuration from file if available, overriding defaults."""
        if self.config_path and os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    user_config = json.load(f)
                    if isinstance(user_config, dict):
                        self._config.update(user_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load config from {self.config_path}: {err}")

        # Environment variable overrides
        if os.getenv("APP_DEBUG") is not None:
            self._config["debug"] = os.getenv("APP_DEBUG", "").lower() in ("true", "1", "yes")

        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)
