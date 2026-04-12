def easy_task_grader(actions, emails):
    total = len(emails)
    correct = sum([1 for a, e in zip(actions, emails) if a == "archive"])
    
    score = correct / total if total > 0 else 0.5
    return min(max(score, 0.01), 0.99)


def medium_task_grader(actions, emails):
    total = len(emails)
    correct = sum([
        1 for a, e in zip(actions, emails)
        if (e["type"] == "spam" and a == "mark_spam")
    ])
    
    score = correct / total if total > 0 else 0.5
    return min(max(score, 0.01), 0.99)


def hard_task_grader(actions, emails):
    total = len(emails)
    correct = 0

    for a, e in zip(actions, emails):
        if e["type"] == "spam" and a == "mark_spam":
            correct += 1
        elif e["type"] == "work" and a == "mark_important":
            correct += 1
        elif e["type"] == "personal" and a == "reply":
            correct += 1

    score = correct / total if total > 0 else 0.5
    return min(max(score, 0.01), 0.99)
