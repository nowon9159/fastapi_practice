import fastapi

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/health")
def read_health():
    return {"status": "ok"}