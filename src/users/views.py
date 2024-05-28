from fastapi import APIRouter, Depends, Response
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from .dependencies import validate_user, get_current_user
from .models import User
from .schemas import SUserAuth, TokenInfo
from src.service.exceptions import (
    USER_ALREADY_EXISTS_EXCEPTION,
)
from .crud import UserCRUD
from .auth import get_password_hash, encode_jwt


router = APIRouter(tags=["Auth & Пользователи"])
security = HTTPBasic()


@router.get("/basic-auth")
async def basic_auth(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"msg": "Hello World", "credentials": credentials}


@router.post("/register", status_code=201)
async def register_user(user_data: Annotated[SUserAuth, Depends()]):
    existing_user_by_email = await UserCRUD.find_one_or_none(email=user_data.email)
    existing_user_by_username = await UserCRUD.find_one_or_none(
        username=user_data.username
    )
    if existing_user_by_email or existing_user_by_username:
        raise USER_ALREADY_EXISTS_EXCEPTION

    hash_psw = get_password_hash(user_data.password)
    await UserCRUD.add_obj(
        username=user_data.username, email=user_data.email, password=hash_psw
    )
    return {"success": "User created"}


@router.post("/login", response_model=TokenInfo)
async def login_user(response: Response, user: SUserAuth = Depends(validate_user)):
    jwt_payload = {"sub": user.id,
                   "username": user.username, "email": user.email}
    token = encode_jwt(payload=jwt_payload)
    response.headers["Authorization"] = f"Bearer {token}"
    # response.set_cookie(key="access_token", value=token, httponly=True)
    return TokenInfo(access_token=token, token_type="Bearer")


@router.get("/user/me")
async def get_current_user(user: User = Depends(get_current_user)):
    return user
