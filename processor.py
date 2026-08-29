import json
from typing import List, Dict, Any

class Processor:
    """Handles data processing and cleanup tasks."""

    def __init__(self, input_data: List[Dict[str, Any]]):
        self.input_data = input_data
        self.output_data: List[Dict[str, Any]] = []

    def validate_entry(self, entry: Dict[str, Any]) -> bool:
        """Check if entry has required fields."""
        required = ['id', 'name', 'value']
        return all(key in entry for key in required) and isinstance(entry.get('value'), (int, float))

    def clean_data(self) -> None:
        """Remove invalid entries and normalize data."""
        for entry in self.input_data:
            if self.validate_entry(entry):
                cleaned = {
                    'id': entry['id'],
                    'name': entry['name'].strip().lower(),
                    'value': float(entry['value'])
                }
                self.output_data.append(cleaned)

    def transform_data(self) -> None:
        """Apply transformations to cleaned data."""
        for entry in self.output_data:
            entry['value'] *= 1.1  # apply 10% increase
            entry['processed'] = True

    def get_results(self) -> List[Dict[str, Any]]:
        """Return the processed data."""
        return self.output_data

    def save_results(self, filepath: str) -> None:
        """Save processed data to JSON file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.output_data, f, indent=2, ensure_ascii=False)

def run_processing(data: List[Dict[str, Any]], output_file: str = 'processed.json') -> List[Dict[str, Any]]:
    """Main function to run the processor."""
    proc = Processor(data)
    proc.clean_data()
    proc.transform_data()
    results = proc.get_results()
    proc.save_results(output_file)
    return results

# Example usage
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': ' Item One ', 'value': 100},
        {'id': 2, 'name': 'Item Two', 'value': 'invalid'},
        {'id': 3, 'name': 'Item Three', 'value': 300},
    ]
    processed = run_processing(sample_data)
    print(f"Processed {len(processed)} items")
    print(json.dumps(processed, indent=2))