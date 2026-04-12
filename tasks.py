def easy_task_grader(actions, emails):
    correct = 0

    for i in range(len(actions)):
        action = actions[i]
        email = emails[i]

        if action == "mark_spam" and email["type"] == "spam":
            correct += 1
        elif action == "mark_important" and email["type"] == "work":
            correct += 1
        elif action == "reply" and email["type"] == "personal":
            correct += 1

    score = correct / len(emails)


    score = max(0.01, min(score, 0.99))

    return score


def medium_task_grader(actions, emails):
    correct = 0

    for i in range(len(actions)):
        action = actions[i]
        email = emails[i]


        if action in ["mark_spam", "archive"] and email["type"] == "spam":
            correct += 1
        elif action in ["mark_important", "escalate"] and email["type"] == "work":
            correct += 1
        elif action in ["reply", "archive"] and email["type"] == "personal":
            correct += 1

    score = correct / len(emails)


    score = max(0.01, min(score, 0.99))

    return score


def hard_task_grader(actions, emails):
    score = 0

    for i in range(len(actions)):
        action = actions[i]
        email = emails[i]

        if email["type"] == "spam" and action == "mark_spam":
            score += 1
        elif email["type"] == "work" and action == "mark_important":
            score += 1
        elif email["type"] == "personal" and action == "reply":
            score += 1
        else:
            score -= 1  # penalty

    max_score = len(emails)

    # normalize
    final_score = max(0, score) / max_score


    final_score = max(0.01, min(final_score, 0.99))

    return final_score


TASKS = [
    {"name": "easy", "grader": easy_task_grader},
    {"name": "medium", "grader": medium_task_grader},
    {"name": "hard", "grader": hard_task_grader},
]
