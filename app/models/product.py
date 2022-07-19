from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text

from db.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column("id", Integer, primary_key=True)
    title = Column("title", String(length=255), nullable=False, unique=True)
    description = Column("description", Text, nullable=False)
    price = Column("price", Float, nullable=False)
    image = Column("image", String(length=255))
    category_id = Column("category_id", Integer, ForeignKey("categories.id"))
    quantity = Column("quantity", Integer, nullable=False)
