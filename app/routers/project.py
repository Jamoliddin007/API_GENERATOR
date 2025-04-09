from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.db_session import get_db
from app.models.project import Project
from app.models.crud import CrudModel
from app.schemas.project import ProjectCreate
from app.schemas.crud import CrudModelCreate

router = APIRouter()

@router.post("/projects/create")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(name=project.name, subdomain=project.name.lower())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()

@router.post("/admin/{crud_id}/create")
def create_crud_model_for_admin(crud_id: int, data: CrudModelCreate, db: Session = Depends(get_db)):
    # Check CRUD exists
    crud = db.query(CrudModel).filter(CrudModel.id == crud_id).first()
    if not crud:
        raise HTTPException(status_code=404, detail="CRUD model not found")

    # Admin uchun create methodi ochiladi
    crud_model = CrudModel(name=data.name, project_id=crud.project_id)
    db.add(crud_model)
    db.commit()
    db.refresh(crud_model)
    return crud_model
