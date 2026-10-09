from typing import Any, Dict, List

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary, joining keys with a separator."""
    items: List = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, f"{new_key}{sep}{i}", sep=sep).items())
                else:
                    items.append((f"{new_key}{sep}{i}", item))
        else:
            items.append((new_key, v))
    return dict(items)

def clean_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively removes keys with None values or empty strings/dicts/lists."""
    cleaned = {}
    for k, v in data.items():
        if v is None or v == "":
            continue
        if isinstance(v, dict):
            nested = clean_data(v)
            if nested:
                cleaned[k] = nested
        elif isinstance(v, list):
            cleaned_list = []
            for item in v:
                if isinstance(item, dict):
                    item_cleaned = clean_data(item)
                    if item_cleaned:
                        cleaned_list.append(item_cleaned)
                elif item is not None and item != "":
                    cleaned_list.append(item)
            if cleaned_list:
                cleaned[k] = cleaned_list
        else:
            if isinstance(v, str):
                v = v.strip()
            cleaned[k] = v
    return cleaned