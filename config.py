import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "retries": 3,
    "timeout": 30,
    "verbose": False,
    "output_dir": "./data"
}

def load_configuration(path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(path):
        return config
        
    try:
        with open(path, "r") as file:
            user_config = json.load(file)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_configuration(config: Dict[str, Any], path: str = "config.json") -> None:
    """Persists current configuration dictionary to file."""
    try:
        with open(path, "w") as file:
            json.dump(config, file, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")