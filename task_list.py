from typing import List, Optional
from task import Task

class TaskList:
    """Manages a collection of tasks."""
    
    def __init__(self):
        self.tasks: List[Task] = []
    
    def add_task(self, description: str) -> Task:
        """Add a new task to the list."""
        task = Task(description=description)
        self.tasks.append(task)
        return task
    
    def remove_task(self, index: int) -> Optional[Task]:
        """Remove a task by its index."""
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
        return None
    
    def complete_task(self, index: int) -> bool:
        """Mark a task as complete by its index."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()
            return True
        return False
    
    def get_all_tasks(self) -> List[Task]:
        """Get all tasks."""
        return self.tasks
    
    def get_active_tasks(self) -> List[Task]:
        """Get all incomplete tasks."""
        return [task for task in self.tasks if not task.is_completed]
    
    def get_completed_tasks(self) -> List[Task]:
        """Get all completed tasks."""
        return [task for task in self.tasks if task.is_completed] 