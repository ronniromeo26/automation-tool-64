# automation-tool-64

`automation-tool-64` is a lightweight, high-performance Python utility designed to streamline repetitive system tasks through configurable YAML workflows. It enables developers to orchestrate local processes, file operations, and API triggers without the overhead of heavy automation frameworks.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

*   **YAML-Driven Orchestration**: Define complex task sequences in human-readable configuration files for repeatable execution.
*   **Parallel Process Management**: Execute multiple background sub-processes concurrently with real-time stream logging.
*   **Built-in Rate Limiter**: Prevent system saturation by enforcing configurable delays and concurrency caps on batch operations.
*   **Cross-Platform Compatibility**: Native support for POSIX-compliant systems and Windows, ensuring consistent task behavior across environments.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the dependencies:

```bash
git clone https://github.com/Developer/automation-tool-64.git
cd automation-tool-64
pip install -r requirements.txt
```

## Usage

Create a `tasks.yaml` file in your working directory to define your automation sequence:

```yaml
tasks:
  - name: "Cleanup"
    command: "rm -rf ./tmp/*"
  - name: "Deploy"
    command: "python deploy.py --env production"
```

Run the tool using the CLI:

```bash
python main.py --config tasks.yaml --verbose
```

For a full list of configuration parameters and flags, run:

```bash
python main.py --help
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.