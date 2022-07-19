from sqlalchemy import delete, insert, select, update

from auth.utils import get_password_hash
from db.database import database
from models import User
from schemas.user import UserCreate, UserOut


async def get_all():
    query = select(User)
    return await database.fetch_all(query)


async def get_by_id(id: int):
    query = select(User).where(User.id == id)
    return await database.fetch_one(query)


async def get_user_by_username(username: str):
    query = select(User).where(User.username == username)
    return await database.fetch_one(query)


async def post(user: UserCreate):
    query = insert(User).values(
        username=user.username,
        password=get_password_hash(user.password),
    )
    id = await database.execute(query)
    return {**user.dict(), "id": id}


async def put(id: int, user: UserOut):
    query = (
        update(User)
        .where(User.id == id)
        .values(
            username=user.username,
            password=get_password_hash(user.password),
            is_admin=user.is_admin,
            is_superuser=user.is_superuser,
            carts=user.carts,
        )
    )
    user_id = await database.execute(query)
    return {"id": user_id, **user.dict()}


async def delete_by_id(id: int):
    query = delete(User).where(User.id == id)
    return await database.execute(query)
