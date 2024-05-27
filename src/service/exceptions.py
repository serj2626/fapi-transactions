from fastapi import HTTPException


INVALID_TOKEN_EXCEPTION = HTTPException(
    status_code=401, detail="Неверный токен")

INVALID_PASSWORD_EXCEPTION = HTTPException(
    status_code=401, detail="Неверный пароль")

USER_ALREADY_EXISTS_EXCEPTION = HTTPException(
    status_code=400, detail="Пользователь с таким логином или email уже существует")

USER_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=404, detail="Пользователь не найден"
)

INCORRECT_DATA_EXCEPTION = HTTPException(
    status_code=401, detail="Некорректные данные"
)
