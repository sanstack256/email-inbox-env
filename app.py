from fastapi import FastAPI
from environment import EmailEnvironment

app = FastAPI()

env = EmailEnvironment()

@app.get("/")
def home():
    return {"message": "Email Environment Running"}

@app.post("/reset")
def reset():
    email = env.reset()
    return email.dict()

@app.post("/step")
def step(action: str):
    email, reward, done, _ = env.step(action)

    return {
        "next_email": email.dict() if email else None,
        "reward": reward.reward,
        "done": done
    }