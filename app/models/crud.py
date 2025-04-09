from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database.db_session import Base

class CrudModel(Base):
    __tablename__ = "crud_models"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)  # length ni qo'shdik
    project_id = Column(Integer, ForeignKey("projects.id"))

class CrudField(Base):
    __tablename__ = "crud_fields"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)  # length ni qo'shdik
    type = Column(String(255), nullable=False)  # length ni qo'shdik
    nullable = Column(Boolean, default=True)
    default = Column(String(255), nullable=True)  # length ni qo'shdik
    unique = Column(Boolean, default=False)
    index = Column(Boolean, default=False)
    primary_key = Column(Boolean, default=False)
    onupdate = Column(String(255), nullable=True)  # length ni qo'shdik
    format = Column(String(255), nullable=True)  # length ni qo'shdik

    crud_id = Column(Integer, ForeignKey("crud_models.id"))
    crud = relationship("CrudModel", back_populates="fields")
