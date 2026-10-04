import logging

def process_items(data_list):
    """Processes a list of items with strict validation."""
    logger = logging.getLogger(__name__)
    results = []

    for index, item in enumerate(data_list):
        # Ensure item is a dictionary
        if not isinstance(item, dict):
            logger.warning(f"Skipping invalid item at index {index}: Expected dict, got {type(item).__name__}")
            continue

        # Mandatory field validation
        required_fields = ['id', 'payload']
        if not all(k in item for k in required_fields):
            logger.error(f"Validation failure at index {index}: Missing mandatory keys")
            continue

        # Type constraint validation
        if not isinstance(item.get('id'), int):
            logger.error(f"Type mismatch at index {index}: 'id' must be integer")
            continue

        # Execute processing
        try:
            processed_data = f"ID:{item['id']}_DATA:{str(item['payload'])[:10]}"
            results.append(processed_data)
        except Exception as e:
            logger.exception(f"Unexpected processing error at index {index}: {e}")

    return results