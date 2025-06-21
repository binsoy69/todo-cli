import argparse
import json 
import os
from colorama import Fore, Style, init
init(autoreset=True)  # Auto reset color after each print


class TaskManager:
    def __init__(self, filepath='tasks.json'):
        self.filepath = filepath
        self.tasks = self.load()

    def load(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump([], f)
        with open(self.filepath, 'r') as f:
            return json.load(f)
        
    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save()

    def list(self):
        return self.tasks

    def remove(self, task_id):
        removed_task = self.tasks.pop(task_id)
        self.save()
        return removed_task
    
    def complete(self, task_id):
        self.tasks[task_id]['completed'] = True
        self.save()

    def search(self, keyword):
        return [task for task in self.tasks if keyword.lower() in task['task'].lower()]




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

    search_parser = subparsers.add_parser('search', help='Search for a keyword in tasks')
    search_parser.add_argument('keyword', type=str, help='Keyword to search')

    args = parser.parse_args()
    
    tm = TaskManager()

    if args.command == 'add':
       tm.add(args.task)
       print(Fore.GREEN + f"✅ Added: {args.task}")
    elif args.command == 'list':
        tasks = tm.list()
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = Fore.GREEN + '✅' if task['completed'] else Fore.RED + '❌'
                print(f"{i}.{status} {task['task']}")
    elif args.command == 'remove':
        if 1 <= args.task_id <= len(tm.tasks):
            removed = tm.remove(args.task_id - 1)
            print(Fore.RED + f"🗑️ Removed: {removed['task']}")
        else:
            print(Fore.YELLOW + "⚠️ Invalid task number.")
    elif args.command == 'complete':
        if 1 <= args.task_id <= len(tm.tasks):
            tm.complete(args.task_id - 1)
            print(Fore.BLUE + f"✅ Completed: {tm.tasks[args.task_id -1 ]['task']}")
        else:
            print(Fore.YELLOW + "⚠️ Invalid task number.")
    elif args.command == 'search':
        results = tm.search(args.keyword)
        if results:
            print(Fore.CYAN + f"🔍 Found {len(results)} task(s):")
            for i, task in enumerate(results, start=1):
                status = '✅' if task['completed'] else '❌'
                print(f"{i}. {status} {task['task']}")
        else:
            print(Fore.YELLOW + "No tasks found.")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
