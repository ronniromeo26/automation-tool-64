import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name: str, log_file: str = 'automation.log') -> logging.Logger:
    """
    Configures and returns a rotating file logger for automation-tool-64.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if get_logger is called multiple times
    if not logger.handlers:
        # 5MB per file, keeping 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Optional: Add stream handler for console output
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

if __name__ == '__main__':
    # Demo usage
    log = get_logger('proc_logger')
    log.info('logger initialization sequence completed')
