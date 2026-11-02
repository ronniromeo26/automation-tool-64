import os
from typing import Dict, Any

class AppConfig:
    """Configuration management for automation-tool-64."""
    
    DEFAULT_SETTINGS = {
        "log_level": "INFO",
        "max_retries": 3,
        "timeout": 30,
        "data_dir": "./data"
    }

    def __init__(self, env_prefix: str = "AT64_") -> None:
        self.prefix = env_prefix
        self.settings = self._load_env_settings()

    def _load_env_settings(self) -> Dict[str, Any]:
        """Load overrides from environment variables."""
        config = self.DEFAULT_SETTINGS.copy()
        for key in config:
            env_key = f"{self.prefix}{key.upper()}"
            value = os.getenv(env_key)
            if value:
                config[key] = type(config[key])(value)
        return config

    def get(self, key: str) -> Any:
        """Retrieve configuration value by key."""
        return self.settings.get(key, self.DEFAULT_SETTINGS.get(key))

    def update(self, key: str, value: Any) -> None:
        """Dynamic update of configuration settings."""
        self.settings[key] = value

def get_config() -> AppConfig:
    """Singleton-like accessor for application configuration."""
    if not hasattr(get_config, "_instance"):
        get_config._instance = AppConfig()
    return get_config._instance