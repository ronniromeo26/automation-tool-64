import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Optional

DEFAULT_LOG_DIR = "logs"
DEFAULT_LOG_FILE = "automation.log"
MAX_BYTES = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 5


def setup_logger(
    name: str = "automation_tool",
    log_dir: str = DEFAULT_LOG_DIR,
    log_file: str = DEFAULT_LOG_FILE,
    level: int = logging.INFO,
    max_bytes: int = MAX_BYTES,
    backup_count: int = BACKUP_COUNT,
    console_output: bool = True,
) -> logging.Logger:
    """Configures and returns a logger with rotating file and optional console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding duplicate handlers if logger is re-initialized
    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d): %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Create log directory if non-existent
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_file)

    # Set up rotating file handler
    file_handler = RotatingFileHandler(
        filename=log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Optionally output to standard console stream
    if console_output:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


# Main logger instance for default usage
app_logger = setup_logger()
