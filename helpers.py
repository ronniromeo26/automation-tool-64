import os
import shutil
import time
from typing import List

def safe_delete_file(file_path: str) -> bool:
    """Safely delete a file if it exists, returning True on success."""
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
            return True
    except Exception:
        pass
    return False

def clean_directory_by_age(directory_path: str, max_age_seconds: int) -> List[str]:
    """Delete files in a directory that are older than max_age_seconds."""
    deleted_files = []
    if not os.path.isdir(directory_path):
        return deleted_files

    now = time.time()
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                stat = os.stat(file_path)
                if now - stat.st_mtime > max_age_seconds:
                    if safe_delete_file(file_path):
                        deleted_files.append(file_path)
            except OSError:
                continue
    return deleted_files

def ensure_directory_exists(directory_path: str) -> None:
    """Create directory if it does not already exist."""
    os.makedirs(directory_path, exist_ok=True)