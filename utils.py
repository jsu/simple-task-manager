import json
from datetime import datetime
from typing import List, Dict, Any
from task import Task
from task_list import TaskList

def save_tasks(task_list: TaskList, filename: str = "tasks.json") -> bool:
    """Save tasks to a JSON file."""
    try:
        tasks_data = [
            {
                "description": task.description,
                "created_at": task.created_at.isoformat(),
                "completed_at": task.completed_at.isoformat() if task.completed_at else None
            }
            for task in task_list.get_all_tasks()
        ]
        
        with open(filename, 'w') as f:
            json.dump(tasks_data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

def load_tasks(filename: str = "tasks.json") -> TaskList:
    """Load tasks from a JSON file."""
    task_list = TaskList()
    try:
        with open(filename, 'r') as f:
            tasks_data = json.load(f)
            
        for task_data in tasks_data:
            task = Task(
                description=task_data["description"],
                created_at=datetime.fromisoformat(task_data["created_at"])
            )
            if task_data["completed_at"]:
                task.completed_at = datetime.fromisoformat(task_data["completed_at"])
            task_list.tasks.append(task)
            
    except FileNotFoundError:
        # Return empty task list if file doesn't exist
        pass
    except Exception as e:
        print(f"Error loading tasks: {e}")
    
    return task_list 