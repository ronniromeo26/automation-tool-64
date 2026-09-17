import sys

def validate_input(data):
    """Ensure data is a non-empty dictionary."""
    if not isinstance(data, dict) or not data:
        raise ValueError("Invalid input: payload must be a non-empty dictionary")
    return True

def process_payload(data):
    """Process valid data payload."""
    print(f"Processing: {data}")
    return True

def run_loop(input_stream):
    """Main processing loop with input validation."""
    for item in input_stream:
        try:
            if validate_input(item):
                process_payload(item)
        except (ValueError, TypeError) as e:
            print(f"Skipping invalid item: {e}", file=sys.stderr)
            continue

if __name__ == "__main__":
    # Example stream of incoming data
    stream = [{"id": 1}, {}, "invalid", {"id": 2}]
    run_loop(stream)