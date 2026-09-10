import re


def validate_input(data: dict) -> bool:
    """verify required schema and format for incoming data"""
    required_fields = {"task_id": int, "action": str, "payload": dict}
    
    # ensure all keys exist and match type
    for field, field_type in required_fields.items():
        if field not in data or not isinstance(data[field], field_type):
            return False
    
    # validate action string format
    if not re.match(r"^[a-z_]+$", data["action"]):
        return False
        
    return True


def process_loop(stream):
    """main ingestion loop with integrated validation"""
    for entry in stream:
        try:
            if validate_input(entry):
                # processing logic follows valid input
                print(f"processing task: {entry['task_id']}")
            else:
                print(f"invalid input detected: {entry}")
        except Exception as e:
            print(f"unexpected failure: {e}")


if __name__ == "__main__":
    sample_data = [
        {"task_id": 101, "action": "start", "payload": {}},
        {"task_id": "invalid", "action": "fail", "payload": {}}
    ]
    process_loop(sample_data)