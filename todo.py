import argparse

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

    if args.command == 'add':
        print(f"🟩 Add task: {args.task}")
    elif args.command == 'list':
        print("📋 List tasks")
    elif args.command == 'remove':
        print(f"🗑️ Remove task #{args.task_id}")
    elif args.command == 'complete':
        print(f"✅ Complete task #{args.task_id}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
