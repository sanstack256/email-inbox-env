import random


def get_type(email):
    if isinstance(email, dict):
        return email.get("type", "")
    return getattr(email, "type", "")


def normalize(score):
    # force strictly inside (0,1) with smoothing
    return max(0.05, min(score, 0.95))


def easy_task_grader(actions, emails):
    total = len(emails)

    correct = sum([
        1 for a, e in zip(actions, emails)
        if a == "archive"
    ])

    score = correct / total if total > 0 else 0.5

    # smoothing to avoid extremes
    score = 0.8 * score + 0.1

    return normalize(score)


def medium_task_grader(actions, emails):
    total = len(emails)

    correct = sum([
        1 for a, e in zip(actions, emails)
        if get_type(e) == "spam" and a == "mark_spam"
    ])

    score = correct / total if total > 0 else 0.5
    score = 0.7 * score + 0.15

    return normalize(score)


def hard_task_grader(actions, emails):
    total = len(emails)
    correct = 0

    for a, e in zip(actions, emails):
        t = get_type(e)

        if t == "spam" and a == "mark_spam":
            correct += 1
        elif t == "work" and a == "mark_important":
            correct += 1
        elif t == "personal" and a == "reply":
            correct += 1

    score = correct / total if total > 0 else 0.5

    # smoothing + noise to avoid perfect scores
    score = 0.75 * score + 0.1
    score += random.uniform(-0.05, 0.05)

    return normalize(score)
