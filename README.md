# automation-tool-64

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`automation-tool-64` is a lightweight Python framework designed to streamline local task execution, file transformations, and scheduled API interactions. It provides a clean event-driven pipeline architecture to orchestrate repetitive operational workflows with minimal overhead.

## Features

- **Asynchronous Execution:** Execute concurrent system tasks and HTTP webhooks using a native `asyncio` task runner.
- **YAML Pipeline Definitions:** Declare multi-step execution chains, dependencies, and fallback routines in simple configuration files.
- **Built-in Telemetry:** Track task status, execution metrics, and error traces with automated JSON log generation.
- **Smart Retries:** Handle transient network failures and IO bottlenecks with configurable exponential backoff strategies.

## Installation

Install the package directly from PyPI:

```bash
pip install automation-tool-64
```

Or install from source for development:

```bash
git clone https://github.com/Developer/automation-tool-64.git
cd automation-tool-64
pip install -e .
```

## Quick Start

Define and execute a basic task pipeline in Python:

```python
from automation_tool_64 import Pipeline, Task

def process_payload(context):
    raw_data = context.get("data", "")
    return {"status": "processed", "payload": raw_data.strip().upper()}

# Initialize pipeline
pipeline = Pipeline(name="data_cleaner")

# Attach task with automatic retries
pipeline.add_task(Task(
    name="sanitize",
    action=process_payload,
    max_retries=3
))

# Run with context
output = pipeline.run({"data": "  input_value  "})
print(output)
# Output: {'status': 'processed', 'payload': 'INPUT_VALUE'}
```

Run via the command line interface:

```bash
auto64 run --config pipeline.yml --verbose
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.