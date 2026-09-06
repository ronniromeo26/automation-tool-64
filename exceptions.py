"""Custom exceptions for the automation tool.

This module defines the hierarchy of exceptions raised by the automation
tool during configuration, validation, and task execution.
"""

from typing import Any, Dict, Optional


class AutomationError(Exception):
    """Base exception for all errors in automation-tool-64."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the base automation exception.

        Args:
            message: A human-readable error message.
            details: Optional metadata or context surrounding the error.
        """
        super().__init__(message)
        self.message: str = message
        self.details: Dict[str, Any] = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} (Details: {self.details})"
        return self.message


class ConfigurationError(AutomationError):
    """Exception raised when configuration parameters are invalid or missing."""


class TaskExecutionError(AutomationError):
    """Exception raised when an automation task fails during run."""

    def __init__(
        self, message: str, task_name: str, details: Optional[Dict[str, Any]] = None
    ) -> None:
        """Initialize the task execution exception with task context."""
        extended_details = {"task_name": task_name}
        if details:
            extended_details.update(details)
        super().__init__(message, details=extended_details)
        self.task_name: str = task_name


class ValidationError(AutomationError):
    """Exception raised when input data or state validation fails."""
