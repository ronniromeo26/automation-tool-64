[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# automation-tool-64

automation-tool-64 is a lightweight Python tool for creating and managing automated task workflows. It enables users to define complex sequences of operations in simple configuration files and execute them reliably from the command line.

## Features

- Define automations using YAML files with support for variables and conditionals
- Execute shell commands, manage files, and make HTTP requests out of the box
- Built-in retry logic and structured logging for reliable task execution
- CLI interface for running, validating, and inspecting workflows

## Installation

```bash
git clone https://github.com/Developer/automation-tool-64.git
cd automation-tool-64
pip install -e .
```

## Usage

Create a file named `workflow.yaml`:

```yaml
name: data_sync
steps:
  - name: fetch
    type: http_get
    url: https://example.com/data.csv
    output: ./data.csv
  - name: process
    type: shell
    command: python analyze.py ./data.csv
```

Run the workflow:

```bash
automation-tool-64 run workflow.yaml
```