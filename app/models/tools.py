from sqlalchemy import Column, Integer, 

from app.database.db_session import Base


class Tools(Base):
    __tablename__ = "tools"

    id = Column(Integer, primary_key=True, index=True)
