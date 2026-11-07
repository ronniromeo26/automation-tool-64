import logging
import sys
from pathlib import Path

class AutomationLogger:
    """Standardized logging utility for automation-tool-64."""

    def __init__(self, name: str = "automation-tool", log_file: str = "app.log"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # File handler configuration
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Console handler configuration
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

# Global instance for project-wide access
logger_instance = AutomationLogger().get_logger()