import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO",
    "enabled": True
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from json file with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load config file: {e}. Using defaults.")
    
    return config

if __name__ == "__main__":
    # Example usage for automation-tool-64
    current_config = load_config()
    print(f"Active configuration: {current_config}")