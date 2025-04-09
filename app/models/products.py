from sqlalchemy import Column, Integer, Integer, String, Boolean, UUID

from uuid import uuid4

from app.database.db_session import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False, max_length=255)

    description = Column(String)

    price = Column(Integer, nullable=False)

    is_active = Column(Boolean)

    uuid_code = Column(UUID, nullable=False, default=uuid4())
