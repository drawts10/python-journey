import argparse
import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Optional

DATA_DIR = os.path.join(os.path.expanduser("~"), ".taskflow")
DATA_FILE = os.path.join(DATA_DIR, "tasks.json")


class Task:
    def __init__(
        self,
        task_id: int,
        title: str,
        completed: bool = False,
        created_at: Optional[str] = None,
        completed_at: Optional[str] = None,
        tags: Optional[List[str]] = None,
        priority: int = 3,
    ):
        self.id = task_id
        self.title = title
        self.completed = completed
        self.created_at = created_at or self._now()
        self.completed_at = completed_at
        self.tags = tags or []
        self.priority = priority

    def _now(self) -> str:
        return datetime.utcnow().isoformat()

    def complete(self):
        if not self.completed:
            self.completed = True
            self.completed_at = self._now()

    def reopen(self):
        self.completed = False
        self.completed_at = None

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
            "tags": self.tags,
            "priority": self.priority,
        }

    @staticmethod
    def from_dict(data: Dict) -> "Task":
        return Task(
            task_id=data["id"],
            title=data["title"],
            completed=data["completed"],
            created_at=data["created_at"],
            completed_at=data.get("completed_at"),
            tags=data.get("tags", []),
            priority=data.get("priority", 3),
        )


class TaskRepository:
    def __init__(self, path: str):
        self.path = path
        self._ensure_storage()

    def _ensure_storage(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        if not os.path.exists(self.path):
            self._write([])

    def _read(self) -> List[Dict]:
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data: List[Dict]):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load_tasks(self) -> List[Task]:
        raw = self._read()
        return [Task.from_dict(item) for item in raw]

    def save_tasks(self, tasks: List[Task]):
        self._write([task.to_dict() for task in tasks])


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo
        self.tasks = self.repo.load_tasks()

    def _next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def add_task(self, title: str, tags: List[str], priority: int):
        task = Task(
            task_id=self._next_id(),
            title=title,
            tags=tags,
            priority=priority,
        )
        self.tasks.append(task)
        self.repo.save_tasks(self.tasks)
        return task

    def list_tasks(self, show_all: bool = False) -> List[Task]:
        if show_all:
            return self.tasks
        return [t for t in self.tasks if not t.completed]

    def find_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"Task {task_id} not found")

    def complete_task(self, task_id: int):
        task = self.find_task(task_id)
        task.complete()
        self.repo.save_tasks(self.tasks)

    def reopen_task(self, task_id: int):
        task = self.find_task(task_id)
        task.reopen()
        self.repo.save_tasks(self.tasks)

    def delete_task(self, task_id: int):
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.repo.save_tasks(self.tasks)

    def stats(self) -> Dict[str, int]:
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.completed])
        pending = total - completed
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
        }


class Formatter:
    @staticmethod
    def task_line(task: Task) -> str:
        status = "✓" if task.completed else " "
        tags = f"[{', '.join(task.tags)}]" if task.tags else ""
        return f"{task.id:>3}. [{status}] {task.title} {tags} (p{task.priority})"

    @staticmethod
    def print_tasks(tasks: List[Task]):
        if not tasks:
            print("No tasks found.")
            return
        for task in sorted(tasks, key=lambda t: (t.completed, t.priority)):
            print(Formatter.task_line(task))

    @staticmethod
    def print_stats(stats: Dict[str, int]):
        print(f"Total     : {stats['total']}")
        print(f"Completed : {stats['completed']}")
        print(f"Pending   : {stats['pending']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="taskflow")
    sub = parser.add_subparsers(dest="command")

    add = sub.add_parser("add")
    add.add_argument("title")
    add.add_argument("--tags", nargs="*", default=[])
    add.add_argument("--priority", type=int, default=3)

    list_cmd = sub.add_parser("list")
    list_cmd.add_argument("--all", action="store_true")

    done = sub.add_parser("done")
    done.add_argument("id", type=int)

    reopen = sub.add_parser("reopen")
    reopen.add_argument("id", type=int)

    delete = sub.add_parser("delete")
    delete.add_argument("id", type=int)

    sub.add_parser("stats")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    repo = TaskRepository(DATA_FILE)
    service = TaskService(repo)

    if args.command == "add":
        task = service.add_task(args.title, args.tags, args.priority)
        print(f"Added task {task.id}")

    elif args.command == "list":
        tasks = service.list_tasks(show_all=args.all)
        Formatter.print_tasks(tasks)

    elif args.command == "done":
        service.complete_task(args.id)
        print(f"Task {args.id} completed")

    elif args.command == "reopen":
        service.reopen_task(args.id)
        print(f"Task {args.id} reopened")

    elif args.command == "delete":
        service.delete_task(args.id)
        print(f"Task {args.id} deleted")

    elif args.command == "stats":
        stats = service.stats()
        Formatter.print_stats(stats)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
