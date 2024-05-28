"""
    Этот модуль содержит функции для работы с JWT
    Также содержится функция для хеширования пароля

    Подробнее: https://pyjwt.readthedocs.io/en/stable/usage.html

    :func: encode_jwt - кодирование JWT
    :func: decode_jwt - декодирование JWT
    :func: get_password_hash: получение хеша пароля
    :func: verify_password: проверка пароля

"""

from datetime import timedelta, datetime
from typing import Annotated
from fastapi import Depends
import jwt
from src.service.exceptions import INCORRECT_DATA_EXCEPTION
from src.config import settings
from passlib.context import CryptContext
from .schemas import SUserAuth
from .crud import UserCRUD

private_key = settings.auth_jwt.private_key_path.read_text()
public_key = settings.auth_jwt.public_key_path.read_text()
algorithm = settings.auth_jwt.algorithm


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encode_jwt(
    payload: dict,
    private_key: str = private_key,
    algorithm: str = algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
) -> str:

    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        exp = (now + expire_timedelta).timestamp()
    else:
        exp = (now + timedelta(minutes=expire_minutes)).timestamp()
    to_encode.update(exp=exp, iat=now)
    encoded = jwt.encode(to_encode, private_key, algorithm=algorithm)

    return encoded


def decode_jwt(
    token: str | bytes, public_key: str = public_key, algorithm: str = algorithm
) -> dict:
    decoded = jwt.decode(token, public_key, algorithms=[algorithm])

    return decoded


# def hash_pasw(password: str) -> bytes:
#     salt = bcrypt.gensalt()
#     psw_bytes: bytes = password.encode()

#     return bcrypt.hashpw(psw_bytes, salt)


# def validate_password(password: str, hashed_password: bytes) -> bool:
#     psw_bytes: bytes = password.encode()
#     return bcrypt.checkpw(psw_bytes, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
