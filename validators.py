import logging

# Configure logger for automation-tool-64
logger = logging.getLogger(__name__)

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input_data(data: dict) -> bool:
    """
    Validates the structure and content of the input dictionary.
    Ensures required keys are present and data types are valid.
    """
    required_keys = {'task_id', 'payload', 'priority'}
    
    # Check for missing keys
    if not all(key in data for key in required_keys):
        raise ValidationError(f"Missing required keys: {required_keys - data.keys()}")
    
    # Validate data types
    if not isinstance(data['task_id'], int):
        raise ValidationError("task_id must be an integer")
    
    if not isinstance(data['payload'], (dict, list)):
        raise ValidationError("payload must be a dictionary or list")
        
    if not (1 <= data.get('priority', 0) <= 10):
        raise ValidationError("priority must be between 1 and 10")
    
    return True

def process_safe(data: dict):
    """
    Wrapper for the main processing loop to handle validation.
    """
    try:
        if validate_input_data(data):
            logger.info(f"Processing task {data['task_id']} successfully")
            return True
    except ValidationError as e:
        logger.error(f"Validation failed: {e}")
        return False
    return False