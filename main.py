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

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/articles")
def create_article(article: Article, db: Session = Depends(get_db)):
    db_article = Article(author=article.author, title=article.title, content=article.content)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

@app.get("/articles/{article_id}")
def get_article_by_id(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@app.put("/articles/{article_id}")
def update_article(article_id: int, article: Article, db: Session = Depends(get_db)):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    db_article.author = article.author
    db_article.title = article.title
    db_article.content = article.content
    db.commit()
    db.refresh(db_article)
    return db_article

@app.delete("/articles/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    db.delete(db_article)
    db.commit()
    return {"message": "Article deleted successfully"}

