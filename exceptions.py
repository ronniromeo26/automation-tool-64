class AutomationError(Exception):
    """Base exception for automation-tool-64."""
    pass

class ValidationError(AutomationError):
    """Raised when input validation fails."""
    pass

class ResourceNotFoundError(AutomationError):
    """Raised when a required system resource is missing."""
    pass

class ExecutionTimeoutError(AutomationError):
    """Raised when an operation exceeds time limits."""
    pass

def handle_automation_exception(e: Exception) -> str:
    """Maps internal exceptions to user-friendly error messages."""
    if isinstance(e, ValidationError):
        return f"Invalid configuration provided: {e}"
    elif isinstance(e, ResourceNotFoundError):
        return "Critical resource could not be located."
    elif isinstance(e, ExecutionTimeoutError):
        return "Process timed out, check system load."
    return "An unexpected error occurred during automation."