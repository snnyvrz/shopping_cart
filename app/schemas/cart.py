from pydantic import BaseModel, Field

from schemas.product import ProductInCartBase


class CartBase(BaseModel):
    user_id: int = Field(...)
    products: list[ProductInCartBase] | None = None


class CartCreate(CartBase):
    pass


class CartOut(CartBase):
    id: int

    class Config:
        orm_mode = True
