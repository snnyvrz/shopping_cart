from sqlalchemy import Column, Integer, String

from db.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(length=255), nullable=False, unique=True)
