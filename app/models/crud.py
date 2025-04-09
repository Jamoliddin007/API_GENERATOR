from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db_session import Base

class CrudModel(Base):
    __tablename__ = "crud_models"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"))

class CrudField(Base):
    __tablename__ = "crud_fields"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    nullable = Column(Boolean, default=True)
    default = Column(String, nullable=True)
    unique = Column(Boolean, default=False)
    index = Column(Boolean, default=False)
    primary_key = Column(Boolean, default=False)
    onupdate = Column(String, nullable=True)
    format = Column(String, nullable=True)

    crud_id = Column(Integer, ForeignKey("crud_models.id"))
    crud = relationship("CrudModel", back_populates="fields")
