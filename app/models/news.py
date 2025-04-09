from sqlalchemy import Column, String,Integer
from app.database.db_session import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, max_length=255)

    view = Column(String, nullable=False, max_length=255)
