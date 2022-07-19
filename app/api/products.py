from fastapi import APIRouter, Depends, HTTPException, status

from auth.auth import is_admin
from crud import products
from schemas.product import ProductCreate, ProductOut

router = APIRouter()

product_404_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
)


@router.get(
    "/", response_model=list[ProductOut], status_code=status.HTTP_200_OK
)
async def get_all_products():
    return await products.get_all()


@router.post(
    "/", response_model=ProductOut, status_code=status.HTTP_201_CREATED
)
async def create_product(product: ProductCreate, _: bool = Depends(is_admin)):
    return await products.post(product)


@router.get(
    "/{id}/", response_model=ProductOut, status_code=status.HTTP_200_OK
)
async def get_product(id: int):
    return await products.get_by_id(id)


@router.put(
    "/{id}/", response_model=ProductOut, status_code=status.HTTP_202_ACCEPTED
)
async def update_product(
    id: int, product: ProductCreate, _: bool = Depends(is_admin)
):
    original_product = await products.get_by_id(id)
    if not original_product:
        raise product_404_exception
    return await products.put(id, product)


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(id: int, _: bool = Depends(is_admin)):
    product = await products.get_by_id(id)
    if not product:
        raise product_404_exception
    return await products.delete_by_id(id)
