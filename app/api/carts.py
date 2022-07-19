from fastapi import APIRouter, Depends, HTTPException, status

from auth.auth import is_admin
from crud import carts
from schemas.cart import CartCreate, CartOut

router = APIRouter()

cart_404_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Cart not found"
)


@router.get("/", response_model=list[CartOut], status_code=status.HTTP_200_OK)
async def get_all_carts(_: bool = Depends(is_admin)):
    return await carts.get_all()


@router.post("/", response_model=CartOut, status_code=status.HTTP_201_CREATED)
async def create_cart(cart: CartCreate, _: bool = Depends(is_admin)):
    return await carts.post(cart)


@router.get("/{id}/", response_model=CartOut, status_code=status.HTTP_200_OK)
async def get_cart(id: int, _: bool = Depends(is_admin)):
    cart = await carts.get_by_id(id)
    if not cart:
        raise cart_404_exception
    return cart


@router.put(
    "/{id}/", response_model=CartOut, status_code=status.HTTP_202_ACCEPTED
)
async def update_cart(id: int, cart: CartCreate, _: bool = Depends(is_admin)):
    original_cart = await carts.get_by_id(id)
    if not original_cart:
        raise cart_404_exception
    return await carts.put(id, cart)


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cart(id: int, _: bool = Depends(is_admin)):
    cart = await carts.get_by_id(id)
    if not cart:
        raise cart_404_exception
    return await carts.delete_by_id(id)
