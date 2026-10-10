import re

class InputValidator:
    """Handles validation logic for processing jobs."""

    def __init__(self):
        # Regex for standard job ID format (e.g., JOB-12345)
        self.job_id_pattern = re.compile(r'^JOB-\d{5}$')
        self.min_priority = 1
        self.max_priority = 10

    def validate_job_data(self, data: dict) -> bool:
        """Checks if input dictionary contains valid keys and types."""
        job_id = data.get("job_id")
        priority = data.get("priority")

        if not isinstance(job_id, str) or not self.job_id_pattern.match(job_id):
            return False

        if not isinstance(priority, int) or not (self.min_priority <= priority <= self.max_priority):
            return False

        return True

    @staticmethod
    def sanitize_payload(payload: str) -> str:
        """Removes potential injection characters."""
        if not isinstance(payload, str):
            return ""
        return re.sub(r'[^a-zA-Z0-9\s]', '', payload)