from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    """Represents a single task in the task manager."""
    description: str
    created_at: datetime = datetime.now()
    completed_at: Optional[datetime] = None
    
    @property
    def is_completed(self) -> bool:
        """Check if the task is completed."""
        return self.completed_at is not None
    
    def complete(self) -> None:
        """Mark the task as completed."""
        self.completed_at = datetime.now()
    
    def __str__(self) -> str:
        """String representation of the task."""
        status = "✓" if self.is_completed else " "
        return f"[{status}] {self.description}" 