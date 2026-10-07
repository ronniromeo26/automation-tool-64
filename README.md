# automation-tool-64

`automation-tool-64` is a lightweight Python framework designed to streamline repetitive cross-platform administrative tasks. It provides a robust execution engine to orchestrate file system operations, remote command execution, and automated report generation.

## Features

*   **Task Scheduling:** Built-in cron-like syntax support for triggering automated scripts at specific intervals.
*   **Workflow Chaining:** Create complex dependency graphs where the output of one task serves as the input for the next.
*   **Encrypted Configuration:** Built-in support for secure credential management using environment-based AES-256 encryption.
*   **Real-time Logging:** Integrated structured logging to JSON or stdout for seamless ingestion into ELK or Splunk stacks.

## Installation

Ensure you have Python 3.9+ installed. You can install the tool via pip:

```bash
git clone https://github.com/Developer/automation-tool-64.git
cd automation-tool-64
pip install -r requirements.txt
python setup.py install
```

## Usage

Define your automation workflow in a YAML file, then execute the tool using the command-line interface:

```bash
# Example: Running a defined workflow
auto64 run --config workflows/cleanup.yaml --verbose
```

**Example YAML configuration:**

```yaml
tasks:
  - name: "Log Cleanup"
    command: "rm -rf /tmp/app-logs/*"
    schedule: "0 0 * * *"
  - name: "Notify Admin"
    command: "python notify.py --status success"
    dependencies: ["Log Cleanup"]
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the terms of the MIT license.