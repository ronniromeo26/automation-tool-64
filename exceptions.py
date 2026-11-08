class AutomationError(Exception):
    """Base exception for automation-tool-64."""
    pass

class ValidationError(AutomationError):
    """Raised when input validation fails."""
    pass

class ExecutionError(AutomationError):
    """Raised when an automation task fails."""
    pass

class ConfigurationError(AutomationError):
    """Raised when settings are invalid."""
    pass

class TimeoutError(AutomationError):
    """Raised when a task exceeds time limit."""
    pass

def raise_if_none(value, message, exception_type=ValidationError):
    """Utility to check for null values."""
    if value is None:
        raise exception_type(message)
    return value

def wrap_execution(func, *args, **kwargs):
    """Wrapper to catch execution errors."""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        raise ExecutionError(f"Task failed: {str(e)}") from e