from fastapi import APIRouter, HTTPException, status

from crud import categories
from schemas.category import CategoryCreate, CategoryOut

router = APIRouter()


@router.get(
    "/",
    response_model=list[CategoryOut],
    status_code=status.HTTP_200_OK,
)
async def get_all_categories():
    return await categories.get_all()


@router.post(
    "/",
    response_model=CategoryOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_category(category: CategoryCreate):
    return await categories.post(category)


@router.get(
    "/{id}/", response_model=CategoryOut, status_code=status.HTTP_200_OK
)
async def get_category(id: int):
    category = await categories.get_by_id(id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.put(
    "/{id}/", response_model=CategoryOut, status_code=status.HTTP_202_ACCEPTED
)
async def update_category(id: int, category: CategoryCreate):
    original_category = await categories.get_by_id(id)
    if not original_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return await categories.put(id, category)


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(id: int):
    category = await categories.get_by_id(id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return await categories.delete_by_id(id)
