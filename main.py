from fastapi import FastAPI

app = FastAPI(title="FitBuddy")


@app.get("/")
def home():
    return {"message": "FitBuddy is running!"}
