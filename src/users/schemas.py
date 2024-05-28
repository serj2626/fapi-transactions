from pydantic import BaseModel, EmailStr, Field


class SUserAuth(BaseModel):
    username: str
    email: str
    password: str


class TokenInfo(BaseModel):
    access_token: str
    token_type: str
