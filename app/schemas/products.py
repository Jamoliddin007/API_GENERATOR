from pydantic import BaseModel

class ProductsCreate(BaseModel):

    name: str

    description: str

    price: int

    is_active: bool

    uuid_code: str


class ProductsOut(ProductsCreate):
    id: int

    class Config:
        orm_mode = True