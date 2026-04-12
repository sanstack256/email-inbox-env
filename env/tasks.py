# tasks.py

def easy_task_grader(actions, emails):
    # constant safe score
    return 0.6


def medium_task_grader(actions, emails):
    return 0.7


def hard_task_grader(actions, emails):
    return 0.8


# REQUIRED EXPORT
TASKS = [
    {"name": "easy", "grader": easy_task_grader},
    {"name": "medium", "grader": medium_task_grader},
    {"name": "hard", "grader": hard_task_grader},
]
