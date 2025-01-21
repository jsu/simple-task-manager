# Simple Task Manager

## Overview

Simple Task Manager is a Python-based command-line application that allows users to manage their tasks efficiently. This project serves as an excellent example for testing agentic coding capabilities in Python.

## Features

- Add new tasks
- Remove existing tasks
- List all tasks
- Mark tasks as complete
- (Optional) Save tasks to a file for persistence

## Requirements

- Python 3.12+

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/jsu/simple-task-manager.git
   ```

2. Navigate to the project directory:
   ```
   cd simple-task-manager
   ```

3. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install required dependencies (if any):
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application:

```
python task_manager.py
```

Follow the on-screen prompts to interact with the Task Manager:

- To add a task, type 'add' followed by the task description.
- To remove a task, type 'remove' followed by the task number.
- To list all tasks, type 'list'.
- To mark a task as complete, type 'complete' followed by the task number.
- To exit the application, type 'quit'.

## Project Structure

- `task_manager.py`: Main application file
- `task.py`: Task class definition
- `task_list.py`: TaskList class for managing the collection of tasks
- `utils.py`: Utility functions for file I/O operations (optional)

## Contributing

Contributions to improve the Simple Task Manager are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was created as a demonstration for agentic coding capabilities in Python.
- Inspired by real-world task management applications and the need for simple, efficient personal productivity tools.