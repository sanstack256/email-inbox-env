from email_data import emails
from pydantic import BaseModel


class EmailObservation(BaseModel):
    id: int
    subject: str
    body: str
    type: str


class EmailAction(BaseModel):
    action: str


class EmailReward(BaseModel):
    reward: float


class EmailEnvironment:
    def __init__(self):
        self.emails = emails
        self.current_index = 0

    def reset(self):
        self.current_index = 0
        return EmailObservation(**self.emails[self.current_index])

    def step(self, action):
        current_email = EmailObservation(**self.emails[self.current_index])

        reward = 0

        if action == "mark_spam" and current_email.type == "spam":
            reward = 1
        elif action == "mark_important" and current_email.type == "work":
            reward = 1
        elif action == "reply" and current_email.type == "personal":
            reward = 1
        elif action == "archive":
            reward = 0
        elif action == "escalate" and current_email.type == "work":
            reward = 2
        else:
            reward = -1

        self.current_index += 1

        done = self.current_index >= len(self.emails)

        if not done:
            next_email = EmailObservation(**self.emails[self.current_index])
        else:
            next_email = None

        return next_email, EmailReward(reward=reward), done, {}

    def state(self):
        return {
            "current_index": self.current_index,
            "remaining_emails": len(self.emails) - self.current_index
        }
