import logging

def validate_input(data):
    """Ensures data is a non-empty dictionary."""
    if not isinstance(data, dict):
        return False
    if not data:
        return False
    return 'task_id' in data

def process_requests(request_queue):
    """
    Main processing loop for automation-tool-64.
    Validates input before execution to prevent system errors.
    """
    logger = logging.getLogger(__name__)
    
    while True:
        task = request_queue.get()
        if task is None:
            break
            
        try:
            if not validate_input(task):
                logger.warning(f"Invalid task skipped: {task}")
                continue
            
            # Simulate task execution
            logger.info(f"Processing task: {task.get('task_id')}")
            
        except Exception as e:
            logger.error(f"Unexpected loop error: {e}")
            
        request_queue.task_done()

if __name__ == '__main__':
    import queue
    q = queue.Queue()
    q.put({'task_id': 101})
    q.put("invalid_data")
    q.put(None)
    process_requests(q)