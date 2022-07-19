from sqlalchemy import delete, insert, select, update

from db.database import database
from models import Cart
from schemas.cart import CartCreate


async def get_all():
    query = select(Cart)
    return await database.fetch_all(query)


async def get_by_id(id: int):
    query = select(Cart).where(Cart.id == id)
    return await database.fetch_one(query)


async def post(cart: CartCreate):
    query = insert(Cart).values(user_id=cart.user_id)
    id = await database.execute(query)
    return {**cart.dict(), "id": id}


async def put(id: int, cart: CartCreate):
    query = (
        update(Cart)
        .where(Cart.id == id)
        .values(user_id=cart.user_id)
        .returning(Cart.id)
    )
    cart_id = await database.execute(query)
    return {"id": cart_id, **cart.dict()}


async def delete_by_id(id: int):
    query = delete(Cart).where(Cart.id == id)
    return await database.execute(query)
