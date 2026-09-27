import os
import json
from pathlib import Path
from typing import Any, Dict

class ConfigurationManager:
    """Manages configuration loading, environment overrides, and workspace directory setups."""
    
    DEFAULT_CONFIG = {
        "input_dir": "./data/input",
        "output_dir": "./data/output",
        "temp_dir": "./data/temp",
        "max_retries": 3,
        "timeout_seconds": 30
    }

    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self.settings = self._load_settings()
        self._ensure_directories()

    def _load_settings(self) -> Dict[str, Any]:
        """Loads configuration from file, falling back to default settings."""
        settings = self.DEFAULT_CONFIG.copy()
        
        if self.config_path.exists() and self.config_path.is_file():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    user_config = json.load(f)
                    settings.update(user_config)
            except (json.JSONDecodeError, IOError):
                pass

        # Override with environment variables if present
        for key in settings:
            env_key = f"AUTO_TOOL_{key.upper()}"
            if env_key in os.environ:
                val = os.environ[env_key]
                if isinstance(settings[key], int):
                    try:
                        settings[key] = int(val)
                    except ValueError:
                        pass
                else:
                    settings[key] = val

        return settings

    def _ensure_directories(self) -> None:
        """Creates configured workspace directories securely if they do not exist."""
        for key in ["input_dir", "output_dir", "temp_dir"]:
            dir_path = Path(self.settings[key])
            dir_path.mkdir(parents=True, exist_ok=True)

    def get(self, key: str) -> Any:
        """Retrieves a loaded configuration value."""
        return self.settings.get(key)