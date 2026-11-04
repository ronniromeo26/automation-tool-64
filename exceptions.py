class AutomationError(Exception):
    """Base exception for all automation-tool-64 issues."""

class ConfigurationError(AutomationError):
    """Raised when tool configuration is invalid or missing."""

class ExecutionError(AutomationError):
    """Raised when an automation task fails during runtime."""

class ValidationError(AutomationError):
    """Raised when input data fails internal integrity checks."""

def handle_exception(e: Exception) -> None:
    """Centralized error reporting and categorization."""
    if isinstance(e, (ConfigurationError, ValidationError)):
        print(f"Critical setup issue: {e}")
    elif isinstance(e, ExecutionError):
        print(f"Runtime failure encountered: {e}")
    else:
        print(f"Unexpected system error: {type(e).__name__} - {e}")

if __name__ == "__main__":
    try:
        raise ExecutionError("Failed to initialize process driver")
    except AutomationError as err:
        handle_exception(err)