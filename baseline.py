from environment import EmailEnvironment
from tasks import hard_task_grader

env = EmailEnvironment()

email = env.reset()

done = False
actions_taken = []

while not done:
    # simple rule-based agent
    if email.type == "spam":
        action = "mark_spam"
    elif email.type == "work":
        action = "mark_important"
    elif email.type == "personal":
        action = "reply"
    else:
        action = "archive"

    actions_taken.append(action)

    email, reward, done, _ = env.step(action)

score = hard_task_grader(actions_taken, env.emails)

print("Baseline Score:", score)