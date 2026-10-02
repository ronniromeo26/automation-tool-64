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
    """loads configuration from json file with defaults"""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"failed to load config, using defaults: {e}")
            
    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """persists configuration dictionary to json file"""
    try:
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"failed to save config: {e}")

if __name__ == "__main__":
    current_config = load_config()
    print(f"active configuration: {current_config}")