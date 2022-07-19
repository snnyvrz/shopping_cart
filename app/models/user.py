from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    username = Column(
        "username", String(length=255), nullable=False, unique=True
    )
    password = Column("password", String(length=255), nullable=False)
    is_admin = Column("is_admin", Boolean)
    is_superuser = Column("is_superuser", Boolean)
    cart = relationship("Cart", uselist=False)
