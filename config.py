import os
import json
from typing import Any, Dict, Optional


class ConfigError(Exception):
    """Base exception for configuration-related errors."""
    pass


class ConfigurationLoader:
    """Loads and validates configuration from a file with environment overrides."""

    def __init__(self, default_config: Dict[str, Any]):
        self.defaults = default_config

    def load(self, filepath: Optional[str]) -> Dict[str, Any]:
        """Loads configuration from JSON file, falling back to defaults and env vars."""
        config = self.defaults.copy()

        if not filepath:
            return self._apply_env_overrides(config)

        if not os.path.exists(filepath):
            raise ConfigError(f"Configuration file not found at: {filepath}")

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                file_data = json.load(f)
        except json.JSONDecodeError as err:
            raise ConfigError(f"Malformed JSON in configuration file: {err}") from err
        except PermissionError as err:
            raise ConfigError(f"Permission denied reading config: {filepath}") from err

        if not isinstance(file_data, dict):
            raise ConfigError("Configuration root must be a JSON object/dictionary")

        # Merge keys and enforce type alignment with defaults
        for key, val in file_data.items():
            if key in config:
                if type(val) is not type(config[key]) and config[key] is not None:
                    raise ConfigError(
                        f"Type mismatch for '{key}': expected {type(config[key]).__name__}, got {type(val).__name__}"
                    )
            config[key] = val

        return self._apply_env_overrides(config)

    def _apply_env_overrides(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Overrides configuration values using matching environment variables."""
        for key, val in config.items():
            env_key = f"APP_{key.upper()}"
            env_val = os.environ.get(env_key)
            if env_val is not None:
                try:
                    if isinstance(val, bool):
                        config[key] = env_val.lower() in ("true", "1", "yes")
                    elif isinstance(val, int):
                        config[key] = int(env_val)
                    elif isinstance(val, float):
                        config[key] = float(env_val)
                    else:
                        config[key] = env_val
                except ValueError as err:
                    raise ConfigError(
                        f"Failed to cast env var {env_key} value '{env_val}' to type {type(val).__name__}"
                    ) from err
        return config
