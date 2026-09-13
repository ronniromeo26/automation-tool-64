import os
import shutil
import logging
from typing import List

logger = logging.getLogger(__name__)

def clear_temp_directory(directory_path: str) -> bool:
    """Removes all files within the specified temp directory."""
    if not os.path.exists(directory_path):
        return False
    
    try:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        return True
    except OSError as e:
        logger.error(f"failed to clean {directory_path}: {e}")
        return False

def get_valid_file_paths(base_path: str, extensions: List[str]) -> List[str]:
    """Filters files by extension in a given directory."""
    valid_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                valid_files.append(os.path.join(root, file))
    return valid_files

def format_byte_size(size: int) -> str:
    """Converts bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"