import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with default values.
    """
    config = defaults.copy()

    if not os.path.exists(path):
        return config

    try:
        with open(path, 'r') as file:
            user_config = json.load(file)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, IOError) as e:
        # Silently revert to defaults if configuration file is corrupted
        print(f"Warning: Could not load config {path}: {e}")

    return config

def save_config(path: str, data: Dict[str, Any]) -> None:
    """
    Saves configuration dictionary to a JSON file.
    """
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)