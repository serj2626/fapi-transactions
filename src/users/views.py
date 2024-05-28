from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from .models import User
from .schemas import SUserAuth
from src.service.exceptions import USER_ALREADY_EXISTS_EXCEPTION
from .crud import UserCRUD
from .auth import get_password_hash, verify_password

router = APIRouter(prefix="/auth", tags=["Auth & Пользователи"])
security = HTTPBasic()


@router.get("/basic-auth")
async def basic_auth(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"msg": "Hello World", "credentials": credentials}


@router.post("/register")
async def register_user(user_data: Annotated[SUserAuth, Depends()]):
    existing_user = await UserCRUD.find_one_or_none(email=user_data.email)
    if existing_user:
        raise USER_ALREADY_EXISTS_EXCEPTION
    
    hash_psw = get_password_hash(user_data.password)
    print(hash_psw)
    await UserCRUD.add_obj(username=user_data.username,
                           email=user_data.email,
                           password=hash_psw)
    return {"message": "User created", "pasw": hash_psw}
