import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "timeout": 30,
    "retries": 3,
    "log_level": "INFO",
    "enabled": True
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Load configuration from json file with fallback defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            # Fallback to defaults on file read or parse error
            pass
            
    return config

def get_setting(key: str, default: Any = None) -> Any:
    """
    Fetch a specific setting from the application config.
    """
    config = load_config()
    return config.get(key, default)