import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    # Default configuration values for the automation tool
    DEFAULTS: Dict[str, Any] = {
        "timeout": 30,
        "retries": 3,
        "log_level": "INFO",
        "output_dir": "./output",
        "verbose": False,
        "max_workers": 4
    }

    def __init__(self, config_path: str = "config.json") -> None:
        """Initialize the configuration loader."""
        self.config_path = config_path
        self.config: Dict[str, Any] = {}
        self._load()

    def _load(self) -> None:
        """Load configuration from file, falling back to defaults."""
        self.config = self.DEFAULTS.copy()
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    user_config = json.load(f)
                    if isinstance(user_config, dict):
                        self.config.update(user_config)
            except Exception:
                # Ignore errors and use defaults
                pass

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Get a value from config or return provided default."""
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a value in the current config."""
        self.config[key] = value

    def save(self) -> bool:
        """Save the current config to the file. Returns success status."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception:
            return False

    def get_all(self) -> Dict[str, Any]:
        """Return a copy of all configuration values."""
        return self.config.copy()

    def reset_to_defaults(self) -> None:
        """Reset config to default values."""
        self.config = self.DEFAULTS.copy()

# Example usage to demonstrate the loader
if __name__ == "__main__":
    # Create loader instance
    config = ConfigLoader("my_config.json")
    # Get some values
    print("Timeout:", config.get("timeout"))
    print("Log level:", config.get("log_level"))
    # Modify and save
    config.set("verbose", True)
    if config.save():
        print("Configuration saved.")
    # Get all
    print("Full config:", config.get_all())