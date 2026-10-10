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
    Loads configuration from JSON file with fallback defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load {config_path}: {e}. Using defaults.")
            
    return config

if __name__ == "__main__":
    # Example usage for automation-tool-64
    current_config = load_config()
    print(f"Active configuration: {current_config}")