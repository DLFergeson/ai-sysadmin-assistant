from dotenv import load_dotenv; load_dotenv()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Web UI placeholder"}
