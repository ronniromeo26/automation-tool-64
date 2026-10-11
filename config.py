import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_CONFIG: Dict[str, Any] = {
    "timeout": 30,
    "max_retries": 3,
    "log_level": "INFO",
    "output_dir": "./output",
    "concurrent_jobs": 4,
    "enable_cache": True,
}


class ConfigLoader:
    """Handles loading and merging application configuration settings."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path) if config_path else None

    def load(self) -> Dict[str, Any]:
        """Load configuration from defaults, JSON file, and environment variables."""
        config = DEFAULT_CONFIG.copy()

        # Load from JSON file if path is valid and exists
        if self.config_path and self.config_path.is_file():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    file_config = json.load(f)
                    if isinstance(file_config, dict):
                        config.update(file_config)
            except (json.JSONDecodeError, OSError) as err:
                print(f"Warning: Failed to load config file ({err}). Using defaults.")

        # Override settings with matching environment variables
        env_mappings = {
            "AUTO_TIMEOUT": ("timeout", int),
            "AUTO_MAX_RETRIES": ("max_retries", int),
            "AUTO_LOG_LEVEL": ("log_level", str),
            "AUTO_OUTPUT_DIR": ("output_dir", str),
            "AUTO_CONCURRENT_JOBS": ("concurrent_jobs", int),
        }

        for env_var, (config_key, target_type) in env_mappings.items():
            val = os.getenv(env_var)
            if val is not None:
                try:
                    config[config_key] = target_type(val)
                except ValueError:
                    pass

        return config
