import logging
import sys
from typing import Optional

class AutomationLogger:
    """Handles standardized logging for automation-tool-64 tasks."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        formatter: logging.Formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Logs informational messages."""
        self.logger.info(message)

    def error(self, message: str, exc_info: bool = False) -> None:
        """Logs error messages with optional traceback details."""
        self.logger.error(message, exc_info=exc_info)

def get_logger(name: str, level: int = logging.INFO) -> AutomationLogger:
    """Factory function for creating an AutomationLogger instance."""
    return AutomationLogger(name, level)