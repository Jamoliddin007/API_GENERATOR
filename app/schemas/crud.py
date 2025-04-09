from pydantic import BaseModel
from typing import Optional

class CrudModelCreate(BaseModel):
    name: str

class CrudFieldCreate(BaseModel):
    name: str
    type: str
    nullable: Optional[bool] = True
    format: Optional[str] = None
