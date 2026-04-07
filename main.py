from environment import EmailEnvironment
from tasks import easy_task_grader
from tasks import hard_task_grader

env = EmailEnvironment()

email = env.reset()

done = False
actions_taken = []

while not done:
    print("\nCurrent Email:", email)

    # fake AI decision
    if email.type == "spam":
        action = "mark_spam"
    elif email.type == "work":
        action = "mark_important"
    elif email.type == "personal":
        action = "reply"

    actions_taken.append(action)

    print("Action taken:", action)

    email, reward, done, _ = env.step(action)

    print("Reward:", reward)

# grading
score = easy_task_grader(actions_taken, env.emails)

print("\nFinal Score:", score)


score = hard_task_grader(actions_taken, env.emails)
print("\nFinal Score (Hard Task):", score)