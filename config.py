import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30
}

def load_config(filepath: str) -> Dict[str, Any]:
    """Loads JSON configuration and merges with defaults."""
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

if __name__ == "__main__":
    # Example usage for automation-tool-64
    current_cfg = load_config("settings.json")
    print(f"Active configuration: {current_cfg}")