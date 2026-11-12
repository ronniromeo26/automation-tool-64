import os
from typing import Dict, Any, Optional

class ConfigLoader:
    """Handles loading and validation of application settings."""

    def __init__(self, env: str = "development") -> None:
        self.env: str = env
        self.settings: Dict[str, Any] = {}

    def load_from_env(self, prefix: str = "APP_") -> Dict[str, Any]:
        """Extract environment variables matching the provided prefix."""
        extracted: Dict[str, Any] = {}
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                extracted[config_key] = self._parse_value(value)
        self.settings.update(extracted)
        return self.settings

    def _parse_value(self, value: str) -> Any:
        """Attempt to cast string environment values to appropriate types."""
        if value.lower() in ("true", "yes", "1"):
            return True
        if value.lower() in ("false", "no", "0"):
            return False
        try:
            return int(value)
        except ValueError:
            return value

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a configuration value by key."""
        return self.settings.get(key, default)

def get_default_config() -> ConfigLoader:
    """Factory function for a pre-configured loader instance."""
    loader = ConfigLoader()
    loader.load_from_env()
    return loader