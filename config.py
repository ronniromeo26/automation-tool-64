import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "data_dir": "./data"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from a JSON file with defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config file: {e}. Using defaults.")
    
    return config

if __name__ == "__main__":
    # Example usage
    current_config = load_config()
    print(f"Active configuration: {current_config}")