from fastapi import Depends, Form, Request
from .models import User
from src.service.exceptions import (
    INVALID_USERNAME_OR_PASSWORD_EXCEPTION,
    INVALID_TOKEN_EXCEPTION,
)
from .auth import verify_password, decode_jwt
from .crud import UserCRUD
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt.exceptions import InvalidTokenError

http_bearer = HTTPBearer()


async def validate_user(username: str = Form(), password: str = Form()) -> User:
    user = await UserCRUD.find_one_or_none(username=username)

    if not user:
        raise INVALID_USERNAME_OR_PASSWORD_EXCEPTION

    if not verify_password(password, user.password):
        raise INVALID_USERNAME_OR_PASSWORD_EXCEPTION

    return user


def get_current_token_payliad(credentials: HTTPAuthorizationCredentials = Depends(http_bearer)) -> dict:
    token = credentials.credentials
    print(token)
    try:
        payload = decode_jwt(token=token)
    except InvalidTokenError:
        raise INVALID_TOKEN_EXCEPTION
    return payload


async def get_current_user(payload: dict = Depends(get_current_token_payliad)) -> User:
    username = payload.get("username")

    if not username:
        raise INVALID_TOKEN_EXCEPTION

    user = await UserCRUD.find_one_or_none(username=username)

    if not user:
        raise INVALID_TOKEN_EXCEPTION

    return user
