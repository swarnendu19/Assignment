from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from typing import Union

from models.user import User
from config.settings import settings

SECRET_KEY = settings.JWT_PRIVATE_KEY.encode()  
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Token data model
class TokenData(BaseModel):
    user_id: Union[str, None] = None


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN)):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id = payload.get("sub")
#         if user_id is None:
#             raise credentials_exception
#         token_data = TokenData(user_id=str(user_id))
#     except JWTError:
#         raise credentials_exception
#     user = await User.get(token_data.user_id)
#     if user is None:
#         raise credentials_exception
#     return user


# async def require_user(current_user: User = Depends(get_current_user)):
#     if not current_user:
#         raise HTTPException(status_code=400, detail="User not found")
#     return current_user