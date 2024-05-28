from fastapi import Form
from .models import User
from src.service.exceptions import INVALID_USERNAME_OR_PASSWORD_EXCEPTION
from .auth import verify_password
from .crud import UserCRUD


async def validate_user(username: str = Form(), password: str = Form()) -> User:
    user = await UserCRUD.find_one_or_none(username=username)

    if not user:
        raise INVALID_USERNAME_OR_PASSWORD_EXCEPTION

    if not verify_password(password, user.password):
        raise INVALID_USERNAME_OR_PASSWORD_EXCEPTION

    return user
