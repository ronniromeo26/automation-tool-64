import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
    "enabled": True
}

def load_config(config_path: str) -> Dict[str, Any]:
    """Loads JSON configuration with system defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config file: {e}")
            
    return config

def get_config_value(key: str, config: Dict[str, Any]) -> Any:
    """Retrieves value from config dictionary."""
    return config.get(key, DEFAULT_CONFIG.get(key))