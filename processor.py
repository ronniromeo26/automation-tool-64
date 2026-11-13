from typing import List, Dict, Optional, Any

def process_data_batch(data_items: List[Dict[str, Any]], filter_key: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Processes a list of dictionaries by filtering and normalizing values.

    Args:
        data_items: A list of dictionaries containing raw data records.
        filter_key: Optional key to filter the result set by existence.

    Returns:
        A list of processed dictionaries with trimmed values.
    """
    processed_results: List[Dict[str, Any]] = []

    for item in data_items:
        if filter_key and filter_key not in item:
            continue

        clean_item: Dict[str, Any] = {
            str(k).lower().strip(): str(v).strip() if isinstance(v, str) else v
            for k, v in item.items()
        }
        processed_results.append(clean_item)

    return processed_results

def format_batch_summary(results: List[Dict[str, Any]]) -> str:
    """
    Generates a human-readable summary of the processed batch.

    Args:
        results: List of processed data dictionaries.

    Returns:
        A string representation of the batch summary.
    """
    count: int = len(results)
    keys_found: set = set()
    for row in results:
        keys_found.update(row.keys())

    return f"processed {count} items with schema fields: {', '.join(sorted(keys_found))}"