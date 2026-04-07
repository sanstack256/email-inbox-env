from environment import EmailEnvironment
from tasks import hard_task_grader

env = EmailEnvironment()

email = env.reset()

done = False
actions_taken = []

print("[START] Running inference")

while not done:
    print(f"[STEP] Current email: {email}")

    # simple rule-based agent
    if email.type == "spam":
        action = "mark_spam"
    elif email.type == "work":
        action = "mark_important"
    elif email.type == "personal":
        action = "reply"
    else:
        action = "archive"

    print(f"[STEP] Action: {action}")

    actions_taken.append(action)

    email, reward, done, _ = env.step(action)

    print(f"[STEP] Reward: {reward.reward}")

score = hard_task_grader(actions_taken, env.emails)

print(f"[END] Final Score: {score}")