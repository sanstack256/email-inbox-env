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

        # reward logic
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

        # move to next email
        self.current_index += 1

        done = self.current_index >= len(self.emails)

        if not done:
            next_email = self.emails[self.current_index]
        else:
            next_email = None

        if next_email:
            next_obs = EmailObservation(**next_email)
        else:
            next_obs = None

        return next_obs, EmailReward(reward=reward), done, {}

    def state(self):
        return {
            "current_index": self.current_index,
            "remaining_emails": len(self.emails) - self.current_index
        }