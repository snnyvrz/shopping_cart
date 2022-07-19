from fastapi import APIRouter, HTTPException, status

from crud import users
from schemas.user import UserCreate, UserOut

router = APIRouter()


@router.get("/", response_model=list[UserOut], status_code=status.HTTP_200_OK)
async def get_all_users():
    return await users.get_all()


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    return await users.post(user)


@router.get("/{id}/", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_user(id: int):
    return await users.get_by_id(id)


@router.put(
    "/{id}/", response_model=UserOut, status_code=status.HTTP_202_ACCEPTED
)
async def update_user(id: int, user: UserCreate):
    original_user = await users.get_by_id(id)
    if not original_user:
        raise HTTPException(status_code=404, detail="User not found")
    return await users.put(id, user)


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int):
    user = await users.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await users.delete_by_id(id)
