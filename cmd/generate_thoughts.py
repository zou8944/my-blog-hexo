import os
import sys
from datetime import datetime


class DayThought:

    def __init__(self, date: datetime, thoughts: list[str]):
        self.date = date
        self.thoughts = thoughts


def generate_thoughts_single_file(file_path: str):
    day_thoughts = []
    with open(file_path) as f:
        lines = f.readlines()
        days = []
        day_lines = []
        for line in lines:
            line = line.strip("\n")
            if line.strip().startswith("##"):
                if day_lines:
                    days.append(day_lines)
                day_lines = []
            day_lines.append(line)
        if day_lines:
            days.append(day_lines)

        for day_lines in days:
            date = datetime.strptime(day_lines[0].strip("#").strip(" \n"), "%Y-%m-%d")
            thoughts = day_lines[1:]
            day_thoughts.append(DayThought(date, thoughts))
    return day_thoughts


def generate_thoughts_content(dir: str):
    day_thoughts = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            day_thoughts.extend(generate_thoughts_single_file(file_path))
    return day_thoughts


def print_front_matter():
    print("---")
    print("title: 小想法")
    print("""date: 2024-06-29 17:54:50""")
    print("---")
    print()


def print_day_thoughts(day_thoughts: list[DayThought]):
    day_thoughts.sort(key=lambda x: x.date, reverse=True)
    for day_thought in day_thoughts:
        print("## " + day_thought.date.strftime("%Y-%m-%d"))
        for thought in day_thought.thoughts:
            print(thought)
        print()


if __name__ == '__main__':
    thought_dir = sys.argv[1]
    # thought_dir = 'cache/my-words-main/thoughts'
    print_front_matter()
    print_day_thoughts(generate_thoughts_content(thought_dir))
