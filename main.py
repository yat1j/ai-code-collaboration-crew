from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "working"}

@app.get("/test")
def test():
    try:
        from src.crew import build_crew
        return {"import": "success"}
    except Exception as e:
        return {"error": str(e)}
