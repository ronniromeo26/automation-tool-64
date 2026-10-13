import logging

def process_items(items):
    """Main processing loop for automation-tool-64."""
    logger = logging.getLogger(__name__)
    
    for item in items:
        try:
            # Validate input format and presence of required keys
            if not isinstance(item, dict) or 'id' not in item:
                logger.warning(f"Skipping invalid item: {item}")
                continue
                
            if not isinstance(item.get('payload'), (str, int)):
                logger.error(f"Invalid payload type for id: {item['id']}")
                continue

            # Execution logic for valid items
            result = perform_task(item)
            logger.info(f"Processed {item['id']}: {result}")
            
        except Exception as e:
            logger.error(f"Unexpected error processing item {item}: {e}")

def perform_task(item):
    """Business logic stub for automation tasks."""
    return f"success-{item['id']}"

if __name__ == '__main__':
    data = [{'id': 1, 'payload': 'test'}, {'id': 2, 'payload': 100}, {'invalid': 'data'}]
    process_items(data)