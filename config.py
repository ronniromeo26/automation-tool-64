import os
from typing import Dict, Any, Optional

class Config:
    """Manages application settings and environment variables."""

    def __init__(self, env: str = "development") -> None:
        self.env: str = env
        self.settings: Dict[str, Any] = self._load_defaults()

    def _load_defaults(self) -> Dict[str, Any]:
        """Initializes default configuration parameters."""
        return {
            "timeout": 30,
            "retries": 3,
            "debug": self.env == "development"
        }

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a setting value by key."""
        return self.settings.get(key, default)

    def update(self, key: str, value: Any) -> None:
        """Updates or adds a setting value."""
        self.settings[key] = value

    @classmethod
    def from_env(cls, prefix: str = "APP_") -> "Config":
        """Creates a config instance from environment variables."""
        instance = cls()
        for key, value in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                instance.update(clean_key, value)
        return instance