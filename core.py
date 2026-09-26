import os
import shutil
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-64')

class AutomationCore:
    def __init__(self, workspace_path: str):
        self.workspace = workspace_path

    def purge_temp_files(self, extension: str = '.tmp'):
        """Removes temporary files with specified extension."""
        if not os.path.exists(self.workspace):
            logger.error(f'Workspace {self.workspace} not found.')
            return

        count = 0
        for root, _, files in os.walk(self.workspace):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        count += 1
                    except OSError as e:
                        logger.warning(f'Failed to delete {file}: {e}')
        
        logger.info(f'Cleanup complete. Removed {count} files.')

    def reorganize_logs(self, archive_dir: str):
        """Moves log files into an archive directory."""
        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)
            
        for item in os.listdir(self.workspace):
            if item.endswith('.log'):
                src = os.path.join(self.workspace, item)
                dst = os.path.join(archive_dir, item)
                shutil.move(src, dst)
                logger.info(f'Archived {item}')

if __name__ == '__main__':
    tool = AutomationCore('./data')
    tool.purge_temp_files()
    tool.reorganize_logs('./archive')