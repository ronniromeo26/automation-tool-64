import json
from pathlib import Path
from typing import Any, Dict, List, Optional

class Config:
    """Configuration handler for automation-tool-64.

    Provides typed access to settings with load and save.
    """

    def __init__(self, config_file: Optional[str] = None) -> None:
        """Initialize config with file path.

        Args:
            config_file: Path to JSON config.
        """

        self.config_file: Path = Path(config_file) if config_file is not None else Path("config.json")
        self.data: Dict[str, Any] = {}
        self._load()

    def _load(self) -> None:
        """Load from file or use defaults."""

        if self.config_file.exists():
            with open(self.config_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = {"name": "automation-tool-64", "max_workers": 4, "timeout": 30}

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Get value for key.

        Args:
            key: Setting key.
            default: Default if absent.
        Returns:
            Value or default.
        """

        return self.data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set value for key.

        Args:
            key: Setting key.
            value: New value.
        """

        self.data[key] = value

    def save(self) -> None:
        """Persist data to config file."""

        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def get_tasks(self) -> List[str]:
        """Get task list if present.

        Returns:
            List of tasks.
        """

        return self.get("tasks", [])

def load_config(path: Optional[str] = None) -> Config:
    """Create config from optional path.

    Args:
        path: Config file location.
    Returns:
        Config instance.
    """

    return Config(path)
