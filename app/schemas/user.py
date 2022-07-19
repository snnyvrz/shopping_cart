from pydantic import BaseModel, Field

from schemas.cart import CartOut


class UserBase(BaseModel):
    username: str = Field(...)


class UserCreate(UserBase):
    password: str = Field(...)


class UserOut(UserBase):
    id: int
    carts: list[CartOut] | None = None

    class Config:
        orm_mode = True
