import logging
import sys
from pathlib import Path
from typing import Optional


class ColoredConsoleFormatter(logging.Formatter):
    """Format console output with ANSI color codes for readability."""

    GREY = "\x1b[38;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"
    LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

    FORMATS = {
        logging.DEBUG: GREY + LOG_FORMAT + RESET,
        logging.INFO: GREY + LOG_FORMAT + RESET,
        logging.WARNING: YELLOW + LOG_FORMAT + RESET,
        logging.ERROR: RED + LOG_FORMAT + RESET,
        logging.CRITICAL: BOLD_RED + LOG_FORMAT + RESET,
    }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno, self.LOG_FORMAT)
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)


def setup_logger(
    name: str = "automation_tool",
    log_file: Optional[Path] = None,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configure and return a centralized logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        logger.handlers.clear()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(ColoredConsoleFormatter())
    logger.addHandler(console_handler)

    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(level)
        file_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger
