from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from auth.auth import (
    authenticate_user,
    create_access_token,
    get_current_user,
    is_admin,
    is_superuser,
)
from core.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from crud import users
from schemas.user import UserCreate, UserOut

router = APIRouter()

user_404_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
)


@router.get("/", response_model=list[UserOut], status_code=status.HTTP_200_OK)
async def get_all_users(_: bool = Depends(is_admin)):
    return await users.get_all()


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    return await users.post(user)


@router.get("/me/", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_me(current_user: UserOut = Depends(get_current_user)):
    return current_user


@router.post("/token/", status_code=status.HTTP_201_CREATED)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/{id}/", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_user(id: int, _: bool = Depends(is_admin)):
    return await users.get_by_id(id)


@router.put(
    "/{id}/", response_model=UserOut, status_code=status.HTTP_202_ACCEPTED
)
async def update_user(
    id: int,
    user: UserOut,
    _: bool = Depends(is_admin),
):
    original_user = await users.get_by_id(id)
    if not original_user:
        raise user_404_exception
    return await users.put(id, user)


@router.delete("/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int, _: bool = Depends(is_admin)):
    user = await users.get_by_id(id)
    if not user:
        raise user_404_exception
    return await users.delete_by_id(id)
