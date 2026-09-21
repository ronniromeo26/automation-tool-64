import re

def validate_input(data):
    """Validates dictionary input for required keys and format."""
    required_fields = ['id', 'payload', 'timestamp']
    
    # Check for missing keys
    if not all(key in data for key in required_fields):
        return False, "missing required fields"
    
    # Validate ID format (must be alphanumeric)
    if not re.match(r'^[a-zA-Z0-9]+$', str(data['id'])):
        return False, "invalid id format"
    
    # Validate payload type
    if not isinstance(data['payload'], dict):
        return False, "payload must be a dictionary"
    
    return True, None

def process_main_loop(queue):
    """Main processing loop with input validation integration."""
    for item in queue:
        is_valid, error_msg = validate_input(item)
        
        if not is_valid:
            print(f"Skipping invalid entry: {error_msg}")
            continue
            
        try:
            # Simulate core logic execution
            print(f"Processing record {item['id']} successfully.")
        except Exception as e:
            print(f"Runtime error processing {item.get('id')}: {e}")