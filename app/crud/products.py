from sqlalchemy import delete, insert, select, update

from db.database import database
from models import Product
from schemas.product import ProductCreate


async def get_all():
    query = select(Product)
    return await database.fetch_all(query)


async def get_by_id(id: int):
    query = select(Product).where(Product.id == id)
    return await database.fetch_one(query)


async def post(product: ProductCreate):
    query = insert(Product).values(
        price=product.price,
        quantity=product.quantity,
        title=product.title,
        description=product.description,
        image=product.image,
        category_id=product.category_id,
    )
    id = await database.execute(query)
    return {**product.dict(), "id": id}


async def put(id: int, product: ProductCreate):
    query = (
        update(Product)
        .where(Product.id == id)
        .values(
            price=product.price,
            quantity=product.quantity,
            title=product.title,
            description=product.description,
            image=product.image,
            category_id=product.category_id,
        )
        .returning(Product.id)
    )
    product_id = await database.execute(query)
    return {"id": product_id, **product.dict()}


async def delete_by_id(id: int):
    query = delete(Product).where(Product.id == id)
    return await database.execute(query)
