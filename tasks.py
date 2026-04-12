def easy_task_grader(actions, emails):
    score = 0.6
    return score


def medium_task_grader(actions, emails):
    score = 0.7
    return score


def hard_task_grader(actions, emails):
    correct = 0

    for i in range(len(actions)):
        action = actions[i]
        email = emails[i]

        if email["type"] == "spam" and action == "mark_spam":
            correct += 1
        elif email["type"] == "work" and action == "mark_important":
            correct += 1
        elif email["type"] == "personal" and action == "reply":
            correct += 1

    score = correct / len(emails)


    if score <= 0:
        score = 0.1
    elif score >= 1:
        score = 0.9

    return score


TASKS = [
    {"name": "easy", "grader": easy_task_grader},
    {"name": "medium", "grader": medium_task_grader},
    {"name": "hard", "grader": hard_task_grader},
]
