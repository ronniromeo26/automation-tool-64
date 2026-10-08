import os
import shutil
import logging

# configure logging for operational transparency
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def cleanup_directory(target_path: str, extension: str = '.tmp') -> int:
    """Removes files with specific extension from target path."""
    count = 0
    if not os.path.exists(target_path):
        logger.error(f"path {target_path} does not exist")
        return 0

    for item in os.listdir(target_path):
        if item.endswith(extension):
            file_path = os.path.join(target_path, item)
            try:
                os.remove(file_path)
                count += 1
            except OSError as e:
                logger.warning(f"failed to remove {item}: {e}")
    
    logger.info(f"cleanup complete: {count} files removed")
    return count

def organize_files(source_dir: str, target_base: str) -> None:
    """Reorganize files into categorized subdirectories."""
    for filename in os.listdir(source_dir):
        ext = filename.split('.')[-1].lower() if '.' in filename else 'misc'
        dest_dir = os.path.join(target_base, ext)
        
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(os.path.join(source_dir, filename), os.path.join(dest_dir, filename))

if __name__ == "__main__":
    # execution entry point for automation tasks
    cleanup_directory('./temp')
    organize_files('./data', './archive')