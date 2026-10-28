
from fastapi import FastAPI

app = FastAPI()

APP_VERSION = "1.0"

@app.get("/")
def home():
    return {
        "application": "Deployment Rollback Lab",
        "version": APP_VERSION
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": APP_VERSION
    }
