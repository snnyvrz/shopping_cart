from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    title: str = Field(...)
    description: str | None = None
    price: float = Field(...)
    image: str | None = None
    quantity: int = Field(...)
    category_id: int = Field(...)


class ProductCreate(ProductBase):
    pass


class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductInCartBase(BaseModel):
    product_id: int = Field(...)
    quantity_in_cart: int = Field(...)


class ProductInCartOut(ProductInCartBase):
    id: int

    class Config:
        orm_mode = True
