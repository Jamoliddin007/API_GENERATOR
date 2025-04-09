from fastapi import FastAPI
from app.core.config import settings
from app.routers import project
from app.database.db_session import Base, engine
from app.routers import crud
from app.routers import news,project,products



Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(project.router)
app.include_router(crud.router)
app.include_router(news.router)
app.include_router(project.router)
app.include_router(products.router)