import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "retries": 3,
    "timeout": 30,
    "log_level": "INFO"
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk with fallback to defaults."""
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load config at {config_path}: {e}")
            
    return config

def save_config(config: Dict[str, Any], config_path: str = "config.json") -> None:
    """Persists configuration dictionary to a JSON file."""
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    # Demonstration of loading sequence
    app_config = load_config()
    print(f"Loaded configuration: {app_config}")