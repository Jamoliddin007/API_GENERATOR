from pydantic import BaseModel

class WindowsCreate(BaseModel):


class WindowsOut(WindowsCreate):
    id: int

    class Config:
        orm_mode = True