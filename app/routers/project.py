# app/routers/project.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import uuid4

from app.database.db_session import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectOut

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=ProjectOut)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    admin_token = str(uuid4())
    client_token = str(uuid4())

    db_project = Project(
        name=project.name,
        subdomain=project.subdomain,
        admin_token=admin_token,
        client_token=client_token,
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/", response_model=list[ProjectOut])
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()
