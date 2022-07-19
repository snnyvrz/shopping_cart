from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(...)


class CategoryCreate(CategoryBase):
    pass


class CategoryOut(CategoryBase):
    id: int

    class Config:
        orm_mode = True
