# automation-tool-64

`automation-tool-64` is a lightweight, high-performance Python utility designed to streamline repetitive local workflows and system administration tasks. It provides a robust command-line interface to orchestrate file operations, process monitoring, and environment configuration with minimal overhead.

## Features

*   **Task Scheduling:** Execute complex chains of shell commands and Python scripts based on defined triggers or time intervals.
*   **Dynamic Logging:** Integrated rotating log system that captures task execution metrics and error states in standardized JSON format.
*   **Environment Validation:** Automated pre-flight checks to ensure required dependencies, directory permissions, and system variables are active before process execution.
*   **Plugin Architecture:** Extend functionality by dropping custom scripts into the `plugins/` directory for modular expansion.

## Installation

Ensure you have Python 3.9+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-64.git
cd automation-tool-64
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Basic Usage

Run the tool using the CLI to execute a defined task configuration file:

```bash
python main.py --config config/tasks.yaml --run
```

To list all available modules currently detected by the system:

```bash
python main.py --list-modules
```

## Configuration

Tasks are defined in YAML format. A sample configuration:

```yaml
tasks:
  - name: cleanup_logs
    command: "rm -rf ./temp/*.log"
    interval: "daily"
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.