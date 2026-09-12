import logging
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger instance for automation tasks.

    Args:
        name: The name of the module or process.
        level: The logging threshold, defaults to INFO.

    Returns:
        A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger

class TaskLogger:
    """
    Wrapper for logging automation task lifecycles.
    """
    def __init__(self, name: str) -> None:
        self.logger = get_logger(name)

    def log_start(self, task_name: str) -> None:
        """Logs the initiation of a specific automation task."""
        self.logger.info(f"Starting task: {task_name}")

    def log_error(self, message: str, exc: Optional[Exception] = None) -> None:
        """Logs task failure with optional exception traceback."""
        if exc:
            self.logger.error(f"Error in task: {message} - {str(exc)}", exc_info=True)
        else:
            self.logger.error(f"Error in task: {message}")