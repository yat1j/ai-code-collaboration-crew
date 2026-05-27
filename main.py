from fastapi import FastAPI
from src.crew import build_crew
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/generate")
def generate(feature: str):
    crew = build_crew(feature)
    result = crew.kickoff()

    return {
        "result": str(result)
    }
