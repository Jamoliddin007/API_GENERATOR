from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from app.database.db_session import Base
from uuid import uuid4
from datetime import datetime

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    subdomain = Column(String(255), nullable=False, unique=True)  
    admin_token = Column(String(255), nullable=False, default=str(uuid4())) 
    client_token = Column(String(255), nullable=True, default=str(uuid4())) 
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
