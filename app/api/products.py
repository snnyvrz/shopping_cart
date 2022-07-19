from fastapi import APIRouter, HTTPException, status

from crud import products
from schemas.product import ProductCreate, ProductOut

router = APIRouter()


@router.get(
    "/", response_model=list[ProductOut], status_code=status.HTTP_200_OK
)
async def get_all_products():
    return await products.get_all()


@router.post(
    "/", response_model=ProductOut, status_code=status.HTTP_201_CREATED
)
async def create_product(product: ProductCreate):
    return await products.post(product)


@router.get(
    "/{id}/", response_model=ProductOut, status_code=status.HTTP_200_OK
)
async def get_product(id: int):
    return await products.get_by_id(id)


@router.put(
    "/{id}/", response_model=ProductOut, status_code=status.HTTP_202_ACCEPTED
)
async def update_product(id: int, product: ProductCreate):
    original_product = await products.get_by_id(id)
    if not original_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return await products.put(id, product)


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(id: int):
    product = await products.get_by_id(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return await products.delete_by_id(id)
