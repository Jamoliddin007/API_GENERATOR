from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, UUID
from sqlalchemy.orm import relationship
from app.database.db_session import Base
from uuid import uuid4
from datetime import datetime

class CrudModel(Base):
    __tablename__ = "crud_models"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"))
    uuid_code = Column(UUID, default=uuid4, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class CrudField(Base):
    __tablename__ = "crud_fields"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    nullable = Column(Boolean, default=True)
    default = Column(String(255), nullable=True)
    unique = Column(Boolean, default=False)
    index = Column(Boolean, default=False)
    primary_key = Column(Boolean, default=False)
    onupdate = Column(String(255), nullable=True)
    format = Column(String(255), nullable=True)

    crud_id = Column(Integer, ForeignKey("crud_models.id"))
    crud = relationship("CrudModel", back_populates="fields")
