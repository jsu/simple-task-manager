from task_list import TaskList
from utils import save_tasks, load_tasks

def print_help():
    """Print available commands."""
    print("\nAvailable commands:")
    print("  add <description>  - Add a new task")
    print("  list              - List all tasks")
    print("  complete <number> - Mark a task as complete")
    print("  remove <number>   - Remove a task")
    print("  help             - Show this help message")
    print("  quit             - Exit the application")

def main():
    """Main application loop."""
    task_list = load_tasks()
    print("Welcome to Simple Task Manager!")
    print_help()
    
    while True:
        try:
            command = input("\nEnter a command: ").strip().split(maxsplit=1)
            if not command:
                continue
                
            cmd = command[0].lower()
            args = command[1] if len(command) > 1 else ""
            
            if cmd == "quit":
                save_tasks(task_list)
                print("Goodbye!")
                break
                
            elif cmd == "help":
                print_help()
                
            elif cmd == "add":
                if not args:
                    print("Error: Please provide a task description")
                    continue
                task_list.add_task(args)
                print(f"Added task: {args}")
                
            elif cmd == "list":
                tasks = task_list.get_all_tasks()
                if not tasks:
                    print("No tasks found")
                else:
                    print("\nTasks:")
                    for i, task in enumerate(tasks):
                        print(f"{i + 1}. {task}")
                        
            elif cmd == "complete":
                try:
                    index = int(args) - 1
                    if task_list.complete_task(index):
                        print("Task marked as complete")
                    else:
                        print("Error: Invalid task number")
                except ValueError:
                    print("Error: Please provide a valid task number")
                    
            elif cmd == "remove":
                try:
                    index = int(args) - 1
                    task = task_list.remove_task(index)
                    if task:
                        print(f"Removed task: {task.description}")
                    else:
                        print("Error: Invalid task number")
                except ValueError:
                    print("Error: Please provide a valid task number")
                    
            else:
                print(f"Unknown command: {cmd}")
                print_help()
                
        except KeyboardInterrupt:
            print("\nSaving tasks and exiting...")
            save_tasks(task_list)
            break
            
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 