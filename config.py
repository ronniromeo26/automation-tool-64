import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "AutomationTool64",
    "version": "1.0.0",
    "debug": False,
    "log_level": "INFO",
    "timeout": 30,
    "max_retries": 3,
    "paths": {
        "output_dir": "./output",
        "log_dir": "./logs",
    },
}


class ConfigLoader:
    """Loads configuration files with sensible default fallbacks."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def _deep_merge(self, base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively merge user overrides into default dictionary."""
        merged = base.copy()
        for key, value in override.items():
            if isinstance(value, dict) and key in merged and isinstance(merged[key], dict):
                merged[key] = self._deep_merge(merged[key], value)
            else:
                merged[key] = value
        return merged

    def load(self) -> Dict[str, Any]:
        """Loads configuration file if present, applying overrides."""
        if not os.path.exists(self.config_path):
            return self.config

        try:
            with open(self.config_path, "r", encoding="utf-8") as file:
                user_config = json.load(file)
                if isinstance(user_config, dict):
                    self.config = self._deep_merge(DEFAULT_CONFIG, user_config)
        except (json.JSONDecodeError, OSError) as err:
            print(f"Warning: Failed to load {self.config_path} ({err}). Using defaults.")

        return self.config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option by key."""
        return self.config.get(key, default)
