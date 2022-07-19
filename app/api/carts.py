from fastapi import APIRouter, HTTPException, status

from crud import carts
from schemas.cart import CartCreate, CartOut

router = APIRouter()


@router.get("/", response_model=list[CartOut], status_code=status.HTTP_200_OK)
async def get_all_carts():
    return await carts.get_all()


@router.post("/", response_model=CartOut, status_code=status.HTTP_201_CREATED)
async def create_cart(cart: CartCreate):
    return await carts.post(cart)


@router.get("/{id}/", response_model=CartOut, status_code=status.HTTP_200_OK)
async def get_cart(id: int):
    cart = await carts.get_by_id(id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart


@router.put(
    "/{id}/", response_model=CartOut, status_code=status.HTTP_202_ACCEPTED
)
async def update_cart(id: int, cart: CartCreate):
    original_cart = await carts.get_by_id(id)
    if not original_cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return await carts.put(id, cart)


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cart(id: int):
    cart = await carts.get_by_id(id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return await carts.delete_by_id(id)
