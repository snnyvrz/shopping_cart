from sqlalchemy import Column, ForeignKey, Integer

from db.database import Base


class CartProduct(Base):
    __tablename__ = "cart_products"

    id = Column("id", Integer, primary_key=True)
    product_quantity = Column("product_quantity", Integer)
    cart_id = Column("cart_id", Integer, ForeignKey("carts.id"))
    product_id = Column("product_id", Integer, ForeignKey("products.id"))
