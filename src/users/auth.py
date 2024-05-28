"""
    Этот модуль содержит функции для работы с JWT
    Также содержится функция для хеширования пароля

    Подробнее: https://pyjwt.readthedocs.io/en/stable/usage.html

    :func: encode_jwt - кодирование JWT
    :func: decode_jwt - декодирование JWT
    :get_password_hash: хеширование пароля
    :verify_password: проверка пароля

"""


import jwt
from src.config import settings
from passlib.context import CryptContext

private_key = settings.auth_jwt.private_key_path.read_text()
public_key = settings.auth_jwt.public_key_path.read_text()
algorithm = settings.auth_jwt.algorithm


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encode_jwt(
    payload: dict,
    private_key: str = private_key,
    algorithm: str = algorithm
) -> str:
    encoded = jwt.encode(payload, private_key, algorithm=algorithm)

    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = public_key,
    algorithm: str = algorithm

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


