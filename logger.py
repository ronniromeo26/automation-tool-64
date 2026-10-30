import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = "automation.log", level: int = logging.INFO) -> logging.Logger:
    """Configures a standardized logger for automation-tool-64."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Console output handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File output handler
        log_path = Path(log_file)
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def get_log_summary(log_file: str) -> str:
    """Reads and returns the tail of the log file."""
    path = Path(log_file)
    if not path.exists():
        return "No log file found."
    
    with open(path, "r") as f:
        lines = f.readlines()[-10:]
    return "".join(lines)