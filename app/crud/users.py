from sqlalchemy import delete, insert, select, update

from db.database import database
from models import User
from schemas.user import UserCreate


async def get_all():
    query = select(User)
    return await database.fetch_all(query)


async def get_by_id(id: int):
    query = select(User).where(User.id == id)
    return await database.fetch_one(query)


async def post(user: UserCreate):
    query = insert(User).values(
        username=user.username,
        password=user.password,
    )
    id = await database.execute(query)
    return {**user.dict(), "id": id}


async def put(id: int, user: UserCreate):
    query = (
        update(User)
        .where(User.id == id)
        .values(
            username=user.username,
            password=user.password,
        )
        .returning(User.id)
    )
    user_id = await database.execute(query)
    return {"id": user_id, **user.dict()}


async def delete_by_id(id: int):
    query = delete(User).where(User.id == id)
    return await database.execute(query)
