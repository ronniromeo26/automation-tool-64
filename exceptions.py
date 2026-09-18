"""
Custom exception classes for automation-tool-64.

Provides structured error handling and serialization capabilities for common
automation pipeline failures.
"""

from typing import Any, Dict, Optional


class AutomationError(Exception):
    """Base exception for all automation-related issues."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the exception data into a dictionary for logging or API outputs."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "details": self.details
        }


class ConnectionTimeoutError(AutomationError):
    """Raised when external services or APIs fail to respond within limits."""
    pass


class ValidationError(AutomationError):
    """Raised when configuration inputs or pipeline payloads fail validation."""
    pass


class TaskExecutionError(AutomationError):
    """Raised when a specific automation step fails during runtime execution."""

    def __init__(self, message: str, task_name: str, step_id: int, details: Optional[Dict[str, Any]] = None) -> None:
        context = {"task_name": task_name, "step_id": step_id}
        if details:
            context.update(details)
        super().__init__(message, details=context)
