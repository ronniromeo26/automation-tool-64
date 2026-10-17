import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


def setup_logger(
    name: str = "automation_tool",
    log_dir: str = "logs",
    log_file: str = "app.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 3,
) -> logging.Logger:
    """Configures and returns a logger instance with console and rotating file handlers."""
    # Create log directory if it does not exist
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    full_log_path = log_path / log_file

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # Standard log formatting
    log_format = logging.Formatter(
        "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Stream handler for console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Rotating file handler to manage log storage
    file_handler = RotatingFileHandler(
        full_log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    app_logger = setup_logger()
    app_logger.info("Logger configured and ready for automation tasks.")
    app_logger.warning("This is a sample warning message.")
