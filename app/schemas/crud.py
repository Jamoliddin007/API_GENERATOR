from pydantic import BaseModel
from typing import Optional

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
