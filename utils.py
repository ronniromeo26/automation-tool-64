"""Utility functions for automation-tool-64.

Cleaned up and reorganized common helpers.
"""

import os
import json
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List

# File utilities

def ensure_directory(path: str) -> str:
    """Ensure the directory exists."""
    os.makedirs(path, exist_ok=True)
    return os.path.abspath(path)

def list_files(directory: str, extension: Optional[str] = None) -> List[str]:
    """List files optionally by extension."""
    files = []
    for root, _, filenames in os.walk(directory):
        for name in filenames:
            if not extension or name.endswith(extension):
                files.append(os.path.join(root, name))
    return files

def cleanup_old_files(dir_path: str, days: int = 7) -> int:
    """Clean files older than given days."""
    if not os.path.isdir(dir_path):
        return 0
    cutoff = datetime.now().timestamp() - days * 86400
    count = 0
    for root, _, files in os.walk(dir_path):
        for f in files:
            fp = os.path.join(root, f)
            if os.path.getmtime(fp) < cutoff:
                try:
                    os.remove(fp)
                    count += 1
                except OSError:
                    pass
    return count

# JSON utilities

def load_json(path: str) -> Dict[str, Any]:
    """Load JSON or empty dict."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

def save_json(data: Dict[str, Any], path: str) -> bool:
    """Save data to JSON file."""
    try:
        ensure_directory(os.path.dirname(path) or ".")
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception:
        return False

# Misc utilities

def get_timestamp() -> str:
    """Get current timestamp string."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def setup_logger(name: str = "automation") -> logging.Logger:
    """Configure logger."""
    log = logging.getLogger(name)
    if not log.handlers:
        h = logging.StreamHandler()
        h.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        log.addHandler(h)
    log.setLevel(logging.INFO)
    return log