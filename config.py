import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "retry_attempts": 3,
    "timeout": 30,
    "debug_mode": False,
    "log_level": "INFO"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with hardcoded defaults.
    """
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not read config file, using defaults: {e}")

    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """
    Persists the current configuration dictionary to a JSON file.
    """
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error: Failed to save configuration: {e}")