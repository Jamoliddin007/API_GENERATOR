from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db_session import get_db
from app.models.crud import CrudModel, CrudField
from app.models.project import Project
from app.schemas.crud import CrudModelCreate, CrudFieldCreate

router = APIRouter(prefix="/crud", tags=["CRUD Builder"])

@router.post("/project/create")
def create_crud_model(data: CrudModelCreate, db: Session = Depends(get_db)):
    # Oxirgi projectni olish
    project = db.query(Project).order_by(Project.id.desc()).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    crud = CrudModel(name=data.name, project_id=project.id)
    db.add(crud)
    db.commit()
    db.refresh(crud)
    return crud



@router.post("/{crud_id}/fields/")
def add_field_to_crud(crud_id: int, field: CrudFieldCreate, db: Session = Depends(get_db)):
    # Check CRUD exists
    crud = db.query(CrudModel).filter(CrudModel.id == crud_id).first()
    if not crud:
        raise HTTPException(status_code=404, detail="CRUD model not found")

    db_field = CrudField(
        name=field.name,
        type=field.type,
        nullable=field.nullable,
        format=field.format,
        crud_id=crud_id
    )
    db.add(db_field)
    db.commit()
    db.refresh(db_field)
    return db_field
