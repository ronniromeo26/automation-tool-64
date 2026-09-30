import time
import random
import urllib.request
import urllib.error
import socket
import logging

logger = logging.getLogger("automation_tool.handler")

class NetworkHandler:
    """Handles network requests with built-in retry logic and exponential backoff."""

    def __init__(self, max_retries: int = 3, backoff_factor: float = 1.5, timeout: float = 10.0):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.timeout = timeout

    def execute_request(self, url: str) -> str:
        """Executes a GET request with exponential backoff and jitter."""
        retries = 0
        delay = 1.0

        while True:
            try:
                logger.info(f"Fetching URL: {url} (Attempt {retries + 1}/{self.max_retries + 1})")
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "AutomationTool64/1.0"}
                )
                with urllib.request.urlopen(req, timeout=self.timeout) as response:
                    return response.read().decode('utf-8')
            except (urllib.error.URLError, socket.timeout) as e:
                retries += 1
                if retries > self.max_retries:
                    logger.error(f"Failed to fetch {url} after {self.max_retries} retries. Error: {e}")
                    raise

                # Calculate exponential backoff with jitter
                jitter = random.uniform(0.1, 0.5)
                sleep_time = (delay * self.backoff_factor) + jitter
                logger.warning(f"Request failed due to {e}. Retrying in {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)
                delay = sleep_time
