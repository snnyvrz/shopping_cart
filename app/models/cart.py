from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from db.database import Base


class Cart(Base):
    __tablename__ = "carts"

    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"))
    products = relationship("Product", secondary="cart_products")
