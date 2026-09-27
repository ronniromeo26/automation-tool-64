import os
from typing import Final

# Configuration constants for performance optimization
# Caching thresholds and concurrency limits for core tasks

BUFFER_SIZE: Final[int] = 65536
MAX_WORKER_THREADS: Final[int] = os.cpu_count() or 4
DEFAULT_TIMEOUT: Final[float] = 30.0
CACHE_TTL: Final[int] = 3600

# Path constants for resource management
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
DATA_DIR: Final[str] = os.path.join(BASE_DIR, 'data')
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Performance optimization parameters
BATCH_SIZE: Final[int] = 100
RETRY_ATTEMPTS: Final[int] = 3
USE_ASYNC_IO: Final[bool] = True

# Ensure environment directories exist for efficiency
for directory in [DATA_DIR, LOG_DIR]:
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)