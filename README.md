[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# automation-tool-64

`automation-tool-64` is a lightweight Python engine designed to streamline recurring system workflows and background processing tasks. It combines asynchronous event scheduling with native file system monitoring to eliminate boilerplate code from your operational pipelines.

## Features

- **Asynchronous Task Scheduler:** Execute recurring jobs and cron-like routines using non-blocking `asyncio` loops.
- **File System Watchers:** Trigger custom handlers instantly upon file creation, modification, or deletion within target directories.
- **Webhook Dispatcher:** Send structured JSON payloads to Slack, Discord, or custom HTTP endpoints on task state changes.
- **YAML Pipeline Definitions:** Declare complex multi-step workflows, retry logic, and dependencies in simple configuration files.

## Installation

Install the package via `pip`:

```bash
pip install automation-tool-64
```

Alternatively, build directly from the source repository:

```bash
git clone https://github.com/Developer/automation-tool-64.git
cd automation-tool-64
pip install -e .
```

## Quick Start

Create a script named `app.py` to monitor a directory and log automated tasks:

```python
from automation_64 import AutomationEngine, TaskContext

app = AutomationEngine()

@app.on_file_change(path="./data", pattern="*.csv")
async def process_new_csv(ctx: TaskContext):
    print(f"Detected modification in: {ctx.event_path}")
    # Run data processing steps here

@app.schedule(interval_seconds=300)
async def periodic_cleanup(ctx: TaskContext):
    print("Running scheduled 5-minute cleanup routine...")

if __name__ == "__main__":
    app.run()
```

Run the application:

```bash
python app.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.