import os
import time
from typing import List, Callable, Any

class AutomationCore:
    def __init__(self) -> None:
        self.tasks: List[Callable[[], Any]] = []
        self.results: List[Any] = []

    def add_task(self, task: Callable[[], Any]) -> None:
        # Add a callable task to the list
        if callable(task):
            self.tasks.append(task)

    def run_all(self) -> None:
        # Execute each task sequentially with basic error handling
        for index, task in enumerate(self.tasks, 1):
            print(f"Starting task {index}")
            try:
                result = task()
                self.results.append(result)
                print(f"Task {index} succeeded")
            except Exception as error:
                print(f"Task {index} failed with error: {error}")
                self.results.append(None)

    def get_summary(self) -> dict:
        # Return a summary of execution
        return {
            "total_tasks": len(self.tasks),
            "successful": len([r for r in self.results if r is not None]),
            "results": self.results
        }

def create_file_task(filename: str, content: str) -> Callable[[], str]:
    # Factory to create a task that writes to a file
    def task() -> str:
        with open(filename, 'w') as f:
            f.write(content)
        return f"Created {filename}"
    return task

def main() -> None:
    # Example usage of the core automation
    core = AutomationCore()
    core.add_task(lambda: time.sleep(0.1) or "Slept briefly")
    core.add_task(create_file_task("temp.txt", "Automated content"))
    core.add_task(lambda: "Final task completed")
    core.run_all()
    summary = core.get_summary()
    print("Execution summary:", summary)
    # Cleanup the temp file
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")

if __name__ == "__main__":
    main()