from pydantic import BaseModel, Field

from schemas.cart_product import CartProductOut


class CartBase(BaseModel):
    user_id: int = Field(...)
    products: list[CartProductOut] | None = None


class CartCreate(CartBase):
    pass


class CartOut(CartBase):
    id: int

    class Config:
        orm_mode = True
