import logging
import os
from pathlib import Path
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-64')

class AutomationCore:
    """Handles core directory cleanup and reorganization tasks."""

    def __init__(self, target_dir: str):
        self.target_dir = Path(target_dir)

    def cleanup_files(self, extension: str) -> None:
        """Removes files with specific extension in target path."""
        if not self.target_dir.exists():
            logger.error(f'Directory {self.target_dir} not found')
            return

        files_to_remove = list(self.target_dir.glob(f'*{extension}'))
        for file_path in files_to_remove:
            try:
                file_path.unlink()
                logger.info(f'Removed {file_path.name}')
            except OSError as e:
                logger.error(f'Failed to remove {file_path}: {e}')

    def reorganize_structure(self, sub_dir_name: str) -> None:
        """Moves existing files into a structured subdirectory."""
        dest = self.target_dir / sub_dir_name
        dest.mkdir(exist_ok=True)

        for item in self.target_dir.iterdir():
            if item.is_file():
                item.rename(dest / item.name)
                logger.info(f'Moved {item.name} to {sub_dir_name}')

if __name__ == '__main__':
    # Practical execution example for core modules
    core = AutomationCore('./data')
    core.cleanup_files('.tmp')
    core.reorganize_structure('archive')