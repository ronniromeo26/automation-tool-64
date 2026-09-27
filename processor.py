import logging

def validate_input(data):
    """Ensures input data conforms to expected structure."""
    if not isinstance(data, dict):
        return False
    required_fields = ['id', 'payload']
    return all(field in data for field in required_fields)

def run_processing_loop(data_stream):
    """
    Main loop for 'automation-tool-64' processing.
    Validates input before execution to prevent runtime crashes.
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    for item in data_stream:
        if not validate_input(item):
            logger.warning(f"Skipping invalid entry: {item}")
            continue

        try:
            # Simulate core business logic processing
            process_item(item)
            logger.info(f"Successfully processed ID: {item['id']}")
        except Exception as e:
            logger.error(f"Unexpected error during processing: {e}")

def process_item(item):
    """Placeholder for core item processing logic."""
    # Actual logic would go here
    pass