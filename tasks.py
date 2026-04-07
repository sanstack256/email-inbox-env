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
    return score

def hard_task_grader(actions, emails):
    score = 0

    for i in range(len(actions)):
        action = actions[i]
        email = emails[i]

        # correct classification
        if email["type"] == "spam" and action == "mark_spam":
            score += 1
        elif email["type"] == "work" and action == "mark_important":
            score += 1
        elif email["type"] == "personal" and action == "reply":
            score += 1
        else:
            score -= 1  # penalty for wrong decisions

    # normalize score between 0 and 1
    max_score = len(emails)
    final_score = max(0, score) / max_score

    return final_score