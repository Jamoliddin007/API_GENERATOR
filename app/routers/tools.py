from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db_session import get_db
from app.models.tools import Tools
from app.schemas.tools import ToolsCreate, ToolsOut

router = APIRouter(prefix="/tools", tags=["Tools"])

@router.post("/", response_model=ToolsOut)
def create_tools(data: ToolsCreate, db: Session = Depends(get_db)):
    new = Tools(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.get("/", response_model=list[ToolsOut])
def list_tools(db: Session = Depends(get_db)):
    return db.query(Tools).all()