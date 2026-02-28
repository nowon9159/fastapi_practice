from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# --- Week 0: 기본 엔드포인트 ---

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/health")
def read_health():
    return {"status": "ok"}

