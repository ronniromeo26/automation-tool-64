import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='automation-tool-64', log_file='app.log', level=logging.INFO):
    """
    Configures a rotating file logger for the application.
    Limits file size to 5MB with 3 backup rotations.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers if setup is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotating file handler configuration
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)

        # Console output for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Initialize default logger instance
logger = setup_logger()