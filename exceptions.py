import logging
from typing import Any, Callable, Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('automation_tool')

class AutomationError(Exception):
    """Base exception class for the automation tool."""
    def __init__(self, message: str, context: Optional[dict] = None) -> None:
        self.message = message
        self.context = context or {}
        super().__init__(self.message)

class InvalidConfigurationError(AutomationError):
    """Raised when configuration has invalid values or missing keys."""
    pass

class EdgeCaseInputError(AutomationError):
    """Raised for unexpected input values like empty lists or zero values."""
    pass

class ResourceAccessError(AutomationError):
    """Raised when accessing files, APIs or other resources fails."""
    pass

class ProcessingTimeoutError(AutomationError):
    """Raised when an operation takes too long to complete."""
    pass

def handle_edge_cases(operation: Callable[[], Any], retries: int = 2) -> Any:
    """Wrapper function to handle various edge cases with retries.
    Handles invalid inputs, timeouts, resource errors.
    """
    for attempt in range(retries + 1):
        try:
            result = operation()
            if result is None:
                raise EdgeCaseInputError("Operation returned None, which is invalid")
            if isinstance(result, (list, dict)) and len(result) == 0:
                raise EdgeCaseInputError("Empty result from operation")
            return result
        except (InvalidConfigurationError, EdgeCaseInputError) as e:
            logger.error(f"Edge case error: {e.message} | Context: {e.context}")
            raise
        except ProcessingTimeoutError as e:
            logger.warning(f"Timeout on attempt {attempt + 1}: {e.message}")
            if attempt == retries:
                raise AutomationError("Max retries exceeded for timeout", e.context)
            continue
        except Exception as e:
            logger.error(f"Unexpected error during operation: {str(e)}")
            if attempt == retries:
                raise AutomationError(f"Failed after {retries + 1} attempts", {"original_error": str(e)})
            continue
    raise AutomationError("Operation failed without specific error")

def example_operation() -> int:
    """Example function that might hit edge cases."""
    import random
    value = random.choice([0, 5, None, []])
    if value == 0:
        raise EdgeCaseInputError("Zero value encountered", {"value": value})
    if value is None:
        raise InvalidConfigurationError("None value in config")
    if value == []:
        raise ResourceAccessError("Empty list from resource")
    return value