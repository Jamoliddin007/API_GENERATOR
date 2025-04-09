from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db_session import get_db
from app.models.news import News
from app.schemas.news import NewsCreate, NewsOut

router = APIRouter(prefix="/news", tags=["News"])

@router.post("/", response_model=NewsOut)
def create_news(data: NewsCreate, db: Session = Depends(get_db)):
    new = News(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.get("/", response_model=list[NewsOut])
def list_news(db: Session = Depends(get_db)):
    return db.query(News).all()