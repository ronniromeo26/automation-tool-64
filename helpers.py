import os
import shutil
from typing import List, Optional

def clean_temp_directories(paths: List[str]) -> None:
    """Removes temporary directories if they exist."""
    for path in paths:
        if os.path.exists(path) and os.path.isdir(path):
            try:
                shutil.rmtree(path)
            except OSError:
                continue

def consolidate_logs(source_dir: str, destination: str) -> None:
    """Moves log files into a centralized archive."""
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source_dir):
        if item.endswith('.log'):
            source_path = os.path.join(source_dir, item)
            dest_path = os.path.join(destination, item)
            shutil.move(source_path, dest_path)

def get_directory_size(path: str) -> int:
    """Calculates total size of a directory tree."""
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def validate_path_exists(path: Optional[str]) -> bool:
    """Checks if a provided path string is valid."""
    return path is not None and os.path.exists(path)