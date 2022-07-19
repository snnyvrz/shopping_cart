from pydantic import BaseModel, Field


class CartProductBase(BaseModel):
    product_quantity: int = Field(...)
    product_id: int = Field(...)


class CartProductCreate(CartProductBase):
    pass


class CartProductOut(CartProductBase):
    class Config:
        orm_mode = True
