"""Custom exceptions and error handling context for automation-tool-64."""

from typing import Any, Dict, Optional


class AutomationError(Exception):
    """Base exception for all automation tool errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        """Return exception details as a dictionary for logging/reporting."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "details": self.details,
        }


class ResourceNotFoundError(AutomationError):
    """Raised when a required file, directory, or target is missing."""

    def __init__(self, resource_path: str, resource_type: str = "Resource"):
        msg = f"{resource_type} not found at location: '{resource_path}'"
        super().__init__(msg, {"path": resource_path, "type": resource_type})


class TaskTimeoutError(AutomationError):
    """Raised when an automated task exceeds its allocated execution time."""

    def __init__(self, task_name: str, timeout_seconds: float):
        msg = f"Task '{task_name}' timed out after {timeout_seconds} seconds"
        super().__init__(msg, {"task_name": task_name, "timeout": timeout_seconds})


class RetryLimitExceededError(AutomationError):
    """Raised when retry attempts for an operation are exhausted."""

    def __init__(
        self, operation_name: str, max_retries: int, last_error: Optional[str] = None
    ):
        msg = f"Operation '{operation_name}' failed after {max_retries} retries"
        if last_error:
            msg += f". Last error: {last_error}"
        super().__init__(
            msg,
            {
                "operation": operation_name,
                "retries": max_retries,
                "last_error": last_error,
            },
        )


class ConfigurationError(AutomationError):
    """Raised when invalid configuration settings are provided."""

    pass
