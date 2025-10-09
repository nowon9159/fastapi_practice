from sqlalchemy import create_engine, Integer, String, Text, DateTime, func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session
from datetime import datetime

DB_URL = "sqlite:///./app.db"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class Item(Base):
    __tablename__ = "items"
    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, index=True)
    description = mapped_column(Text, index=True)
    created_at = mapped_column(DateTime, default=datetime.utcnow)
    updated_at = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

