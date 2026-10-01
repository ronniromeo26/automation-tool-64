import sys

def validate_input(data):
    """Ensures input is a non-empty dictionary with required keys."""
    if not isinstance(data, dict):
        return False, "Input must be a dictionary"
    if 'task_id' not in data or 'payload' not in data:
        return False, "Missing mandatory task_id or payload keys"
    return True, None

def process_items(data_stream):
    """Main processing loop with integrated input validation."""
    for item in data_stream:
        is_valid, error = validate_input(item)
        
        if not is_valid:
            print(f"Validation error: {error}. Skipping item.")
            continue
            
        try:
            print(f"Processing task {item['task_id']}: {item['payload']}")
        except Exception as e:
            print(f"Unexpected processing failure: {e}")

if __name__ == "__main__":
    # Example input stream for automation-tool-64
    sample_data = [
        {'task_id': 1, 'payload': 'data_alpha'},
        {'invalid': 'data_beta'},
        {'task_id': 2, 'payload': 'data_gamma'}
    ]
    process_items(sample_data)