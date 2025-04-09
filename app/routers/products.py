from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db_session import get_db
from app.models.products import Products
from app.schemas.products import ProductsCreate, ProductsOut

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductsOut)
def create_products(data: ProductsCreate, db: Session = Depends(get_db)):
    new = Products(**data.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.get("/", response_model=list[ProductsOut])
def list_products(db: Session = Depends(get_db)):
    return db.query(Products).all()