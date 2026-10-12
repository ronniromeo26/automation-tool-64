import shutil
import tempfile
from pathlib import Path
from typing import List, Generator, Optional


class TempDirectoryManager:
    """Context manager for safely handling temporary automation workspaces."""

    def __init__(self, prefix: str = "auto_"):
        self.prefix = prefix
        self.path: Optional[Path] = None

    def __enter__(self) -> Path:
        self.path = Path(tempfile.mkdtemp(prefix=self.prefix))
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.path and self.path.exists():
            shutil.rmtree(self.path, ignore_errors=True)


def batch_file_finder(directory: str, extensions: List[str]) -> Generator[Path, None, None]:
    """Yield paths to files matching specific extensions within a target directory."""
    target_dir = Path(directory)
    if not target_dir.exists() or not target_dir.is_dir():
        raise ValueError(f"Invalid directory path: {directory}")

    normalized_exts = {ext.lower().lstrip(".") for ext in extensions}
    for path in target_dir.rglob("*"):
        if path.is_file() and path.suffix.lower().lstrip(".") in normalized_exts:
            yield path


def sanitize_filename(name: str, replacement: str = "_") -> str:
    """Clean string input to generate safe file names for cross-platform automation."""
    invalid_chars = '<>:"/\\|?*\0'
    for char in invalid_chars:
        name = name.replace(char, replacement)
    return name.strip().rstrip(".")
