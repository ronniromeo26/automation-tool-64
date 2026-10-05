import re
import os

def is_valid_email(email: str) -> bool:
    """Validate email address format using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def is_valid_file_path(path: str) -> bool:
    """Check if path is absolute and points to an existing file."""
    return os.path.isfile(path) and os.path.isabs(path)

def sanitize_input(user_input: str) -> str:
    """Remove non-alphanumeric characters for security."""
    return re.sub(r'[^a-zA-Z0-9]', '', user_input)

def validate_port(port: int) -> bool:
    """Validate network port range."""
    return 1 <= port <= 65535

def check_required_env_vars(vars_list: list) -> bool:
    """Verify presence of mandatory environment configuration."""
    return all(os.getenv(var) is not None for var in vars_list)