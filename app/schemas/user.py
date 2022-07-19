from pydantic import BaseModel, Field

from schemas.cart import CartOut


class UserBase(BaseModel):
    username: str = Field(...)
    is_admin: bool | None = None
    is_superuser: bool | None = None


class UserCreate(UserBase):
    password: str = Field(...)


class UserOut(UserBase):
    id: int
    cart: CartOut | None = None

    class Config:
        orm_mode = True
