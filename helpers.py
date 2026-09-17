import os
import shutil
from pathlib import Path
from typing import List, Union

def clear_temp_directory(directory_path: Union[str, Path]) -> None:
    """Removes all files and subdirectories within the specified path."""
    path = Path(directory_path)
    if not path.exists():
        return

    for item in path.iterdir():
        try:
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
        except OSError as e:
            print(f"Error removing {item}: {e}")

def archive_old_logs(source_dir: str, target_dir: str, extension: str = '.log') -> List[Path]:
    """Moves files with a specific extension to an archive directory."""
    src = Path(source_dir)
    dst = Path(target_dir)
    dst.mkdir(parents=True, exist_ok=True)

    archived = []
    for log_file in src.glob(f"*{extension}"):
        dest_path = dst / log_file.name
        shutil.move(str(log_file), str(dest_path))
        archived.append(dest_path)
    
    return archived

def ensure_directory_exists(path: str) -> None:
    """Creates a directory if it does not exist already."""
    Path(path).mkdir(parents=True, exist_ok=True)