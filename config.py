import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "retry_attempts": 3,
    "timeout_seconds": 30,
    "log_level": "INFO",
    "enabled_features": []
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file or returns defaults."""
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

# usage example for automation-tool-64
if __name__ == "__main__":
    settings = load_config()
    print(f"Active configuration: {settings}")