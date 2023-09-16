from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Tuple, List

from config import PATH_TO_DAILY_DIR, TASKS


@dataclass
class Task:
    start_date: date
    interval_num: int
    interval_type: str
    description: str


def is_due_today(today: date, task: Task) -> bool:
    delta_days = (today - task.start_date).days

    if delta_days < 0:
        return False
    if task.interval_type == "w":
        return delta_days % 7 == 0
    if task.interval_type == "m" and today.day == task.start_date.day:
        return True
    return delta_days == 0


def generate_tasks(today: date, tasks: Tuple[Tuple[str, int, str, str]]) -> List[Task]:
    output = []
    for t in tasks:
        start_date, interval_num, interval_type, description = t
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        task = Task(
            start_date=start_date,
            interval_num=interval_num,
            interval_type=interval_type,
            description=description,
        )

        if is_due_today(today, task):
            output.append(task)

    return output


def write_tasks(path: Path, tasks: List[Task]):
    if path.exists():
        with open(path, "a") as f:
            f.write("\n## Tasks\n")
            for task in tasks:
                f.write(f"- [ ] {task.description}\n")
    else:
        with open(path, "w") as f:
            f.write("\n## Tasks\n")
            for task in tasks:
                f.write(f"- [ ] {task.description}\n")


def main():
    today = date.today()
    path = Path(PATH_TO_DAILY_DIR, f"{today.strftime('%Y-%m-%d')}.md")

    tasks = generate_tasks(today, TASKS)
    write_tasks(path, tasks)


if __name__ == "__main__":
    main()
