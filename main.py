from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from sqlalchemy import select, update, delete, String, Text
from sqlalchemy.orm import Mapped, mapped_column, Session

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

