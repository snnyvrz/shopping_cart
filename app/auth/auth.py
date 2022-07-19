from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from auth.utils import oauth2_scheme, verify_password
from core.settings import JWT_SECRET_KEY, ALGORITHM
from crud import users
from schemas.token import TokenData
from schemas.user import UserOut


async def authenticate_user(username: str, password: str):
    user = await users.get_user_by_username(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if not username:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await users.get_user_by_username(token_data.username)
    if not user:
        raise credentials_exception
    return user


async def is_admin(current_user: UserOut = Depends(get_current_user)):
    return current_user.is_admin


async def is_superuser(current_user: UserOut = Depends(get_current_user)):
    return current_user.is_superuser
