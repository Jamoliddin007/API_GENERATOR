# app/schemas/project.py

from pydantic import BaseModel

class ProjectBase(BaseModel):
    name: str
    subdomain: str

class ProjectCreate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    id: int
    admin_token: str
    client_token: str

    class Config:
        orm_mode = True
