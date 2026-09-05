from typing import Dict, Any

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Recursively flattens a nested dictionary into a single level dictionary.
    Combines keys using the specified separator.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def safe_get(data: Dict[str, Any], path: str, default: Any = None, sep: str = '.') -> Any:
    """
    Safely retrieves a value from a nested dictionary using a delimited path string.
    Returns the default value if any key in the path does not exist.
    """
    if not isinstance(data, dict):
        return default
        
    keys = path.split(sep)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current
