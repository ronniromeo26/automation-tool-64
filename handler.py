import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-64')

class AutomationError(Exception):
    """Base exception for automation-tool-64."""
    pass

def execute_task(file_path: str, data: dict):
    """
    Executes tasks with robust error handling for edge cases.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Target path {file_path} not found")
        
        if not isinstance(data, dict) or not data:
            raise ValueError("Invalid or empty input data provided")

        # Simulate task processing
        result = data.get('key')
        if result is None:
            raise KeyError("Required key missing from input dictionary")
            
        logger.info(f"Successfully processed task at {file_path}")
        return True

    except FileNotFoundError as e:
        logger.error(f"IO error: {e}")
        return False
    except ValueError as e:
        logger.warning(f"Validation error: {e}")
        return False
    except KeyError as e:
        logger.error(f"Schema error: {e}")
        return False
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}", exc_info=True)
        raise AutomationError("Critical failure in task execution") from e