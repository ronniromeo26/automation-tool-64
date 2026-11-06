import re

def validate_input(data):
    """Validates input dictionary fields for automation-tool-64."""
    required_fields = {'task_id', 'payload', 'priority'}
    
    if not isinstance(data, dict):
        return False, "Input must be a dictionary"
    
    if not required_fields.issubset(data.keys()):
        missing = required_fields - data.keys()
        return False, f"Missing fields: {missing}"
    
    if not isinstance(data['task_id'], int) or data['task_id'] < 0:
        return False, "task_id must be a positive integer"
    
    if not isinstance(data['payload'], str) or len(data['payload']) > 1024:
        return False, "payload must be a string under 1024 chars"
    
    if data['priority'] not in ['low', 'medium', 'high']:
        return False, "priority must be low, medium, or high"
    
    return True, "success"

def run_processing_loop(data_stream):
    """Main processing loop with input validation integration."""
    for item in data_stream:
        is_valid, error = validate_input(item)
        if not is_valid:
            print(f"Validation error skipped: {error}")
            continue
        
        process_item(item)

def process_item(item):
    """Stub for core processing logic."""
    print(f"Processing valid task {item['task_id']}")