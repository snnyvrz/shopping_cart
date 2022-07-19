from fastapi import FastAPI
import uvicorn

from db.database import database, init_db
from api import carts, categories, products, users

init_db()

app = FastAPI()

app.include_router(
    categories.router, prefix="/categories", tags=["categories"]
)
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(carts.router, prefix="/carts", tags=["carts"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="127.0.0.1", port=5000, log_level="info", reload=True
    )
