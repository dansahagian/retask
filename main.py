#! /Users/dan/d/code/retodo/venv/bin/python3

from datetime import date
from enum import Enum
from pathlib import Path
from typing import Tuple, List

from pydantic import BaseModel

from config import PATH_TO_DAILY_DIR, TODOS


class IntervalType(str, Enum):
    DAY = "d"
    WEEK = "w"
    MONTH = "m"


class Todo(BaseModel):
    start_date: date
    interval_num: int
    interval_type: IntervalType
    description: str


def is_due_today(today: date, todo: Todo) -> bool:
    delta_days = (today - todo.start_date).days

    if delta_days < 0:
        return False
    if todo.interval_type == "w":
        return delta_days % 7 == 0
    if todo.interval_type == "m" and today.day == todo.start_date.day:
        return True
    return delta_days == 0


def generate_todos(today: date, todos: Tuple[Tuple[str, int, str, str]]) -> List[Todo]:
    output = []
    for t in todos:
        start_date, interval_num, interval_type, description = t
        todo = Todo(
            start_date=start_date,
            interval_num=interval_num,
            interval_type=interval_type,
            description=description,
        )

        if is_due_today(today, todo):
            output.append(todo)

    return output


def write_todos(path: Path, todos: List[Todo]):
    if path.exists():
        with open(path, "a") as f:
            f.write("\n## Tasks\n")
            for todo in todos:
                f.write(f"- [ ] {todo.description}\n")
    else:
        with open(path, "w") as f:
            f.write("\n## Tasks\n")
            for todo in todos:
                f.write(f"- [ ] {todo.description}\n")


def main():
    today = date.today()
    path = Path(PATH_TO_DAILY_DIR, f"{today.strftime('%Y-%m-%d')}.md")

    todos = generate_todos(today, TODOS)
    write_todos(path, todos)


if __name__ == "__main__":
    main()
