import os
import logging
from typing import List

# Configure module logger
logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles cleanup and data normalization tasks."""

    def __init__(self, directory: str, extensions: List[str]):
        self.directory = directory
        self.extensions = extensions

    def get_target_files(self) -> List[str]:
        """Identifies files matching the target extension list."""
        if not os.path.exists(self.directory):
            return []
        return [f for f in os.listdir(self.directory) if f.endswith(tuple(self.extensions))]

    def perform_cleanup(self) -> int:
        """Removes target files and returns deletion count."""
        files = self.get_target_files()
        count = 0
        for filename in files:
            file_path = os.path.join(self.directory, filename)
            try:
                os.remove(file_path)
                count += 1
            except OSError as e:
                logger.error(f"failed to delete {filename}: {e}")
        return count

    def reorganize(self, target_subdir: str) -> None:
        """Moves existing files into a structured subdirectory."""
        dest_path = os.path.join(self.directory, target_subdir)
        os.makedirs(dest_path, exist_ok=True)

        for filename in os.listdir(self.directory):
            if filename != target_subdir:
                source = os.path.join(self.directory, filename)
                if os.path.isfile(source):
                    os.rename(source, os.path.join(dest_path, filename))