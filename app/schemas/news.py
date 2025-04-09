from pydantic import BaseModel

class NewsCreate(BaseModel):

    title: str

    view: str


class NewsOut(NewsCreate):
    id: int

    class Config:
        orm_mode = True