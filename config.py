import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO",
    "enabled": True
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file or returns defaults."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

if __name__ == "__main__":
    # Example usage for automation-tool-64
    app_settings = load_config()
    print(f"Loaded settings: {app_settings}")