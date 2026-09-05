import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "automation-tool-64",
    "log_level": "INFO",
    "max_threads": 4,
    "timeout": 30,
    "output_dir": "./output",
    "retry_count": 3,
}


class ConfigLoader:
    """Loads and manages application configuration with fallback defaults."""

    def __init__(self, config_path: Optional[str] = None):
        self._config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        if config_path:
            self.load_from_file(config_path)
        self._apply_env_overrides()

    def load_from_file(self, config_path: str) -> None:
        """Load settings from a JSON file and merge with defaults."""
        path = Path(config_path)
        if path.exists() and path.is_file():
            try:
                with path.open("r", encoding="utf-8") as file:
                    file_config = json.load(file)
                    self._config.update(file_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load config from {config_path}: {err}")

    def _apply_env_overrides(self) -> None:
        """Override configuration values using matching environment variables."""
        for key in self._config:
            env_key = f"AUTO64_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                default_val = DEFAULT_CONFIG.get(key)
                if isinstance(default_val, int):
                    try:
                        self._config[key] = int(val)
                    except ValueError:
                        pass
                elif isinstance(default_val, bool):
                    self._config[key] = val.lower() in ("true", "1", "yes")
                else:
                    self._config[key] = val

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option by key with an optional fallback."""
        return self._config.get(key, default)

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of the current active configuration."""
        return self._config.copy()
