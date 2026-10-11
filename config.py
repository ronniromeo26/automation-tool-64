import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO",
    "enabled": True
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from a JSON file with defaults."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: could not load config file: {e}. Using defaults.")

    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """Persists configuration dictionary to a JSON file."""
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error: failed to save config: {e}")