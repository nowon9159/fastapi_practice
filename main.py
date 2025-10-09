from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from sqlalchemy import select, update, delete, String, Text
from sqlalchemy.orm import Mapped, mapped_column, Session
from database import get_db, Item, engine, Base


app = FastAPI()

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("테이블이 생성되었습니다!")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def get_item_by_id(item_id: int, db: Session = Depends(get_db)):
    # 특정 ID로 아이템 조회
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/db/info")
def get_database_info(db: Session = Depends(get_db)):
    # 테이블 정보 조회
    from sqlalchemy import inspect
    inspector = inspect(engine)
    
    tables = inspector.get_table_names()
    items_columns = inspector.get_columns('items') if 'items' in tables else []
    
    return {
        "tables": tables,
        "items_columns": items_columns,
        "items_count": db.query(Item).count()
    }