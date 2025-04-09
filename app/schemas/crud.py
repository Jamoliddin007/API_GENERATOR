from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class CrudModelCreate(BaseModel):
    name: str
    project_id: Optional[int] = None

    class Config:
        from_attributes = True

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

class CrudFieldOut(CrudFieldCreate):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
