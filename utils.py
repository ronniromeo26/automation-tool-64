from typing import Any, Dict

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Recursively flattens a nested dictionary, concatenating keys with a separator.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, val in enumerate(v):
                list_key = f"{new_key}{sep}{i}"
                if isinstance(val, dict):
                    items.extend(flatten_dict(val, list_key, sep=sep).items())
                else:
                    items.append((list_key, val))
        else:
            items.append((new_key, v))
    return dict(items)

def clean_data(data: Dict[str, Any], remove_nulls: bool = True, strip_whitespace: bool = True) -> Dict[str, Any]:
    """
    Cleans general dictionary data by optionally stripping strings and removing null values.
    """
    cleaned = {}
    for k, v in data.items():
        clean_key = k.strip() if isinstance(k, str) and strip_whitespace else k
        
        if v is None and remove_nulls:
            continue
            
        if isinstance(v, str) and strip_whitespace:
            cleaned[clean_key] = v.strip()
        elif isinstance(v, dict):
            cleaned[clean_key] = clean_data(v, remove_nulls, strip_whitespace)
        elif isinstance(v, list):
            cleaned_list = []
            for item in v:
                if isinstance(item, dict):
                    cleaned_list.append(clean_data(item, remove_nulls, strip_whitespace))
                elif isinstance(item, str) and strip_whitespace:
                    cleaned_list.append(item.strip())
                elif item is None and remove_nulls:
                    continue
                else:
                    cleaned_list.append(item)
            cleaned[clean_key] = cleaned_list
        else:
            cleaned[clean_key] = v
    return cleaned
