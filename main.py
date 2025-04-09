from fastapi import FastAPI
from app.database.db_session import Base, engine
from app.routers import crud

from app.routers import crud, project

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Generator")


app.include_router(project.router)

app.include_router(crud.router)  # crud routeri