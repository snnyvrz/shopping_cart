from sqlalchemy import delete, insert, select, update

from db.database import database
from models import Category
from schemas.category import CategoryCreate


async def get_all():
    query = select(Category)
    return await database.fetch_all(query)


async def get_by_id(id: int):
    query = select(Category).where(Category.id == id)
    return await database.fetch_one(query)


async def post(category: CategoryCreate):
    query = insert(Category).values(name=category.name)
    id = await database.execute(query)
    return {**category.dict(), "id": id}


async def put(id: int, category: CategoryCreate):
    query = (
        update(Category)
        .where(Category.id == id)
        .values(name=category.name)
        .returning(Category.id)
    )
    category_id = await database.execute(query)
    return {"id": category_id, **category.dict()}


async def delete_by_id(id: int):
    query = delete(Category).where(Category.id == id)
    return await database.execute(query)
