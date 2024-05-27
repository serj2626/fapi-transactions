from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from .models import User
from auth.schemas import SUserAuth
from src.service.exceptions import USER_ALREADY_EXISTS_EXCEPTION
from .crud import AuthCRUD


router = APIRouter(prefix="/auth", tags=["Auth & Пользователи"])
security = HTTPBasic()


@router.get("/basic-auth")
async def basic_auth(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return {"msg": "Hello World", "credentials": credentials}


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await AuthCRUD.find_one_or_none(email=user_data.email)
    if existing_user:
        raise USER_ALREADY_EXISTS_EXCEPTION
    # hash_psw = get_password_hash(user_data.password)
    await AuthCRUD.add_obj(
        username=user_data.name,
        email=user_data.email,
        password=user_data.password)
    return {"message": "User created", "data": user_data}
