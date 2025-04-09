from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db_session import get_db
from app.models.windows import Windows
from app.schemas.windows import WindowsCreate, WindowsOut

router = APIRouter(prefix="/windows", tags=["Windows"])

@router.post("/", response_model=WindowsOut)
def create_windows(data: WindowsCreate, db: Session = Depends(get_db)):
    new = Windows(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.get("/", response_model=list[WindowsOut])
def list_windows(db: Session = Depends(get_db)):
    return db.query(Windows).all()