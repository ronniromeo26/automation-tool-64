import logging
import functools
from datetime import datetime

# Configure global logger for automation-tool-64
logger = logging.getLogger('automation-tool-64')
logger.setLevel(logging.INFO)

# Memoization cache for performance improvement
_performance_cache = {}

def memoize_performance(func):
    """Decorator to cache function results and avoid redundant processing."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _performance_cache:
            _performance_cache[key] = func(*args, **kwargs)
        return _performance_cache[key]
    return wrapper

class AutomationLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    @memoize_performance
    def log_event(self, message: str, level: str = 'info'):
        """Standardized logging entry with caching capability."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_msg = f"[{timestamp}] {message}"
        
        if level == 'info':
            self.logger.info(formatted_msg)
        elif level == 'error':
            self.logger.error(formatted_msg)
        return True

# Instantiate singleton for global usage
app_logger = AutomationLogger('core-module')