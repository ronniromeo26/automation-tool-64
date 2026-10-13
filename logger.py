import logging
from logging.handlers import RotatingFileHandler
import os

# configuration for automation-tool-64 logging
LOG_FILE = "automation.log"
MAX_BYTES = 5 * 1024 * 1024
BACKUP_COUNT = 3

def setup_logger(name: str = "automation-tool") -> logging.Logger:
    """Configures a rotating file logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # avoid duplicate handlers if initialized multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # rotation setup: 5MB limit per file
        handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=MAX_BYTES, 
            backupCount=BACKUP_COUNT
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # stream output for console visibility
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

if __name__ == "__main__":
    log = setup_logger()
    log.info("logger initialization complete")