from sqlalchemy import Column, Integer

from app.database.db_session import Base


class Windows(Base):
    __tablename__ = "windows"

    id = Column(Integer, primary_key=True, index=True)
