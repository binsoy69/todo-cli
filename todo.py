import argparse
import json 
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Simple To-Do CLI App")
    subparsers = parser.add_subparsers(dest='command')

    # Add Task
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task', type=str, help='The task description')

    # List Tasks
    subparsers.add_parser('list', help='List all tasks')

    # Remove Task
    remove_parser = subparsers.add_parser('remove', help='Remove a task')
    remove_parser.add_argument('task_id', type=int, help='The task number to remove')

    # Complete Task
    complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
    complete_parser.add_argument('task_id', type=int, help='The task number to complete')

    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == 'add':
        tasks.append({'task': args.task, 'completed': False})
        save_tasks(tasks)
        print(f"🟩 Added: {args.task}")
    elif args.command == 'list':
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = '✅' if task['completed'] else '❌'
                print(f"{i}.{status} {task['task']}")
    elif args.command == 'remove':
        if 1 <= args.task_id <= len(tasks):
            removed = tasks.pop(args.task_id - 1)
            save_tasks(tasks)
            print(f"🗑️ Removed: {removed['task']}")
        else:
            print("⚠️ Invalid task number.")
    elif args.command == 'complete':
        if 1 <= args.task_id <= len(tasks):
            tasks[args.task_id - 1]['completed'] = True
            save_tasks(tasks)
            print(f"✅ Completed: {tasks[args.task_id -1 ]['task']}")
        else:
            print("⚠️ Invalid task number.")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
