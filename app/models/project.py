from sqlalchemy import Column, Integer, String
from app.database.db_session import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    subdomain = Column(String, unique=True, nullable=False)
    admin_token = Column(String, nullable=False)
    client_token = Column(String, nullable=False)
