import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "retries": 3,
    "timeout": 30,
    "log_level": "INFO",
    "enabled": True
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from json file, merging with defaults.
    Returns a dictionary containing final configuration values.
    """
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass

    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """
    Persists the current configuration to a json file.
    """
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)