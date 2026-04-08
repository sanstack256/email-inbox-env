import os
from openai import OpenAI
from environment import EmailEnvironment
from tasks import hard_task_grader

# Initialize OpenAI client using proxy
client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

env = EmailEnvironment()

email = env.reset()

done = False
actions_taken = []

print("[START] Running inference")

while not done:
    print(f"[STEP] Current email: {email}")

    # Format email
    email_text = f"""
    Subject: {email.subject}
    Body: {email.body}
    Type: {email.type}
    """

    # Safe model selection
    model = os.environ.get("MODEL_NAME", "gpt-3.5-turbo")

    try:
        # LLM call (REQUIRED)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an email assistant. Choose one action: mark_spam, mark_important, reply, archive."
                },
                {
                    "role": "user",
                    "content": f"Given this email:\n{email_text}\nWhat should be the correct action?"
                }
            ]
        )

        action = response.choices[0].message.content.strip().lower()

    except Exception as e:
        print(f"[ERROR] LLM failed: {e}")
        action = "archive"

    # Safety check
    if action not in ["mark_spam", "mark_important", "reply", "archive"]:
        action = "archive"

    print(f"[STEP] Action: {action}")

    actions_taken.append(action)

    email, reward, done, _ = env.step(action)

    print(f"[STEP] Reward: {reward.reward}")

# Final scoring
score = hard_task_grader(actions_taken, env.emails)

print(f"[END] Final Score: {score}")
