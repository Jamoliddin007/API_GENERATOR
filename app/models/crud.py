from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database.db_session import Base

class CrudModel(Base):
    __tablename__ = "crud_models"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"))

class CrudField(Base):
    __tablename__ = "crud_fields"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    nullable = Column(Boolean, default=True)
    format = Column(String, nullable=True)
    crud_id = Column(Integer, ForeignKey("crud_models.id"))
