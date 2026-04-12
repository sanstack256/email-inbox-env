def get_type(email):
    # handle BOTH dict and object
    if isinstance(email, dict):
        return email.get("type", "")
    return getattr(email, "type", "")


def easy_task_grader(actions, emails):
    total = len(emails)
    correct = sum([
        1 for a, e in zip(actions, emails)
        if a == "archive"
    ])

    score = correct / total if total > 0 else 0.5
    return min(max(score, 0.01), 0.99)


def medium_task_grader(actions, emails):
    total = len(emails)
    correct = sum([
        1 for a, e in zip(actions, emails)
        if get_type(e) == "spam" and a == "mark_spam"
    ])

    score = correct / total if total > 0 else 0.5
    return min(max(score, 0.01), 0.99)


def hard_task_grader(actions, emails):
    total = len(emails)
    correct = 0

    for a, e in zip(actions, emails):
        email_type = get_type(e)

        if email_type == "spam" and a == "mark_spam":
            correct += 1
        elif email_type == "work" and a == "mark_important":
            correct += 1
        elif email_type == "personal" and a == "reply":
            correct += 1

    score = correct / total if total > 0 else 0.5
    return min(max(score, 0.01), 0.99)
