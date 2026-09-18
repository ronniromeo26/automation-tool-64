import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "enabled": True
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file, merging with system defaults.
    """
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
    current_config = load_config()
    print(f"Loaded config: {current_config}")