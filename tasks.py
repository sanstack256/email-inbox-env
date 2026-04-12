def easy_task_grader(actions, emails):
    total = len(emails)
    if total == 0:
        return 0.5

    correct = 0
    for a in actions:
        if a == "archive":
            correct += 1

    score = correct / total

    if score <= 0:
        return 0.1
    if score >= 1:
        return 0.9

    return score


def medium_task_grader(actions, emails):
    total = len(emails)
    if total == 0:
        return 0.5

    correct = 0
    for a, e in zip(actions, emails):
        if isinstance(e, dict) and e["type"] == "spam" and a == "mark_spam":
            correct += 1

    score = correct / total

    if score <= 0:
        return 0.2
    if score >= 1:
        return 0.8

    return score


def hard_task_grader(actions, emails):
    total = len(emails)
    if total == 0:
        return 0.5

    correct = 0

    for a, e in zip(actions, emails):
        t = e["type"] if isinstance(e, dict) else e.type

        if t == "spam" and a == "mark_spam":
            correct += 1
        elif t == "work" and a == "mark_important":
            correct += 1
        elif t == "personal" and a == "reply":
            correct += 1

    score = correct / total

    if score <= 0:
        return 0.3
    if score >= 1:
        return 0.9

    return score
