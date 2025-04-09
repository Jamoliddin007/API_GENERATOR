from pydantic import BaseModel

class ToolsCreate(BaseModel):


class ToolsOut(ToolsCreate):
    id: int

    class Config:
        orm_mode = True