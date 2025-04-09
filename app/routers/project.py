from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.db_session import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate

router = APIRouter()

@router.post("/projects/create")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(name=project.name)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()
