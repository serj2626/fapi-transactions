from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials


router = APIRouter(prefix="/auth", tags=["Auth & Пользователи"])
security = HTTPBasic()


@router.get("/basic-auth")
async def basic_auth(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return {"msg": "Hello World", "credentials": credentials}
