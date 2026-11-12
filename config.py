import os
from typing import Dict, Any, Optional

class ConfigLoader:
    """Handles loading and validation of application settings."""

    def __init__(self, env: str = "development") -> None:
        self.env: str = env
        self.settings: Dict[str, Any] = {
            "debug": True,
            "timeout": 30,
            "db_url": os.getenv("DATABASE_URL", "sqlite:///default.db")
        }

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a setting value by key."""
        return self.settings.get(key, default)

    def update(self, key: str, value: Any) -> None:
        """Update or add a setting parameter."""
        self.settings[key] = value

    def validate(self) -> bool:
        """Check for mandatory configuration keys."""
        required_keys: list[str] = ["db_url", "timeout"]
        return all(key in self.settings for key in required_keys)

    def __repr__(self) -> str:
        return f"ConfigLoader(env={self.env}, settings_count={len(self.settings)})"