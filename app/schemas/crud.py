from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class CrudFieldCreate(BaseModel):
    name: str
    type: str
    nullable: Optional[bool] = True
    default: Optional[str] = None
    unique: Optional[bool] = False
    index: Optional[bool] = False
    primary_key: Optional[bool] = False
    onupdate: Optional[str] = None
    format: Optional[str] = None

    class Config:
        from_attributes = True
git add app/schemas/crud.py
git commit -m "✨ Update CrudFieldCreate schema to support full field options and use 'from_attributes'"

class CrudFieldOut(CrudFieldCreate):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
