import json
import os
from typing import Any, Dict


class Config:
    """Configuration loader with support for defaults and file overrides."""

    DEFAULTS: Dict[str, Any] = {
        "debug": False,
        "log_level": "INFO",
        "timeout": 30,
        "max_workers": 4,
        "input_dir": "input",
        "output_dir": "output",
        "retry_attempts": 3,
        "features": ["core"],
    }

    def __init__(self, config_file: str = "config.json") -> None:
        self.config_file = config_file
        self._config = self._load()

    def _load(self) -> Dict[str, Any]:
        """Load config from file, falling back to defaults."""
        config = self.DEFAULTS.copy()
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                    config.update(loaded)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Failed to load {self.config_file}: {e}")
        # Fill in any missing defaults
        for key, value in self.DEFAULTS.items():
            if key not in config:
                config[key] = value
        return config

    def get(self, key: str, default: Any = None) -> Any:
        """Get a config value or default."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Update a config value in memory."""
        self._config[key] = value

    def save(self) -> None:
        """Write current config to the file."""
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(self._config, f, indent=4)
        except IOError as e:
            print(f"Error: Could not save config to {self.config_file}: {e}")

    def __getitem__(self, key: str) -> Any:
        if key in self._config:
            return self._config[key]
        raise KeyError(f"Config key not found: {key}")

    def __setitem__(self, key: str, value: Any) -> None:
        self._config[key] = value

    def as_dict(self) -> Dict[str, Any]:
        """Return copy of full configuration."""
        return self._config.copy()