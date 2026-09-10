import json
import os
from typing import Any, Dict

def load_config(config_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    loads json config file and merges with provided default values.
    """
    config = defaults.copy()

    if not os.path.exists(config_path):
        return config

    try:
        with open(config_path, 'r') as f:
            user_config = json.load(f)
            if isinstance(user_config, dict):
                config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(config_path: str, config: Dict[str, Any]) -> None:
    """
    persists configuration dictionary to a json file.
    """
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)