from pydantic import BaseModel, Field

from schemas.category import CategoryCreate


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
